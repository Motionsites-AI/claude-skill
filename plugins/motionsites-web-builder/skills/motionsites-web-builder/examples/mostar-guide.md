<!-- Mostar Guide · Travel · 639 likes · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260730_235046_ab8d2f0d-42b9-4091-8371-cdefe46e898f.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=mostar-guide -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

# PROMPT — Recreate "Mostar city" cinematic scroll page exactly

Build a **single standalone page** (`index.html` + `styles.css` + `script.js`, vanilla — no frameworks, no build step, no local assets). Every image and font must be loaded from the **remote URLs below**. Reproduce all values verbatim; they are not approximations.

---

## 1. Remote assets (the only allowed sources)

**Font — display serif, family name must be `"Ogg Medium"`**
```
https://dcym8fthxf5uu.cloudfront.net/fonts/247a073c-29f5-4a89-aa3a-741020f346fc/OggText-Medium.woff2
```

**Scene photographs (transparent-edge PNG layers)**

| Layer role | URL |
|---|---|
| Sky / farthest background | `https://raft-blast-61784561.figma.site/_assets/v11/16b5007d9c93971e26ffe4e0e3e37946f6bd538c.png` |
| Back "four" glow layer | `https://raft-blast-61784561.figma.site/_assets/v11/8a7f8af50e0ce92ec2e228e7b0b4112178c51cf1.png` |
| Bazaar mid-back | `https://raft-blast-61784561.figma.site/_assets/v11/864afe00e41e2fa20a5aa546e15cb807e0f81384.png` |
| Splitframe LEFT | `https://raft-blast-61784561.figma.site/_assets/v11/7536d7b60a1fce482cf6edf3f0bffd3bad5d0f8a.png` |
| Splitframe RIGHT | `https://raft-blast-61784561.figma.site/_assets/v11/392db6a6a6b98e868bd7f8d3f55bb719d51e5028.png` |
| Bridge foreground | `https://raft-blast-61784561.figma.site/_assets/v11/c6a6d8ef49bca43f708aa852692942c45ec950d4.png` |
| Frame-two river close-up | `https://raft-blast-61784561.figma.site/_assets/v11/ba75252bab2b1c510987b74837770f7bc8a6b2d4.png` |

**Sight-card pin icons (transparent cutouts, square)**

| Icon | URL |
|---|---|
| icon1 | `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260730_230438_d526b8b6-8a2e-4e3b-9993-3908acae03a7.png` |
| icon2 | `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260730_230442_140bc25b-b165-4249-904a-f708bff6970e.png` |
| icon3 | `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260730_230448_825949c9-ccdb-4857-b4a6-e349eccc9010.png` |

Favicon: `<link rel="icon" href="data:," />`

---

## 2. Document head

```html
<html lang="en">
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Mostar city</title>
<meta name="description" content="A cinematic three-screen scroll story for Mostar city." />
```
Stylesheet linked normally; script linked with `defer`.

---

## 3. Exact DOM tree and source order

Source order **is** the paint order for equal z-index, so keep it exactly:

```
main.site-shell
└─ section.cinema-scroll#cinema  [aria-label="Mostar cinematic scroll story"]
   └─ div.stage
      ├─ div.world
      │  ├─ img.scene-img.sky-img                    → sky URL
      │  ├─ header.site-header                       [aria-label="Primary navigation"]
      │  │  ├─ a.site-logo[href="#cinema"]           "Bosnia and Herzegovina"
      │  │  ├─ nav.site-nav [aria-label="Main menu"] Intro/#cinema, Bridge/#bridge,
      │  │  │                                        Bazaar/#bazaar, Routes/#routes
      │  │  └─ button.language-switcher              [aria-label="Change language"]
      │  │     ├─ span "EN"
      │  │     └─ span[aria-hidden="true"] "⌄"
      │  ├─ div.back-stack
      │  │  ├─ img.scene-img.back-img.back-four      → back-four URL
      │  │  ├─ section.sights-slider                 [aria-label="Mostar sights slider"]
      │  │  │  └─ div.sights-track
      │  │  │     └─ 5 × article.sight-card [tabindex="0" role="button"]
      │  │  └─ img.scene-img.back-img.back-bazaar    → bazaar URL
      │  ├─ div.sights-controls                      [aria-label="Slider controls"]
      │  │  ├─ button.sight-nav.sight-prev "←"       [aria-label="Previous sight"]
      │  │  └─ button.sight-nav.sight-next "→"       [aria-label="Next sight"]
      │  ├─ h1.hero-title                            "MOSTAR"
      │  ├─ img.scene-img.splitframe-img.splitframe-left   → splitframe-1 URL
      │  ├─ img.scene-img.splitframe-img.splitframe-right  → splitframe-2 URL
      │  ├─ img.scene-img.bridge-img                 → bridge URL
      │  ├─ img.scene-img.frame-two-img              → frame-two URL
      │  └─ div.shade
      ├─ section.intro-copy                          [aria-label="Mostar overview"]
      ├─ section.story-panel.story-panel-bridge      [aria-label="Old Bridge details"]
      └─ section.story-panel.story-panel-bazaar      [aria-label="Old town details"]
```

