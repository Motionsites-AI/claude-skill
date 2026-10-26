# Surfaces & buttons

Materials (glass, frost, grain) and the button and card finishes built on them.

**Conventions.** Single-file, no build step, `*,*::before,*::after{box-sizing:border-box}`, dark page unless stated. Shared tokens (paste once):
```css
:root{
  --ease-out-expo:cubic-bezier(.16,1,.3,1);
  --ease-out-quint:cubic-bezier(.22,1,.36,1);
  --ease-standard:cubic-bezier(.25,.1,.25,1);
}
```
Always keep the `-webkit-` prefixes shown (`backdrop-filter`, `mask`, `mask-composite`, `background-clip`).

---

## 1. Liquid-glass surface (gradient hairline rim)

**What / when:** An almost-invisible frosted surface whose "edge" is a gradient hairline: bright at the top and bottom, fading to nothing at the sides, like light catching the rim of a lens. The signature chrome for UI floating over cinematic video: nav pills, logo discs, badges, secondary CTAs, email inputs, stat and feature cards. It replaces borders completely. Pair it with **one** solid white primary button.

**Premium parameters**
- Fill `rgba(255,255,255,.01)` + `background-blend-mode: luminosity`. The look comes from the blur and the rim, not the fill.
- **Subtle tier** (nav, chips, cards): `blur(4px)` (heavier blur kills the glass read on small chips), `inset 0 1px 1px rgba(255,255,255,.1)`, rim stops `.45 / .15 / 0 / 0 / .15 / .45` at `0 / 20 / 40 / 60 / 80 / 100 %`.
- **Strong tier** (primary glass CTA, big panels): `blur(50px)`, `4px 4px 4px rgba(0,0,0,.05), inset 0 1px 1px rgba(255,255,255,.15)`, rim `.5 / .2 / 0 / 0 / .2 / .5`. For menus and sheets you can drop the rim.
- **Dark tier** (bright footage): fill `rgba(0,0,0,.4)`, rim `.3 / .1 / 0 / 0 / .1 / .3`.
- Rim 1.4 px, drawn on `::before` with padding plus mask compositing (content-box XOR border-box). No `border` anywhere; `border-radius: inherit` on the pseudo-element.
- Sizes: 48×48 logo disc; nav pill `padding 6px` with `8px 12px` 14 px links; pills `10px 24px`; 40×40 icon circles; stat cards `p 20px, w 220px, radius 1.25rem`; feature cards `p 24px, min-h 360px, radius 1.25rem` with a nested 44×44 icon tile (radius .75rem); tags `4px 12px`, 11 px. Hover `scale(1.03)`.
- On a flat black background glass reads only as a hairline outline: it needs moving footage behind it.

**Implementation**
```css
.liquid-glass{position:relative;overflow:hidden;border:none;
  background:rgba(255,255,255,.01);background-blend-mode:luminosity;
  -webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);
  box-shadow:inset 0 1px 1px rgba(255,255,255,.1)}
.liquid-glass::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1.4px;pointer-events:none;
  background:linear-gradient(180deg,
    rgba(255,255,255,var(--rim-a,.45)) 0%,rgba(255,255,255,var(--rim-b,.15)) 20%,
    rgba(255,255,255,0) 40%,rgba(255,255,255,0) 60%,
    rgba(255,255,255,var(--rim-b,.15)) 80%,rgba(255,255,255,var(--rim-a,.45)) 100%);
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;          /* Chrome/Safari legacy keyword */
          mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
          mask-composite:exclude}      /* standard */
.liquid-glass--strong{-webkit-backdrop-filter:blur(50px);backdrop-filter:blur(50px);
  box-shadow:4px 4px 4px rgba(0,0,0,.05),inset 0 1px 1px rgba(255,255,255,.15)}
.liquid-glass--strong::before{--rim-a:.5;--rim-b:.2}
.liquid-glass--dark{background:rgba(0,0,0,.4)}
.liquid-glass--dark::before{--rim-a:.3;--rim-b:.1}
.liquid-glass--norim::before{content:none}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .liquid-glass{background:rgba(255,255,255,.08)}}
```
Keep the exact three-line mask form: it is the cross-browser-safe one. The rim covers the element, but the mask removes its content box, so only the 1.4 px ring paints and clicks pass through.

