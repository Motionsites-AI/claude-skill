# Depth & interaction

Pointer-driven depth, cursor effects and interactive showcases.

**Conventions.** Single-file, no build step, dark page unless stated. Shared tokens (paste once):
```css
:root{
  --ease-out-expo:cubic-bezier(.16,1,.3,1);
  --ease-out-quint:cubic-bezier(.22,1,.36,1);
  --ease-standard:cubic-bezier(.25,.1,.25,1);
  --ease-material:cubic-bezier(.4,0,.2,1);
}
```
Pointer effects run only on `(hover: hover) and (pointer: fine)` with motion allowed; give touch screens an autonomous or static alternative. Measure an **untransformed** wrapper and move an inner element, or the moving box feeds back into its own measurement.

---

## 1. Depth carousel with role slots and background-colour crossfade

**What / when:** A product or character carousel built from depth rather than sliding. One item is huge and sharp in the centre; two are small and slightly blurred to the sides; the rest are tiny and more blurred at the back. Navigating rotates items through these *roles*, and the page background crossfades to the active item's colour. For collectibles, colourways and character line-ups (3–6 items). Pairs with a ghost word behind the subject (type-and-text-motion.md, technique 11) and grain.

**Premium parameters**
- One shared transition on every animated property: **650 ms** `cubic-bezier(.4,0,.2,1)`, which also drives the background colour.
- Desktop roles: center `left 50%, height 92%, bottom 0, scale 1.68`, no blur, z 20 · left `left 30%, height 28%, bottom 12%, blur(2px), opacity .85`, z 10 · right the same at `left 70%` · back `left 50%, height 22%, bottom 12%, blur(4px)`, z 5.
- Mobile (<640 px): center `height 60%, bottom 22%, scale 1.25`; sides at 20 % / 80 %, `height 16%, bottom 32%`; back `height 13%, bottom 32%`.
- Items `aspect-ratio: .6/1`, `object-fit:contain; object-position:bottom center`, `will-change: transform, filter, opacity`. Preload all images.
- An animation lock (650 ms) ignores clicks mid-transition.
- Controls: 48 → 64 px circular outline buttons (2 px white border, 26 px arrow at stroke 2.25); hover `scale(1.08)` + `rgba(255,255,255,.12)` fill over 150 ms.
- Palette idea: each item gets a saturated bg and a lighter panel tint (`#F4845F/#F79B7F`, `#6BBF7A/#85CC92`, `#E882B4/#ED9DC4`, `#6EB5FF/#8DC4FF`).

