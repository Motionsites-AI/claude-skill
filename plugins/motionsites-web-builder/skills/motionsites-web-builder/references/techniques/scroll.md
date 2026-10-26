# Scroll

Reveals, pinned stages, parallax and scroll-linked motion. (Scroll-scrubbed video lives in video-and-media.md; the scroll-linked word reveal in type-and-text-motion.md.)

**Conventions.** Single-file, no build step. Shared tokens (paste once):
```css
:root{
  --ease-out-expo:cubic-bezier(.16,1,.3,1);
  --ease-out-quint:cubic-bezier(.22,1,.36,1);
  --ease-reveal:cubic-bezier(.25,.1,.25,1);
}
```
Scroll handlers are passive and rAF-throttled (`if (!ticking) { ticking = true; requestAnimationFrame(update); }`). **Never** put `overflow:hidden` on an ancestor of a sticky element: it kills `position:sticky`. Use `overflow-x:clip` on wrappers. Scroll-driven motion is user-driven, so under reduced motion keep the mapping but drop smoothing and autonomous movement.

---

## 1. Viewport-triggered staggered reveal (+ directional corner decor)

**What / when:** Below-the-fold blocks fade and rise once as they enter the viewport, with per-element delays so a group cascades. The workhorse for every section after the hero. The corner-decor version frames a centred heading with four objects (3D renders, icons) that slide in from the left and right toward the corners: good for an About or Intro section.

**Premium parameters**
- Default `opacity 0, y 30px` → rest, **0.7 s** `cubic-bezier(.25,.1,.25,1)`, once. Large headings y 40 px; media blocks y 60 px, 0.9 s; two-column splits from `x −40px` / `x +40px`; card grids `scale(.95)` + fade with `--ease-out-quint`.
- Trigger: IntersectionObserver `threshold .15`, `rootMargin: 0px 0px -10% 0px` (lets the reader see it happen). Eager alternative: `threshold 0`, `rootMargin 50px`.
- Stagger formulas `base + i × step`: list `150 + i·120 ms`, panel rows `300 + i·110 ms`, nav links `100 + i·100 ms`, stat columns `i·150 ms` (y 30, 0.8 s), grid cards `i·100 ms` (y 20, 0.7 s).
- Corner decor: `x ±80px`, 0.9 s, delays .10 / .15 / .25 / .30 s; sizes 120 → 160 → 210 px by breakpoint; top pair at `top 4 %`, `left/right 1 % → 4 %`; bottom pair at `bottom 8 %`, `3 % → 10 %`.
- Hide targets only when JS is running (`.js` class on `<html>`), so content never disappears if a script fails.
- Gotcha: `threshold` is a fraction of the *element*; a block taller than ~6.6 viewports can never reach 0.15, so use `threshold: 0` plus `rootMargin` for very tall blocks.

**Implementation**
```html
<script>document.documentElement.classList.add('js')</script> <!-- in <head> -->
<ul data-stagger="120" data-stagger-base="150">
  <li data-reveal>…</li><li data-reveal>…</li><li data-reveal>…</li>
</ul>
<section class="about">
  <img class="decor decor--tl" data-reveal style="--x:-80px;--y:0px;--dur:.9s;--d:.10s" src="obj1.png" alt="">
  <img class="decor decor--tr" data-reveal style="--x:80px;--y:0px;--dur:.9s;--d:.15s" src="obj2.png" alt="">
  <img class="decor decor--bl" data-reveal style="--x:-80px;--y:0px;--dur:.9s;--d:.25s" src="obj3.png" alt="">
  <img class="decor decor--br" data-reveal style="--x:80px;--y:0px;--dur:.9s;--d:.30s" src="obj4.png" alt="">
  <h2 data-reveal style="--y:40px">About</h2>
</section>
```
```css
.js [data-reveal]{opacity:0;transform:translate3d(var(--x,0px),var(--y,30px),0);
  transition:opacity var(--dur,.7s) var(--ease,var(--ease-reveal)) var(--d,0s),
             transform var(--dur,.7s) var(--ease,var(--ease-reveal)) var(--d,0s)}
.js [data-reveal="scale"]{transform:scale(.95);--ease:var(--ease-out-quint)}
.js [data-reveal].is-in{opacity:1;transform:none}
.about{position:relative;min-height:100vh;display:grid;place-items:center;padding:80px 20px;overflow-x:clip}
.decor{position:absolute;width:clamp(120px,14vw,210px);height:auto;pointer-events:none}
.decor--tl{top:4%;left:clamp(1%,2vw,4%)} .decor--tr{top:4%;right:clamp(1%,2vw,4%)}
.decor--bl{bottom:8%;left:clamp(3%,5vw,10%);width:clamp(100px,12vw,180px)}
.decor--br{bottom:8%;right:clamp(3%,5vw,10%);width:clamp(130px,15vw,220px)}
@media (prefers-reduced-motion:reduce){.js [data-reveal]{opacity:1;transform:none;transition:none}}
```
```js
document.querySelectorAll('[data-stagger]').forEach((group) => {
  const step = +group.dataset.stagger, base = +(group.dataset.staggerBase || 0);
  group.querySelectorAll('[data-reveal]').forEach((el, i) => el.style.setProperty('--d', `${base + i * step}ms`));
});
const revealIO = new IntersectionObserver((entries) => entries.forEach((e) => {
  if (e.isIntersecting) { e.target.classList.add('is-in'); revealIO.unobserve(e.target); }
}), { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
document.querySelectorAll('[data-reveal]').forEach((el) => revealIO.observe(el));
```