All `img.scene-img` have `alt=""`.

**Sight card internal order (per card):** `span.sight-kicker` → `img.sight-pin` → `h3` → `p`.

| # | aria-label | kicker | h3 | p | pin |
|---|---|---|---|---|---|
| 1 | Open Stari Most card | Old Bridge | Stari Most | The stone arch over the Neretva and Mostar's main landmark. | icon1 |
| 2 | Open Kujundziluk card | Bazaar Street | Kujundziluk | Copper shops, souvenirs, and the old bazaar lane by the bridge. | icon2 |
| 3 | Open Koski Mehmed Pasha Mosque card | Viewpoint | Koski Mehmed Pasha Mosque | A classic minaret view back toward Stari Most and the river. | icon3 |
| 4 | Open Kajtaz House card | Ottoman House | Kajtaz House | A preserved residential house showing Mostar's Ottoman layers. | icon1 |
| 5 | Open War Photo Exhibition card | Museum | War Photo Exhibition | A compact, moving stop for context on the city's recent history. | icon2 |

**intro-copy content:** `<p>A stone arch, emerald water, and a compact old city made for slow mornings, late light, and one unforgettable crossing.</p>` then `div.hero-tags[aria-label="Mostar highlights"]` with three spans: `Old Bridge`, `Neretva River`, `UNESCO old city`.

**story-panel-bridge:** `h2` = `The bridge is the city's compass.`; `p` = `Stari Most links the banks of the Neretva and anchors a historic quarter shaped by Ottoman, Mediterranean, and European layers.`; then `dl.facts` with two `div` groups: `dt 1566 / dd Original bridge completed` and `dt 2005 / dd Old Bridge Area inscribed by UNESCO`.

**story-panel-bazaar:** `h2` = `The bazaar keeps Mostar close.`; `p` = `Stone lanes, mosque courtyards, copper stalls, and riverside coffee stay within a short walk of Stari Most.`; then `button.note-button` containing `span[aria-hidden="true"] ↗` and `span Open old town notes`.

---

## 4. CSS custom properties — exact `:root` block

```css
:root {
  --mx: 0; --my: 0;
  --back-opacity: 1; --back-x: 0px; --back-y: 0px; --back-scale: 0.76;
  --four-y: 10vh; --four-scale: 0.78;
  --bazaar-y: 20vh;
  --blur-px: 0px; --back-brightness: 1;
  --bazaar-blur-px: 0px; --bazaar-brightness: 1; --bazaar-saturation: 1;
  --shade-opacity: 1; --shade-z: 2;
  --shade-top-alpha: 0; --shade-mid-alpha: 0; --shade-bottom-alpha: 0;
  --blur-tint: 74, 181, 224;
  --title-y: 0px; --title-scale: 1; --title-opacity: 1;
  --bridge-x: -50%; --bridge-y: 0px; --bridge-bottom: 5vh;
  --bridge-width: 67.2vw; --bridge-scale: 1.02;
  --split-left-x: -50%;  --split-left-y: 0px;  --split-left-scale: 1;
  --split-right-x: -50%; --split-right-y: 0px; --split-right-scale: 1;
  --frame2-opacity: 0; --frame2-x: -50%; --frame2-y: -50%; --frame2-scale: 1.06;
  --intro-copy-y: 0px; --intro-copy-opacity: 1;
  --panel2-opacity: 0; --panel2-y: calc(-50% + 58px);
  --panel3-opacity: 0; --panel3-y: calc(-50% + 58px);
  --sights-opacity: 0; --sights-controls-opacity: 0; --sights-y: 0px;
  --sights-enter-x: 420vw; --sights-visibility: hidden;
  --sights-shift: 0px; --sights-scale: 1;
  --sights-top: clamp(112px, 19vh, 220px);
  --sights-screen-top: clamp(112px, 19vh, 220px);
  --ink: #111411; --paper: #fdf1e1; --shadow: rgba(0, 0, 0, 0.32);
  font-family: Inter, Satoshi, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--paper);
  background: #0b1110;
  letter-spacing: 0;
}
```

