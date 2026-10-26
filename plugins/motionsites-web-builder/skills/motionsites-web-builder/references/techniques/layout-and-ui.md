# Layout & UI patterns

Hero compositions, navigation, menus, proof elements, carousels and other components.

**Conventions.** Single-file, no build step, dark page unless stated. Shared tokens (paste once):
```css
:root{
  --ease-out-expo:cubic-bezier(.16,1,.3,1);
  --ease-out-quint:cubic-bezier(.22,1,.36,1);
  --ease-material:cubic-bezier(.4,0,.2,1);
  --ease-sheet:cubic-bezier(.32,.72,0,1);   /* iOS-like bottom sheets */
}
```
`.liquid-glass` / `.liquid-glass--strong` refer to the material in surfaces-and-buttons.md, technique 1.

---

## 1. Hero composition patterns

**What / when:** Proven ways to arrange the first viewport over a full-bleed visual. Pick by how much of the visual must stay unobstructed. Centred-and-middle is the least premium default; several strong heroes avoid it on purpose.

**Patterns and their values**
- **A. Bottom-anchored centre stack + stat footer.** Page grid `auto 1fr auto` (header / hero / stats). The hero uses `align-items:flex-end` with a large bottom gap (85 px → 36 px on phones), so the copy sits low and the top two-thirds of the video stay clean. Stats footer `space-between`, 72 px side padding, a column on phones.
- **B. Bottom-left editorial.** Copy block `absolute; bottom:0; left:0`, `max-width 42rem`, padding 24/48 px, bottom 40 → 64 px. H1 36 → 60 px, medium, tight. Sub at 60 % white, 14 px, `max-width 28rem`. Buttons: white solid + glass ghost.
- **C. Split top/bottom (`justify-between`).** Badge and headline top-left; paragraph and CTA bottom-left; content height `calc(100vh − nav)`. Reads as a magazine cover.
- **D. Swiss corner layout.** All uppercase, weight 600, wide tracking. Stats right-aligned in the vertical middle (`flex:1; align-items:center; justify-content:flex-end`). Bottom row 1: a small three-line tagline left, the accent CTA right. Bottom row 2: a fixed-width description (120 → 280 px, right-aligned on desktop) left, a giant three-word stacked heading right (`clamp(2rem, 9vw, 9rem)`, lh .88). One accent only: the logo dot, the "+" in stats (at .5 em) and the CTA.
- **E. Four-corner HUD.** Nav top, centred headline in the top third, product blurb + CTAs bottom-left, a "▶ Watch the film · 1:35" link bottom-right (24 px glass play disc). Text colour flips per breakpoint to match what the video shows behind it.
- **F. Framed hero card.** On a `#f9fafb` page the hero is a contained card: `max-width 1400px`, `height 600px`, radius 48 px, `1px solid rgb(226 232 240/.5)`, `0 40px 100px -20px rgba(0,0,0,.03)`, video at `scale(1.05)`, copy top-left, and a bottom-centred floating dock nav (technique 3d). A logo marquee (technique 10) follows 40 px below.
- **G. Split glass panel.** Over one video: the left 52 % holds a strong-glass slab inset 16–24 px with radius 24 px (nav, logo, headline, CTA, feature pills, a quote); the right 48 % (desktop only) is a bento of small glass cards.
- **H. Ghost-type stage.** A giant word behind a cut-out subject (type-and-text-motion.md, technique 11): label top-left, copy and round arrows bottom-left, a big condensed CTA word bottom-right.

**Implementation (A, D, F, G)**
```css
/* A. Bottom-anchored */
.page{position:relative;z-index:1;display:grid;grid-template-rows:auto 1fr auto;min-height:100vh;min-height:100dvh}
.hero{display:flex;align-items:flex-end;justify-content:center;padding:8px 24px var(--hero-gap,85px);text-align:center}
.hero-copy{display:flex;flex-direction:column;align-items:center;max-width:860px;width:100%}
.stats-foot{display:flex;align-items:center;justify-content:space-between;gap:24px;color:#d8d8d8;font-size:13.5px;letter-spacing:-.015em;
  padding:0 72px max(36px,env(safe-area-inset-bottom))}
@media (max-width:900px){.hero{padding:20px 20px 64px}.stats-foot{flex-direction:column;gap:16px;padding:0 20px max(28px,env(safe-area-inset-bottom))}}

/* D. Swiss corner layout */
.swiss{min-height:100dvh;display:flex;flex-direction:column;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:#000}
.swiss-stats{flex:1;display:flex;align-items:center;justify-content:flex-end;gap:clamp(20px,4vw,40px);padding:32px clamp(20px,4vw,48px);text-align:right}
.swiss-stats .num{font-size:clamp(1.5rem,5vw,3.5rem);letter-spacing:-.02em;line-height:1}
.swiss-stats .num .plus{font-size:.5em;vertical-align:top;color:var(--accent,#5E0ED7)}
.swiss-stats .lbl{font-size:clamp(10px,1.1vw,14px);line-height:1.2;white-space:pre-line}
.swiss-bottom{display:flex;flex-direction:column;gap:clamp(24px,4vw,48px);padding:0 clamp(20px,4vw,48px) clamp(32px,4vw,48px)}
.swiss-row{display:flex;justify-content:space-between;gap:16px}
.swiss-row--a{align-items:center}.swiss-row--b{align-items:flex-end}
.swiss .tag{max-width:clamp(130px,20vw,320px);font-size:clamp(10px,1.1vw,14px);line-height:1.35;margin:0}
.swiss .desc{flex:none;width:clamp(120px,22vw,280px);font-size:clamp(9px,1.1vw,14px);line-height:1.35;margin:0}
.swiss .cta{color:var(--accent,#5E0ED7);font-size:clamp(16px,2vw,24px);white-space:nowrap;text-decoration:none}
@media (min-width:768px){.swiss .desc{text-align:right}}

/* F. Framed hero card */
.frame{position:relative;display:flex;flex-direction:column;max-width:1400px;height:600px;margin:24px auto;overflow:hidden;
  border-radius:48px;background:#fff;border:1px solid rgb(226 232 240/.5);box-shadow:0 40px 100px -20px rgba(0,0,0,.03)}
.frame>video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:scale(1.05);pointer-events:none}
.frame-copy{position:relative;z-index:20;max-width:560px;padding:clamp(48px,5vw,64px) clamp(32px,5vw,64px) 0}
.frame-copy h1{margin:0;font:500 clamp(42px,4vw,56px)/1.05 Outfit,Inter,sans-serif;letter-spacing:-.03em;color:#0a1b33}
.frame-copy p{font-size:15px;line-height:1.6;color:#64748b}

/* G. Split glass panel */
.split-glass{position:relative;min-height:100dvh;display:flex}
.split-glass>video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}
.panel-left{position:relative;z-index:10;flex:0 0 100%;display:flex}
.panel-left>.slab{position:absolute;inset:16px;border-radius:24px}
.panel-content{position:relative;flex:1;display:flex;flex-direction:column;padding:40px}
.panel-right{display:none}
@media (min-width:1024px){
  .panel-left{flex-basis:52%}
  .panel-left>.slab{inset:24px}
  .panel-right{position:relative;z-index:10;display:flex;flex-direction:column;gap:16px;flex:0 0 48%;padding:24px}
}
```
```html
<!-- G markup -->
<section class="split-glass">
  <video muted playsinline autoplay loop src="VIDEO_URL.mp4" aria-hidden="true"></video>
  <div class="panel-left"><div class="slab liquid-glass liquid-glass--strong" aria-hidden="true"></div>
    <div class="panel-content"><!-- nav · centred logo + h1 + CTA + pills · bottom quote --></div></div>
  <aside class="panel-right"><!-- glass social pill · community card · bento cards --></aside>
</section>
```