Applications:
```html
<!-- Announcement badge with an inner chip -->
<div class="liquid-glass" style="display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:4px 12px 4px 4px">
  <span style="background:#fff;color:#000;border-radius:999px;padding:4px 12px;font:600 12px/1 system-ui">New</span>
  <span style="font-size:14px;color:rgb(255 255 255/.9)">Announcing something worth reading</span>
</div>

<!-- Email capture pill, submit inside -->
<form class="liquid-glass" style="display:flex;align-items:center;gap:12px;border-radius:999px;padding:8px 8px 8px 24px;max-width:36rem">
  <input type="email" placeholder="Enter your email" aria-label="Email" style="flex:1;min-width:0;background:transparent;border:0;outline:0;color:#fff;font-size:16px">
  <button style="background:#fff;color:#000;border:0;border-radius:999px;padding:12px 28px;font-weight:500">Join</button>
</form>

<!-- Capability card: nested icon tile, right-aligned tags, flex spacer, serif-italic title -->
<article class="liquid-glass" style="border-radius:1.25rem;padding:24px;min-height:360px;display:flex;flex-direction:column">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px">
    <span class="liquid-glass" style="width:44px;height:44px;border-radius:.75rem;display:grid;place-items:center"><!-- svg --></span>
    <div style="display:flex;flex-wrap:wrap;justify-content:flex-end;gap:6px;max-width:70%">
      <span class="liquid-glass" style="border-radius:999px;padding:4px 12px;font-size:11px;white-space:nowrap">Tag one</span>
    </div>
  </div>
  <div style="flex:1"></div>
  <h3 style="font:italic 400 clamp(30px,3vw,36px)/1 'Instrument Serif',serif;letter-spacing:-1px">Card title</h3>
  <p style="margin-top:12px;font-size:14px;font-weight:300;line-height:1.35;max-width:32ch;color:rgb(255 255 255/.9)">Short supporting sentence.</p>
</article>
```

**Light-surface sibling ("frosted white"):** on bright footage use `background: rgb(255 255 255/.7); backdrop-filter: blur(12px); border: 1px solid rgb(255 255 255/.6); box-shadow: 0 1px 2px rgb(0 0 0/.05)`. A floating dock uses `.9` alpha, `blur(40px)` and `0 12px 40px rgba(0,0,0,.08)`.

**Perf:** `backdrop-filter` re-samples the moving video every frame. Use at most a few large `blur(50px)` surfaces; use the 4 px tier for repeated chips.

---

## 2. Frosted glass UI kit over video (chips, accent badge, numbered panel, contact card)

**What / when:** A consistent token set for an editorial page over moving footage: frosted chips, a left-accent label badge, a frosted list panel with numbered rows, and a "talk to a human" contact card. Heavier frost than liquid glass: use it where text *on* the glass must be legible.

**Premium parameters**
- Frost `rgba(255,255,255,.15)` (small chips) / `.10` (large panels), `blur(12px)`, border `1px rgba(255,255,255,.15–.25)`.
- Dark frosted pill (bright footage): `rgba(23,23,23,.9)` + `blur(8px)`; bright frosted pill: `rgba(255,255,255,.2)` + `blur(12px)` + border `rgba(255,255,255,.3)`.
- Left-accent badge: `border-left: 2px solid #fff`, `padding 6px 12px`, mono 11 px uppercase, tracking `.15em`.
- Text over video: white + layered `drop-shadow` (no box); mono labels 10–12 px, `.15em`, 55–60 % white.
- Numbered rows: mono index 11 px at 55 %; title 16–18 px medium; body 14 px at 70 %; dividers `rgba(255,255,255,.15)`; row padding 20 px; chevron nudges 2 px right on hover.
- Contact card: radius 12 px, padding 12 px, portrait **80×96** radius 8 px, name 14 px medium, role mono 10 px, mini white pill CTA 12 px with chevron.