Global: `* { box-sizing: border-box }`; `html { min-height:100%; scroll-behavior:smooth; background:#0b1110 }`; `body { min-height:100%; margin:0; overflow-x:clip; background:#0b1110 }`; `button { border:0; font:inherit }`; `.site-shell { min-height:100vh }`.

---

## 5. Exact positioning of every element

**Scroll rig**
- `.cinema-scroll { position: relative; height: calc(100vh + 3700px) }`
- `.stage { position: sticky; top: 0; height: 100vh; min-height: 620px; overflow: hidden; isolation: isolate; background: #7fb4d4 }`
- These are all `position: absolute`: `.world, .back-stack, .sky-img, .shade, .scene-img, .site-header, .sights-slider, .sights-controls, .hero-title, .intro-copy, .story-panel`
- `.world { inset: 0; overflow: hidden; background: #79b7dd }`

**Header (z-index 10)** — `top:0; left:0; right:0;` `display:grid; grid-template-columns: minmax(260px,1fr) auto minmax(260px,1fr); align-items:center; gap:32px; padding:32px; color:rgba(253,241,225,0.86); pointer-events:auto`
- `.site-logo` — `justify-self:start`, Ogg Medium 24px/1 weight 500, `rgba(253,241,225,0.92)`, no underline, `white-space:nowrap`
- `.site-nav` — flex, centered, `gap: clamp(24px, 2.2vw, 44px)`
- `.site-nav a, .language-switcher` — `rgba(253,241,225,0.86)`, `font-weight:700`, `line-height:1`, `text-shadow: 0 2px 16px rgba(0,0,0,0.2)`; `.site-nav a` overrides to `font-size:20px; font-weight:400`
- `.language-switcher` — `justify-self:end`, inline-flex centered, `gap:5px`, `padding:0`, transparent bg, `font-size:16px`, `cursor:pointer`; its spans are inline-flex, `line-height:1`

**Scene images (shared)** — `display:block; user-select:none; -webkit-user-drag:none; will-change: transform, opacity, filter; pointer-events:none`

**Sky (z 0)** — `inset:0; width:100%; height:100%; object-fit:cover; transform:none;` `filter: blur(var(--blur-px)) brightness(var(--back-brightness))`

**`.back-stack` (z 1)** — `top:0; bottom:0; left:-3vw; right:-3vw;` `opacity: var(--back-opacity)`; `transform: translate3d(var(--back-x), var(--back-y), 0) scale(var(--back-scale))`; `transform-origin: 50% 100%`; `will-change: transform, filter, opacity`

**`.back-img` base** — `inset:0; width:100%; height:100%; object-fit:cover;` `filter: blur(var(--blur-px)) brightness(var(--back-brightness))`

**Both `.back-bazaar` and `.back-four` override** — `top:auto; bottom:0; left:48%; right:auto; width:112%; height:auto; object-fit:contain`
- `.back-bazaar` — `z-index:3; opacity:1;` `filter: blur(var(--bazaar-blur-px)) brightness(var(--bazaar-brightness)) saturate(var(--bazaar-saturation));` `transform: translate3d(-50%, var(--bazaar-y), 0) scale(0.86)`
- `.back-four` — `z-index:1; opacity:0.72; mix-blend-mode:screen;` `transform: translate3d(-50%, calc(var(--four-y) - 110px), 0) scale(var(--four-scale))`