---

## 2. Viewport-locked single-frame hero (height-based design units)

**What / when:** The first screen is one composed frame that matches the comp at any window size. Every measurement is a "design pixel" tied to the **viewport height**, so the headline, CTA and bottom logo strip always land in the same proportional spots and nothing is cut off on a 13" laptop. For poster-like heroes over a video plate, where the composition is the product.

**Premium parameters**
- `--u = 100dvh / <comp height>` (e.g. 1058), `--uw = 100vw / <comp width>` (e.g. 1487). Type uses `--h = clamp(--u, .65·--u + .35·--uw, 1.16·--u)`: it grows up to 16 % on ultra-wide screens and never drops below the height-locked size.
- Elements placed absolutely in `--u` (e.g. brand at 75u / 27u, headline top 230.5u, logos at ~995u of 1058). Offsets inside the copy block use `--h`, so text and spacing scale together.
- Portrait (`max-aspect-ratio: 11/10`): normal flow with `--u = min(100vw / 430, 1.34px)`; a tablet band (≥600 px portrait) can use `min(100vw/860, 100vh/760, 1.25px)`.
- Token-set alternative: tokens per width (≥1600 / ≥1920 / ≥2560: h1 64 / 76 / 88 px) **plus height queries** (`(min-width:901px) and (max-height:850px)` → h1 40, smaller gaps; `max-height:720px` → h1 34). On desktop `html, body {height:100%; overflow:hidden}`: one frame, no scroll; phones scroll normally. Height queries come **after** width queries so they win on wide-but-short screens.
- Fluid spacing in vh: `padding: clamp(16px, 2.4vh, 28px) clamp(14px, 3vw, 32px)`.

**Implementation**
```css
:root{--u:calc(100vh / 1058);--uw:calc(100vw / 1487);
  --h:clamp(var(--u), calc(var(--u) * .65 + var(--uw) * .35), calc(var(--u) * 1.16))}
@supports (height:100dvh){:root{--u:calc(100dvh / 1058)}}
html,body{height:100%;margin:0;overflow:hidden;background:#050505;color:#fafafa}
.stage{position:relative;height:100vh;height:100dvh;overflow:hidden}
.brand   {position:absolute;left:calc(75 * var(--u));top:calc(27 * var(--u));width:calc(31.5 * var(--u))}
.nav     {position:absolute;left:50%;top:calc(51 * var(--u));transform:translate(-50%,-50%);
          display:flex;gap:calc(24.5 * var(--u));font-size:calc(19 * var(--u));color:#b6b5b5}
.cta-nav {position:absolute;right:calc(75.4 * var(--u));top:calc(27 * var(--u));height:calc(49 * var(--u));
          padding:0 calc(32 * var(--u));font-size:calc(20.6 * var(--u))}
.headline{position:absolute;left:calc(75.5 * var(--u));top:calc(230.5 * var(--u));margin:0;white-space:nowrap;
          font-size:calc(71.6 * var(--h));line-height:calc(80.5 * var(--h));font-weight:400;letter-spacing:calc(.3 * var(--h))}
.headline span{display:block}
.sub     {position:absolute;left:calc(75.5 * var(--u));top:calc(230.5 * var(--u) + 189 * var(--h));margin:0;
          font-size:calc(20.7 * var(--h));line-height:calc(23.5 * var(--h));color:#a7a6a6}
.actions {position:absolute;left:calc(75 * var(--u));top:calc(230.5 * var(--u) + 264.5 * var(--h));display:flex;align-items:center;gap:calc(45 * var(--h))}
.logos   {position:absolute;left:50%;top:calc(995 * var(--u));transform:translateX(-50%);display:flex;gap:calc(120 * var(--u));color:#8b8a8a}
@media (max-aspect-ratio:11/10){
  :root{--u:min(100vw / 430, 1.34px);--h:var(--u)}
  html,body{height:auto;overflow:auto}
  .stage{height:auto;min-height:100dvh;display:flex;flex-direction:column;gap:calc(24 * var(--u));
         padding:calc(24 * var(--u)) calc(20 * var(--u)) max(calc(24 * var(--u)),env(safe-area-inset-bottom))}
  .brand,.nav,.cta-nav,.headline,.sub,.actions,.logos{position:static;transform:none}
  .headline{white-space:normal}
  .headline span{display:inline}
  .logos{display:grid;grid-template-columns:1fr 1fr}
}
```
Height-query token sets (alternative or complement):
```css
:root{--h1:48px;--lede:15.5px;--hero-gap:85px;--stats-y:36px}
@media (min-width:1600px){:root{--h1:64px;--lede:18px}}
@media (min-width:1920px){:root{--h1:76px;--lede:20px}}
@media (min-width:2560px){:root{--h1:88px;--lede:22px}}
@media (min-width:901px) and (max-height:850px){:root{--h1:40px;--hero-gap:48px;--stats-y:24px}}
@media (min-width:901px) and (max-height:720px){:root{--h1:34px;--lede:14px;--hero-gap:32px;--stats-y:18px}}
@media (min-width:901px){html,body{height:100%;overflow:hidden}}
@media (max-height:560px){html,body{overflow:auto}}   /* safety valve */
```

---

## 3. Floating pill navigation

**What / when:** Navigation as a floating object rather than a bar. Variants: (a) **balanced three-part header**: logo disc left, links in a centred glass pill with the CTA *inside* it, an invisible spacer right so the pill is truly centred; (b) **frosted white pill** whose dark CTA hugs the right edge; (c) **solid white pill** with a three-dot active indicator; (d) **bottom dock** floating near the bottom of a framed hero; (e) **editorial text nav** with comma-separated links.

**Premium parameters**
- Header grid `1fr auto 1fr` keeps the centre column centred whatever the sides hold. Fixed `top:16px`, side padding 32 → 64 px.
- Glass pill `padding 6px`; links `8px 12px`, 14 px, 500, `rgba(255,255,255,.9)`; CTA inside the pill is white with black text plus an arrow-up-right.
- Frosted pill: `rgb(255 255 255/.7)`, `blur(12px)`, `1px solid rgb(255 255 255/.6)`, asymmetric padding `4px 4px 4px 24px` so the CTA sits flush. Active link semibold dark, others medium muted.
- White pill: height `clamp(44px, 5.2vw, 48px)`, `max-width 430px`, `0 4px 14px rgba(0,0,0,.16)`. Links at opacity .5, hover .75, active 1; active marker = three 3 px dots 5 px apart, 5 px from the bottom. Companion dark pill (`#28282a`, text `#c8c8c8`) for "Sign in". A circular white logo disc holds the mark at 72 %.
- Bottom dock: `bottom:40px`, centred, `rgb(255 255 255/.9)` + `blur(40px)`, `padding 6px`, `0 12px 40px rgba(0,0,0,.08)`; 36 px logo disc, 12 px semibold slate links, a white bordered CTA with a chevron; it enters after the hero copy.
- Editorial nav: 23 px text links separated by commas at 40 % opacity, hover .6, an underlined "Get in touch" (`text-underline-offset:2px`); logo 21 → 26 px tight-tracked with ® and a decorative ✳︎.
- Centre with the individual `translate` property so entrance keyframes on `transform` don't break it.