**Framer Motion variant:** `<motion.div initial={{ opacity: 0, x, y }} whileInView={{ opacity: 1, x: 0, y: 0 }} viewport={{ once: true, margin: '-100px' }} transition={{ delay, duration: 0.7, ease: [0.25, 0.1, 0.25, 1] }} />`

---

## 2. Sticky cinematic stage with CSS-variable choreography (scroll windows, split-frame parting, depth-of-field, tint)

**What / when:** A whole "film" told in one pinned viewport. Layered transparent cut-outs (sky → midground → giant title → subject → foreground halves) move independently as the user scrolls a long runway. The title sits *between* background and subject; the foreground splits apart like curtains to reveal a close-up; the background racks out of focus and takes on a tint; story panels slide through. For destination, product-launch or brand-story pages with layered photography.

**Architecture**
- Runway section `height: calc(100vh + N px)` (~3000–3700 px) with a `position:sticky; top:0; height:100vh; min-height:620px` stage.
- JS computes `scroll = clamp(-section.top, 0, section.height − innerHeight)` in **pixels**, smooths it (`lerp 0.14`, snap when `|Δ| < 0.08px`), then writes ~25 CSS custom properties per frame; CSS owns all transforms. rAF runs only while something is still settling.
- Two helpers build the timeline: `smoothstep(e0, e1, s)` and `segment(s, a, b, c, d)` → `{enter, exit, active = enter × (1 − exit)}`, a "scroll window" that fades in over `[a,b]` and out over `[c,d]`.
- Write the story as a table of pixel windows first, e.g.:

| Scroll px | What happens |
|---|---|
| 90 → 650 | Title rises `−210px`, scales to `.92`, fades; intro copy + pills sink `+90px`, fade |
| 560 → 900 (enter) | Foreground halves part to `∓46vw` (eased `enter^1.5`), rise `−180px`, scale `+0.74`; subject widens `67.2 → 105vw`, lifts; close-up fades in; background blurs to **14px**, brightness `−25.5 %`, tint rises to alphas **.465 / .42 / .51** |
| 1300 → 1620 (exit) | Subject launches `−760px`, scales `+0.46`; chapter panel slides `+58 → −86px` and fades |
| next windows | Repeat with new layers (saturation boosts, a card row flying in from `420vw`, …) |

- Constant drift across the runway: `progress = scroll / 2700` adds `−74px` Y and `+0.23` scale to the hero layers and grows the back stack `0.76 → 0.96`.
- Pointer parallax mixed in (depth-and-interaction.md, technique 3): background `x·−12 / y·−4`, subject `x·18 / y·8`, foreground halves `x·22 / y·10`, close-up `x·10 / y·8`.

