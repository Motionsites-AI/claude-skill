<!-- Agent Wave · AI · 801 likes · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260818_075101_ea68beb6-4f5a-4e14-9dd0-6f07c6a8e27c.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=agent-wave -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Recreate this exact single-viewport landing page for **Vesper.ai**. Document title: `Vesper.ai — Operational AI Infrastructure`. `lang="en"`. One HTML file with inline CSS and a small IIFE for the menu + animation fallback. Pure black `#000000`. No extra sections, cards, forms, pricing tables, or footer beyond the three stats. Do **not** add a video, WebGL, Three.js, or Lottie. Do **not** invent a CloudFront URL.

Force black immediately so the page can never flash white:

- First CSS rule: `html, body { background: #000000 !important; color: #ffffff; }`
- Body attribute: `style="background:#000;color:#fff"`
- Then again: `html, body { background: #000000; background: var(--bg, #000000); color: #ffffff; color: var(--text, #ffffff); }`

---

### Fonts (exact)

Self-hosted WOFF2s sitting next to `index.html`:

```css
@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url("inter.woff2") format("woff2");
}
@font-face {
  font-family: "Instrument Serif";
  font-style: italic;
  font-weight: 400;
  font-display: swap;
  src: url("instrument-serif-italic.woff2") format("woff2");
}
```

Stacks:

- UI / logo / nav / buttons / badge / lede / stats: `"Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
- **Only** the H1 words `AI agents`: `"Instrument Serif", "Times New Roman", Times, serif`

If those files are missing, load this exact Google Fonts CSS (Inter variable roman + Instrument Serif italic only):

```
https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900&family=Instrument+Serif:ital@1&display=swap
```

Body: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; overflow-x: hidden; position: relative`. `html { scroll-behavior: smooth }`. Universal reset: `box-sizing: border-box; margin: 0; padding: 0`. Links `color: inherit; text-decoration: none`. Buttons `font-family: inherit`.

---

### Image / asset URLs (exact — there are only these)

**1. Herovide obackgorumf 100% opacity no overlay**  
Relative file, same folder as the HTML:

```
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260818_072341_50851634-bbc3-4c33-9acc-7647d4db44aa.mp4
```

**3. Favicon (exact data URI)** — same mark as the logo, white:

```
data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cg transform='rotate(-30 12 12)'%3E%3Ccircle cx='7.3' cy='3.2' r='1.45'/%3E%3Crect x='5.5' y='4.7' width='3.6' height='14.6' rx='1.8'/%3E%3Crect x='14.9' y='4.7' width='3.6' height='14.6' rx='1.8'/%3E%3Ccircle cx='16.7' cy='20.8' r='1.45'/%3E%3C/g%3E%3C/svg%3E
```

No other images. All other icons are inline SVG.

---

### Tokens (default / ~1440px)

```
--bg: #000000
--text: #ffffff
--muted: #9a9a9a
--stat: #d8d8d8
--border: rgba(255, 255, 255, 0.16)
--border-soft: rgba(255, 255, 255, 0.12)

--logo: 15.5px
--logo-mark: 22px
--nav: 14px
--nav-h: 40px
--btn: 13.5px
--btn-h: 40px
--hero-btn-h: 42px
--h1: 48px
--lede: 15.5px
--badge: 12.5px
--stat-size: 13.5px
--header-y: 22px
--header-x: 40px
--stats-x: 72px
--stats-y: 36px
--hero-gap: 85px
--copy-max: 860px
--lede-max: 470px
```

---

### Layer stack (back → front)

1. `html/body` black  
2. `.hero-photo` + `::after` scrim  
3. `.page` — `position: relative; z-index: 1; display: grid; grid-template-rows: auto 1fr auto; min-height: 100vh / 100dvh`  
4. `.grain` at `z-index: 100`

Markup order inside body:

```
.grain
.hero-photo
.page
  .menu-backdrop
  header.header
  main.hero#top
  footer.stats
script
```

---

### Header — 3-column grid

`display: grid; grid-template-columns: 1fr auto 1fr; align-items: center;`  
Padding: `var(--header-y) var(--header-x) 10px`. `z-index: 50; position: relative`.

