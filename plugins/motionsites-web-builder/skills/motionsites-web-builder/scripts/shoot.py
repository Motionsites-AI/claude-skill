"""Screenshot + QA a page so you can SEE what you built.

Usage:
  python scripts/shoot.py path/to/index.html [out_dir] [--wait 2.5] [--full]
  python scripts/shoot.py http://localhost:5173 [out_dir]

Writes desktop (1440x900) and mobile (390x844) screenshots after entrance
animations settle, plus an "early" desktop frame (0.35s) to check the first
paint, then prints a QA report: console errors, failed requests (broken asset
URLs), horizontal overflow, fonts, videos and images that did not load.

Needs Playwright:  pip install playwright && python -m playwright install chromium
Falls back to headless Chrome (screenshots only, no QA) if Playwright is missing.
"""
import json, os, shutil, subprocess, sys, time
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = sys.argv[1:]
if not args:
    sys.exit(__doc__)
target = args[0]
out = Path(args[1] if len(args) > 1 else "shots")
out.mkdir(parents=True, exist_ok=True)
wait = float(flags[flags.index("--wait") + 1]) if "--wait" in flags else 2.5
full = "--full" in flags
url = target if "://" in target else Path(target).resolve().as_uri()

VIEWS = [("desktop", 1440, 900), ("mobile", 390, 844)]

QA_JS = """() => {
  const vw = document.documentElement.clientWidth;
  const wide = [...document.querySelectorAll('body *')].filter(e => {
    const r = e.getBoundingClientRect(); return r.right > vw + 1 && getComputedStyle(e).position !== 'fixed';
  }).slice(0, 5).map(e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : ''));
  const vids = [...document.querySelectorAll('video')].map(v => ({src: (v.currentSrc || v.src || '').slice(0, 90), ready: v.readyState, paused: v.paused, error: v.error ? v.error.code : null}));
  const imgs = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(0, 90));
  const fonts = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, ''));
  const h1 = document.querySelector('h1');
  return {
    title: document.title,
    scrollWidth: document.documentElement.scrollWidth, viewport: vw,
    horizontalOverflow: document.documentElement.scrollWidth > vw + 1, overflowingElements: wide,
    pageHeight: document.documentElement.scrollHeight,
    videos: vids, brokenImages: imgs, fontsLoaded: [...new Set(fonts)],
    h1: h1 ? {text: h1.innerText.slice(0, 80), fontSize: getComputedStyle(h1).fontSize, font: getComputedStyle(h1).fontFamily.slice(0, 40)} : null,
  };
}"""


def with_playwright():
    from playwright.sync_api import sync_playwright
    report = {}
    with sync_playwright() as p:
        # Real Chrome plays H.264 MP4s; Playwright's bundled Chromium cannot (videos stay black).
        try:
            browser, engine = p.chromium.launch(channel="chrome"), "chrome"
        except Exception:
            browser, engine = p.chromium.launch(), "chromium (no H.264: MP4 videos will not play)"
        report["browser"] = engine
        for name, w, h in VIEWS:
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=1,
                                      is_mobile=name == "mobile", has_touch=name == "mobile")
            page = ctx.new_page()
            errors, failed = [], []
            page.on("console", lambda m: errors.append(m.text[:200]) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)[:200]))
            page.on("requestfailed", lambda r: failed.append(f"{r.url[:100]} ({r.failure})"))
            page.on("response", lambda r: failed.append(f"{r.url[:100]} (HTTP {r.status})") if r.status >= 400 else None)
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            if name == "desktop":
                page.wait_for_timeout(350)
                page.screenshot(path=str(out / "desktop-early.png"))
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except Exception:
                pass
            page.wait_for_timeout(int(wait * 1000))
            page.screenshot(path=str(out / f"{name}.png"), full_page=full)
            qa = page.evaluate(QA_JS)
            if engine != "chrome" and any(v["error"] == 4 for v in qa["videos"]):
                qa["videoNote"] = "This browser cannot decode the MP4; judge the video area from the poster/source, not as a bug."
            qa["consoleErrors"], qa["failedRequests"] = errors[:10], [f for f in failed if "ERR_ABORTED" not in f][:10]
            report[name] = qa
            ctx.close()
        browser.close()
    return report


def with_chrome():
    chrome = next((c for c in ["google-chrome", "chromium", "chromium-browser",
                               "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
                   if shutil.which(c) or os.path.exists(c)), None)
    if not chrome:
        sys.exit("No Playwright and no Chrome found. Install: pip install playwright && python -m playwright install chromium")
    for name, w, h in VIEWS:
        subprocess.run([chrome, "--headless=new", "--hide-scrollbars", f"--window-size={w},{h}",
                        f"--virtual-time-budget={int(wait * 1000)}", f"--screenshot={out / (name + '.png')}", url],
                       capture_output=True, timeout=120)
    return {"note": "headless Chrome fallback: screenshots only, no QA report"}


try:
    import playwright  # noqa: F401
    rep = with_playwright()
except ImportError:
    rep = with_chrome()

print(json.dumps(rep, indent=1))
print("\nScreenshots:", ", ".join(str(p) for p in sorted(out.glob("*.png"))))
print("Now LOOK at them (open the PNGs) and review against references/review.md.")