**`.sights-slider` (z 2)** — `left:0; right:0; top: var(--sights-top); padding:0;` `opacity:1` (literal — the fade is done by `visibility` + X translate, not opacity); `visibility: var(--sights-visibility);` `transform: translate3d(var(--sights-enter-x), var(--sights-y), 0) scale(var(--sights-scale));` `transform-origin: 0 0; pointer-events:auto; will-change:transform`

**`.sights-track`** — `display:flex; gap: clamp(16px, 1.15vw, 24px); align-items:stretch;` `transform: translate3d(calc(var(--sights-shift) - 18vw), 0, 0);` `transition: transform 640ms cubic-bezier(0.22, 1, 0.36, 1); will-change:transform`. Class `.is-jumping { transition: none }`

**`.sight-card`** — `position:relative; flex: 0 0 clamp(360px, 19.4vw, 430px); height:220px; padding:24px; overflow:hidden; border:1px solid rgba(253,241,225,0.42); border-radius:24px; color:#000; background:#fdf1e1; box-shadow: 0 18px 52px rgba(2,47,64,0.12); backdrop-filter:none; cursor:pointer; pointer-events:auto; user-select:none`. `::before/::after { content:none }`. Kicker/h3/p carry `text-shadow:none` and `position:relative; z-index:1`. `:focus-visible` and `.is-active` → `outline:none`.
- `.sight-kicker` — `display:block; margin-bottom:56px; color:#000; font-size:12px; font-weight:500; line-height:1.05; text-transform:uppercase`
- `.sight-pin` — `position:absolute; top:24px; right:24px; width:67.2px; height:67.2px; pointer-events:none`
- `.sight-card h3` — `position:absolute; left:24px; right:24px; bottom: calc(24px + (16px * 1.16 * 2) + 12px); max-width: calc(100% - 76px); margin:0; color:#000; font-size:24px; font-weight:800; line-height:0.95; overflow:hidden; text-overflow:ellipsis; white-space:nowrap`
- `.sight-card p` — `position:absolute; left:24px; right:24px; bottom:24px; max-width:100%; margin:12px 0 0; color:#000; font-size:16px; font-weight:400; line-height:1.16; display:-webkit-box; max-height: calc(2em * 1.16); overflow:hidden; -webkit-box-orient:vertical; -webkit-line-clamp:2`

**`.sights-controls` (z 5)** — `left:48px; right:auto; top: calc(var(--sights-screen-top) + 220px + 16px); display:flex; justify-content:flex-start; gap:14px;` `opacity: var(--sights-controls-opacity);` `transform: translate3d(0, var(--sights-y), 0);` `pointer-events:none; will-change:transform, opacity`. `.is-ready { pointer-events:auto }`
- `.sight-nav` — `54px × 54px`, inline-flex centered, `border-radius:999px; color:#111411; background:rgba(253,241,225,0.94); box-shadow: 0 18px 36px rgba(0,0,0,0.2); cursor:pointer`

**`.hero-title` (z 3)** — `left:50%; top: clamp(122px, 19vh, 205px); width: min(94vw, 1780px); margin:0; color:#fdf1e1;` Ogg Medium `font-size:14rem; font-weight:500; line-height:0.78; text-align:center; text-shadow:none;` `transform: translate3d(-50%, var(--title-y), 0) scale(var(--title-scale));` `opacity: var(--title-opacity); will-change: transform, opacity`

**`.bridge-img` (z 4)** — `left:50%; bottom: var(--bridge-bottom); width: min(var(--bridge-width), 2140px); height:auto;` `transform: translate3d(var(--bridge-x), var(--bridge-y), 0) scale(var(--bridge-scale));` `transform-origin: 50% 48%`

**`.splitframe-img` (z 6)** — `left:50%; bottom:-2vh; width: min(118vw, 2240px); height:auto; pointer-events:none`
- `.splitframe-left` — `transform: translate3d(var(--split-left-x), var(--split-left-y), 0) scale(var(--split-left-scale)); transform-origin: 21% 52%`
- `.splitframe-right` — `transform: translate3d(var(--split-right-x), var(--split-right-y), 0) scale(var(--split-right-scale)); transform-origin: 79% 52%`