**Implementation**
```html
<section class="cine" style="--runway:3000px" aria-label="Story">
  <div class="cine__stage">
    <img class="cine__layer cine__sky" src="sky.jpg" alt="">
    <img class="cine__layer cine__mid" src="midground-cutout.png" alt="">
    <div class="cine__shade" aria-hidden="true"></div>
    <h1 class="cine__title">Title</h1>
    <img class="cine__layer cine__subject" src="subject-cutout.png" alt="">
    <img class="cine__layer cine__closeup" src="closeup.png" alt="">
    <img class="cine__layer cine__split cine__split--l" src="foreground-left-half.png" alt="">
    <img class="cine__layer cine__split cine__split--r" src="foreground-right-half.png" alt="">
    <div class="cine__intro">
      <p>One-sentence promise of the place or product.</p>
      <div class="cine__tags"><span>Tag one</span><span>Tag two</span><span>Tag three</span></div>
    </div>
    <div class="cine__panel"><h2>Chapter headline.</h2><p>Two short lines of supporting copy.</p></div>
  </div>
</section>
```
```css
.cine{position:relative;height:calc(100vh + var(--runway,3000px))}
.cine__stage{position:sticky;top:0;height:100vh;min-height:620px;overflow:hidden;isolation:isolate;background:#7fb4d4;
  --tint:74,181,224;
  --mx:0;--my:0;--blur:0px;--bright:1;--shade:0;--mid-s:.76;
  --title-y:0px;--title-s:1;--title-o:1;
  --subj-y:0px;--subj-w:67.2vw;--subj-b:5vh;--subj-s:1.02;
  --split-x:0vw;--split-y:0px;--split-s:1;
  --close-o:0;--close-y:0px;--close-s:1.06;
  --intro-y:0px;--intro-o:1;--panel-o:0;--panel-y:58px}
.cine__layer{position:absolute;display:block;max-width:none;pointer-events:none;user-select:none;-webkit-user-drag:none;will-change:transform,opacity,filter}
.cine__sky{inset:0;width:100%;height:100%;object-fit:cover;z-index:0;filter:blur(var(--blur)) brightness(var(--bright))}
.cine__mid{left:50%;bottom:0;width:112%;height:auto;z-index:1;transform-origin:50% 100%;
  transform:translate3d(calc(-50% + var(--mx) * -12px),calc(var(--my) * -4px),0) scale(var(--mid-s));
  filter:blur(var(--blur)) brightness(var(--bright))}
.cine__shade{position:absolute;inset:0;z-index:2;pointer-events:none;
  background:linear-gradient(180deg,rgba(var(--tint),calc(var(--shade) * .465)) 0%,rgba(var(--tint),calc(var(--shade) * .42)) 48%,rgba(var(--tint),calc(var(--shade) * .51)) 100%)}
.cine__title{position:absolute;left:50%;top:clamp(122px,19vh,205px);z-index:3;width:min(94vw,1780px);margin:0;text-align:center;
  font:500 14rem/.78 Georgia,serif;color:#fdf1e1;
  transform:translate3d(-50%,var(--title-y),0) scale(var(--title-s));opacity:var(--title-o);will-change:transform,opacity}
.cine__subject{left:50%;bottom:var(--subj-b);width:min(var(--subj-w),2140px);height:auto;z-index:4;transform-origin:50% 48%;
  transform:translate3d(calc(-50% + var(--mx) * 18px),var(--subj-y),0) scale(var(--subj-s))}
.cine__closeup{left:50%;top:50%;width:min(122vw,2160px);height:auto;z-index:5;opacity:var(--close-o);transform-origin:50% 48%;
  transform:translate3d(calc(-50% + var(--mx) * 10px),calc(-50% + var(--close-y)),0) scale(var(--close-s))}
.cine__split{left:50%;bottom:-2vh;width:min(118vw,2240px);height:auto;z-index:6}
.cine__split--l{transform-origin:21% 52%;
  transform:translate3d(calc(-50% - var(--split-x) + var(--mx) * 22px),calc(var(--split-y) + var(--my) * 10px),0) scale(var(--split-s))}
.cine__split--r{transform-origin:79% 52%;
  transform:translate3d(calc(-50% + var(--split-x) + var(--mx) * 22px),calc(var(--split-y) + var(--my) * 10px),0) scale(var(--split-s))}
.cine__intro{position:absolute;left:50%;bottom:clamp(56px,28vh,400px);z-index:9;width:min(560px,calc(100vw - 40px));text-align:center;
  transform:translate3d(-50%,var(--intro-y),0);opacity:var(--intro-o)}
.cine__intro p{margin:0;color:#fdf1e1;font-size:1.18rem;font-weight:500;line-height:1.18;text-shadow:0 2px 18px rgba(0,0,0,.42)}
.cine__tags{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:26px}
.cine__tags span{min-height:42px;display:inline-flex;align-items:center;padding:0 25px;border-radius:999px;background:#fdf1e1;
  color:#111411;font-size:.98rem;font-weight:500;box-shadow:0 12px 30px rgba(0,0,0,.18)}
.cine__panel{position:absolute;left:50%;top:60%;z-index:10;width:min(760px,calc(100vw - 42px));text-align:center;pointer-events:none;
  opacity:var(--panel-o);transform:translate3d(-50%,calc(-50% + var(--panel-y)),0)}
.cine__panel h2{margin:0;color:#fdf1e1;font:500 4.75rem/.95 Georgia,serif;text-shadow:0 16px 38px rgba(0,0,0,.32)}
.cine__panel p{width:min(520px,100%);margin:26px auto 0;color:#fdf1e1;font-size:1.14rem;font-weight:500;line-height:1.18;text-shadow:0 2px 18px rgba(0,0,0,.42)}
@media (max-width:1500px){.cine__title{font-size:11rem}.cine__panel h2{font-size:4.1rem}}
@media (max-width:1100px){.cine__title{top:15vh;font-size:7.5rem}.cine__subject{width:138vw}.cine__closeup{width:132vw}.cine__panel h2{font-size:3.2rem}}
@media (max-width:640px){.cine__stage{min-height:640px}.cine__title{top:16vh;font-size:4.5rem}
  .cine__subject{bottom:2vh;width:190vw}.cine__closeup{width:176vw}.cine__intro{bottom:42px}
  .cine__intro p,.cine__panel p{font-size:1rem}.cine__panel{top:42%}.cine__panel h2{font-size:2.45rem}}
```
```js
(() => {
  const section = document.querySelector('.cine');
  const stage = section.querySelector('.cine__stage');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const smoothstep = (e0, e1, v) => { const x = clamp((v - e0) / (e1 - e0)); return x * x * (3 - 2 * x); };
  const lerp = (a, b, t) => a + (b - a) * t;
  const segment = (s, a, b, c, d) => { const enter = smoothstep(a, b, s), exit = smoothstep(c, d, s); return { enter, exit, active: enter * (1 - exit) }; };
  const set = (k, v) => stage.style.setProperty(k, v);
  let target = 0, smooth = 0, mx = 0, my = 0, tmx = 0, tmy = 0, init = false, pending = false;

  function update() {
    pending = false;
    const rm = reduce.matches;
    target = clamp(-section.getBoundingClientRect().top, 0, section.offsetHeight - innerHeight);
    smooth = (!init || rm) ? target : lerp(smooth, target, 0.14);
    init = true;
    if (Math.abs(smooth - target) < 0.08) smooth = target;
    mx = rm ? 0 : lerp(mx, tmx, 0.12);
    my = rm ? 0 : lerp(my, tmy, 0.12);

    const s = smooth;
    const intro = smoothstep(90, 650, s);                 // hero exit
    const ch = segment(s, 560, 900, 1300, 1620);          // chapter 1 window
    const progress = clamp(s / 2700);
    const split = Math.pow(ch.enter, 1.5);                // eased parting
    const drift = progress * -74, grow = progress * 0.23;

    set('--mx', mx.toFixed(4)); set('--my', my.toFixed(4));
    set('--title-y', `${intro * -210}px`); set('--title-s', (1 - intro * 0.08).toFixed(4)); set('--title-o', (1 - intro).toFixed(4));
    set('--intro-y', `${intro * 90}px`);   set('--intro-o', (1 - intro).toFixed(4));
    set('--mid-s', (0.76 + progress * 0.2 + ch.enter * 0.18).toFixed(4));
    set('--blur', `${(ch.active * 14).toFixed(2)}px`);
    set('--bright', (1 - ch.active * 0.255).toFixed(4));
    set('--shade', ch.active.toFixed(4));
    set('--subj-y', `${(my * 8 + drift - ch.exit * 760).toFixed(1)}px`);
    set('--subj-b', `${(5 - ch.enter * 13).toFixed(2)}vh`);
    set('--subj-w', `${(67.2 + ch.enter * 37.8).toFixed(2)}vw`);
    set('--subj-s', (1.02 + grow + ch.exit * 0.46).toFixed(4));
    set('--split-x', `${(split * 46).toFixed(2)}vw`);
    set('--split-y', `${(drift - split * 180).toFixed(1)}px`);
    set('--split-s', (1 + grow + ch.enter * 0.74).toFixed(4));
    set('--close-o', ch.active.toFixed(4));
    set('--close-y', `${(my * 8 - ch.exit * 150).toFixed(1)}px`);
    set('--close-s', (1.06 + ch.enter * 0.08 + ch.exit * 0.08).toFixed(4));
    set('--panel-o', (ch.active * (1 - ch.exit)).toFixed(4));
    set('--panel-y', `${(-ch.exit * 86 + (1 - ch.enter) * 58).toFixed(1)}px`);

    const settling = Math.abs(smooth - target) > 0.08 || (!rm && (Math.abs(mx - tmx) > 0.001 || Math.abs(my - tmy) > 0.001));
    if (settling) requestTick();
  }
  function requestTick() { if (!pending) { pending = true; requestAnimationFrame(update); } }
  addEventListener('scroll', requestTick, { passive: true });
  addEventListener('resize', requestTick);
  if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
    addEventListener('pointermove', (e) => { tmx = e.clientX / innerWidth - 0.5; tmy = e.clientY / innerHeight - 0.5; requestTick(); }, { passive: true });
  }
  requestTick();
})();
```