**Implementation**
```css
.frost{background:rgba(255,255,255,.15);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.frost--panel{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.15);border-radius:16px}
.frost--dark{background:rgba(23,23,23,.9);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.on-video{color:#fff;filter:drop-shadow(0 4px 3px rgba(0,0,0,.07)) drop-shadow(0 2px 2px rgba(0,0,0,.06))}
.on-video--lg{filter:drop-shadow(0 10px 8px rgba(0,0,0,.04)) drop-shadow(0 4px 3px rgba(0,0,0,.1))}
.mono-label{font:500 11px/1.2 ui-monospace,'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.15em}
.accent-badge{display:inline-block;border-left:2px solid #fff;padding:6px 12px;
  background:rgba(255,255,255,.15);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.rows{max-width:28rem;padding:0 24px}
.row{display:flex;gap:20px;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.15)}
.row:last-child{border-bottom:0}
.row__idx{font:11px/1.6 ui-monospace,monospace;letter-spacing:.15em;color:rgba(255,255,255,.55)}
.row__title{display:flex;align-items:center;gap:6px;font-size:18px;font-weight:500}
.row__title svg{color:rgba(255,255,255,.4);transition:transform .3s,color .3s}
.row:hover .row__title svg{transform:translateX(2px);color:#fff}
.row__body{margin-top:6px;font-size:14px;line-height:1.6;color:rgba(255,255,255,.7)}
.contact-card{display:flex;align-items:center;gap:16px;padding:12px;border-radius:12px}
.contact-card img{width:80px;height:96px;border-radius:8px;object-fit:cover}
.contact-card .cta{margin-top:6px;display:inline-flex;align-items:center;gap:4px;border-radius:999px;background:#fff;color:#000;
  padding:8px 16px;font-size:12px;font-weight:500;transition:background .3s}
.contact-card .cta:hover{background:rgba(255,255,255,.85)}
```
```html
<span class="accent-badge mono-label">Short proof statement</span>
<div class="frost frost--panel rows">
  <div class="row"><span class="row__idx">01</span><div>
    <div class="row__title">Capability <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></div>
    <p class="row__body">One-line explanation.</p></div></div>
  <!-- 02, 03 … -->
</div>
<div class="frost contact-card">
  <img src="portrait.jpg" alt="Team member">
  <div><div style="font-size:14px;font-weight:500">Name Surname</div><div class="mono-label" style="font-size:10px;opacity:.6">Role</div>
    <a class="cta" href="#contact">Book a call ›</a></div>
</div>
```

---

## 3. Premium button finishes (liquid-metal + sweep shine, halo pill, jewel pill)

**What / when:** Finishes that make a CTA feel machined rather than flat. **(a) Liquid-metal** brushed gradients with a light sweep on hover, for monochrome or tech brands. **(b) Halo-glow white pill**, the single bright object on a dark video. **(c) Jewel-gradient pill**, saturated multi-stop gradient with inner shadow and an inset white ring, for creator or portfolio pages.

**Premium parameters**
- **Sweep shine:** a 115° band `transparent 20–30 % → rgba(255,255,255,.16–.45) ~50 % → transparent 70–76 %`, from `translateX(-120…-130%)` to `+120…130%` over 0.6–0.65 s ease on hover. `isolation:isolate` + `z-index:-1` makes it pass between the fill and the label.
- **Chrome solid:** `linear-gradient(180deg,#fff 0%,#e7e7e7 48%,#cfcfcf 100%)`, text `#111`, `1px solid #fff`, `inset 0 1px 0 rgba(255,255,255,.95)`. Hover `#fff → #f3f6ff 42% → #d5def2` with glow `0 0 22px rgba(186,208,255,.35), 0 8px 18px rgba(255,255,255,.12)`.
- **Frosted ghost:** `linear-gradient(135deg, rgba(255,255,255,.12), rgba(0,0,0,.5) 46%, rgba(150,170,200,.1))`, `1px solid rgba(198,198,198,.55)`, `blur(16px)`. Hover border `rgba(220,230,255,.8)`, glow `0 0 24px rgba(170,200,255,.28)`.
- **Metal nav tab:** `linear-gradient(105deg,#050505 0%,#2a2a2a 48%,#4a4a4a 100%)`, `1px solid rgba(198,198,198,.55)`, radius 7 px, height 40 px, padding 0 18 px. Hover `#111 → #3a3a3a 45% → #6a6a6a`, border `rgba(235,235,235,.9)`, glow `0 0 18px rgba(200,210,230,.18)`.
- **Metal badge:** `linear-gradient(90deg,#7d7d7d 0%,#2a2a2a 52%,#0a0a0a 100%)`, radius 5 px, padding 9×15 px, a 4-point sparkle icon with `drop-shadow(0 0 3px rgba(255,255,255,.45))`.
- Geometry: height 40–42 px, radius 6 px (crisp) or 999 px (pill), weight 500, `letter-spacing:-.02em`, `line-height:1`, 0.35 s transitions on background, border, shadow, colour, filter.
- **Halo pill:** white, black text, weight 600, `0 0 0 1px rgba(255,255,255,.15), 0 0 22px rgba(255,255,255,.32), 0 0 44px rgba(255,255,255,.12)`; hover `translateY(-2px) scale(1.02)` with a stronger glow.
- **Jewel pill:** `linear-gradient(123deg,#18011F 7%,#B600A8 37%,#7621B0 72%,#BE4C00 100%)` (near-black → magenta → violet → burnt orange), `0 4px 4px rgba(181,1,167,.25), inset 4px 4px 12px #7721B1`, `outline: 2px solid #fff; outline-offset: -3px`, uppercase, wide tracking.
- Icon nudge: arrow-up-right `translate(2px,-2px)`, chevron `+1px` x. Press `scale(.98)`.