**Implementation**
```html
<section class="dc" tabindex="0" aria-roledescription="carousel" aria-label="Collection">
  <div class="dc-stage">
    <img class="dc-item" src="a.png" alt="Item A" draggable="false">
    <img class="dc-item" src="b.png" alt="Item B" draggable="false">
    <img class="dc-item" src="c.png" alt="Item C" draggable="false">
    <img class="dc-item" src="d.png" alt="Item D" draggable="false">
  </div>
  <button class="dc-btn" data-dir="-1" aria-label="Previous">←</button>
  <button class="dc-btn" data-dir="1" aria-label="Next">→</button>
</section>
```
```css
.dc{--e:cubic-bezier(.4,0,.2,1);position:relative;height:100vh;height:100dvh;overflow:hidden;
  background:var(--bg,#F4845F);transition:background-color 650ms var(--e)}
.dc-stage{position:absolute;inset:0;z-index:3}
.dc-item{position:absolute;aspect-ratio:.6/1;object-fit:contain;object-position:bottom center;
  transform:translateX(-50%) scale(1);transform-origin:bottom center;will-change:transform,filter,opacity;
  transition:transform 650ms var(--e),filter 650ms var(--e),opacity 650ms var(--e),left 650ms var(--e),height 650ms var(--e),bottom 650ms var(--e)}
.dc-item[data-role=center]{left:50%;height:92%;bottom:0;transform:translateX(-50%) scale(1.68);filter:none;opacity:1;z-index:20}
.dc-item[data-role=left]  {left:30%;height:28%;bottom:12%;filter:blur(2px);opacity:.85;z-index:10}
.dc-item[data-role=right] {left:70%;height:28%;bottom:12%;filter:blur(2px);opacity:.85;z-index:10}
.dc-item[data-role=back]  {left:50%;height:22%;bottom:12%;filter:blur(4px);opacity:1;z-index:5}
@media (max-width:639px){
  .dc-item[data-role=center]{height:60%;bottom:22%;transform:translateX(-50%) scale(1.25)}
  .dc-item[data-role=left]{left:20%;height:16%;bottom:32%}
  .dc-item[data-role=right]{left:80%;height:16%;bottom:32%}
  .dc-item[data-role=back]{height:13%;bottom:32%}
}
.dc-btn{position:relative;z-index:60;width:64px;height:64px;border-radius:50%;border:2px solid #fff;background:transparent;color:#fff;
  cursor:pointer;transition:transform 150ms,background-color 150ms}
.dc-btn:hover{transform:scale(1.08);background:rgba(255,255,255,.12)}
@media (max-width:639px){.dc-btn{width:48px;height:48px}}
@media (prefers-reduced-motion:reduce){.dc,.dc-item{transition:none}}
```
```js
(function depthCarousel(root, colors) {
  const items = [...root.querySelectorAll('.dc-item')];
  const N = items.length;
  const roleFor = (off) => (off === 0 ? 'center' : off === 1 ? 'right' : off === N - 1 ? 'left' : 'back');
  let active = 0, locked = false;
  items.forEach((img) => { const p = new Image(); p.src = img.src; });   // preload
  const render = () => {
    items.forEach((el, i) => {
      const role = roleFor((i - active + N) % N);
      el.dataset.role = role;
      el.setAttribute('aria-hidden', String(role !== 'center'));
    });
    root.style.setProperty('--bg', colors[active % colors.length]);
  };
  const go = (dir) => {
    if (locked) return;
    locked = true;
    active = (active + (dir > 0 ? 1 : N - 1)) % N;
    render();
    setTimeout(() => { locked = false; }, 650);
  };
  root.querySelectorAll('.dc-btn').forEach((b) => b.addEventListener('click', () => go(+b.dataset.dir)));
  root.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight') go(1); if (e.key === 'ArrowLeft') go(-1); });
  let x0 = null;                                  // swipe
  root.addEventListener('pointerdown', (e) => { x0 = e.clientX; });
  root.addEventListener('pointerup', (e) => { if (x0 !== null && Math.abs(e.clientX - x0) > 40) go(e.clientX < x0 ? 1 : -1); x0 = null; });
  render();
})(document.querySelector('.dc'), ['#F4845F', '#6BBF7A', '#E882B4', '#6EB5FF']);
```

---

## 2. Magnetic hover (element drifts toward the cursor)

**What / when:** When the cursor comes within a generous radius, an element (portrait, CTA, logo) eases toward it by a fraction of the distance, then floats back slowly when the cursor leaves. It adds weight and life. Use it on hero subjects and primary buttons.

**Premium parameters**
- Activation zone: the element's box plus 150 px (40–80 px for buttons).
- Strength 3: the element moves 1/3 of the cursor offset from its centre (2–4 is the sweet spot).
- Asymmetric easing: `transform .3s ease-out` while tracking, `.6s ease-in-out` on release. The return is slower than the pull.
- Measure the untransformed wrapper, move an inner element. Positioning transforms (like centring with `translateX(-50%)`) belong on the wrapper.
- `translate3d` + `will-change: transform`; fine pointers with motion allowed only.

**Implementation**
```html
<div class="magnet" data-padding="150" data-strength="3"><img class="magnet-inner" src="portrait.png" alt=""></div>
```
```js
function magnet(wrap, { padding = 150, strength = 3 } = {}) {
  if (!matchMedia('(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)').matches) return;
  const inner = wrap.firstElementChild;
  inner.style.willChange = 'transform';
  let active = false, raf = 0, mx = 0, my = 0;
  const update = () => {
    raf = 0;
    const r = wrap.getBoundingClientRect();          // wrapper is never transformed
    const dx = mx - (r.left + r.width / 2), dy = my - (r.top + r.height / 2);
    const inside = Math.abs(dx) < r.width / 2 + padding && Math.abs(dy) < r.height / 2 + padding;
    if (inside) {
      if (!active) { active = true; inner.style.transition = 'transform .3s ease-out'; }
      inner.style.transform = `translate3d(${dx / strength}px, ${dy / strength}px, 0)`;
    } else if (active) {
      active = false;
      inner.style.transition = 'transform .6s ease-in-out';
      inner.style.transform = 'translate3d(0,0,0)';
    }
  };
  addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; if (!raf) raf = requestAnimationFrame(update); }, { passive: true });
}
document.querySelectorAll('.magnet').forEach((el) => magnet(el, { padding: +el.dataset.padding || 150, strength: +el.dataset.strength || 3 }));
```