**Implementation**
```html
<header class="topbar">
  <a class="logo-disc liquid-glass" href="#" aria-label="Home">a</a>
  <nav class="nav-pill liquid-glass" aria-label="Primary">
    <a href="#" aria-current="page">Home</a><a href="#">Work</a><a href="#">Studio</a><a href="#">Journal</a>
    <a class="nav-cta" href="#start">Start a project <span aria-hidden="true">↗</span></a>
  </nav>
  <span class="topbar-spacer" aria-hidden="true"></span>
</header>
```
```css
.topbar{position:fixed;top:16px;left:0;right:0;z-index:50;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:0 clamp(16px,4vw,64px)}
.logo-disc{justify-self:start;width:48px;height:48px;border-radius:50%;display:grid;place-items:center;color:#fff;text-decoration:none;
  font:italic 400 24px/1 'Instrument Serif',serif}
.nav-pill{display:flex;align-items:center;gap:2px;padding:6px;border-radius:999px}
.nav-pill a{padding:8px 12px;border-radius:999px;font:500 14px/1 system-ui,sans-serif;color:rgb(255 255 255/.9);text-decoration:none}
.nav-pill .nav-cta{margin-left:4px;padding:8px 14px;background:#fff;color:#000;white-space:nowrap}
.topbar-spacer{justify-self:end;width:48px;height:48px}
@media (max-width:767px){.nav-pill{display:none}}

/* (c) three-dot active indicator on a white pill */
.nav-white{display:flex;align-items:center;justify-content:space-around;height:clamp(44px,5.2vw,48px);max-width:430px;flex:1;padding:4px 8px;
  border-radius:999px;background:#fff;box-shadow:0 4px 14px rgba(0,0,0,.16)}
.nav-white a{position:relative;padding:10px 12px;color:#2e2e2e;opacity:.5;text-decoration:none;font:500 clamp(13px,1.4vw,15px)/1 Inter,sans-serif;letter-spacing:-.01em;transition:opacity .2s}
.nav-white a:hover{opacity:.75}
.nav-white a[aria-current=page]{opacity:1}
.nav-white a[aria-current=page]::after{content:"";position:absolute;left:50%;bottom:5px;width:3px;height:3px;border-radius:50%;
  background:currentColor;translate:-50% 0;box-shadow:-5px 0 0 currentColor,5px 0 0 currentColor}

/* (d) bottom dock */
.dock{position:absolute;left:50%;bottom:40px;translate:-50% 0;z-index:30;display:flex;align-items:center;gap:4px;padding:6px;border-radius:999px;
  background:rgb(255 255 255/.9);-webkit-backdrop-filter:blur(40px);backdrop-filter:blur(40px);
  border:1px solid rgb(226 232 240/.4);box-shadow:0 12px 40px rgba(0,0,0,.08);animation:dock-in .7s cubic-bezier(.22,1,.36,1) .5s both}
@keyframes dock-in{from{opacity:0;transform:translateY(16px)}}
.dock a{padding:8px 14px;font:600 12px/1 Inter,sans-serif;color:#64748b;text-decoration:none}
.dock a:hover{color:#0a1b33}
.dock .dock-cta{background:#fff;color:#0a1b33;border:1px solid rgb(226 232 240/.6);border-radius:999px;box-shadow:0 1px 2px rgb(0 0 0/.05)}

/* (e) editorial text nav */
.nav-text{display:flex;font-size:23px;color:#000}
.nav-text a{color:inherit;text-decoration:none;transition:opacity .2s}
.nav-text a:hover{opacity:.6}
.nav-text .sep{opacity:.4;white-space:pre}
.cta-underline{font-size:23px;color:inherit;text-decoration:underline;text-underline-offset:2px}
@media (prefers-reduced-motion:reduce){.dock{animation:none}}
```

---

## 4. Expanding glass capsule menu

**What / when:** The nav is part of the show: a 48 px glass square with a hamburger springs open sideways into a ~290 px capsule revealing 2–4 links, while the logo sits in its own glass pill beside it and a solid CTA pill sits right. For minimal heroes where a full link row would be noise.

**Premium parameters**
- Capsule 48 px tall, radius 14 px, `rgba(255,255,255,.15)` + `blur(12px)`; width `48 → 290px` with a spring (stiffness 350, damping 28 ≈ `cubic-bezier(.34,1.25,.64,1)` over ~0.55 s).
- The toggle shrinks `48 → 36px`, radius `14 → 11px`, and gains `rgba(255,255,255,.1)`; links fade and slide `x 15 → 0` after ~120 ms.
- Compact 3-bar icon: `18×12` box, 1.5 px bars, open offsets `±5.25px` + `±45deg`, slight overshoot.
- Mobile: everything 36 px / radius 10 px; the logo pill collapses to width 0 while the capsule takes 100 %, or switch to the bottom sheet in technique 5.

**Implementation**
```html
<nav class="capnav" aria-label="Primary">
  <a class="cap cap--logo" href="#">Brand</a>
  <div class="cap cap--menu" data-open="false">
    <button class="cap__toggle" aria-expanded="false" aria-controls="cap-links" aria-label="Menu">
      <span class="cap__bars" aria-hidden="true"><i></i><i></i><i></i></span>
    </button>
    <div class="cap__links" id="cap-links"><a href="#about">About</a><a href="#work">Work</a><a href="#contact">Contact</a></div>
  </div>
  <a class="cap-cta" href="#">Get started</a>
</nav>
```
```css
.capnav{position:fixed;top:16px;left:16px;right:16px;z-index:50;display:flex;align-items:center;gap:8px}
.cap{height:48px;border-radius:14px;display:flex;align-items:center;color:#fff;
  background:rgba(255,255,255,.15);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.cap--logo{padding:0 20px;font-size:16px;font-weight:500;letter-spacing:-.02em;text-decoration:none;transition:transform .2s,background .2s}
.cap--logo:hover{transform:scale(1.02);background:rgba(255,255,255,.22)}
.cap--menu{width:48px;overflow:hidden;transition:width .55s cubic-bezier(.34,1.25,.64,1)}
.cap--menu[data-open="true"]{width:290px}
.cap__toggle{flex:none;width:48px;height:48px;border:0;border-radius:14px;background:transparent;color:inherit;display:grid;place-items:center;
  cursor:pointer;transition:width .3s,height .3s,border-radius .3s,background .3s,margin .3s}
.cap--menu[data-open="true"] .cap__toggle{width:36px;height:36px;border-radius:11px;margin-left:6px;background:rgba(255,255,255,.1)}
.cap__links{display:flex;gap:20px;padding:0 20px;white-space:nowrap;opacity:0;transform:translateX(15px);visibility:hidden;
  transition:opacity .3s,transform .3s,visibility 0s .3s}
.cap--menu[data-open="true"] .cap__links{opacity:1;transform:none;visibility:visible;transition-delay:.12s,.12s,0s}
.cap__links a{color:rgba(255,255,255,.85);text-decoration:none;font-size:16px}
.cap__links a:hover{color:#fff}
.cap-cta{margin-left:auto;height:48px;display:inline-flex;align-items:center;padding:0 24px;border-radius:999px;background:#fff;color:#000;
  text-decoration:none;transition:transform .2s,background .2s}
.cap-cta:hover{transform:scale(1.03);background:#e2e2e6}
.cap__bars{position:relative;width:18px;height:12px}
.cap__bars i{position:absolute;left:0;width:100%;height:1.5px;border-radius:2px;background:currentColor;transition:transform .35s cubic-bezier(.34,1.4,.64,1),opacity .2s}
.cap__bars i:nth-child(1){top:0}.cap__bars i:nth-child(2){top:5.25px}.cap__bars i:nth-child(3){bottom:0}
[aria-expanded="true"] .cap__bars i:nth-child(1){transform:translateY(5.25px) rotate(45deg)}
[aria-expanded="true"] .cap__bars i:nth-child(2){opacity:0;transform:scaleX(0)}
[aria-expanded="true"] .cap__bars i:nth-child(3){transform:translateY(-5.25px) rotate(-45deg)}
@media (max-width:640px){.cap,.cap__toggle,.cap-cta{height:36px}.cap,.cap__toggle{border-radius:10px}.cap__toggle{width:36px}
  .cap--menu{width:36px}.capnav:has(.cap--menu[data-open="true"]) .cap--logo{display:none}.cap--menu[data-open="true"]{width:100%}}
@media (prefers-reduced-motion:reduce){.cap--menu,.cap__links,.cap__bars i{transition-duration:.01s}}
```
```js
(() => {
  const menu = document.querySelector('.cap--menu');
  const btn = menu.querySelector('.cap__toggle');
  const links = menu.querySelector('.cap__links');
  const set = (open) => { btn.setAttribute('aria-expanded', String(open)); menu.dataset.open = String(open); links.inert = !open; };
  set(false);
  btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && menu.dataset.open === 'true') { set(false); btn.focus(); } });
})();
```