**Implementation**
```css
.btn{position:relative;isolation:isolate;overflow:hidden;display:inline-flex;align-items:center;justify-content:center;gap:8px;
  height:42px;padding:0 18px;border-radius:6px;font:500 14px/1 Inter,system-ui,sans-serif;letter-spacing:-.02em;white-space:nowrap;
  cursor:pointer;text-decoration:none;
  transition:background .35s ease,border-color .35s ease,box-shadow .35s ease,color .35s ease,transform .2s ease}
.btn::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:linear-gradient(115deg,transparent 20%,rgba(255,255,255,.45) 48%,transparent 76%);
  transform:translateX(-130%);transition:transform .65s ease}
.btn:hover::after{transform:translateX(130%)}
.btn:active{transform:scale(.98)}
.btn--chrome{color:#111;border:1px solid #fff;background:linear-gradient(180deg,#fff 0%,#e7e7e7 48%,#cfcfcf 100%);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.95)}
.btn--chrome:hover{border-color:#f2f6ff;background:linear-gradient(180deg,#fff 0%,#f3f6ff 42%,#d5def2 100%);
  box-shadow:inset 0 1px 0 #fff,0 0 22px rgba(186,208,255,.35),0 8px 18px rgba(255,255,255,.12)}
.btn--ghost{color:#fff;border:1px solid rgba(198,198,198,.55);
  background:linear-gradient(135deg,rgba(255,255,255,.12),rgba(0,0,0,.5) 46%,rgba(150,170,200,.1));
  -webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);box-shadow:inset 0 1px 0 rgba(255,255,255,.12)}
.btn--ghost:hover{border-color:rgba(220,230,255,.8);box-shadow:inset 0 1px 0 rgba(255,255,255,.22),0 0 24px rgba(170,200,255,.28)}
.btn .icon{transition:transform .25s ease}
.btn:hover .icon{transform:translate(2px,-2px)}

.tab-metal{position:relative;overflow:hidden;display:inline-flex;align-items:center;height:40px;padding:0 18px;border-radius:7px;
  color:#f3f3f3;font-size:14px;letter-spacing:-.01em;border:1px solid rgba(198,198,198,.55);
  background:linear-gradient(105deg,#050505 0%,#2a2a2a 48%,#4a4a4a 100%);
  transition:background .35s ease,border-color .35s ease,box-shadow .35s ease}
.tab-metal::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.16) 50%,transparent 70%);
  transform:translateX(-120%);transition:transform .6s ease}
.tab-metal:hover{border-color:rgba(235,235,235,.9);background:linear-gradient(105deg,#111 0%,#3a3a3a 45%,#6a6a6a 100%);box-shadow:0 0 18px rgba(200,210,230,.18)}
.tab-metal:hover::before{transform:translateX(120%)}

.btn-halo{display:inline-flex;align-items:center;border-radius:999px;background:#fff;color:#000;font:600 14.5px/1 Inter,sans-serif;
  padding:13px 28px;border:0;cursor:pointer;
  box-shadow:0 0 0 1px rgba(255,255,255,.15),0 0 22px rgba(255,255,255,.32),0 0 44px rgba(255,255,255,.12);
  transition:transform .3s cubic-bezier(.22,1,.36,1),box-shadow .3s ease}
.btn-halo:hover{transform:translateY(-2px) scale(1.02);
  box-shadow:0 0 0 1px rgba(255,255,255,.25),0 0 30px rgba(255,255,255,.45),0 0 64px rgba(255,255,255,.18)}

.btn-jewel{display:inline-flex;align-items:center;border-radius:999px;border:0;color:#fff;cursor:pointer;
  padding:16px 48px;font:500 16px/1 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.1em;
  background:linear-gradient(123deg,#18011F 7%,#B600A8 37%,#7621B0 72%,#BE4C00 100%);
  box-shadow:0 4px 4px rgba(181,1,167,.25),inset 4px 4px 12px #7721B1;
  outline:2px solid #fff;outline-offset:-3px;transition:transform .2s ease,filter .2s ease}
.btn-jewel:hover{transform:translateY(-1px);filter:brightness(1.08)}
.btn-jewel:focus-visible{outline-width:3px}
@media (prefers-reduced-motion:reduce){.btn::after,.tab-metal::before{transition:none}}
```