**Extra tricks**
- *Screen-true UI inside a zooming layer:* a card row inside the scaling back stack gets `scale(1 / backScale)` with `transform-origin:0 0`, and its top solves `parentTop = vh − (vh − screenTop) / backScale` (back stack origin `50% 100%`), so cards stay pixel-stable while the world zooms.
- *Hide, don't just fade:* off-stage interactive elements use `visibility:hidden` + an off-screen X (`420vw`); controls get `pointer-events:auto` only once their enter value passes **0.98**.
- *Glow layer:* a duplicate background at `opacity .72; mix-blend-mode: screen` adds atmospheric light.
- Asset prep: export each depth plane as transparent PNG/WebP at ~2× viewport width; cut the foreground into a left and a right file (each keeps one half, the other half transparent).

**Reduced motion / mobile:** smoothing and pointer parallax are bypassed (values snap, `--mx/--my = 0`); the composition still scrubs because it's user-driven. Mobile widens subject and close-up (`138vw → 190vw`) so planes still cover, and shrinks the title `14rem → 11 → 7.5 → 4.5rem`.

---

## 3. Panel slide-over hero + viewport-scaled scattered gallery + blend outro

**What / when:** A fashion / archive pattern: a full-bleed video hero, then a black panel slides up over it carrying a sparse, asymmetric grid of tall images that *grow* as they enter the viewport and *shrink away* as they exit, each growing toward the page centre. At the end a white veil fades over everything and a giant pill CTA scales in from the corner. Fixed UI stays legible throughout via exclusion blending (depth-and-interaction.md, technique 6).