---

## 5. Mobile menu: burger morph + staggered overlay / drawer / bottom sheet

**What / when:** A mobile menu that feels designed rather than toggled. The burger folds into an X, a blurred overlay (or a side drawer, or a bottom sheet) fades in, and the links cascade in one after another. Use it on every page with navigation below 768–1024 px.

**Premium parameters**
- Burger: three bars 18–24 × 1.5–2 px, gap 5 px; open = top `translateY(bar + gap) rotate(45deg)` (7 px for 2 px bars), middle `opacity 0`, bottom mirrored; 0.25–0.3 s. The button is a 40–48 px circle (dark translucent or glass) above the overlay.
- 2-line asymmetric burger (light pages): `32 × 1.5px`, gap 6 px; hover → 24 px / 40 px; open → `±3.75px` + `±45deg`.
- Icon-crossfade alternative: stack Menu and X icons in one grid cell; the Menu icon goes to `rotate(90deg) scale(.5) opacity 0` while X arrives from `rotate(-90deg) scale(.5)`, 300 ms; press `scale(.9)`.
- Full-screen overlay: `rgba(8,8,8,.42)` + `blur(24px)` (or `rgba(0,0,0,.95)` + 4–8 px), opacity .28–.5 s. Links 28–40 px, 500–600, rising `translateY(20px) → 0`, stagger `100 + i × 80 ms`; a trailing CTA at ~400 ms. On close, delays reset to 0 so the menu leaves at once.
- Drawer: `width 85%; max-width 24rem`, `translateX(100%) → 0` over 500 ms `cubic-bezier(.22,1,.36,1)`, link stagger `150 + i × 70 ms`, a tinted scrim (`rgba(0,0,0,.4)` + `blur(4px)`) that closes on click.
- Bottom sheet: white, `margin 12px`, radius 16 px, `translateY(100%) → 0` **500 ms** `--ease-sheet`, backdrop `rgba(0,0,0,.6)`, links 28–32 px with a 50 ms stagger.
- Behaviour: `aria-expanded`, `aria-controls`, a label toggling "Open menu"/"Close menu"; Escape closes and returns focus to the burger; clicking a link or the backdrop closes; resizing to desktop closes; body scroll locked while open; the closed menu is `inert`; safe-area padding top and bottom.

**Implementation (overlay)**
```html
<button class="burger" aria-controls="mobile-menu" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button>
<div class="menu" id="mobile-menu">
  <nav class="menu-links" aria-label="Mobile">
    <a href="#work" style="--i:0">Work</a>
    <a href="#studio" style="--i:1">Studio</a>
    <a href="#journal" style="--i:2">Journal</a>
    <a href="#contact" class="menu-cta" style="--i:4">Get in touch</a>
  </nav>
</div>
```
```css
.burger{display:none;position:relative;z-index:80;width:44px;height:44px;border-radius:999px;place-content:center;gap:5px;cursor:pointer;
  background:rgb(8 8 8/.55);border:1px solid rgb(255 255 255/.16)}
.burger span{display:block;width:18px;height:2px;border-radius:1px;background:#fff;transition:transform .3s cubic-bezier(.22,1,.36,1),opacity .2s ease}
.menu-open .burger span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.menu-open .burger span:nth-child(2){opacity:0}
.menu-open .burger span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.menu{position:fixed;inset:0;z-index:70;display:flex;flex-direction:column;justify-content:center;
  padding:max(96px,calc(env(safe-area-inset-top) + 88px)) 24px max(32px,env(safe-area-inset-bottom));
  background:rgb(8 8 8/.42);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);
  opacity:0;visibility:hidden;transition:opacity .28s ease,visibility 0s linear .28s}
.menu-open .menu{opacity:1;visibility:visible;transition:opacity .28s ease}
.menu-links a{display:block;padding:12px 0;color:#fff;text-decoration:none;font-size:clamp(28px,8vw,40px);font-weight:500;letter-spacing:-.02em;
  opacity:0;transform:translateY(20px);transition:opacity .5s cubic-bezier(.22,1,.36,1),transform .5s cubic-bezier(.22,1,.36,1)}
.menu-open .menu-links a{opacity:1;transform:none;transition-delay:calc(100ms + var(--i) * 80ms)}
body.menu-open{overflow:hidden}
@media (max-width:767px){.burger{display:grid}}
@media (min-width:768px){.menu{display:none}}
@media (prefers-reduced-motion:reduce){.burger span,.menu,.menu-links a{transition-duration:.001s!important;transition-delay:0s!important}}
```
```js
(function mobileMenu(burger) {
  const menu = document.getElementById(burger.getAttribute('aria-controls'));
  const desktop = matchMedia('(min-width: 768px)');
  const isOpen = () => document.body.classList.contains('menu-open');
  const set = (open) => {
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.inert = !open;
    if (open) menu.querySelector('a, button')?.focus({ preventScroll: true });
  };
  menu.inert = true;
  burger.addEventListener('click', () => set(!isOpen()));
  menu.addEventListener('click', (e) => { if (e.target.closest('a') || e.target === menu) set(false); });
  document.addEventListener('click', (e) => { if (e.target.closest('[data-menu-close]')) set(false); });   // scrims / backdrops
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && isOpen()) { set(false); burger.focus(); } });
  desktop.addEventListener('change', (e) => { if (e.matches) set(false); });
})(document.querySelector('.burger'));
```
**Drawer variant** (give the panel `id="mobile-menu"` and class `drawer`; add `<div class="drawer-scrim" data-menu-close></div>`):
```css
.drawer{position:fixed;top:0;right:0;bottom:0;z-index:70;width:85%;max-width:24rem;padding:96px 32px 32px;
  background:rgb(255 255 255/.95);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);box-shadow:0 25px 50px -12px rgb(0 0 0/.25);
  transform:translateX(100%);transition:transform .5s cubic-bezier(.22,1,.36,1)}
.menu-open .drawer{transform:none}
.drawer a{display:block;padding:16px 0;border-bottom:1px solid rgb(0 0 0/.08);font-size:24px;font-weight:600;
  opacity:0;transform:translateX(32px);transition:opacity .5s,transform .5s}
.menu-open .drawer a{opacity:1;transform:none;transition-delay:calc(150ms + var(--i) * 70ms)}
.drawer-scrim{position:fixed;inset:0;z-index:60;background:rgb(0 0 0/.4);-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);
  opacity:0;pointer-events:none;transition:opacity .3s}
.menu-open .drawer-scrim{opacity:1;pointer-events:auto}
```
**Bottom-sheet variant** (panel `id="mobile-menu"` wraps backdrop + sheet):
```html
<div class="sheet" id="mobile-menu">
  <div class="sheet__backdrop" data-menu-close></div>
  <div class="sheet__panel" role="dialog" aria-modal="true" aria-label="Menu">
    <a href="#" style="--i:0">Projects</a><a href="#" style="--i:1">Studio</a><a href="#" style="--i:2">Journal</a>
  </div>
</div>
```
```css
.sheet{position:fixed;inset:0;z-index:70;visibility:hidden;pointer-events:none;transition:visibility 0s .5s}
.menu-open .sheet{visibility:visible;pointer-events:auto;transition-delay:0s}
.sheet__backdrop{position:absolute;inset:0;background:rgba(0,0,0,.6);opacity:0;transition:opacity .5s ease}
.sheet__panel{position:absolute;left:12px;right:12px;bottom:max(12px,env(safe-area-inset-bottom));padding:24px;border-radius:16px;background:#fff;color:#111;
  transform:translateY(calc(100% + 24px));transition:transform .5s var(--ease-sheet)}
.menu-open .sheet__backdrop{opacity:1}
.menu-open .sheet__panel{transform:none}
.sheet__panel a{display:block;padding:6px 0;color:inherit;text-decoration:none;font-size:clamp(28px,8vw,32px);font-weight:500;letter-spacing:-.02em;
  opacity:0;transform:translateY(16px);transition:opacity .5s var(--ease-material),transform .5s var(--ease-material)}
.menu-open .sheet__panel a{opacity:1;transform:none;transition-delay:calc(100ms + var(--i,0) * 50ms)}
@media (min-width:768px){.sheet{display:none}}
```
**2-line burger** (light pages):
```css
.burger2{display:flex;flex-direction:column;align-items:flex-end;gap:6px;background:none;border:0;padding:8px;cursor:pointer}
.burger2 i{display:block;width:32px;height:1.5px;background:#000;transition:width .3s,transform .3s}
.burger2:hover i:first-child{width:24px}.burger2:hover i:last-child{width:40px}
[aria-expanded="true"].burger2 i{width:32px}
[aria-expanded="true"].burger2 i:first-child{transform:translateY(3.75px) rotate(45deg)}
[aria-expanded="true"].burger2 i:last-child{transform:translateY(-3.75px) rotate(-45deg)}
```