---

## 4. Text-roll button with rotating arrow chip

**What / when:** The label is stacked twice in a 20 px-tall window; on hover the stack slides up so a fresh copy rolls in from below, while an arrow in a circular chip at the right edge rotates. Tiny, tactile, unmistakably "studio". Use it for primary and nav CTAs.

**Premium parameters**
- Window height = line-height = **20 px**; roll `translateY(-50%)` **500 ms** `--ease-standard`.
- Asymmetric padding `8px 8px 8px 20–24px` so the chip hugs the right edge; chip 24 px (nav) / 28–32 px (hero), white with the button colour as the arrow colour.
- Arrow `rotate(-45deg)` on hover (→ becomes ↗), same duration and easing.
- Colours: one accent (e.g. orange `#F26522`, hover `#e05a1a`) or near-black `#111` with a white chip. Cream-pill variant: black chip 36–40 px, hover gap `8 → 12px`, chip `scale(1.1)`.
- Text arrows (`→`) in links nudge `translateX(2px)` over 200 ms.

**Implementation**
```html
<a class="btn-roll" href="#">
  <span class="btn-roll__label"><span class="btn-roll__inner">
    <span>Start a project</span><span aria-hidden="true">Start a project</span>
  </span></span>
  <span class="btn-roll__chip" aria-hidden="true">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  </span>
</a>
```
```css
.btn-roll{display:inline-flex;align-items:center;gap:12px;padding:8px 8px 8px 24px;border-radius:999px;background:#F26522;color:#fff;
  font:500 14px/20px system-ui,-apple-system,sans-serif;text-decoration:none;transition:background-color .3s}
.btn-roll:hover{background:#e05a1a}
.btn-roll__label{display:block;height:20px;overflow:hidden}
.btn-roll__inner{display:flex;flex-direction:column;transition:transform .5s var(--ease-standard)}
.btn-roll__inner>span{display:block;height:20px;white-space:nowrap}
.btn-roll:hover .btn-roll__inner,.btn-roll:focus-visible .btn-roll__inner{transform:translateY(-50%)}
.btn-roll__chip{width:32px;height:32px;border-radius:999px;background:#fff;color:#F26522;display:grid;place-items:center;flex:none}
.btn-roll__chip svg{transition:transform .5s var(--ease-standard)}
.btn-roll:hover .btn-roll__chip svg,.btn-roll:focus-visible .btn-roll__chip svg{transform:rotate(-45deg)}
.btn-roll--dark{background:#111;font-size:13px;padding-left:20px}
.btn-roll--dark .btn-roll__chip{width:24px;height:24px;color:#111}
@media (prefers-reduced-motion:reduce){.btn-roll__inner,.btn-roll__chip svg{transition:none}}
```

---

## 5. Sliding-fill buttons (+ hard offset shadow)

**What / when:** On hover a colour panel wipes across the button from one side and the label inverts above it. Two flavours: a fast accent wipe on a dark pill, and a slow paper-white wipe on a near-black button with a playful icon tilt and a hard offset shadow (editorial / museum feel).

**Premium parameters**
- Accent wipe: `::after` `translateX(-100%) → 0`, **0.4 s** `--ease-out-quint`; paired buttons wipe from opposite sides. Pill `border-radius 50px`, `padding 12px 26px`, 15 px / 500.
- Paper wipe: panel `translateX(-101%) → 0`, **700 ms** `--ease-out-expo`; label colour flips; icon `scale(1.1) rotate(-12deg) translateY(-4px)`; the button lifts `translateY(-2px)` and gains `box-shadow: 3px 3px 0 rgba(17,17,17,.5)`; `:active` resets lift and shadow. A 1 px border in the dark colour keeps the edge crisp under the light panel.
- `isolation:isolate` + `z-index:-1` paints the panel above the button background and below the label, with no extra wrappers.