**`.frame-two-img` (z 5)** — `filter: none !important; backdrop-filter:none; left:50%; top:50%; width: min(122vw, 2160px); height:auto;` `opacity: var(--frame2-opacity);` `transform: translate3d(var(--frame2-x), var(--frame2-y), 0) scale(var(--frame2-scale)); transform-origin: 50% 48%`

**`.shade`** — `inset:0; z-index: var(--shade-z); pointer-events:none; opacity: var(--shade-opacity);`
```css
background: linear-gradient(180deg,
  rgba(var(--blur-tint), var(--shade-top-alpha)) 0%,
  rgba(var(--blur-tint), var(--shade-mid-alpha)) 48%,
  rgba(var(--blur-tint), var(--shade-bottom-alpha)) 100%);
```

**`.intro-copy` (z 9)** — `left:50%; bottom: clamp(56px, 28vh, 400px); width: min(560px, calc(100vw - 40px)); text-align:center;` `transform: translate3d(-50%, var(--intro-copy-y), 0); opacity: var(--intro-copy-opacity); will-change: transform, opacity`
- `p` — `margin:0 auto; max-width:560px; color:#fdf1e1; font-size:1.18rem; font-weight:500; line-height:1.18; text-shadow: 0 2px 18px rgba(0,0,0,0.42)`
- `.hero-tags` — flex, wrap, centered, `gap:10px; margin-top:26px`
- `.hero-tags span` — `min-height:42px`, inline-flex centered, `padding:0 25px; color:var(--ink); border-radius:999px; background:#fdf1e1; font-size:0.98rem; font-weight:500; box-shadow: 0 12px 30px rgba(0,0,0,0.18)`

**`.story-panel` (z 10)** — `left:50%; top:45%; width: min(760px, calc(100vw - 42px)); text-align:center; pointer-events:none; transform: translate3d(-50%, -50%, 0); will-change: transform, opacity`
- `h2` — `margin:0; color:#fdf1e1;` Ogg Medium `font-size:4.75rem; font-weight:500; line-height:0.95; text-shadow: 0 16px 38px var(--shadow)`
- `p` — `width: min(520px, 100%); margin:26px auto 0; color:#fdf1e1; font-size:1.14rem; font-weight:500; line-height:1.18; text-shadow: 0 2px 18px rgba(0,0,0,0.42)`
- `.story-panel-bridge` — `top:60%; opacity: var(--panel2-opacity); transform: translate3d(-50%, var(--panel2-y), 0)`
- `.story-panel-bazaar` — `top:29%; opacity: var(--panel3-opacity); transform: translate3d(-50%, var(--panel3-y), 0)`
- `.facts` — `display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap:86px; width: min(470px, 100%); margin:72px auto 0`
- `.facts dt` — `color:#fdf1e1;` Ogg Medium `font-size:4.2rem; font-weight:500; line-height:0.9; text-shadow: 0 14px 34px var(--shadow)`
- `.facts dd` — `margin:18px 0 0; color:#fdf1e1; font-size:1rem; font-weight:500; line-height:1.14; text-shadow: 0 2px 18px rgba(0,0,0,0.42)`
- `.note-button` — `min-height:50px; margin-top:28px;` inline-flex centered `gap:12px; padding:0 28px; border-radius:999px; color:var(--ink); background:#fdf1e1; box-shadow: 0 16px 34px rgba(0,0,0,0.18); pointer-events:auto; cursor:pointer`; first span `font-size:1.25rem; line-height:1`

---

## 6. Media queries (exact)