**Left — logo** `a.logo.appear.appear--scale` → `#top`, `aria-label="Vesper.ai"`.  
`display: inline-flex; align-items: center; gap: 9px; justify-self: start; font-size: var(--logo); font-weight: 600; letter-spacing: -0.03em; color: #fff`.

Mark SVG 22×22, `viewBox="0 0 24 24"`, `fill="currentColor"`, group `transform="rotate(-30 12 12)"`:

- `circle cx="7.3" cy="3.2" r="1.45"`
- `rect x="5.5" y="4.7" width="3.6" height="14.6" rx="1.8"`
- `rect x="14.9" y="4.7" width="3.6" height="14.6" rx="1.8"`
- `circle cx="16.7" cy="20.8" r="1.45"`

Wordmark: `Vesper` + `<span class="logo-suffix">.ai</span>` at `font-weight: 400`.

**Center — nav** `#site-nav`, `aria-label="Primary"`, `display: flex; align-items: center; gap: 8px; justify-self: center`.

| Label | href | appear class |
|---|---|---|
| Benefits | `#benefits` | `appear--scale` |
| How It Works | `#how-it-works` | `appear--soft` |
| FAQs | `#faqs` | `appear--scale` |
| Pricing | `#pricing` | `appear--soft` |

Each link is a **liquid-metal pill**: `height: var(--nav-h); padding: 0 18px; border-radius: 7px; overflow: hidden; position: relative;`  
`border: 1px solid rgba(198,198,198,0.55)`  
`background: linear-gradient(105deg, #050505 0%, #2a2a2a 48%, #4a4a4a 100%)`  
color `#f3f3f3`, `font-size: var(--nav)`, weight 400, `letter-spacing: -0.01em`, `white-space: nowrap`.  
Transition: `background / border-color / box-shadow 0.35s ease`.

Shine `::before`: `linear-gradient(115deg, transparent 30%, rgba(255,255,255,0.16) 50%, transparent 70%)`, idle `translateX(-120%)`, hover `translateX(120%)` over `0.6s ease`.

Hover: border `rgba(235,235,235,0.9)`, gradient `#111 → #3a3a3a 45% → #6a6a6a`, glow `0 0 18px rgba(200,210,230,0.18)`.

**Right — header CTA:** `a.btn.btn-solid.header-cta.appear.appear--scale` “Start for Free” → `#start`, `justify-self: end`.

**Burger** (hidden ≥901px, `display: none` → `display: grid` on phone): 42×42, `border-radius: 6px`, `border: 1px solid var(--border)`, `background: rgba(8,8,8,0.55)`, `z-index: 60`, `aria-controls="site-nav"`, `aria-expanded="false"`, label “Open menu”. Three white bars 16×1.5px, gap 5px, `border-radius: 1px`. Hover: border `rgba(255,255,255,0.32)`, bg `rgba(255,255,255,0.05)`. Open (`body.menu-open`): bar 1 `translateY(6.5px) rotate(45deg)`, bar 2 `opacity: 0`, bar 3 `translateY(-6.5px) rotate(-45deg)`, 0.25s / 0.2s.

---

### Buttons (shared liquid-glass language)

`.btn`: `position: relative; isolation: isolate; overflow: hidden; display: inline-flex; align-items: center; justify-content: center; height: var(--btn-h); padding: 0 16px; border-radius: 6px; font-size: var(--btn); font-weight: 500; letter-spacing: -0.02em; line-height: 1; white-space: nowrap; cursor: pointer`. Transitions 0.35s on background, border, shadow, color, filter.

Shine `::after`: `linear-gradient(115deg, transparent 20%, rgba(255,255,255,0.45) 48%, transparent 76%)`, idle `translateX(-130%)`, hover `translateX(130%)` in `0.65s ease`.

**Solid:**  
`background: linear-gradient(180deg, #ffffff 0%, #e7e7e7 48%, #cfcfcf 100%)`  
`color: #111; border: 1px solid #fff`  
`box-shadow: inset 0 1px 0 rgba(255,255,255,0.95)`  
Hover: `#fff → #f3f6ff 42% → #d5def2`, border `#f2f6ff`,  
`inset 0 1px 0 #fff, 0 0 22px rgba(186,208,255,0.35), 0 8px 18px rgba(255,255,255,0.12)`