---

## 3. Pointer parallax depth layers

**What / when:** Stacked transparent layers drift with or against the pointer by different amounts, giving a still photo real depth. Cheap, subtle, and works on any layered hero (combines with the sticky cinematic stage in scroll.md).

**Premium parameters**
- Normalised pointer `[-0.5, 0.5]`, eased with **lerp 0.12** per rAF; the loop stops once settled.
- Depths (px per unit of pointer): far background **−12 x / −4 y** (moves against the cursor), subject **+18 / +8**, foreground **+22 / +10**. Vertical ≈ 0.35–0.45 × horizontal: horizontal parallax reads stronger and vertical motion feels seasick.
- Overscan every layer (`inset:-4%` or `scale(1.03+)`) so edges never show.

**Implementation**
```html
<div class="px-scene">
  <img class="px-layer" style="--dx:-12;--dy:-4" src="far.jpg" alt="">
  <img class="px-layer" style="--dx:18;--dy:8"   src="subject.png" alt="">
  <img class="px-layer" style="--dx:22;--dy:10"  src="foreground.png" alt="">
</div>
```
```css
.px-scene{position:relative;height:100vh;height:100dvh;overflow:hidden;--mx:0;--my:0}
.px-layer{position:absolute;inset:-4%;width:108%;height:108%;object-fit:cover;pointer-events:none;will-change:transform;
  transform:translate3d(calc(var(--mx) * var(--dx) * 1px),calc(var(--my) * var(--dy) * 1px),0)}
```
```js
(() => {
  const scene = document.querySelector('.px-scene');
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let tx = 0, ty = 0, x = 0, y = 0, raf = 0;
  const loop = () => {
    x += (tx - x) * 0.12; y += (ty - y) * 0.12;
    scene.style.setProperty('--mx', x.toFixed(4)); scene.style.setProperty('--my', y.toFixed(4));
    raf = (Math.abs(tx - x) > 0.0005 || Math.abs(ty - y) > 0.0005) ? requestAnimationFrame(loop) : 0;
  };
  addEventListener('pointermove', (e) => {
    tx = e.clientX / innerWidth - 0.5; ty = e.clientY / innerHeight - 0.5;
    if (!raf) raf = requestAnimationFrame(loop);
  }, { passive: true });
})();
```

---

## 4. Cursor-following spotlight reveal mask

**What / when:** Two aligned full-bleed images (surface vs cross-section, day vs night, sketch vs render); a soft glowing circle trailing the cursor reveals the second one. A signature "discovery" interaction for explanatory heroes.

**Premium parameters**
- Radius **260 px**; cursor smoothing **lerp 0.1** per rAF (the trailing lag is what makes it feel physical).
- Feathered mask stops: `0 → 1`, `.4 → 1`, `.6 → .75`, `.75 → .4`, `.88 → .12`, `1 → 0`.
- Start off-screen (`-999px`) so nothing shows until the first move; snap to the first pointer position (no fly-in). The radius eases to 0 on pointer leave via an animatable `@property`.
- Base image settles `scale(1.12 → 1)` over 1.8 s `--ease-out-expo`. The heading uses `pointer-events:none` so it never blocks the reveal.
- Touch screens: the spotlight drifts on its own along a slow Lissajous path.
- A CSS `radial-gradient` mask driven by custom properties is far cheaper than drawing a canvas mask every frame.