**Implementation**
```html
<a class="btn-fill" href="#"><span>Join now</span></a>
<a class="btn-fill btn-fill--from-right" href="#"><span>Start project</span></a>
<a class="btn-paper" href="#"><svg class="btn-paper__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17 17 7M8 7h9v9"/></svg><span>Explore now</span></a>
```
```css
.btn-fill{position:relative;display:inline-flex;align-items:center;gap:8px;overflow:hidden;isolation:isolate;
  border-radius:50px;padding:12px 26px;background:#000;color:#fff;font:500 15px/1 Inter,sans-serif;text-decoration:none}
.btn-fill::after{content:"";position:absolute;inset:0;z-index:-1;background:var(--fill,#A068FF);
  transform:translateX(-100%);transition:transform .4s var(--ease-out-quint)}
.btn-fill--from-right::after{transform:translateX(100%)}
.btn-fill:hover::after,.btn-fill:focus-visible::after{transform:translateX(0)}

.btn-paper{position:relative;display:inline-flex;align-items:center;gap:10px;overflow:hidden;isolation:isolate;
  padding:14px 24px;border:1px solid #1a1a1a;border-radius:6px;background:#1a1a1a;color:#fff;font:500 15px/1 Inter,sans-serif;
  text-decoration:none;box-shadow:0 1px 2px rgba(0,0,0,.05);
  transition:transform .3s var(--ease-out-expo),box-shadow .3s var(--ease-out-expo),color .7s var(--ease-out-expo)}
.btn-paper::before{content:"";position:absolute;inset:0;z-index:-1;background:#fcfcfc;transform:translateX(-101%);
  transition:transform .7s var(--ease-out-expo)}
.btn-paper:hover{color:#111;transform:translateY(-2px);box-shadow:3px 3px 0 rgba(17,17,17,.5)}
.btn-paper:hover::before{transform:translateX(0)}
.btn-paper:active{transform:none;box-shadow:none}
.btn-paper__icon{width:18px;height:18px;transition:transform .7s var(--ease-out-expo)}
.btn-paper:hover .btn-paper__icon{transform:scale(1.1) rotate(-12deg) translateY(-4px)}
@media (prefers-reduced-motion:reduce){.btn-fill::after,.btn-paper,.btn-paper::before,.btn-paper__icon{transition-duration:.01s}}
```

---

## 6. Animated gradient border ring (@property conic spin · hover ring)

**What / when:** A thin conic-gradient border that endlessly travels around a pill (draws the eye to the one CTA that matters), and a calmer variant where a gradient ring appears only on hover.

**Premium parameters**
- Spinning ring: `inset:-3px; padding:3px`, `conic-gradient(from var(--border-angle), accent, deep, accent, deep, accent)` (e.g. `#A068FF / #070319`), **3 s linear infinite** via a registered `@property`.
- Hover ring: `inset:-2px`, `linear-gradient(90deg, #89AACC, #4E85BF)` fading in over 0.3 s, background-position drifting over **6 s**; the inner surface keeps the page colour; the button scales 1.05 on hover.
- Logo variant: 36 px circle with a 2 px gradient ring, `scale(1.1)` on hover with the gradient direction reversed.
- `@property` works in Chrome/Edge 85+, Safari 16.4+, Firefox 128+; elsewhere the ring renders static, an acceptable fallback.

**Implementation**
```html
<span class="ring-spin"><a class="btn-fill" href="#"><span>Join now</span></a></span>
<a class="ring-hover" href="#"><span>See works</span></a>
```
```css
@property --border-angle{syntax:'<angle>';inherits:false;initial-value:0deg}
.ring-spin{position:relative;display:inline-block;border-radius:50px}
.ring-spin::before{content:"";position:absolute;inset:-3px;padding:3px;border-radius:inherit;pointer-events:none;
  background:conic-gradient(from var(--border-angle),#A068FF,#070319,#A068FF,#070319,#A068FF);
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask-composite:exclude;
  animation:border-spin 3s linear infinite}
@keyframes border-spin{to{--border-angle:360deg}}

.ring-hover{position:relative;display:inline-block;border-radius:999px;isolation:isolate;text-decoration:none;transition:transform .3s var(--ease-out-expo)}
.ring-hover::before{content:"";position:absolute;inset:-2px;border-radius:inherit;z-index:-1;opacity:0;
  background:linear-gradient(90deg,#89AACC,#4E85BF,#89AACC);background-size:200% 100%;
  transition:opacity .3s;animation:gradient-shift 6s ease infinite}
.ring-hover>span{display:block;border-radius:inherit;padding:14px 28px;background:#141414;color:#f5f5f5;font-size:14px}
.ring-hover:hover{transform:scale(1.05)}
.ring-hover:hover::before,.ring-hover:focus-visible::before{opacity:1}
@keyframes gradient-shift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
@media (prefers-reduced-motion:reduce){.ring-spin::before,.ring-hover::before{animation:none}}
```