Hero solid hover glow is slightly stronger: `0 0 26px rgba(186,208,255,0.4), 0 8px 18px rgba(255,255,255,0.14)`.

**Ghost (header-level):**  
`background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(0,0,0,0.45) 50%, rgba(160,175,200,0.08))`  
`color: #fff; border: 1px solid rgba(198,198,198,0.45)`  
`box-shadow: inset 0 1px 0 rgba(255,255,255,0.12)`  
Hover: `rgba(210,225,255,0.18) → rgba(0,0,0,0.35) 48% → rgba(180,195,220,0.16)`, border `rgba(220,230,255,0.75)`,  
`inset 0 1px 0 rgba(255,255,255,0.22), 0 0 20px rgba(170,200,255,0.22)`

**Hero ghost** (stronger frost):  
`background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(0,0,0,0.5) 46%, rgba(150,170,200,0.1))`  
`border: 1px solid rgba(198,198,198,0.55)`  
`backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px)`  
Hover glow `0 0 24px rgba(170,200,255,0.28)`, border `rgba(220,230,255,0.8)`.

Hero action buttons: height `var(--hero-btn-h)`, padding `0 18px`.

---

### Hero (bottom-centered, NOT vertically centered)

`.hero`: `display: flex; align-items: flex-end; justify-content: center; padding: 8px 24px var(--hero-gap); min-height: 0`.

`.hero-copy`: `position: relative; z-index: 1; flex-direction: column; align-items: center; text-align: center; max-width: var(--copy-max); width: 100%`.

**Badge** `.badge.appear.appear--pop` — text `Operational AI Infrastructure`  
`inline-flex; gap: 8px; margin-bottom: 22px; padding: 9px 15px; border: 0; border-radius: 5px`  
`background: linear-gradient(90deg, #7d7d7d 0%, #2a2a2a 52%, #0a0a0a 100%)`  
color `#f2f2f2`, `font-size: var(--badge)`, weight 400, `letter-spacing: -0.01em`.

Sparkle SVG 18×20, white, `filter: drop-shadow(0 0 3px rgba(255,255,255,0.45))`, path:

```
M12 2.6C12.55 2.6 12.88 3.15 13.08 4.7c.62 4.7 1.52 5.6 6.22 6.22 1.55.2 2.1.53 2.1 1.08s-.55.88-2.1 1.08c-4.7.62-5.6 1.52-6.22 6.22-.2 1.55-.53 2.1-1.08 2.1s-.88-.55-1.08-2.1c-.62-4.7-1.52-5.6-6.22-6.22C3.15 12.88 2.6 12.55 2.6 12s.55-.88 2.1-1.08c4.7-.62 5.6-1.52 6.22-6.22C11.12 3.15 11.45 2.6 12 2.6Z
```

**H1** two masked lines, Inter 500, `letter-spacing: -0.045em`, `line-height: 1.12`, `#fff`, column, centered:

- Line 1: `Train <em>AI agents</em> on your`
- Line 2: `workflows in minutes.`

`.headline-line`: `display: block; overflow: hidden; padding: 0.06em 0.15em 0.14em`.  
`em`: Instrument Serif italic 400, `font-size: 1.08em`, `letter-spacing: -0.03em`, color **`#9a9a9a`** (not white).

**Lede** `.lede.appear.appear--soft`, `max-width: var(--lede-max)`, `margin-top: 18px`, color `#9a9a9a`, `15.5px`, weight 400, `line-height: 1.55`, `letter-spacing: -0.015em`:

`Deploy adaptive AI agents that learn, execute, and scale operational tasks across your business.`

**Actions** `.hero-actions`: flex, wrap, center, gap `10px`, `margin-top: 26px`.

1. Solid `.appear.appear--btn`: `Start for Free` → `#start`  
2. Ghost `.appear.appear--side`: `See it in action` → `#demo`

---

### Stats footer

`.stats`: flex, `align-items: center; justify-content: space-between; gap: 24px;`  
padding `0 var(--stats-x) var(--stats-y)` and `padding-bottom: max(var(--stats-y), env(safe-area-inset-bottom))`, color `#d8d8d8`.