```css
@media (max-width: 1500px) {
  .hero-title { font-size: 11rem; }
  .story-panel h2 { font-size: 4.1rem; }
}

@media (max-width: 1100px) {
  .hero-title { top: 15vh; font-size: 7.5rem; }
  .bridge-img { width: 138vw; }
  .frame-two-img { width: 132vw; }
  .story-panel h2 { font-size: 3.2rem; }
  .facts { gap: 34px; margin-top: 44px; }
  .facts dt { font-size: 3.2rem; }
  .sight-card { flex-basis: clamp(320px, 40vw, 390px); min-height: 178px; }
}

@media (max-width: 640px) {
  .stage { min-height: 640px; }
  .site-header { grid-template-columns: 1fr auto; gap: 18px; padding: 24px; }
  .site-nav { grid-column: 1 / -1; grid-row: 2; justify-content: flex-start;
              gap: 18px; overflow-x: auto; scrollbar-width: none; }
  .site-nav::-webkit-scrollbar { display: none; }
  .hero-title { top: 16vh; font-size: 4.5rem; }
  .bridge-img { bottom: 2vh; width: 190vw; }
  .frame-two-img { width: 176vw; }
  .intro-copy { bottom: 42px; }
  .intro-copy p, .story-panel p { font-size: 1rem; }
  .hero-tags { gap: 8px; }
  .hero-tags span { min-height: 38px; padding: 0 16px; font-size: 0.88rem; }
  .story-panel { top: 42%; }
  .story-panel-bazaar { top: 26%; }
  .story-panel h2 { font-size: 2.45rem; }
  .facts { gap: 18px; margin-top: 34px; }
  .facts dt { font-size: 2.5rem; }
  .sights-slider { padding: 0; }
  .sights-track { gap: 12px; transform: translate3d(calc(var(--sights-shift) - 18vw), 0, 0); }
  .sight-card { flex-basis: min(82vw, 330px); height: 220px; padding: 24px; border-radius: 24px; }
  .sights-controls { top: calc(var(--sights-screen-top) + 236px); }
  .sight-card h3 { max-width: 78%; }
  .sight-card p { max-width: 100%; margin-top: 10px; }
  .sight-kicker { margin-bottom: 56px; }
  .sight-pin { top: 24px; right: 24px; width: 57.6px; height: 57.6px; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .scene-img, .back-stack, .hero-title, .intro-copy,
  .story-panel, .sights-track, .sights-slider { transition: none; }
}
```

---

## 7. JavaScript — animation engine, exact math

Query on load: `.cinema-scroll`, `document.documentElement`, `matchMedia("(prefers-reduced-motion: reduce)")`, `.sights-track`, `.sights-controls`, `.sight-prev`, `.sight-next`, and the original `.sight-card` list.

State: `targetMouseX/Y`, `mouseX/Y`, `targetScroll`, `smoothScroll`, `initialized`, `rafPending`, `sightCards`, `originalSightCount`, `activeSight = originalSightCount`.

**Helpers**
```js
clamp(v, min = 0, max = 1) => Math.min(max, Math.max(min, v))
smoothstep(e0, e1, v) => { const x = clamp((v - e0) / (e1 - e0)); return x * x * (3 - 2 * x); }
lerp(a, b, t) => a + (b - a) * t
segmentInOut(s, a, b, c, d) => {
  const enter = smoothstep(a, b, s), exit = smoothstep(c, d, s);
  return { enter, exit, active: enter * (1 - exit) };
}
getScrollDistance() => clamp(-section.getBoundingClientRect().top, 0,
                             section.offsetHeight - window.innerHeight)
```

**Per-frame `update()`**
```js
targetScroll = getScrollDistance();
if (!initialized || reduceMotion.matches) { smoothScroll = targetScroll; initialized = true; }
else { smoothScroll = lerp(smoothScroll, targetScroll, 0.14); }
if (Math.abs(smoothScroll - targetScroll) < 0.08) smoothScroll = targetScroll;

mouseX = lerp(mouseX, targetMouseX, 0.12);
mouseY = lerp(mouseY, targetMouseY, 0.12);

const frame2 = segmentInOut(smoothScroll, 560, 900, 1300, 1620);
const frame3 = segmentInOut(smoothScroll, 1760, 2140, 2540, 2700);
const progress = clamp(smoothScroll / 2700);
const introExit = smoothstep(90, 650, smoothScroll);
const sightsEnterRaw = smoothstep(2760, 3560, smoothScroll);
const sightsEnter = Math.pow(sightsEnterRaw, 1.55);
const sightsControlsEnter = smoothstep(3360, 3660, smoothScroll);
const blurActive = clamp(frame2.active + frame3.active);
const frame2Opacity = frame2.active * (1 - frame3.enter);
const splitDrift = Math.pow(frame2.enter, 1.5);
const panel2Opacity = frame2.active * (1 - frame2.exit);
const panel3Opacity = frame3.active * (1 - frame3.exit);
const backScale = 0.76 + progress * 0.2 + frame2.enter * 0.18 + frame3.enter * 0.16;
const sharedHeroY = progress * -74;
const sharedHeroScale = progress * 0.23;
const sightsScreenTop = Math.min(220, Math.max(112, window.innerHeight * 0.19)) - 50;
const sightsParentTop = window.innerHeight - (window.innerHeight - sightsScreenTop) / backScale;
```