---

## 6. Overlapping avatar trust cluster with pill

**What / when:** A compact social-proof chip: three small "logo coins" overlap each other and tuck into the start of a pill that carries the claim. It sits above the headline. Use it on SaaS and AI heroes instead of a loose logo row.

**Premium parameters**
- Size token `--s: clamp(36px, 4.5vw, 42px)` (34 px at ≤420 px).
- Coins are **rings, not discs**: an outer dark ring (`#28282a`, `1px solid rgba(255,255,255,.4)`, `padding 5px`) around a white circle holding a black glyph at `0.34 × --s`.
- Overlap `margin-left: −0.42 × --s`; z-order 1 / 2 / 4; the pill sits at z 3 so the last coin overlaps it.
- Pill: same height and border, `margin-left: −0.42 × --s`, `padding-left: 0.58 × --s` so the text clears the coin; Inter 500, `#c4c2c3`, `clamp(12px, 1.4vw, 13.5px)`.
- Hover lift −2 / −4 / −2 px over .35 s. Margin below `clamp(16px, 2.5vh, 26px)`.
- Photo alternative: 3 × 32 px avatars, overlap −8 px, a 2 px ring in the page colour, + "7,000+ people already…" in 14 px muted. Cinematic alternative: a glass chip line ("Collaborating with …") over a row of partner names set in italic serif (24 → 30 px, gaps 48 → 64 px).

**Implementation**
```html
<div class="trust">
  <span class="coin"><span>A</span></span><span class="coin"><span>B</span></span><span class="coin"><span>C</span></span>
  <span class="trust-pill">Trusted by 2,000+ teams</span>
</div>
```
```css
.trust{--s:clamp(36px,4.5vw,42px);display:inline-flex;align-items:center;margin-bottom:clamp(16px,2.5vh,26px)}
.coin{position:relative;width:var(--s);height:var(--s);flex:none;border-radius:50%;padding:5px;
  background:#28282a;border:1px solid rgba(255,255,255,.4);transition:transform .35s cubic-bezier(.22,1,.36,1)}
.coin>span{display:grid;place-items:center;width:100%;height:100%;border-radius:50%;background:#fff;color:#111;font:700 calc(var(--s) * .34)/1 Inter,sans-serif}
.coin+.coin{margin-left:calc(var(--s) * -.42)}
.coin:nth-child(1){z-index:1}.coin:nth-child(2){z-index:2}.coin:nth-child(3){z-index:4}
.trust:hover .coin:nth-child(1),.trust:hover .coin:nth-child(3){transform:translateY(-2px)}
.trust:hover .coin:nth-child(2){transform:translateY(-4px)}
.trust-pill{position:relative;z-index:3;display:inline-flex;align-items:center;height:var(--s);
  margin-left:calc(var(--s) * -.42);padding:0 16px 0 calc(var(--s) * .58);border-radius:999px;
  background:#28282a;border:1px solid rgba(255,255,255,.4);color:#c4c2c3;font:500 clamp(12px,1.4vw,13.5px)/1 Inter,sans-serif;white-space:nowrap}
@media (max-width:420px){.trust{--s:34px}}
```

---

## 7. Selectable chip group with spring check and auto-height summary

**What / when:** A multi-select of service or interest pills in place of checkboxes. A selected chip turns dark and a check mark springs in; below the group a summary panel grows open ("You're asking about: A, B") with a CTA. For contact and enquiry heroes, onboarding and filters: it turns a form into a conversation.

**Premium parameters**
- Inactive: white, dark-green text (`#1C2E1E`), hairline border (`#F1F3F1`), hover tint `rgba(241,243,241,.55)`. Active: dark fill `#1C2E1E`, white text, very soft shadow `0 4px 6px rgba(2,44,34,.05)`.
- Check springs in: `cubic-bezier(.34,1.56,.64,1)` ~0.4 s, scale 0 → 1 with a slight rotate (Framer: `spring, stiffness 300, damping 20`).
- Summary: an empty-state hint (12 px italic, 50 %) swaps for a panel that expands to auto height (`grid-template-rows: 0fr → 1fr`, .4 s). Panel `#FAFBF9`, 1 px border, radius 16 px, uppercase 12 px CTA in a green accent `#4D6D47`.
- Copy: title 24 px medium tight ("What do you need?"), subtitle muted ("Select all that apply").
- `aria-pressed` on buttons, `aria-live="polite"` on the summary.