Each `.stat.appear.appear--stat`: `inline-flex; align-items: center; gap: 14px; font-size: var(--stat-size); letter-spacing: -0.015em; white-space: nowrap`. Icon 20×20 (`#e8e8e8`). Wide avatar icon 38×21.

**1. Dual-pill / workflow icon** (`viewBox="0 0 24 24"`):  
Left rect `x=3.4 y=2.6 w=7.2 h=18.8 rx=3.6` fill linear `#ffffff@0.38 → #3a3a3a@0.62` (`x1=3 y1=2 x2=14 y2=22`).  
Right rect `x=13.4 y=2.6` same size, inverted `#3a3a3a@0.38 → #ffffff@0.62`.  
Connector `x=9.2 y=10.9 w=5.6 h=2.2 rx=1.1` fill `#4a4a4a`.  
Label: `4.2M+ workflows automated`

**2. Download tile:** white rounded square `x=2.4 y=2.4 w=19.2 h=19.2 rx=6.2` fill `#ffffff`. Arrow `#111` stroke-width `1.85` round: vertical `M12 7.1v7.4`, chevron `M8.15 12.35L12 16.2l3.85-3.85`.  
Label: `92% reduction in manual operations`

**3. Three avatars** (`viewBox="0 0 40 22"`, class `stat-icon-wide`):  
- Dark circle `cx=10.2 cy=11 r=9.2` `#2b2b2b` + pale ellipse face `cx=10.2 cy=12.1 rx=4.15 ry=3.7` `#f4f4f4` + two ear triangles + eyes `r=0.7` `#1a1a1a`  
- White circle `cx=20.2` `#ffffff` + black eyes `r=1.7` + nose ellipse + smile path stroke `#111` width `1.2`  
- Orange circle `cx=30.2` `#f26b1d` + white Inter 700 `e` at `x=30.2 y=15.1 font-size=12.5 text-anchor=middle`  
Label: `180+ operational teams onboarded`

---

### Entrance motion (exact)

`.appear` resting opacity is **1** (so the page is never blank if animations fail).  
`animation-duration: 1.05s; animation-fill-mode: both; animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1); animation-delay: var(--d, 0.08s)`.  
`both` applies the 0% keyframe during the delay, so they still hide then fade in when animations run.

On each element’s own `animationend`, add `.is-in` (`animation: none; opacity: 1; transform: none; clip-path: none; filter: none`). Same for `.hero-photo.is-in`.

JS fallback: after two `requestAnimationFrame`s, if `el.getAnimations()` has nothing `running` or `finished`, add `.is-in` to every `.appear` and `.hero-photo`.

| Element | Modifier | `--d` |
|---|---|---|
| Logo | `appear--scale` | 0.08s |
| Nav 1 Benefits | `appear--scale` | 0.16s |
| Nav 2 How It Works | `appear--soft` | 0.28s |
| Nav 3 FAQs | `appear--scale` | 0.40s |
| Nav 4 Pricing | `appear--soft` | 0.52s |
| Header CTA + burger | `appear--scale` | 0.34s |
| Badge | `appear--pop` | 0.22s |
| H1 line 1 | `appear--mask` | 0.42s |
| H1 line 2 | `appear--mask` | 0.62s |
| Lede | `appear--soft` | 0.82s, duration **1.25s** |
| Solid CTA | `appear--btn` | 0.96s |
| Ghost CTA | `appear--side` | 1.10s |
| Stat 1 | `appear--stat` | 1.12s |
| Stat 2 | `appear--stat` | 1.28s |
| Stat 3 | `appear--stat` | 1.44s |

Keyframes (all end at opacity 1 / identity transform):

- `in-scale`: `opacity 0, scale(0.84)` → 1  
- `in-soft`: `opacity 0, translateY(14px)` → 0  
- `in-mask`: `opacity 0, translateY(40%)` → 0 (clipped by `.headline-line` overflow)  
- `in-pop`: 0 `scale(0.9)` → 70% `scale(1.03)` → 100% `scale(1)`  
- `in-btn`: `translateY(18px) scale(0.94)` → rest  
- `in-side`: `translateX(22px)` → 0  
- `in-stat`: `translateY(20px)` → 0  
- `in-star` on `.badge-star`, `0.9s`, delay `0.28s`, both: `scale(0.2) rotate(-50deg)` → 65% `scale(1.2) rotate(8deg)` → rest  
- `in-em` on `h1 em`, `1.2s`, delay `0.72s`, both: `opacity 0.35; filter: blur(4px)` → sharp  