**Variable writes (verbatim, `.toFixed` precision included)**
```js
--mx  = reduceMotion.matches ? 0 : mouseX      (4 decimals)
--my  = reduceMotion.matches ? 0 : mouseY      (4 decimals)

--back-opacity     = (1 - frame2.active * 0.06)
--back-x           = `${mouseX * -12}px`
--back-y           = `${mouseY * -4}px`
--back-scale       = backScale
--four-y           = `${10 + progress * 10}vh`
--four-scale       = 0.78 + progress * 0.16
--bazaar-y         = `${20 - progress * 8}vh`
--blur-px          = `${blurActive * 14}px`
--back-brightness  = 1 - blurActive * 0.255
--bazaar-blur-px   = `${frame2.active * 14}px`
--bazaar-brightness= 1 - frame2.active * 0.255 - frame3.active * 0.06
--bazaar-saturation= 1 + frame3.active * 0.18
--shade-opacity    = "1"
--shade-z          = frame2.active > 0.02 ? "2" : "0"
--shade-top-alpha    = blurActive * 0.465
--shade-mid-alpha    = blurActive * 0.42
--shade-bottom-alpha = blurActive * 0.51

--title-y        = `${introExit * -210}px`
--title-scale    = 1 - introExit * 0.08
--title-opacity  = 1 - introExit

--bridge-x      = `calc(-50% + ${mouseX * 18}px)`
--bridge-y      = `${mouseY * 8 + sharedHeroY - frame2.exit * 760}px`
--bridge-bottom = `${5 - frame2.enter * 13}vh`
--bridge-width  = `${67.2 + frame2.enter * 37.8}vw`
--bridge-scale  = 1.02 + sharedHeroScale + frame2.exit * 0.46

--split-left-x      = `calc(-50% + ${-splitDrift * 46}vw + ${mouseX * 22}px)`
--split-left-y      = `${mouseY * 10 + sharedHeroY - splitDrift * 180}px`
--split-left-scale  = 1 + sharedHeroScale + frame2.enter * 0.74
--split-right-x     = `calc(-50% + ${ splitDrift * 46}vw + ${mouseX * 22}px)`
--split-right-y     = `${mouseY * 10 + sharedHeroY - splitDrift * 180}px`
--split-right-scale = 1 + sharedHeroScale + frame2.enter * 0.74

--frame2-opacity = frame2Opacity
--frame2-x       = `calc(-50% + ${mouseX * 10}px)`
--frame2-y       = `calc(-50% + ${mouseY * 8 - frame2.exit * 150}px)`
--frame2-scale   = 1.06 + frame2.enter * 0.08 + frame2.exit * 0.08

--intro-copy-y       = `${introExit * 90}px`
--intro-copy-opacity = 1 - introExit
--panel2-opacity = panel2Opacity
--panel2-y       = `calc(-50% + ${-frame2.exit * 86 + (1 - frame2.enter) * 58}px)`
--panel3-opacity = panel3Opacity
--panel3-y       = `calc(-50% + ${-frame3.exit * 86 + (1 - frame3.enter) * 58}px)`

--sights-opacity          = sightsEnter
--sights-controls-opacity = sightsControlsEnter
sightsControls.classList.toggle("is-ready", sightsControlsEnter > 0.98)
--sights-visibility  = sightsEnter > 0.01 ? "visible" : "hidden"
--sights-y           = "0px"
--sights-enter-x     = `${(1 - sightsEnter) * 420}vw`
--sights-scale       = 1 / backScale
--sights-top         = `${sightsParentTop}px`
--sights-screen-top  = `${sightsScreenTop}px`
```