---

## 7. Media card hover: icon-to-label pill, zoom, frosted veil

**What / when:** Case-study cards with muted autoplay video or images. On hover a small circular icon in the corner stretches into a labelled pill ("View case study"), the media zooms 5 %, and (bento variant) a frosted veil fades over the image with a centred label. Clean at rest, expressive on hover.

**Premium parameters**
- Pill: 36×36 circle → width **148–168 px**, `width .3s ease-in-out`; label fades in with a **100 ms** delay; icon `rotate(-45deg) → 0`. Light pill on dark media, dark (`#111`) on light media.
- Media: `aspect-ratio` per card (e.g. `329/246`, `1/1`), radius 16 px, a placeholder background close to the media's average colour; zoom `scale(1.05)` over 0.7 s expo.
- Below the card: description 13–14 px grey, title 14–15 px semibold, `margin-top 16px / 4px`.
- Bento variant: 12-column grid, spans **7/5/5/7**, cards radius 24 px with a 1 px stroke; a halftone overlay (technique 8) at 20 %; hover veil `rgba(10,10,10,.7)` + `blur(16px)`; white label pill with a gradient ring, "View — *Title*" (title in italic serif).

**Implementation**
```html
<a class="mcard" href="#">
  <div class="mcard__media" style="aspect-ratio:329/246;background:#1a1d2e">
    <video src="case.mp4" autoplay muted loop playsinline></video>
    <span class="mcard__pill"><span class="mcard__label">View case study</span>
      <svg class="mcard__icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </span>
  </div>
  <p class="mcard__desc">One-line outcome of the project.</p>
  <h3 class="mcard__title">Project name</h3>
</a>
```
```css
.mcard{display:block;color:inherit;text-decoration:none}
.mcard__media{position:relative;border-radius:16px;overflow:hidden}
.mcard__media video,.mcard__media img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .7s var(--ease-out-expo)}
.mcard:hover .mcard__media video,.mcard:hover .mcard__media img{transform:scale(1.05)}
.mcard__pill{position:absolute;left:16px;bottom:16px;height:36px;width:36px;border-radius:999px;background:#fff;color:#111;
  display:flex;align-items:center;justify-content:flex-end;overflow:hidden;white-space:nowrap;transition:width .3s ease-in-out}
.mcard:hover .mcard__pill,.mcard:focus-visible .mcard__pill{width:148px}
.mcard__label{position:absolute;left:16px;top:50%;translate:0 -50%;font:500 13px/1 Inter,sans-serif;opacity:0;transition:opacity .2s ease}
.mcard:hover .mcard__label,.mcard:focus-visible .mcard__label{opacity:1;transition-delay:.1s}
.mcard__icon{flex:none;width:36px;transform:rotate(-45deg);transition:transform .3s ease-in-out}
.mcard:hover .mcard__icon,.mcard:focus-visible .mcard__icon{transform:none}
.mcard__desc{margin:16px 0 0;font-size:14px;line-height:1.6;color:#4b5563}
.mcard__title{margin:4px 0 0;font-size:15px;font-weight:600;color:#111}
/* bento variant */
.bento{display:grid;grid-template-columns:repeat(12,1fr);gap:24px}
.bento>*:nth-child(4n+1),.bento>*:nth-child(4n+4){grid-column:span 7}
.bento>*:nth-child(4n+2),.bento>*:nth-child(4n+3){grid-column:span 5}
@media (max-width:767px){.bento>*{grid-column:1 / -1}}
.bcard{position:relative;border:1px solid #1f1f1f;border-radius:24px;overflow:hidden;background:#141414}
.bcard__veil{position:absolute;inset:0;display:grid;place-items:center;background:rgba(10,10,10,.7);
  -webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);opacity:0;transition:opacity .4s ease}
.bcard:hover .bcard__veil,.bcard:focus-within .bcard__veil{opacity:1}
@media (hover:none){.mcard__pill{width:148px}.mcard__label{opacity:1}}   /* touch: show the affordance */
```