**Implementation**
```html
<fieldset class="chips">
  <legend>What do you need?</legend>
  <p class="hint">Select all that apply</p>
  <div class="chip-row">
    <button type="button" class="chip" aria-pressed="false">Branding<svg class="check" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></button>
    <button type="button" class="chip" aria-pressed="false">Website<svg class="check" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></button>
    <button type="button" class="chip" aria-pressed="false">Motion<svg class="check" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></button>
  </div>
  <div class="summary" aria-live="polite">
    <p class="summary-empty">Please select services above.</p>
    <div class="summary-panel"><div><div class="summary-box">
      <span class="summary-text"></span><a class="summary-go" href="#contact">Let's go →</a>
    </div></div></div>
  </div>
</fieldset>
```
```css
.chips{border:0;margin:0;padding:0;color:#1C2E1E}
.chips legend{padding:0;font-size:24px;font-weight:500;letter-spacing:-.02em;margin-bottom:8px}
.hint{margin:0 0 32px;color:#738273}
.chip-row{display:flex;flex-wrap:wrap;gap:10px}
.chip{display:inline-flex;align-items:center;padding:10px 20px;border-radius:999px;cursor:pointer;font:500 15px/1 Inter,sans-serif;
  background:#fff;color:#1C2E1E;border:1px solid #F1F3F1;transition:background-color .2s,color .2s,border-color .2s,box-shadow .2s,transform .15s}
.chip:hover{background:rgb(241 243 241/.55)}
.chip:active{transform:scale(.96)}
.chip[aria-pressed=true]{background:#1C2E1E;color:#fff;border-color:#1C2E1E;box-shadow:0 4px 6px -1px rgb(2 44 34/.05)}
.chip .check{width:0;height:14px;margin-left:0;opacity:0;transform:scale(0) rotate(-45deg);
  fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;
  transition:width .35s cubic-bezier(.34,1.56,.64,1),margin-left .35s cubic-bezier(.34,1.56,.64,1),opacity .2s ease,transform .45s cubic-bezier(.34,1.56,.64,1)}
.chip[aria-pressed=true] .check{width:14px;margin-left:8px;opacity:1;transform:none}
.summary{margin-top:20px}
.summary-empty{margin:0;font-size:12px;font-style:italic;opacity:.5}
.summary.has .summary-empty{display:none}
.summary-panel{display:grid;grid-template-rows:0fr;transition:grid-template-rows .4s cubic-bezier(.22,1,.36,1)}
.summary-panel>div{overflow:hidden}
.summary.has .summary-panel{grid-template-rows:1fr}
.summary-box{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:16px 20px;background:#FAFBF9;border:1px solid #F1F3F1;border-radius:16px}
.summary-go{color:#4D6D47;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;white-space:nowrap}
@media (prefers-reduced-motion:reduce){.chip,.chip .check,.summary-panel{transition:none}}
```
```js
(function chipGroup(root) {
  const chips = [...root.querySelectorAll('.chip')];
  const summary = root.querySelector('.summary');
  const text = root.querySelector('.summary-text');
  const update = () => {
    const picked = chips.filter((c) => c.getAttribute('aria-pressed') === 'true').map((c) => c.textContent.trim());
    summary.classList.toggle('has', picked.length > 0);
    if (picked.length) text.textContent = `You're asking about: ${picked.join(', ')}`;
  };
  chips.forEach((c) => c.addEventListener('click', () => {
    c.setAttribute('aria-pressed', String(c.getAttribute('aria-pressed') !== 'true'));
    update();
  }));
})(document.querySelector('.chips'));
```
**Framer Motion variant:** the check uses `initial={{ scale: 0, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ type: 'spring', stiffness: 300, damping: 20 }}`; the summary swaps the hint for a `motion.div` inside `<AnimatePresence mode="wait">` with `initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }}`.

---

## 8. In-page product UI mockup (app-window chrome)

**What / when:** Instead of a screenshot, the hero continues into a live-coded, realistic product window: traffic lights, a three-pane layout, believable content and an AI summary card. Crisp at any DPI, theme-able and animatable. For SaaS, email, dev tools and dashboards, directly under the hero (optionally after an OS-style menu-bar strip).

**Premium parameters**
- Window: radius 16 px, `1px solid rgba(255,255,255,.1)`, background `rgba(14,16,20,.9)` + `blur(40px)` so the page video glows through faintly.
- Title bar 40 px, traffic lights (12 px dots `#ff5f57`, `#febc2e`, `#28c840`), a centred 12 px title at 50 % white.
- Body: a fixed-height (~520 px) grid split 3 / 4 / 5 (sidebar / list / reader). The sidebar sits on `rgba(0,0,0,.3)` with hairline borders. Active row `rgba(255,255,255,.1)`, hover `.05`.
- Realism cues: believable senders and subjects, timestamps ("9:41 AM", "Yesterday", "Mon"), unread dots, counts, coloured label dots, a gradient avatar bubble, an attachment pill and an "AI summary" card with a sparkle in the accent.
- Optional OS menu-bar strip above it: 40 px, `rgba(0,0,0,.4)` + blur, hairlines top and bottom, 12 px items that progressively hide on small screens, a clock on the right.
- Entrance: `y 40` → 0 at ~1.1 s, after the hero copy.

**Implementation**
```html
<div class="app-window" data-reveal style="--y:40px;--d:1.1s">
  <div class="app-titlebar">
    <span class="tl" style="background:#ff5f57"></span><span class="tl" style="background:#febc2e"></span><span class="tl" style="background:#28c840"></span>
    <span class="app-title">Inbox</span>
  </div>
  <div class="app-body">
    <aside class="app-side">
      <button class="app-compose">✦ Compose</button>
      <a class="app-nav is-active">Inbox <b>12</b></a><a class="app-nav">Starred <b>3</b></a><a class="app-nav">Sent</a>
    </aside>
    <section class="app-list">
      <div class="app-row is-active is-unread"><div class="from"><span class="name">Product team</span><time>9:41 AM</time></div><div class="subj">Quarterly update</div><div class="prev">Here is what changed since the last review…</div></div>
      <!-- 5 more rows -->
    </section>
    <article class="app-reader">
      <div class="ai-summary"><b>✦ Summary</b> Three decisions need your input; the rest is informational.</div>
      <p>Hi all, a quick summary of the quarter…</p>
    </article>
  </div>
</div>
```
```css
.app-window{max-width:72rem;margin:0 auto;border-radius:16px;overflow:hidden;color:#fff;font-size:13px;
  border:1px solid rgb(255 255 255/.1);background:rgb(14 16 20/.9);-webkit-backdrop-filter:blur(40px);backdrop-filter:blur(40px)}
.app-titlebar{position:relative;display:flex;align-items:center;gap:8px;height:40px;padding:0 16px;border-bottom:1px solid rgb(255 255 255/.1)}
.tl{width:12px;height:12px;border-radius:50%}
.app-title{position:absolute;left:50%;translate:-50% 0;font-size:12px;color:rgb(255 255 255/.5)}
.app-body{display:grid;grid-template-columns:3fr 4fr 5fr;height:520px}
.app-side{padding:16px;background:rgb(0 0 0/.3);border-right:1px solid rgb(255 255 255/.1);display:flex;flex-direction:column;gap:4px}
.app-compose{margin-bottom:12px;padding:8px 12px;border:0;border-radius:8px;background:#fff;color:#000;font-weight:600;font-size:12px;text-align:left}
.app-nav{display:flex;justify-content:space-between;padding:6px 10px;border-radius:6px;color:rgb(255 255 255/.6)}
.app-nav.is-active{background:rgb(255 255 255/.1);color:#fff}
.app-list{border-right:1px solid rgb(255 255 255/.1);overflow:hidden}
.app-row{padding:12px 16px;border-bottom:1px solid rgb(255 255 255/.05)}
.app-row.is-active{background:rgb(255 255 255/.1)}
.app-row .from{display:flex;justify-content:space-between;font-weight:600}
.app-row time,.app-row .prev{color:rgb(255 255 255/.45);font-weight:400}
.app-row.is-unread .name::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:#00d2ff;margin-right:6px;vertical-align:middle}
.app-reader{padding:24px;overflow:hidden;line-height:1.6;color:rgb(255 255 255/.8)}
.ai-summary{padding:12px 14px;border-radius:12px;background:rgb(164 244 253/.06);border:1px solid rgb(164 244 253/.15);margin-bottom:16px}
@media (max-width:767px){.app-body{grid-template-columns:1fr;height:auto}.app-side,.app-reader{display:none}}
```
The mockup is decorative: give the window `aria-hidden="true"` (or `role="img"` with a one-line `aria-label`) so screen readers don't wade through fake rows.