**Implementation**
```html
<section class="spot">
  <div class="spot__base"   style="background-image:url(base.jpg)"></div>
  <div class="spot__reveal" style="background-image:url(reveal.jpg)"></div>
  <div class="spot__content">…</div>
</section>
```
```css
@property --spot-r{syntax:'<length>';inherits:true;initial-value:0px}
.spot{position:relative;height:100vh;height:100dvh;overflow:hidden;background:#000;
  --x:-999px;--y:-999px;--spot-r:0px;transition:--spot-r .45s var(--ease-out-expo)}
.spot.is-lit{--spot-r:260px}
.spot__base,.spot__reveal{position:absolute;inset:0;background-position:center;background-size:cover;background-repeat:no-repeat}
.spot__base{z-index:1;animation:spot-settle 1.8s var(--ease-out-expo) both}
.spot__reveal{z-index:3;pointer-events:none;
  -webkit-mask-image:radial-gradient(circle var(--spot-r) at var(--x) var(--y),#000 0%,#000 40%,rgba(0,0,0,.75) 60%,rgba(0,0,0,.4) 75%,rgba(0,0,0,.12) 88%,transparent 100%);
          mask-image:radial-gradient(circle var(--spot-r) at var(--x) var(--y),#000 0%,#000 40%,rgba(0,0,0,.75) 60%,rgba(0,0,0,.4) 75%,rgba(0,0,0,.12) 88%,transparent 100%);
  -webkit-mask-repeat:no-repeat;mask-repeat:no-repeat}
.spot__content{position:relative;z-index:5;height:100%;pointer-events:none}
.spot__content a,.spot__content button{pointer-events:auto}
@keyframes spot-settle{from{transform:scale(1.12)}to{transform:scale(1)}}
@media (prefers-reduced-motion:reduce){.spot__base{animation:none}}
```
```js
(() => {
  const spot = document.querySelector('.spot');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let tx = 0, ty = 0, sx = 0, sy = 0, seeded = false, raf = 0;
  const loop = () => {
    const k = reduce ? 1 : 0.1;
    sx += (tx - sx) * k; sy += (ty - sy) * k;
    spot.style.setProperty('--x', sx.toFixed(1) + 'px');
    spot.style.setProperty('--y', sy.toFixed(1) + 'px');
    raf = (Math.abs(tx - sx) > 0.1 || Math.abs(ty - sy) > 0.1) ? requestAnimationFrame(loop) : 0;
  };
  const setTarget = (x, y) => {
    tx = x; ty = y;
    if (!seeded) { sx = x; sy = y; seeded = true; }    // no fly-in from off-screen
    spot.classList.add('is-lit');
    if (!raf) raf = requestAnimationFrame(loop);
  };
  spot.addEventListener('pointermove', (e) => { const r = spot.getBoundingClientRect(); setTarget(e.clientX - r.left, e.clientY - r.top); });
  spot.addEventListener('pointerleave', () => spot.classList.remove('is-lit'));
  if (matchMedia('(hover: none)').matches) {          // touch: slow autonomous drift (parked in the centre for reduced motion)
    const t0 = performance.now();
    (function drift(now) {
      const r = spot.getBoundingClientRect(), p = (now - t0) / 1000, k = reduce ? 0 : 1;
      setTarget(r.width * (0.5 + 0.28 * Math.sin(p * 0.45) * k), r.height * (0.55 + 0.18 * Math.sin(p * 0.8) * k));
      if (!reduce) requestAnimationFrame(drift);
    })(t0);
  }
})();
```
`@property` makes the radius animatable (Chrome/Edge, Safari 16.4+, Firefox 128+); elsewhere it simply snaps.

---

## 5. Cursor image trail

**What / when:** Moving the mouse over a big CTA block spawns thumbnails of your work at the cursor, each slightly rotated, fading and shrinking away: a playful "portfolio spray" behind a "Let's work together" heading.

**Premium parameters:** spawn at most every **80 ms**; random rotation **−10°…+10°**; life **1000 ms**, fading to `opacity 0, scale(.6)`; thumbs ~200–240 px, radius 12 px, soft shadow; a huge calm container (`padding 12rem 0`, radius 40 px, subtle shadow), heading 48 → 80 px. Off on touch and for reduced motion.

**Implementation**
```html
<section class="trail-area">
  <h2 class="trail-area__title">Let's build together</h2>
  <a class="btn" href="#">Start a chat</a>
</section>
```
```css
.trail-area{position:relative;overflow:hidden;padding:12rem 1.5rem;border-radius:40px;background:#fff;text-align:center;box-shadow:0 4px 16px rgba(0,0,0,.08)}
.trail-area>*:not(.trail-img){position:relative;z-index:2}
.trail-area__title{font-size:clamp(48px,6vw,80px);letter-spacing:-.02em;margin:0 0 3rem}
.trail-img{position:absolute;z-index:1;pointer-events:none;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.15);object-fit:cover}
```
```js
function imageTrail(area, srcs, { every = 80, life = 1000, size = 220 } = {}) {
  if (matchMedia('(prefers-reduced-motion: reduce), (hover: none)').matches) return;
  srcs.forEach((s) => { const i = new Image(); i.src = s; });           // preload
  let last = 0, n = 0;
  area.addEventListener('pointermove', (e) => {
    const now = performance.now();
    if (now - last < every) return;
    last = now;
    const r = area.getBoundingClientRect();
    const img = document.createElement('img');
    img.src = srcs[n++ % srcs.length]; img.alt = ''; img.className = 'trail-img';
    img.style.width = `${size}px`; img.style.aspectRatio = '4 / 3';
    img.style.left = `${e.clientX - r.left}px`; img.style.top = `${e.clientY - r.top}px`;
    const rot = (Math.random() * 20 - 10).toFixed(1);
    area.append(img);
    img.animate([
      { opacity: 1, transform: `translate(-50%,-50%) rotate(${rot}deg) scale(1)` },
      { opacity: 0, transform: `translate(-50%,-50%) rotate(${rot}deg) scale(.6)` },
    ], { duration: life, easing: 'cubic-bezier(.4,0,.2,1)', fill: 'forwards' }).onfinish = () => img.remove();
  });
}
imageTrail(document.querySelector('.trail-area'), ['w1.webp', 'w2.webp', 'w3.webp', 'w4.webp']);
```