**Premium parameters**
- Panel black, top padding `min(400px, 40vh)`; it slides over the sticky hero for the first 100vh.
- Columns 2 / 3 / 4 at `<640 / <1024 / ≥1024 px`; cells `aspect-ratio: 2/3`.
- Scatter rule per row `r`: primary column `a = (2r + r mod 2) mod cols`; every 3rd row adds a second image at `(a + 2) mod cols` (or `a + 1` if equal); other cells stay empty.
- Scale per frame: enter `min(1, (vh − top) / (0.6·vh))`, exit `min(1, bottom / (0.4·vh))`, `scale = min(enter, exit)`, 0 off-screen. Left-half cards `transform-origin: right bottom`, right-half `left bottom`.
- Outro over one screen: white veil `opacity 0 → 1`; CTA `scale(0 → 1)` from `right bottom`; pill `border-radius 1335px`, desktop `330 × 174px`, text **110 px** (72 px mobile), `-.04em`. The double exclusion makes it white-with-black-text over black and the inverse over the veil.
- Measure the *cell*, scale the *image* (`getBoundingClientRect()` includes transforms).

**Implementation**
```html
<section class="pg-hero"><video src="VIDEO_URL.mp4" autoplay muted loop playsinline aria-hidden="true"></video></section>
<section class="pg-panel"><div class="pg-grid" id="pgGrid"></div></section>
<section class="pg-outro" aria-label="End"></section>
<div class="pg-veil" aria-hidden="true"></div>
<a class="pg-cta" href="#"><span>view</span></a>
```
```css
.pg-hero{position:sticky;top:0;height:100vh;height:100svh;z-index:0;overflow:hidden}
.pg-hero video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.pg-panel{position:relative;z-index:10;background:#000;padding-top:min(400px,40vh);min-height:100vh}
.pg-grid{display:grid;grid-template-columns:repeat(var(--cols,4),1fr)}
.pg-cell{aspect-ratio:2/3}
.pg-card{display:block;width:100%;height:100%;object-fit:cover;transform:scale(0);will-change:transform}
.pg-outro{position:relative;z-index:10;height:100vh;background:#000}
.pg-veil{position:fixed;inset:0;z-index:12;background:#fff;opacity:0;pointer-events:none}
.pg-cta{position:fixed;right:32px;bottom:32px;z-index:20;width:330px;height:174px;border-radius:1335px;background:#fff;
  display:flex;align-items:center;justify-content:center;transform:scale(0);transform-origin:right bottom;
  mix-blend-mode:exclusion;text-decoration:none;pointer-events:none}
.pg-cta span{color:#fff;mix-blend-mode:exclusion;font:500 110px/1 'Inter Tight',Inter,sans-serif;letter-spacing:-.04em}
@media (max-width:640px){.pg-cta{left:16px;right:16px;bottom:60px;width:auto;height:100px}.pg-cta span{font-size:72px}}
```
```js
(() => {
  const IMAGES = ['p1.jpg', 'p2.jpg', 'p3.jpg' /* … ~10 */];
  const grid = document.getElementById('pgGrid');
  const veil = document.querySelector('.pg-veil'), cta = document.querySelector('.pg-cta');
  const outro = document.querySelector('.pg-outro');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let cells = [], cols = 0, ticking = false;
  function buildLayout(count, c) {
    const out = []; let placed = 0, r = 0;
    while (placed < count) {
      const row = new Array(c).fill(-1);
      const a = (r * 2 + (r % 2)) % c;
      row[a] = placed++;
      if (r % 3 === 0 && placed < count) { let b = (a + 2) % c; if (b === a) b = (a + 1) % c; row[b] = placed++; }
      out.push(...row); r++;
    }
    return out;
  }
  function render() {
    const c = innerWidth < 640 ? 2 : innerWidth < 1024 ? 3 : 4;
    if (c === cols) return;
    cols = c;
    grid.style.setProperty('--cols', c);
    grid.replaceChildren(...buildLayout(IMAGES.length, c).map((idx, k) => {
      const cell = document.createElement('div'); cell.className = 'pg-cell';
      if (idx >= 0) {
        const img = new Image(); img.src = IMAGES[idx]; img.alt = ''; img.decoding = 'async'; img.className = 'pg-card';
        img.style.transformOrigin = (k % c) < c / 2 ? 'right bottom' : 'left bottom';   // grow toward the centre
        cell.append(img);
      }
      return cell;
    }));
    cells = [...grid.querySelectorAll('.pg-card')].map((img) => [img.parentElement, img]);
  }
  function frame() {
    ticking = false;
    const vh = innerHeight;
    const rects = cells.map(([cell]) => cell.getBoundingClientRect());   // read all…
    cells.forEach(([, img], i) => {                                      // …then write (no layout thrash)
      const r = rects[i];
      let s = reduce ? 1 : 0;
      if (!reduce && r.bottom > 0 && r.top < vh) s = Math.min(1, (vh - r.top) / (vh * 0.6), r.bottom / (vh * 0.4));
      img.style.transform = `scale(${s.toFixed(4)})`;
    });
    const p = Math.min(1, Math.max(0, 1 - outro.getBoundingClientRect().top / vh));
    veil.style.opacity = p.toFixed(3);
    cta.style.transform = `scale(${p.toFixed(4)})`;
    cta.style.pointerEvents = p > 0.9 ? 'auto' : 'none';
  }
  const tick = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  render(); frame();
  addEventListener('scroll', tick, { passive: true });
  addEventListener('resize', () => { render(); tick(); });
})();
```
**Perf:** pause or `visibility:hidden` the hero video once the panel covers it (past 100vh).