---

## 9. Desktop grid that becomes a mobile scroll-snap rail

**What / when:** Three to four large cards (pricing, plans, features) form a grid on desktop and a native, swipeable, snapping rail on tablet and phone. Beats stacking three 580 px-tall cards. Pairs with dark glass cards that lift on hover.

**Premium parameters**
- Desktop: 3 columns, 24 px gap, `max-width 1100px`.
- ≤1024 px: `display:flex; overflow-x:auto; scroll-snap-type:x mandatory`, cards `flex: 0 0 min(320px, 82vw)`, `scroll-snap-align:center`, 16 px gap. The rail bleeds to the screen edges (negative inline margin equal to the gutter, plus `scroll-padding-inline`). Scrollbar hidden.
- Cards: `linear-gradient(135deg, rgba(0,0,0,.7), rgba(0,0,0,.4))` + `blur(14px) brightness(.91)`, `1px solid #fff`, radius 44 px, `padding 50px 24px`, `min-height 580px`, a diagonal sheen `::before` (`rgba(255,255,255,.1)` → 0 at 50 %).
- Hover (desktop only): `translateY(-12px) scale(1.01)`, border switches to the accent, .6 s `cubic-bezier(.22,1,.36,1)`.
- Internals: tier 1.1 rem at 60 % white; price 2.8 rem/500/−.02em; description .88 rem at 45 %; checklist rows with 28 px translucent circle checks; a white pill button pinned with `margin-top:auto`.
- Billing toggle: 52 × 28 track, 20 px knob, `translateX(24px)`, .3 s `cubic-bezier(.4,0,.2,1)`, `role="switch"`.

**Implementation**
```css
.plans{--gutter:20px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1100px;margin:60px auto 0}
.plan{position:relative;overflow:hidden;display:flex;flex-direction:column;min-height:580px;padding:50px 24px;border-radius:44px;color:#fff;
  border:1px solid #fff;background:linear-gradient(135deg,rgb(0 0 0/.7),rgb(0 0 0/.4));
  -webkit-backdrop-filter:blur(14px) brightness(.91);backdrop-filter:blur(14px) brightness(.91);
  transition:transform .6s cubic-bezier(.22,1,.36,1),background .6s cubic-bezier(.22,1,.36,1),border-color .6s cubic-bezier(.22,1,.36,1)}
.plan::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:linear-gradient(135deg,rgb(255 255 255/.1) 0%,transparent 50%)}
@media (hover:hover){.plan:hover{background:rgb(15 15 15/.6);border-color:rgb(34 211 238/.7);transform:translateY(-12px) scale(1.01)}}
.plan .btn-plan{margin-top:auto;align-self:center;padding:10px 32px;border:0;border-radius:100px;background:#fff;color:#000;font-weight:600}
@media (max-width:1024px){
  .plans{display:flex;gap:16px;max-width:none;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain;
    margin-inline:calc(-1 * var(--gutter));padding:0 var(--gutter) 8px;scroll-padding-inline:var(--gutter);scrollbar-width:none}
  .plans::-webkit-scrollbar{display:none}
  .plan{flex:0 0 min(320px,82vw);scroll-snap-align:center;min-height:520px}
}
.toggle{position:relative;width:52px;height:28px;padding:0;border:0;border-radius:999px;background:#fff;cursor:pointer;transition:background .3s cubic-bezier(.4,0,.2,1)}
.toggle::after{content:"";position:absolute;top:4px;left:4px;width:20px;height:20px;border-radius:50%;background:#000;
  transition:transform .3s cubic-bezier(.4,0,.2,1),background .3s cubic-bezier(.4,0,.2,1)}
.toggle[aria-checked=true]{background:rgb(255 255 255/.2)}
.toggle[aria-checked=true]::after{transform:translateX(24px);background:#fff}
```
```html
<button class="toggle" role="switch" aria-checked="false" aria-label="Yearly billing"
        onclick="this.setAttribute('aria-checked', this.getAttribute('aria-checked') !== 'true')"></button>
```

---

## 10. Seamless infinite marquee (logos, image strip, giant text) with edge-fade mask

**What / when:** Endless horizontal strips: a partner-logo ticker under a hero, a strip of tall rounded previews between sections, or a giant uppercase phrase ("… • … •") above a footer CTA. Edge-fade masks make items materialise rather than get cut; logo cards can bloom a gradient on hover.

**Premium parameters**
- Always linear; keep **pixels per second** constant (~40–60 px/s for logos) by computing the duration from the group width, so mobile and desktop feel the same.
- Logos `137 × 40px` contain, gap **64 px**, at 40–50 % opacity (or white pill cards); image strip height **500 px** desktop / **280 px** mobile, radius 16 px; giant text phrase + ` • ` repeated, ~40 s per loop, `clamp(3rem,10vw,9rem)`, `-.04em`.
- The track holds the group twice and animates `translateX(0 → -50%)`. Each group carries its trailing gap as `padding-right`, so the two halves are identical and the loop has no seam (a plain flex `gap` between groups makes −50 % off by half a gap).
- Edge fade `mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent)`. Pause on hover.
- Hover-bloom logo card: 160 × 96 px white pill, `1px solid rgb(226 232 240/.6)`; on hover a gradient layer goes `scale(1.5) opacity 0 → scale(1) opacity 1` (.5 s) and the logo flips to white (`brightness(0) invert(1)`).