**Perf:** many autoplaying card videos add up; pause off-screen ones with an IntersectionObserver.

---

## 8. Texture overlays: film grain, noise inside type, halftone, dot grid

**What / when:** A barely-there texture that kills the "flat digital" look of video, solid colour fields and gradients, and removes compression banding: a fixed page-wide grain, fractal noise blended over a hero video, an animated grain, noise *inside* glyphs for poster type, a halftone screen over project images, a faint dot grid behind tech heroes.

**Premium parameters**
- Page grain: `feTurbulence fractalNoise baseFrequency .9 numOctaves 4 stitchTiles stitch`, rect opacity `.08` inside the SVG × layer opacity `.4` (≈ 3 % effective), 200 px tile, fixed, `z-index` 50–100 above content, `pointer-events:none`. UI that must stay crisp (nav) may sit above it.
- Video grain: `baseFrequency .85 numOctaves 3`, `opacity .7`, `mix-blend-mode: overlay` (shows in mid-tones, vanishes on pure black/white, exactly where banding lives). Section noise: `.9 / 4 octaves`, `opacity .15`.
- Animated grain: oversized noise tile jittered with `steps(6)` over 1 s at ~`.08`. Shader-grade grain strength ≈ 0.05.
- Text noise (multiply): `baseFrequency .9, numOctaves 2`, alpha `.35`, composite `in` SourceGraphic. Watermark noise (overlay): `baseFrequency .5`, `feFuncA slope .075`.
- Halftone: `radial-gradient(circle, #000 1px, transparent 1px)` at **4×4 px**, `opacity .2`, `multiply`. Dot grid: `radial-gradient(#fff 1px, transparent 1px)` at **24×24 px**, `opacity .05`.

**Implementation**
```html
<div class="page-grain" aria-hidden="true"></div>
```
```css
:root{
  --noise-a:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  --noise-b:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
/* fixed page-wide grain */
.page-grain{position:fixed;inset:0;z-index:100;pointer-events:none;opacity:.4;background-size:200px 200px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.08'/%3E%3C/svg%3E")}
/* over a video, as the last child of a position:relative; overflow:hidden media box */
.noise-overlay{position:absolute;inset:0;pointer-events:none;opacity:.7;mix-blend-mode:overlay;background-image:var(--noise-a)}
.bg-noise{position:absolute;inset:0;pointer-events:none;opacity:.15;background-image:var(--noise-b)}
/* animated film grain (parent needs overflow:hidden) */
.grain-anim{position:absolute;inset:-50%;pointer-events:none;opacity:.08;mix-blend-mode:overlay;
  background-image:var(--noise-a);animation:grain 1s steps(6) infinite}
@keyframes grain{0%,100%{transform:translate(0,0)}20%{transform:translate(-5%,3%)}40%{transform:translate(4%,-6%)}
  60%{transform:translate(-3%,5%)}80%{transform:translate(6%,2%)}}
.halftone{position:absolute;inset:0;pointer-events:none;opacity:.2;mix-blend-mode:multiply;
  background-image:radial-gradient(circle,#000 1px,transparent 1px);background-size:4px 4px}
.dot-grid{position:absolute;inset:0;pointer-events:none;opacity:.05;
  background-image:radial-gradient(#fff 1px,transparent 1px);background-size:24px 24px}
@media (prefers-reduced-motion:reduce){.grain-anim{animation:none}}
```
Noise *inside* text (define once per page, then `filter:url(#text-grain)`):
```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <filter id="text-grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.35 0"/>
    <feComposite in2="SourceGraphic" operator="in" result="noise"/>
    <feBlend in="SourceGraphic" in2="noise" mode="multiply"/>
  </filter>
  <filter id="watermark-grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="2" stitchTiles="stitch"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.075"/></feComponentTransfer>
    <feComposite in2="SourceGraphic" operator="in" result="noise"/>
    <feBlend in="SourceGraphic" in2="noise" mode="overlay"/>
  </filter>
</svg>
<h2 style="filter:url(#text-grain)">Poster type</h2>
```

**Perf / mobile:** SVG filters on large text are expensive: use them on one or two elements and drop them ≤1024 px. Overlay grain is cheap (a static tile).