---

## 4. Pinned heading with counter-drifting parallax columns (+ single-element parallax)

**What / when:** A "visual playground" section: a heading stays pinned in the centre while two columns of tilted square images scroll past over it at different speeds, one faster than the page and one slower. Also: a lone portrait drifting against the scroll beside a testimonial.

**Premium parameters**
- Section `min-height: 300vh`; pinned layer `sticky; top:0; height:100vh` underneath (z 1); columns absolutely over it (z 2), `grid-template-columns: 1fr 1fr`, gap `48 → 160px`, `max-width 1400px`.
- Cards `aspect-ratio 1`, `max-width 320px`, rotations `−4° / +3°`, big soft shadow `0 30px 60px rgba(0,0,0,.35)`, radius 20 px.
- Column speeds `-0.6` (rises faster) and `0.3` (lags), applied as `(progress − 0.5) × speed × innerHeight`.
- Single-element parallax: `offset = clamp(−(elementCentre − viewportCentre) × 0.2, −200px, 200px)`, measured on the untransformed parent.

**Implementation**
```html
<section class="pp">
  <div class="pp__pin"><div><p class="eyebrow">Explorations</p><h2>Visual <em>playground</em></h2></div></div>
  <div class="pp__cols">
    <div class="pp__col" data-speed="-0.6"><figure class="pp__card">…</figure><figure class="pp__card">…</figure><figure class="pp__card">…</figure></div>
    <div class="pp__col" data-speed="0.3"><figure class="pp__card">…</figure><figure class="pp__card">…</figure><figure class="pp__card">…</figure></div>
  </div>
</section>
```
```css
.pp{position:relative;min-height:300vh}
.pp__pin{position:sticky;top:0;height:100vh;display:grid;place-items:center;text-align:center;z-index:1}
.pp__cols{position:absolute;inset:0;z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:clamp(48px,10vw,160px);
  max-width:1400px;margin:0 auto;padding:30vh 24px;pointer-events:none}
.pp__col{display:flex;flex-direction:column;gap:30vh;will-change:transform}
.pp__col:nth-child(2){padding-top:40vh}
.pp__col:nth-child(1) .pp__card{margin-left:auto}
.pp__card{pointer-events:auto;aspect-ratio:1;width:100%;max-width:320px;margin:0;border-radius:20px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.pp__card:nth-child(odd){rotate:-4deg}
.pp__card:nth-child(even){rotate:3deg}
.pp__card img{width:100%;height:100%;object-fit:cover}
```
```js
(() => {
  const sec = document.querySelector('.pp');
  const cols = [...sec.querySelectorAll('.pp__col')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let ticking = false;
  const update = () => {
    ticking = false;
    const r = sec.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, -r.top / (r.height - innerHeight)));
    cols.forEach((c) => {
      const y = reduce ? 0 : (p - 0.5) * parseFloat(c.dataset.speed) * innerHeight;
      c.style.transform = `translate3d(0, ${y.toFixed(1)}px, 0)`;
    });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('resize', update);
  update();
})();
// Single-element parallax: <div class="parallax-frame"><img data-parallax="0.2" …></div>
(() => {
  const items = [...document.querySelectorAll('[data-parallax]')];
  if (!items.length || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let ticking = false;
  const update = () => {
    ticking = false;
    items.forEach((el) => {
      const r = el.parentElement.getBoundingClientRect();
      const delta = r.top + r.height / 2 - innerHeight / 2;
      const y = Math.max(-200, Math.min(200, -delta * parseFloat(el.dataset.parallax)));
      el.style.transform = `translate3d(0, ${y.toFixed(1)}px, 0)`;
    });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
})();
```
**GSAP variant:** `ScrollTrigger.create({ trigger: '.pp', start: 'top top', end: 'bottom bottom', pin: '.pp__pin', pinSpacing: false })` and `gsap.to('.pp__col:first-child', { yPercent: -30, ease: 'none', scrollTrigger: { trigger: '.pp', scrub: true } })` (load `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js` + `ScrollTrigger.min.js`, then `gsap.registerPlugin(ScrollTrigger)`).