---

## 6. Exclusion-blend overlay UI & custom cursor

**What / when:** All fixed UI (wordmark, nav, captions, price, footer, cursor) is white with `mix-blend-mode: exclusion`, so it inverts automatically: white over dark footage, black over the white sections that later slide beneath it. One fixed layer survives a page that goes video → black → white. Add a custom circular glyph cursor with the same blend.

**Premium parameters**
- Overlay elements: `position:fixed; color:#fff; mix-blend-mode:exclusion; pointer-events:none` (re-enabled on real links), `z-index:20`; corners at 32 px desktop / 16 px mobile.
- One family at weight 500, `letter-spacing:-.04em`; uppercase 13–15 px nav, 30 px collection label, 80 px price-size numbers.
- Cursor: 48 px SVG (circle `r=22.75`, stroke 2.5) with a glyph inside, centred on the pointer, hidden below 1024 px and on touch; the native cursor is hidden only for fine pointers.
- Micro-detail: a glyph inside a small circle randomises on scroll (`8 $ ^^ % /`), throttled to 80 ms.
- Entrance stagger: logo 0 · nav .15 · caption .3 · product info .45 s (`opacity 0, y 12 → 0`, 0.6 s `--ease-standard`).
- **Stacking gotcha:** blending happens against what is painted inside the same stacking context. Keep blended elements as direct children of `body` (or of the media's wrapper). A parent with `transform`, `filter`, `opacity < 1`, `isolation` or `will-change` traps the blend, so animate the blended element itself, not a wrapper.

**Implementation**
```html
<div class="ui-blend ui-blend--logo">WORDMARK</div>
<nav class="ui-blend ui-blend--nav"><a href="#">About</a><a href="#">[ Cart ]</a></nav>
<div class="ui-blend ui-blend--info"><span class="glyph-ring"><span class="glyph">8</span></span>…</div>
<div class="cursor" aria-hidden="true">
  <svg width="48" height="48" viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="22.75" stroke="#fff" stroke-width="2.5"/>
    <path d="M17 24h14M24 17v14" stroke="#fff" stroke-width="2.5"/></svg>
</div>
```
```css
.ui-blend{position:fixed;z-index:20;color:#fff;mix-blend-mode:exclusion;pointer-events:none;
  font:500 15px/1 'Inter Tight',Inter,sans-serif;letter-spacing:-.04em;text-transform:uppercase}
.ui-blend a{pointer-events:auto;color:inherit;text-decoration:none}
.ui-blend--logo{top:32px;left:32px}
.ui-blend--nav{top:32px;right:32px;width:330px;display:flex;justify-content:space-between}
.ui-blend--info{right:32px;bottom:80px;width:330px;text-align:center}
.glyph-ring{display:inline-grid;place-items:center;width:30px;height:30px;border:2.5px solid currentColor;border-radius:50%;font-size:15px}
@media (max-width:640px){.ui-blend--logo{top:16px;left:16px}.ui-blend--nav{top:16px;right:16px;width:auto;gap:20px}
  .ui-blend--info{left:0;right:0;bottom:48px;width:auto}}
.cursor{position:fixed;left:0;top:0;z-index:50;pointer-events:none;mix-blend-mode:exclusion;will-change:transform}
@media (hover:none),(pointer:coarse),(max-width:1023px){.cursor{display:none}}
@media (hover:hover) and (pointer:fine) and (min-width:1024px){html.has-cursor,html.has-cursor a,html.has-cursor button{cursor:none}}
```
```js
(() => {
  const cur = document.querySelector('.cursor');
  if (matchMedia('(hover: hover) and (pointer: fine) and (min-width: 1024px)').matches) {
    document.documentElement.classList.add('has-cursor');
    addEventListener('pointermove', (e) => { cur.style.transform = `translate3d(${e.clientX - 24}px, ${e.clientY - 24}px, 0)`; }, { passive: true });
  }
  const glyph = document.querySelector('.glyph'), set = ['8', '$', '^^', '%', '/'];
  let lastG = 0;
  addEventListener('scroll', () => {
    const now = performance.now();
    if (now - lastG < 80) return;
    lastG = now;
    glyph.textContent = set[(Math.random() * set.length) | 0];
  }, { passive: true });
})();
```
Keep a visible focus style for keyboard users even when the native cursor is hidden.

---

## 7. Orbit rings with counter-rotating avatars

**What / when:** A "network" visual for talent marketplaces, communities and integrations: concentric hairline rings slowly rotate in alternating directions, avatars ride on them but stay upright, and a big count-up number sits in the centre. Replaces a boring logo grid or stock illustration.

**Premium parameters**
- Container **720×720**; ring diameters **353 / 501 / 649 / 797 px** (148 px spacing; the outer ring deliberately overflows); periods **30 / 40 / 50 / 60 s**, directions **ccw / cw / cw / ccw**.
- Ring stroke: 1 px gradient `accent 0 → 1 @43 % → 0` via the mask-composite ring, so a bright arc travels as the ring spins.
- Avatars 58 px (feature ones 78–88 px; squircles radius 20–24 px mixed with circles) with a coloured glow `0 0 24px <colour>`, placed by `rotate(a) translate(r) rotate(−a)`, `r = diameter/2`.
- Fly-in per avatar: `scale(.3) rotate(−180deg) blur(8px)` → rest, staggered **0.6 → 2.3 s**, `--ease-out-quint`; container `scale(.85 → 1)` 1.2 s at 0.3 s.
- Centre: count-up 0 → 20 over 2 s starting at 1.2 s (type-and-text-motion.md, technique 13), display font 64 px + 16 px label.
- Responsive scale `.85` ≤1280 px, `.7` ≤1024, `.5` ≤768, `.4` ≤480.

**Implementation**
```html
<div class="orbits-wrap">
  <div class="orbits">
    <div class="orbit" data-dir="ccw" style="--d:353px;--t:30s">
      <div class="orbit__item" style="--a:270deg;--r:177px"><div class="orbit__upright">
        <img class="orbit__pop" src="a1.jpg" alt="" style="--delay:.6s;--glow:#a068ff;border-radius:20px"></div></div>
    </div>
    <div class="orbit" style="--d:501px;--t:40s">
      <div class="orbit__item" style="--a:60deg;--r:251px"><div class="orbit__upright">
        <img class="orbit__pop" src="a2.jpg" alt="" style="--delay:.8s;--glow:#ffd166"></div></div>
      <div class="orbit__item" style="--a:180deg;--r:251px"><div class="orbit__upright">
        <img class="orbit__pop orbit__pop--lg" src="a3.jpg" alt="" style="--delay:1s;--glow:#ff5fa2"></div></div>
    </div>
    <div class="orbit" style="--d:649px;--t:50s"></div>
    <div class="orbit" data-dir="ccw" style="--d:797px;--t:60s"></div>
    <div class="orbits__center"><strong data-count="20" data-suffix="k+">20k+</strong><span>Specialists</span></div>
  </div>
</div>
```
```css
.orbits-wrap{--s:1;display:flex;justify-content:center;height:calc(720px * var(--s));overflow:visible}
.orbits{position:relative;flex:none;width:720px;height:720px;transform:scale(var(--s));transform-origin:top center;
  animation:orbits-in 1.2s var(--ease-out-quint) .3s both}
.orbit{position:absolute;left:50%;top:50%;width:var(--d);height:var(--d);translate:-50% -50%;border-radius:50%;
  animation:orbit-spin var(--t) linear infinite}
.orbit[data-dir="ccw"]{animation-direction:reverse}
.orbit::before{content:"";position:absolute;inset:0;border-radius:50%;padding:1px;pointer-events:none;
  background:linear-gradient(180deg,rgba(217,161,255,0) 0%,rgba(217,161,255,1) 43%,rgba(217,161,255,0) 100%);
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask-composite:exclude}
.orbit__item{position:absolute;left:50%;top:50%;width:0;height:0;transform:rotate(var(--a)) translate(var(--r)) rotate(calc(-1 * var(--a)))}
.orbit__upright{position:absolute;translate:-50% -50%;animation:orbit-spin var(--t) linear infinite reverse}
.orbit[data-dir="ccw"] .orbit__upright{animation-direction:normal}
.orbit__pop{display:block;width:58px;height:58px;border-radius:50%;object-fit:cover;box-shadow:0 0 24px var(--glow);
  animation:orbit-pop 1s var(--ease-out-quint) var(--delay,0s) both}
.orbit__pop--lg{width:88px;height:88px}
.orbits__center{position:absolute;inset:0;display:grid;place-content:center;text-align:center;pointer-events:none}
.orbits__center strong{font:500 64px/1 Urbanist,Inter,sans-serif;font-variant-numeric:tabular-nums}
.orbits__center span{font:600 16px/1.4 Urbanist,Inter,sans-serif}
@keyframes orbit-spin{to{rotate:360deg}}
@keyframes orbit-pop{from{opacity:0;transform:scale(.3) rotate(-180deg);filter:blur(8px)}to{opacity:1;transform:none;filter:none}}
@keyframes orbits-in{from{opacity:0;scale:.85}to{opacity:1;scale:1}}
@media (max-width:1280px){.orbits-wrap{--s:.85}}
@media (max-width:1024px){.orbits-wrap{--s:.7}}
@media (max-width:768px){.orbits-wrap{--s:.5}}
@media (max-width:480px){.orbits-wrap{--s:.4}}
@media (prefers-reduced-motion:reduce){.orbit,.orbit__upright,.orbit__pop,.orbits{animation:none}}
```
How it stays upright: each ring spins via the individual `rotate` property; each avatar wrapper runs the *same* animation reversed, cancelling the ring's rotation; the static `rotate(−a)` in the placement cancels the placement angle. Individual `translate/rotate/scale` properties keep them from fighting the `transform` used by the pop-in. The flex wrapper centres the 720 px box even when the viewport is narrower; clip the section with `overflow-x: clip`.

---

## 8. Sand-dissolve image transition (SVG turbulence) + auto-cycling index list

**What / when:** A specimen or product image that disintegrates into drifting grains and re-forms as the next one, driven by an auto-advancing chapter list with a rolling counter. Archival and physical: great for collections, chapters and product variants.

**Premium parameters**
- Filter chain: `feTurbulence fractalNoise baseFrequency 1.8 numOctaves 4` → `feDisplacementMap` scale **0 → 150** → `feOffset` (exit `dx +30, dy +120`, grains fall; enter from `dx −30, dy −80`) → `feGaussianBlur` **0 → 6** → alpha `1 − p × 1.2`.
- **900 ms** per phase; exit eases in `t³`, enter eases out `1 − (1 − t)⁴`. The filter is removed at rest (no cost).
- Image `object-fit:contain` at 80 % of the panel, `mix-blend-mode: lighten` on a black panel (cut-outs float).
- List: auto-advance every **3500 ms**, pause on hover; active item white, idle `#444`, hover `#999`; 32 px rows divided by `rgba(31,41,55,.8)`; the active item shows a thin `↗`; counter `01 / 05` in mono 10 px with the number rolling vertically.

**Implementation**
```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <filter id="sand" x="-30%" y="-40%" width="160%" height="180%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="1.8" numOctaves="4" seed="3" result="noise"/>
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G" result="disp"/>
    <feOffset in="disp" dx="0" dy="0" result="off"/>
    <feGaussianBlur in="off" stdDeviation="0" result="blur"/>
    <feColorMatrix in="blur" type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0"/>
  </filter>
</svg>
<div class="chapters">
  <figure class="chapters__media"><img id="chapterImg" src="item-3.png" alt=""></figure>
  <div class="chapters__counter"><span class="roll"><span id="chapterNum">03</span></span> / 05</div>
  <ol class="chapters__list">
    <li><button data-img="item-1.png">Chapter one</button></li>
    <li><button data-img="item-2.png">Chapter two</button></li>
    <li><button data-img="item-3.png">Chapter three</button></li>
    <li><button data-img="item-4.png">Chapter four</button></li>
    <li><button data-img="item-5.png">Chapter five</button></li>
  </ol>
</div>
```
```css
.chapters{background:#0a0a0a;color:#fff}
.chapters__media{position:relative;aspect-ratio:1;margin:0;display:grid;place-items:center}
.chapters__media img{width:80%;height:80%;object-fit:contain;mix-blend-mode:lighten}
.chapters__counter{font:10px/1 ui-monospace,monospace;letter-spacing:.1em;color:#888;text-transform:uppercase}
.roll{display:inline-block;overflow:hidden;vertical-align:bottom}
.roll>span{display:inline-block}
.chapters__list{list-style:none;margin:0;padding:0}
.chapters__list button{all:unset;box-sizing:border-box;display:flex;justify-content:space-between;align-items:center;width:100%;
  padding:32px 0;border-bottom:1px solid rgba(31,41,55,.8);cursor:pointer;color:#444;transition:color .3s;
  font-size:clamp(1.5rem,2.4vw,2rem);font-weight:500;letter-spacing:-.025em}
.chapters__list button:hover{color:#999}
.chapters__list button:focus-visible{outline:1px solid #fff;outline-offset:4px}
.chapters__list button[aria-current="true"]{color:#fff}
.chapters__list button::after{content:"\2197";font-weight:200;color:#9ca3af;opacity:0;transform:translate(-6px,6px);transition:opacity .3s,transform .3s}
.chapters__list button[aria-current="true"]::after{opacity:1;transform:none}
```
```js
const sandState = { busy: false, next: null };
async function sandSwap(img, src, { duration = 900 } = {}) {
  if (sandState.busy) { sandState.next = src; return; }
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { img.src = src; return; }
  sandState.busy = true;
  const f = document.getElementById('sand');
  const disp = f.querySelector('feDisplacementMap'), off = f.querySelector('feOffset');
  const blur = f.querySelector('feGaussianBlur'), cm = f.querySelector('feColorMatrix');
  const apply = (p, dir) => {                 // p: 0 intact → 1 dissolved; dir: +1 exit, -1 enter
    disp.setAttribute('scale', (p * 150).toFixed(1));
    off.setAttribute('dx', (p * 30 * dir).toFixed(1));
    off.setAttribute('dy', (p * (dir > 0 ? 120 : -80)).toFixed(1));
    blur.setAttribute('stdDeviation', (p * 6).toFixed(2));
    cm.setAttribute('values', `1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 ${Math.max(0, 1 - p * 1.2).toFixed(3)} 0`);
  };
  const run = (from, to, ease, dir) => new Promise((res) => {
    const t0 = performance.now();
    const step = (now) => {
      const t = Math.min(1, (now - t0) / duration);
      apply(from + (to - from) * ease(t), dir);
      if (t < 1) requestAnimationFrame(step); else res();
    };
    requestAnimationFrame(step);
  });
  img.style.filter = 'url(#sand)';
  await run(0, 1, (t) => t * t * t, 1);                       // dissolve out (ease-in)
  img.src = src;
  try { await img.decode(); } catch (e) { /* show anyway */ }
  await run(1, 0, (t) => 1 - Math.pow(1 - t, 4), -1);         // re-form (ease-out)
  img.style.filter = '';
  sandState.busy = false;
  if (sandState.next && sandState.next !== src) { const n = sandState.next; sandState.next = null; sandSwap(img, n, { duration }); }
  else sandState.next = null;
}
function rollTo(el, text) {
  const out = el.animate([{ transform: 'translateY(0)', opacity: 1 }, { transform: 'translateY(-100%)', opacity: 0 }],
    { duration: 250, easing: 'ease-in', fill: 'forwards' });
  out.onfinish = () => {
    el.textContent = text; out.cancel();
    el.animate([{ transform: 'translateY(100%)', opacity: 0 }, { transform: 'translateY(0)', opacity: 1 }], { duration: 350, easing: 'cubic-bezier(.16,1,.3,1)' });
  };
}
(() => {
  const root = document.querySelector('.chapters');
  const img = document.getElementById('chapterImg'), num = document.getElementById('chapterNum');
  const btns = [...root.querySelectorAll('.chapters__list button')];
  let active = 2, timer = 0;
  const mark = () => btns.forEach((b, k) => b.setAttribute('aria-current', String(k === active)));
  const setActive = (i) => {
    if (i === active) return;
    active = i; mark();
    rollTo(num, String(i + 1).padStart(2, '0'));
    sandSwap(img, btns[i].dataset.img);
  };
  const start = () => { clearInterval(timer); timer = setInterval(() => setActive((active + 1) % btns.length), 3500); };
  btns.forEach((b, i) => b.addEventListener('click', () => { setActive(i); start(); }));
  root.addEventListener('mouseenter', () => clearInterval(timer));
  root.addEventListener('mouseleave', start);
  mark();
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) start();
})();
```
**Perf:** 4-octave high-frequency turbulence is expensive on big bitmaps. Keep the image ≤ ~600 px rendered; with several instances, clone the `<filter>` with unique ids.