`prefers-reduced-motion: reduce`: `transition: none !important; animation: none !important` on `*, *::before, *::after`. Force `.appear, .hero-photo, .hero h1 em, .badge-star` to `opacity: 1; transform: none; clip-path: none; filter: none`.

---

### Responsive (copy these breakpoints)

**≥1600:** logo 17 / mark 24 / nav 15 / nav-h 44 / btn 15 / btn-h 44 / hero-btn 48 / h1 **64** / lede 18 / badge 13.5 / stat 15 / header 28×64 / stats 96×44 / copy 980 / lede-max 540. Nav pad `0 20px`. Badge mb 26, lede mt 22, actions mt 30 gap 12. Icons 22, wide 45×24.

**≥1920:** logo 18 / mark 26 / nav 16 / nav-h 48 / btn 16 / btn-h 48 / hero-btn 52 / h1 **76** / lede 20 / badge 14.5 / stat 16 / header 32×80 / stats 120×52 / copy 1120 / lede-max 620. Nav gap 10, pad `0 22px`. Buttons pad `0 22px`. Badge pad `10px 15px`. Wide icon 48×26.

**≥2560:** h1 **88**, lede 22, header-x 120, stats-x 160, copy 1280, lede-max 680.

**1280–1599:** h1 54, lede 16, header-x 48, stats-x 80, copy 900.

**901–1279:** logo 15, nav 13, nav-h 36, btn 13, btn-h 38, hero-btn 40, h1 **42**, lede 15, badge 12, stat 12.5, header 16×28, stats 36×28, hero-gap 64, copy 760, lede-max 440. Nav pad `0 14px`. Badge mb 16, lede mt 14, actions mt 20.

**≥901 and max-height 850:** header-y 14, stats-y 24, hero-gap 48, h1 40; badge mb 12, lede mt 12, actions mt 16.

**≥901 and max-height 720:** h1 34, lede 14, hero-gap 32, stats-y 18, nav-h 30, btn-h 34, hero-btn 36, badge mb 8.

**≥901 desktop lock:** `html, body { height: 100%; overflow: hidden }`. `.page { height: 100vh / 100dvh; overflow: hidden }`. One frame, **no scroll**.

**≤900 phone:** no 100vh lock; `html/body` `height: auto; overflow-y: auto`. Header `grid-template-columns: 1fr auto auto`, gap 8, safe-area padding. Logo / CTA / burger `z-index: 80`. Burger shown.

Full-screen menu: `.menu-backdrop` `display: block; position: fixed; inset: 0; z-index: 40; background: rgba(8,8,8,0.42)`, idle `opacity: 0; visibility: hidden`. Open: opacity 1 + **`backdrop-filter: blur(24px)`**, 0.28s. Nav becomes full-viewport column, `z-index: 45`, transparent, centered, gap 12, padding `96px 22px 32px` with `padding-top: max(96px, calc(env(safe-area-inset-top) + 88px))`. Links full-width, height 56, `font-size: 19px`, `border-radius: 10px`. Escape / nav click / resize ≥901 closes. Toggle `aria-expanded` and label Open/Close menu. `body.menu-open { overflow: hidden }`.

Hero pad `20px 20px 64px`, still `align-items: flex-end`. Stats **column**, centered, gap 16, `white-space: normal`. Copy/lede max-width 100%. Tokens: logo 16, btn 15 / 46, hero-btn 48, h1 **36**, lede 16.5, badge 13.5, stat 15, header 16×18, stats 20×28, hero-gap 36.

**≤560:** h1 34, lede 16, header-x 16. Hero actions **column**, buttons `width: 100%`.

---

### JS (only this)

1. Each `.appear` → own `animationend` → add `is-in` (`once: true`).  
2. If animations are not running after two rAFs, force `.is-in` on all `.appear` and `.hero-photo`.  
3. Burger toggles `body.menu-open`.  
4. Nav links and Escape close the menu.  
5. Resize to `(min-width: 901px)` closes the menu.

---


---