**Implementation**
```html
<div class="marquee" data-speed="50"><!-- px per second -->
  <div class="marquee__track">
    <div class="marquee__group">
      <img src="logo-1.svg" alt="Partner one"><img src="logo-2.svg" alt="Partner two"><img src="logo-3.svg" alt="Partner three">
      <!-- or: <span class="logo-card" style="--g:linear-gradient(135deg,#60a5fa,#2563eb)"><img src="logo-4.svg" alt="Partner four"></span> -->
    </div>
  </div>
</div>
```
```css
.marquee{overflow:hidden;
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
          mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.marquee__track{display:flex;width:max-content;animation:marquee var(--dur,20s) linear infinite}
.marquee__group{display:flex;align-items:center;flex:none;gap:var(--gap,64px);padding-right:var(--gap,64px)}
.marquee__group>img{width:137px;height:40px;object-fit:contain;opacity:.5}
.marquee:hover .marquee__track{animation-play-state:paused}
@keyframes marquee{to{transform:translateX(-50%)}}
/* image strip */
.marquee--images{--gap:24px}
.marquee--images .marquee__group>img{height:500px;width:auto;border-radius:16px;object-fit:cover;opacity:1;box-shadow:0 10px 15px -3px rgba(0,0,0,.1),0 4px 6px -4px rgba(0,0,0,.1)}
@media (max-width:768px){.marquee--images .marquee__group>img{height:280px}}
/* giant text */
.marquee--text{--gap:0px}
.marquee--text .marquee__group{white-space:nowrap;font:500 clamp(3rem,10vw,9rem)/1 Inter,sans-serif;text-transform:uppercase;letter-spacing:-.04em}
/* hover-bloom logo card */
.logo-card{position:relative;overflow:hidden;flex:none;width:160px;height:96px;border-radius:999px;display:grid;place-items:center;
  background:#fff;border:1px solid rgb(226 232 240/.6);box-shadow:0 1px 2px rgb(0 0 0/.05);transition:border-color .3s}
.logo-card::before{content:"";position:absolute;inset:0;background:var(--g);opacity:0;transform:scale(1.5);transition:opacity .5s ease,transform .5s ease}
.logo-card img{position:relative;height:32px;width:auto;transition:filter .3s}
.logo-card:hover{border-color:rgb(203 213 225)}
.logo-card:hover::before{opacity:1;transform:scale(1)}
.logo-card:hover img{filter:brightness(0) invert(1)}
@media (prefers-reduced-motion:reduce){.marquee{overflow-x:auto}.marquee__track{animation:none}}
```
```js
document.querySelectorAll('.marquee').forEach((m) => {
  const track = m.querySelector('.marquee__track');
  const group = track.querySelector('.marquee__group');
  const originals = [...group.children];
  const build = () => {
    track.querySelectorAll('.marquee__group[aria-hidden]').forEach((g) => g.remove());
    let guard = 0;
    while (group.scrollWidth < m.clientWidth && guard++ < 10) originals.forEach((n) => {   // fill at least one screen
      const c = n.cloneNode(true); c.setAttribute('aria-hidden', 'true'); group.append(c);
    });
    const clone = group.cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    track.append(clone);
    track.style.setProperty('--dur', `${(group.scrollWidth / +(m.dataset.speed || 50)).toFixed(2)}s`);
  };
  const imgs = [...group.querySelectorAll('img')];
  Promise.all(imgs.map((i) => (i.complete ? 0 : new Promise((r) => { i.onload = i.onerror = r; })))).then(build);
});
```
**GSAP variant:** `gsap.to(track, { xPercent: -50, duration: 40, ease: 'none', repeat: -1 })`.

---

## 11. Infinite looping card slider (triple clone + instant re-centre)

**What / when:** A card carousel that loops forever in both directions with real CSS transitions: prev/next buttons, click-a-card-to-focus, optional autoplay that pauses on hover and focus. For locations, testimonials and case studies.

**Premium parameters**
- Track transition **640 ms** `--ease-out-quint` (testimonials: 0.8 s `--ease-material`).
- Cards `flex: 0 0 clamp(300px, 19.4vw, 430px)`, height 220 px, padding 24 px, radius **24 px**, soft shadow `0 18px 52px rgba(2,47,64,.12)`; gap `clamp(16px, 1.15vw, 24px)`; mobile `min(82vw, 330px)`.
- Round controls **54 px**, `rgba(253,241,225,.94)` on photos with `0 18px 36px rgba(0,0,0,.2)` (or bordered 48 px circles on white pages).
- Autoplay **3 s**, paused on hover/focus. Cards that have passed can fade and scale out (`opacity 0, scale(.9)`).
- Loop mechanism: render 3 copies, start in the middle copy; after a transition ends outside the middle copy, jump by ±N with transitions disabled. Only the middle copy is focusable.
- `--peek` positions the active card: a positive gutter (`48px`) aligns it with page content; a negative value (`-18vw`) lets it bleed off the left edge for an editorial crop.

**Implementation**
```html
<div class="slider" data-autoplay="3000">
  <div class="slider__viewport">
    <div class="slider__track">
      <article class="slider__card" tabindex="0" role="button" aria-label="Open card one">…</article>
      <!-- 4–6 cards -->
    </div>
  </div>
  <div class="slider__nav">
    <button class="slider__btn" data-dir="-1" aria-label="Previous">←</button>
    <button class="slider__btn" data-dir="1"  aria-label="Next">→</button>
  </div>
</div>
```
```css
.slider__viewport{overflow:hidden}
.slider__track{--shift:0px;display:flex;gap:clamp(16px,1.15vw,24px);
  transform:translate3d(calc(var(--shift) + var(--peek,48px)),0,0);transition:transform 640ms var(--ease-out-quint);will-change:transform}
.slider__track.is-jumping,.slider__track.is-jumping .slider__card{transition:none}
.slider__card{position:relative;flex:0 0 clamp(300px,19.4vw,430px);height:220px;padding:24px;border-radius:24px;overflow:hidden;
  background:#fdf1e1;color:#000;box-shadow:0 18px 52px rgba(2,47,64,.12);cursor:pointer;user-select:none;transition:opacity .5s ease,transform .5s ease}
.slider__card.is-past{opacity:0;transform:scale(.9)}
.slider__card:focus-visible{outline:2px solid #000;outline-offset:3px}
.slider__nav{display:flex;gap:14px;margin:16px 0 0 48px}
.slider__btn{width:54px;height:54px;border-radius:999px;border:0;background:rgba(253,241,225,.94);color:#111;box-shadow:0 18px 36px rgba(0,0,0,.2);cursor:pointer}
@media (max-width:640px){.slider__card{flex-basis:min(82vw,330px)}}
@media (prefers-reduced-motion:reduce){.slider__track,.slider__card{transition:none}}
```
```js
function initInfiniteSlider(root) {
  const track = root.querySelector('.slider__track');
  const originals = [...track.children];
  const n = originals.length;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const cards = [];
  track.replaceChildren();
  for (let set = 0; set < 3; set++) originals.forEach((card, i) => {
    const c = card.cloneNode(true);
    c.dataset.index = set * n + i;
    if (set !== 1) { c.setAttribute('aria-hidden', 'true'); c.tabIndex = -1; }   // only the middle copy is focusable
    track.append(c); cards.push(c);
  });
  let active = n;
  const update = () => {
    const step = cards[0].offsetWidth + parseFloat(getComputedStyle(track).columnGap || 0);
    track.style.setProperty('--shift', `${-step * active}px`);
    cards.forEach((c, i) => { c.classList.toggle('is-active', i === active); c.classList.toggle('is-past', i < active); });
  };
  const jump = (i) => {                              // teleport to the equivalent card, no transition
    track.classList.add('is-jumping');
    active = i; update();
    void track.offsetWidth;                          // commit before re-enabling transitions
    track.classList.remove('is-jumping');
  };
  const normalize = () => { if (active >= 2 * n) jump(active - n); else if (active < n) jump(active + n); };
  const go = (i) => { active = i; update(); if (reduce) normalize(); };
  const move = (dir) => { if (active + dir < 0 || active + dir > 3 * n - 1) normalize(); go(active + dir); };
  track.addEventListener('transitionend', (e) => { if (e.target === track && e.propertyName === 'transform') normalize(); });
  cards.forEach((c) => {
    c.addEventListener('click', () => go(+c.dataset.index));
    c.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(+c.dataset.index); } });
  });
  root.querySelectorAll('[data-dir]').forEach((b) => b.addEventListener('click', () => move(+b.dataset.dir)));
  addEventListener('resize', () => jump(active));
  const ms = +root.dataset.autoplay || 0;
  if (ms && !reduce) {
    let timer = setInterval(() => move(1), ms);
    const stop = () => clearInterval(timer);
    const start = () => { stop(); timer = setInterval(() => move(1), ms); };
    root.addEventListener('mouseenter', stop); root.addEventListener('mouseleave', start);
    root.addEventListener('focusin', stop);    root.addEventListener('focusout', start);
  }
  jump(active);
}
document.querySelectorAll('.slider').forEach(initInfiniteSlider);
```