**Mobile:** on one column (<640 px) reduce speeds by half and the gap to 48 px, or show the cards as a plain stack.

---

## 5. Sticky stacking cards that scale down

**What / when:** Project cards pin near the top of the viewport one after another. Each new card slides over the previous one, and the cards underneath shrink slightly with a sliver of their top edge still visible, like a deck being dealt. For case studies, project lists and process steps (3–5 cards).

**Premium parameters**
- Each card sits in its own sticky slot (`sticky; top:0; height:85vh`), offset `top: i × 28px` so earlier cards peek out above later ones. Slot padding-top 6 rem (8 rem desktop).
- Target scale per card `1 − (n − 1 − i) × 0.03` (3 cards: .94, .97, 1), interpolated from 1 at section progress `i/n` to the target at progress 1 (section top at viewport top → section bottom at viewport bottom). `transform-origin: top center`.
- Cards: very large radii (40 → 60 px), a 2 px light border (`#D7E2EA`) on near-black (`#0C0C0C`), an inner image grid (40 % column with two stacked images, 60 % column with one tall image) at 40–60 px radii.

**Implementation**
```html
<section class="stack">
  <div class="stack-slot"><article class="stack-card" style="--i:0">…</article></div>
  <div class="stack-slot"><article class="stack-card" style="--i:1">…</article></div>
  <div class="stack-slot"><article class="stack-card" style="--i:2">…</article></div>
</section>
```
```css
.stack{position:relative;padding-bottom:10vh}
.stack-slot{position:sticky;top:0;height:85vh;display:flex;justify-content:center;align-items:flex-start;padding-top:clamp(6rem,10vh,8rem)}
.stack-card{position:relative;top:calc(var(--i) * 28px);width:min(1200px,100%);transform-origin:top center;will-change:transform;
  border-radius:clamp(40px,5vw,60px);border:2px solid #D7E2EA;background:#0C0C0C;padding:clamp(16px,2vw,32px)}
```
```js
(function stackCards(section) {
  const cards = [...section.querySelectorAll('.stack-card')];
  const n = cards.length;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;   // keep sticky, skip scaling
  let ticking = false;
  const update = () => {
    ticking = false;
    const r = section.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, -r.top / Math.max(1, r.height - innerHeight)));
    cards.forEach((card, i) => {
      const target = 1 - (n - 1 - i) * 0.03;
      const t = Math.min(1, Math.max(0, (p - i / n) / (1 - i / n)));
      card.style.transform = `scale(${1 + (target - 1) * t})`;
    });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('resize', update);
  update();
})(document.querySelector('.stack'));
```
**Framer Motion variant**
```tsx
const { scrollYProgress } = useScroll({ target: ref, offset: ['start start', 'end end'] });
const scale = useTransform(scrollYProgress, [i / n, 1], [1, 1 - (n - 1 - i) * 0.03]);   // per card
<div className="h-[85vh] sticky top-0 flex items-start justify-center pt-24 md:pt-32">
  <motion.article style={{ scale, top: i * 28 }} className="relative origin-top …" />
</div>
```

---

## 6. Scroll-linked opposing marquee rows

**What / when:** Two rows of work thumbnails slide horizontally *as you scroll vertically*: the top row to the right, the bottom row to the left. Scrolling becomes a showreel. Use it right after a hero on portfolio or studio pages, or as a "wall of work".