Re-request a frame while `|smoothScroll - targetScroll| > 0.08` or `|mouseX - targetMouseX| > 0.001` or `|mouseY - targetMouseY| > 0.001`. `requestTick()` guards with `rafPending` and calls `requestAnimationFrame(update)`.

**Listeners**
- `window scroll` → `requestTick`, `{ passive: true }`
- `window resize` → `updateSightSlider(); requestTick();`
- `window pointermove` → `targetMouseX = clientX / innerWidth - 0.5; targetMouseY = clientY / innerHeight - 0.5; requestTick();` `{ passive: true }`
- `.sight-prev` click → `moveSightSlider(-1)`; `.sight-next` click → `moveSightSlider(1)`
- On load: `setupSightSlider(); requestTick();`

---

## 8. Infinite slider logic (exact behavior)

```js
setupSightSlider():
  clear .sights-track (replaceChildren)
  for setIndex 0..2:                       // 3 identical sets = 15 cards
    for each original card:
      clone = card.cloneNode(true)
      clone.dataset.sightIndex = setIndex * originalCount + cardIndex
      append clone
  sightCards = all cloned cards
  activeSight = originalCount               // start in middle set
  per card: click → selectSightCard(card)
            keydown Enter or " " → preventDefault, selectSightCard(card)
  track transitionend → normalizeSightSlider
  updateSightSlider()

updateSightSlider():
  cardWidth = sightCards[0].offsetWidth
  gap = parseFloat(getComputedStyle(track).columnGap || "0")
  --sights-shift = `${-(cardWidth + gap) * activeSight}px`
  toggle .is-active on the card whose index === activeSight

moveSightSlider(dir): activeSight += dir; updateSightSlider()
selectSightCard(card): activeSight = Number(card.dataset.sightIndex) (if finite); updateSightSlider()

jumpSightSlider(i):  add .is-jumping; activeSight = i; updateSightSlider();
                     double requestAnimationFrame → remove .is-jumping
normalizeSightSlider(): if activeSight >= originalCount * 2 → jump(activeSight - originalCount)
                        else if activeSight < originalCount → jump(activeSight + originalCount)
```

---

## 9. Resulting choreography (acceptance criteria)

Scrubbing ~3700px through the sticky stage must produce, in order:

1. **0–650px:** `MOSTAR` rises `-210px` while scaling to `0.92` and fading out; intro paragraph + 3 cream pills sink `+90px` and fade. Sky, back-stack, bridge, and splitframes drift subtly with the pointer the whole time.
2. **560–1620px:** bridge widens `67.2vw → 105vw`, its bottom lifts `5vh → -8vh`, then it launches up `-760px` and scales `+0.46` on exit. The two splitframe halves part symmetrically to ∓`46vw` (eased `enter^1.5`), rise `-180px`, scale `+0.74`. The frame-two river close-up fades in behind them. Global blur ramps to `14px`, brightness drops ~25.5%, and the blue `74,181,224` shade gradient rises to alphas `0.465 / 0.42 / 0.51`. Bridge story panel fades in at `top:60%`, sliding from `+58px` to `-86px`.
3. **1760–2700px:** bazaar layer gains `+0.18` saturation while the bridge panel exits; bazaar story panel fades in at `top:29%` with the same `+58px → -86px` slide and its `Open old town notes` pill.
4. **2760–3560px:** the sights slider flies in from `420vw` on X (`enter^1.55` easing), becoming visible past `0.01`, counter-scaled by `1 / backScale` so cards stay screen-true while the back stack keeps zooming; its top is solved so cards sit at `clamp(innerHeight*0.19, 112, 220) - 50` px on screen.
5. **3360–3660px:** the two round `←` `→` buttons fade in at `left:48px` beneath the cards and become clickable only past `0.98`. Prev/next and card clicks slide the track with the `640ms cubic-bezier(0.22, 1, 0.36, 1)` transition and loop seamlessly via the 3-set clone + instant-jump normalization.

Under `prefers-reduced-motion`, scroll smoothing and pointer parallax are bypassed (values snap, `--mx`/`--my` forced to 0) and layer transitions are disabled — the composition still scrubs, just without inertia.