**Premium parameters**
- `offset = (innerHeight − sectionRect.top) × 0.3` (0 when the section's top enters). Row A `translateX(base + offset)`, row B `translateX(base − offset)`.
- Each row's content is **tripled** and starts at `base = −33.333%` (one set to the left), so neither direction ever shows an empty edge. Mark duplicate sets `aria-hidden="true"`.
- Tiles 420 × 270 px (260 × 168 on phones), radius 16 px, `object-fit:cover`, 12 px gaps between tiles and rows; section padding-top 6–10 rem.
- Muted looping MP4/WebM or animated WebP rather than GIF.

**Implementation**
```html
<section class="scroll-rows">
  <div class="sr-row" data-dir="1"><!-- 3 × [tile tile tile …] --></div>
  <div class="sr-row" data-dir="-1"><!-- 3 × [tile tile tile …] --></div>
</section>
```
```css
.scroll-rows{overflow:hidden;padding:clamp(96px,12vw,160px) 0 40px;display:grid;gap:12px}
.sr-row{display:flex;gap:12px;width:max-content;will-change:transform;transform:translate3d(-33.333%,0,0)}
.sr-row img,.sr-row video{width:420px;height:270px;flex:none;border-radius:16px;object-fit:cover;display:block}
@media (max-width:640px){.sr-row img,.sr-row video{width:260px;height:168px}}
```
```js
(function scrollRows(section, factor = 0.3) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const rows = [...section.querySelectorAll('.sr-row')];
  let ticking = false;
  const update = () => {
    ticking = false;
    const offset = (innerHeight - section.getBoundingClientRect().top) * factor;
    rows.forEach((row) => { row.style.transform = `translate3d(calc(-33.333% + ${offset * +row.dataset.dir}px),0,0)`; });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('resize', update);
  update();
})(document.querySelector('.scroll-rows'));
```
(`.scroll-rows` clips its own content; it is not an ancestor of anything sticky, so `overflow:hidden` is fine here.)

---

## 7. 3D tilted text crawl on scroll (spring-smoothed)

**What / when:** A large centred paragraph tilted back in perspective (like an opening crawl) drifts upward as the section scrolls past, lagging on a heavy spring and fading in mid-way. Turns a plain manifesto paragraph into a cinematic moment over background video.

**Premium parameters**
- Container `perspective: 400px`; text `rotateX(24deg) translateY(y) translateZ(15px)`.
- `y` maps progress `0 → 1` to `60px → −120px`; opacity `0 → 1` between progress **0.3 and 0.5**.
- Progress = section from entering at the bottom to leaving at the top, smoothed by a spring **stiffness 15, damping 32, mass 1.8** (heavy, overdamped: the floaty feel).
- Type `clamp(22px, 3.2vw, 42px)`, lh 1.35, `-.02em`, `user-select:none`; a 180 px top gradient from near-black blends the section edge.

**Implementation**
```html
<section class="crawl">
  <video class="crawl__bg" src="VIDEO_URL.mp4" autoplay muted loop playsinline aria-hidden="true"></video>
  <div class="crawl__fade" aria-hidden="true"></div>
  <div class="crawl__stage"><p class="crawl__text">Your manifesto paragraph…</p></div>
</section>
```
```css
.crawl{position:relative;height:100vh;height:100dvh;overflow:hidden;display:grid;place-items:center;background:#000}
.crawl__bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.crawl__fade{position:absolute;left:0;right:0;top:0;height:180px;z-index:1;background:linear-gradient(#010103,transparent)}
.crawl__stage{position:relative;z-index:2;max-width:64rem;perspective:400px}
.crawl__text{margin:0;padding:0 1.5rem;text-align:center;color:#fff;font-size:clamp(22px,3.2vw,42px);line-height:1.35;
  letter-spacing:-.02em;user-select:none;opacity:var(--o,0);transform:rotateX(24deg) translateY(var(--y,60px)) translateZ(15px)}
```
```js
(() => {
  const sec = document.querySelector('.crawl'), txt = sec.querySelector('.crawl__text');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const K = 15, C = 32, M = 1.8;                         // spring constants
  let x = 0, v = 0, last = performance.now();
  function frame(now) {
    const dt = Math.min(0.032, (now - last) / 1000); last = now;
    const r = sec.getBoundingClientRect();
    if (r.bottom > -200 && r.top < innerHeight + 200) {   // only work near the viewport
      const target = Math.min(1, Math.max(0, (innerHeight - r.top) / (innerHeight + r.height)));
      if (reduce) { x = target; v = 0; }
      else { const a = (-K * (x - target) - C * v) / M; v += a * dt; x += v * dt; }   // semi-implicit Euler
      txt.style.setProperty('--y', (60 - 180 * x).toFixed(2) + 'px');
      txt.style.setProperty('--o', Math.min(1, Math.max(0, (x - 0.3) / 0.2)).toFixed(3));
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
```
**Framer Motion variant**
```tsx
const { scrollYProgress } = useScroll({ target: ref, offset: ['start end', 'end start'] });
const smooth = useSpring(scrollYProgress, { stiffness: 15, damping: 32, mass: 1.8 });
const y = useTransform(smooth, [0, 1], [60, -120]);
const opacity = useTransform(smooth, [0.3, 0.5], [0, 1]);
const transform = useMotionTemplate`rotateX(24deg) translateY(${y}px) translateZ(15px)`;
// <div style={{ perspective: 400 }}><motion.p style={{ transform, opacity }}>…</motion.p></div>
```
**A11y:** the text is real DOM text, so it stays readable to screen readers; under reduced motion it tracks scroll without the spring lag.
