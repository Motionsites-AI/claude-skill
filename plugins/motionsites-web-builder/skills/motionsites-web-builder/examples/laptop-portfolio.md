<!-- Laptop Portfolio · Portfolio · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261111_030305_aa366bc0-85e3-4f61-82c1-cbf8ae8217a3.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=laptop-portfolio -->

# Haldoren — "Laptop Dive" Portfolio Hero: Build Brief

Build a single-file (`index.html`, inline CSS and JS, no frameworks, no build step) one-screen portfolio hero for a fictional motion designer, **Haldoren**.

On load you see a photographic hero:
- a young man in a black leather jacket, white shirt and dark-red tie stands in a deep-green studio, holding a retro brick phone to his ear with his **right** hand and an open silver laptop in his **left**;
- a giant white "HALDOREN" wordmark sits *behind* him;
- a handwritten "motion-design" sits over the wordmark;
- a lanyard ID badge hangs from the top right.

When you scroll, a 5-second AI camera move (played in ~1.7 s) pushes into the laptop. The laptop floats out of his hand, turns square to camera and fills the view. Then the laptop screen plays a portfolio case video, framed by a punched paper ticket card, a short description and round prev/next buttons. Cases switch in place. "my studio" eases back out to the hero.

The page never scrolls. `html, body` are `height:100%; overflow:hidden`. Every interaction is captured (wheel, touch, keys, clicks).

---

## 1. Assets (use these exact URLs — do not download, re-host, crop or re-encode)

All images go through the images.higgs.ai wrapper:

```
HX(u) = 'https://images.higgs.ai/?default=1&output=webp&url=' + encodeURIComponent(u) + '&w=2048&q=85'
CF    = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/'
```

| Key | Raw result URL (wrap with HX unless noted) | What it is |
|---|---|---|
| `plate` | `CF + 'hf_20261111_001031_a09dc558-2c69-4e05-83a4-5f01ebdd1363.png'` | Hero photo, 3:2 (2048×1360): the man, the green studio, a black office chair and a white desk with mug and folders at the bottom-left. No text. |
| `casePlate` | `CF + 'hf_20261111_001031_4a7c3fd9-2168-4219-9736-096a17bbb0e2.png'` | Case photo, 3:2: the same silver laptop dead-centre and square to camera, black screen, on a green gradient (dark top `#1b4a34` → mint bottom). No person. |
| `cut` | `CF + 'hf_20261111_001143_ec356b1a-50a2-4b50-82fc-e346c914a406.png'` | Transparent PNG cutout of the man only, pixel-aligned with `plate`. |
| `badge` | `'https://images.higgs.ai/?default=1&output=webp&url=' + encodeURIComponent(CF + 'hf_20261111_001143_65c037e6-0768-4b12-9f17-17be132ce16b.png') + '&w=1200&q=85'` | Transparent PNG of a lanyard (white strap, silver swivel clip) holding an empty clear-plastic ID sleeve with a blank white card inside. |
| `trans` | `CF + 'hf_20261111_001144_2b054228-95af-41d5-922d-b02979fe485b.mp4'` (NOT wrapped) | Kling 3.0 clip, 1280×720, 24 fps, 5.04 s, no audio, single keyframe. First frame = hero (16:9 crop of `plate`), last frame = case (16:9 crop of `casePlate`). The camera pushes in, and the laptop floats out of his left hand, rotates and lands straight-on, filling the frame. |

Case screen videos (MotionSites previews, 16:9 mp4, on R2, `crossOrigin='anonymous'`, `muted loop playsInline`):

```
R2 = 'https://pub-86dc5b5484314368ac5436a674b0d919.r2.dev/aaaf/'
```

| # | Video | Ticket title | Ticket rows | Description key | Description text |
|---|---|---|---|---|---|
| 1 | `R2+'vell-lookbook.mp4'` | VELL LOOKBOOK | STUDIO VELL / E-COMMERCE / 2026 | `// vell lookbook` | `— a runway lookbook where every look steps forward on scroll and the cart follows along.` |
| 2 | `R2+'vasari-vhs-hero.mp4'` | VASARI SHELF | VASARI ARCHIVE / PORTFOLIO / 2026 | `// vasari shelf` | `— a director’s archive told as a shelf of tapes: pull one out and its story plays.` |
| 3 | `R2+'living-portrait-hero.mp4'` | MINA PORTRAIT | MINA 3D / PERSONAL SITE / 2025 | `// mina portrait` | `— a 3D creator’s homepage where the portrait follows your cursor and pulls faces.` |

The descriptions use a curly apostrophe (’) and start with an em dash and a space.

## 2. Fonts

Google Fonts, self-hosted as latin woff2 (the standalone file embeds them as base64 `data:font/woff2` URIs):

```
https://fonts.googleapis.com/css2?family=Inter+Tight:wght@100..900&family=Caveat+Brush&family=Anton&display=swap
```

| Family | Usage |
|---|---|
| **Inter Tight** (variable 100–900) | All UI and the wordmark (weight 900), nav tags (650), badge card (800/700/600), descriptions (700/500), buttons (600) |
| **Caveat Brush** 400 | The "motion-design" handwriting |
| **Anton** 400 | The ticket titles |

Use `font-display:swap` for all three. Body uses `-webkit-font-smoothing:antialiased`.

## 3. Colour tokens

```
--green-900:#0b2f20  (html/body bg)
--green-800:#11402c  (ticket punch holes, next-button arrow)
--green-700:#1a5a40
--mint:#cfeee0       (next-button hover)
--ink:#0d0f0e        (text on white)
```

Stage background on desktop: `linear-gradient(180deg,#0c3523 0%,#14503a 45%,#9fd8bf 100%)`.

## 4. The scene frame (core technique)

Everything photographic lives in one absolutely positioned `.frame`. It is **1440×810 units** (exactly the video's 16:9 frame), with `transform-origin:0 0`. It is placed with a single `transform: translate(x,y) scale(s)` computed in JS (§7). Inside it, in z-order:

| z | Element | Placement |
|---|---|---|
| auto | `img.plate` | `left:0; top:-73.125px; width:1440px; height:956.25px`. The 3:2 photo is taller than 16:9. Its 16:9 crop that matches the video starts 104 px down on the 2048×1360 source, which is 73.125 units at 1440 wide. |
| 3 | `svg.wm` | Wordmark (§5.1) |
| 4 | `img.cut` | Same box as plate (`top:-73.125px`, 1440×956.25), so the man sits on top of the wordmark |
| 5 | `.badge` | Lanyard (§5.3) |
| 6 | `.script` | "motion-design" (§5.2) |
| 6 | `video.trans` | `inset:0; 1440×810; object-fit:cover; opacity:0` |
| 7 | `img.caseplate` | `left:0; top:-105.47px; 1440×956.25; opacity:0`. Its 16:9 crop starts at y=150 of 2048×1360. |
| 8 | `.screen` | Laptop display: `left:272.8px; top:102.7px; width:894.4px; height:604.7px; border-radius:3px; background:#000; overflow:hidden; opacity:0` |
| 9 | `.screen-hit` | Same rect, `cursor:pointer`, `display:none` until case mode (click = next case) |

Inside `.screen`:
- the three case `<video>`s, `position:absolute; inset:0; 100%×100%; object-fit:contain` (the display is taller than 16:9, so previews letterbox with thin black bars and are never cropped), `background:#000; opacity:0`;
- a glass sheen `::after` with `linear-gradient(115deg, rgba(255,255,255,.07) 0%, rgba(255,255,255,0) 38%)`;
- a `.flash` white layer, opacity 0, z 2.

## 5. Hero elements

### 5.1 Wordmark "HALDOREN"

An inline SVG `viewBox="0 0 1440 260" preserveAspectRatio="none"`, positioned at `left:0; top:0; width:1440px; height:260px; overflow:visible`. Its single `<text x="14" y="214" textLength="1412" lengthAdjust="spacingAndGlyphs">HALDOREN</text>` uses Inter Tight 900, 268px, letter-spacing −6px.

The fill is a vertical linearGradient:

| Offset | Colour | Opacity |
|---|---|---|
| 0 | `#ffffff` | 1 |
| .5 | `#f1f5f3` | .9 |
| 1 | `#d7e6de` | .28 |

So the letters melt into the green at their feet. It sits *behind* the man cutout (z 3 vs 4), so his head overlaps the "D" and "O".

### 5.2 Handwriting "motion-design"

Caveat Brush 82px, `line-height:1`, white, letter-spacing −.5px, `transform:rotate(-8deg)`, `transform-origin:0 50%`, `text-shadow:0 2px 14px rgba(0,0,0,.18)`, z 6. It sits `top:148px` in frame units, on the **left**, across the bottom of "HAL" (left is set in §7 `fitHero`).

### 5.3 Lanyard badge

`.badge` is 582×1030 frame units, `transform-origin:288px 0` (it pivots at the strap top), default `left:986px; top:-165px`, `pointer-events:none`. It contains:

- `<img>` of the badge PNG, filling the box.
- `.card` over the blank card inside the sleeve. It is `left:172px; top:536px; 238×392`, `padding:20px 16px 0 16px`, colour `#141615`, Inter Tight:
  - `h4` "DESIGNER<br>CARD" — 30px / line-height .95 / weight 800 / letter-spacing −.5px.
  - `.yr` "2026" — absolute `right:16px; top:62px`, 11px/700.
  - `.role` "ART DIRECTOR // DESIGNER" — `margin-top:12px; padding-top:5px; border-top:1px solid #222`; 9.5px/700, letter-spacing .2px.
  - `.ph` photo, 92×112, `margin:12px auto`, radius 6, `background:#dfe4e1`. Its background-image is the **cutout** URL, with `background-size:471px 313px; background-position:-212px -16px` (a head-and-shoulders crop of the same man) and `box-shadow: inset 0 0 0 1px rgba(0,0,0,.06)`.
  - Four `.row`s. Each is flex, space-between, align flex-end, 9px/700, `padding:6px 0 3px`, `border-bottom:1.5px dotted #333`. The label is a `span`; the value is a `b` at weight 600:

    | Label | Value |
    |---|---|
    | NAME | E. HALDOREN |
    | FOCUS | MOTION DESIGN |
    | TG | @HALDOREN.MOTION |
    | EMAIL | HI@HALDOREN.STUDIO |
- `.hit`, the hover target over the card: `left:160px; top:470px; 262×440; pointer-events:auto; cursor:grab`.

## 6. Viewport-pinned UI (`.ui`, fixed, inset 0, z 20, pointer-events none)

`--n` is the viewport unit: `min(innerWidth/1440, innerHeight/900)` px on desktop, and `100vw/430` under 820px.

**Nav tags** (`.tag`) are white rectangles. They have:
- type: Inter Tight 650, `font-size: 16.5n`, `letter-spacing:-.02em`, colour `--ink`;
- box: `height: 37n`, `padding: 0 18n`, `white-space:nowrap`;
- shadow: `box-shadow: 0 3n 0 rgba(0,0,0,.18), 0 6n 14n rgba(0,0,0,.18)` — a hard 3n ledge plus a soft drop;
- hover: `translateY(-2n) rotate(-1.5deg)`, with the shadow growing to `0 5n 0 rgba(0,0,0,.22), 0 10n 18n rgba(0,0,0,.2)`. The transition is `.25s cubic-bezier(.2,.8,.2,1)`;
- active: `translateY(1n)` with the shadow `0 1n 0`.

They are positioned like this:

| Class | Text | Element | Position |
|---|---|---|---|
| `t1` | my studio | `<button>` | `left:30n; top:7n` |
| `t2` | portfolio | `<button>` | `left:233n; top:7n` |
| `t3` | contacts | `<a href="#contacts">`, default prevented | `right:244n; top:7n` |
| `t4` | discuss a project | `<a href="#discuss">`, default prevented | `right:32n; top:7n` |

**Centre logo** "HALDOREN" (a `<button>`): `left:50%; top:14n; translateX(-50%)`, weight 600, `19n`, letter-spacing .14em. It is `opacity:0` and fades in (`.4s`) only in case mode.

**Scroll hint** "scroll into the work", centred at `bottom:22n`:
- type: `12n`, letter-spacing .18em, uppercase, weight 600, opacity .85;
- before the text: a 1.5n × 22n line in `rgba(255,255,255,.35)`. Inside it a white 40%-tall bead drips top → bottom forever (`@keyframes drip{to{top:100%}}`, 1.6s `cubic-bezier(.6,0,.4,1)`);
- hidden with `visibility:hidden` in case mode and while busy.

### Case UI (desktop)

**Ticket** (top-right): `right:32n; top:98n; 348n × 182n`, white, radius 3n, `box-shadow:0 18n 40n rgba(0,0,0,.28)`, `padding:26n 34n 0 44n`, `transform-origin:50% 0`, starts at opacity 0. It contains:
- four punch holes, 21n circles in `--green-800` with `inset 0 2n 3n rgba(0,0,0,.35)`, 12n in from each corner;
- `h2` title in Anton 400, `50n`, line-height 1, letter-spacing −.01em, nowrap;
- `.rows`, `margin-top:8n`: three right-aligned lines, 700 / `12n` / letter-spacing .02em, `padding:4n 0 3n`, `border-bottom:1.5px dotted #2a2a2a`.

**Description** (left): `left:28n; top:326n; width:172n`:
- `.k` key line: 700 / `17n` / −.02em;
- `p`: `margin-top:14n`, `15n`, line-height 1.36, weight 500, `rgba(255,255,255,.92)`;
- `.num` "01 / 03": `margin-top:22n`, `12n`, letter-spacing .16em, 700, `rgba(255,255,255,.7)`.

Each child starts at opacity 0.

**Prev/next buttons** (`<button class="nav-case prev|next">`): at `bottom:150n`, prev at `left:95n`, next at `right:95n`. Each is a column with a 9n gap. They are opacity 0 and become visible in case mode with `.3s`. Each has:
- `.c`: a 50n circle with a `1.6px solid rgba(255,255,255,.9)` border, holding a 24n stroke-2 arrow SVG. Prev path: `M19 12H5M11 6l-6 6 6 6`. Next path: `M5 12h14M13 6l6 6-6 6`;
- a label "previous `<br>`case" or "next `<br>`case" (keep the space before `<br>`), 600 / `15n` / line-height 1.05, centred;
- next only: its circle is filled white with a `--green-800` arrow, and hover turns it `--mint`;
- hover on either: the circle scales to 1.08;
- prev gets `.dim` (opacity .45) on the first case.

## 7. Frame fitting (JS `pose(mode)`), called on load, on resize (glide removed) and on each transition

**Desktop (> 820px)**, with `cover = max(W/1440, H/810)` and `u = min(W/1440, H/900)`:
- **hero**: `s = cover`, `x = (W−1440s)/2`, `y = 0`. It covers the viewport and is top-anchored, so the wordmark is never cut.
- **case**: the whole laptop (frame y 79 → 762) must fit between the nav and the bottom.
  - Set `top = 66u` and `fit = (H − top − 28u)/(762−79)`.
  - If `fit ≥ cover`: `s = cover`, `y = min(0, max(H−810s, top−79s))`.
  - Otherwise: `s = fit`, `y = top − 79·fit`.
  - In both cases `x = (W−1440s)/2`.

**`fitHero(p)`** (desktop hero only) keeps hero UI inside the visible part of the frame:
- `vl = max(0, −x/s)`, `vr = min(1440, (W−x)/s)`, `pad = 18/s`.
- Wordmark: `left = vl + .6·pad`, `width = vr − vl − 1.2·pad`. The SVG stretches because preserveAspectRatio is none.
- Badge: `left = min(986, vr − pad − 417)`.
- Badge top: `vb = min(810, (H−y)/s)`, then `top = min(−165, vb − 56/s − 935)`. The whole card stays visible with ~56 px clear below it, and the strap simply runs further off the top on short screens.
- Script: `left = vl + pad + 70` (left side, over "HAL").

**Phone/tablet (≤ 820px)**:
- **hero**: `s = min(W/650, 0.62H/810)`, `x = W/2 − 805s`, `y = H − 790s`. The man is centred and bottom-anchored.
- **case**: the laptop sits at the **bottom** and the UI at the top.
  - `navH = 0.022H + 42 + 22`.
  - `uiBottom = 62 + ticketHeight + 18 + max(60, descHeight) + 14`.
  - `s = min((W−28)/905, max(0.2, (H − navH − uiBottom)/(762−95)))`, `x = W/2 − 720s`, `y = H − navH − 762s`.
  - The camera glides *down* slightly into the laptop and never jumps up.

`place(m)`:
- sets the transform;
- toggles the `m-case` class on both `.frame` and `.stage`;
- on mobile, writes `--mbs = mbadgeWidth/582` and `--th = ticketHeight` to `:root`.

`.frame.glide` adds `transition: transform var(--glide) cubic-bezier(.65,0,.35,1)`.

### Edge fades: one mask, animated with registered custom properties

Register `@property` for `--mt`, `--m0`, `--mb` and `--ms` as `<length>`, `inherits:true`.

Each layer gets its overhang beyond the 810 frame, so every layer fades at the same frame line:
- `plate`: `--o:73.125px; --ob:73.125px`;
- `caseplate`: `--o:105.47px; --ob:40.78px`;
- `trans`: 0 for both.

Apply to `.plate`, `.trans` and `.caseplate` (never to `.cut`, which keeps his head crisp):

```
mask-image:
  linear-gradient(180deg,
    transparent calc(var(--o,0px) + var(--m0)),
    rgba(0,0,0,.35) calc(var(--o,0px) + var(--m0) + var(--mt)*.37),
    #000 calc(var(--o,0px) + var(--m0) + var(--mt)),
    #000 calc(100% - var(--ob,0px) - var(--mb)),
    transparent calc(100% - var(--ob,0px))),
  linear-gradient(90deg, transparent 0, #000 var(--ms), #000 calc(100% - var(--ms)), transparent 100%);
mask-composite: intersect;   (-webkit-mask-composite: source-in)
```

The frame gets one class: `d-fade` on desktop or `m-fade` on mobile. The values are:

| State | `--m0` | `--mt` | `--mb` | `--ms` |
|---|---|---|---|---|
| Desktop hero | 0 | 0 | 0 | 0 (no fade) |
| Desktop case (`.d-fade.m-case`) | 0 | 110px | 60px | 170px |
| Mobile hero | 0 | 190px | 0 | 140px |
| Mobile case (`.m-fade.m-case`) | 48px | 40px | 70px | 140px |

Desktop case fades only become visible when the laptop has to shrink.

The variables transition over the same `var(--glide)` and easing as the transform, so the fades move with the camera and never pop.

Mobile stage:
- solid `#0b3b2a` (sampled from the top row of the hero photo);
- a `::before` layer with `linear-gradient(180deg,#1b4a34 0%,#1b4a34 55%,#2f6a50 80%,#7fb79d 100%)` (case colours) cross-fades in over 1.6s when `.stage.m-case` is set, which happens at the *start* of the dive.

## 8. Entrance (once; Web Animations; guard + failsafe)

Add `js` to `<html>` first. `.js .pre{opacity:0}` hides the nav tags, wordmark, script, badge and hint.

The entrance starts in a rAF when `document.fonts.ready` **and** the plate's load/error have both resolved, capped by a 2.5 s race, with an extra 4 s `setTimeout` failsafe. A `data-in` flag guards it so it runs once. Every animation uses `fill:'both'` and default easing `cubic-bezier(.2,.8,.2,1)`:

| Element | Keyframes | Duration | Delay | Easing |
|---|---|---|---|---|
| 4 nav tags | `opacity 0, translateY(-40px) rotate(-4deg)` → none | 700 | 120 + i·80 | `cubic-bezier(.3,1.5,.5,1)` (springy overshoot) |
| Wordmark | `opacity 0, translateY(60px), clip-path inset(100% 0 0 0)` → `inset(0)` (rises out of its own baseline) | 1100 | 260 | default |
| Script | `opacity 0, clip-path inset(0 100% 0 0)` → `inset(0)` (writes on left → right) | 900 | 1050 | `cubic-bezier(.5,0,.3,1)` |
| Badge | `0%: opacity 0, translateY(-120%) rotate(8deg)` → `60%: translateY(0) rotate(-3deg)` → `80%: rotate(1.6deg)` → `rotate(0)` (drops in on its strap and settles) | 1500 | 700 | default |
| Hint | opacity 0 → .85 | 600 | 1800 | default |

When the badge's drop finishes, an **idle sway** starts: `rotate(-1.1deg) ↔ rotate(1.1deg)`, 3200 ms, infinite, alternate, ease-in-out.

**Hover swing**: on `pointerenter` of `.hit` (hero mode only), run `rotate(0) → -6deg → 4deg → -2deg → 0` over 1400 ms, ease-out, with `composite:'add'`, so it layers on top of the sway.

## 9. Hero → laptop dive (`toCase`)

Triggers:
- wheel down (|deltaY| ≥ 18, 900 ms lock, `preventDefault` with `passive:false`);
- touch swipe up (≥ 40 px);
- `ArrowDown`, `PageDown` or `Space`;
- clicking "portfolio".

A `busy` flag blocks re-entry, and `body.busy` hides the hint.

1. **heroOut** (380 ms, `cubic-bezier(.5,0,.75,0)`, fill forwards):
   - the wordmark lifts to `translateY(-40px)` and fades;
   - the script fades;
   - the badge cancels its sway and flies up to `translateY(-110%) rotate(-6deg)` while fading.

   Wait 330 ms.
2. If reduced motion is on, or the clip isn't ready: `place('case')`, fade the caseplate in over 500 ms, and go to arrive.
3. Otherwise:
   - `trans.currentTime = 0; trans.style.opacity = 1`;
   - after two rAFs, hide the plate (`visibility:hidden`) so it can never ghost through faded edges;
   - fade the cutout 1 → 0 over 260 ms ease-out (a soft hand-off to the video, no pop);
   - set `--glide:1.6s`, add `.glide`, then `place('case')`, so the camera, the masks and the background all glide together.
4. Play the clip. The **eased speed curve** runs every rAF:

   ```
   p = currentTime / duration
   playbackRate = max(1.2, 1.8 + 2.4 · sin(π · min(p·1.08, 1)))
   ```

   It is slow at the start, peaks near 4.2× mid-move and eases into the landing, so the 5.04 s clip plays in **≈1.72 s**. Stop when `ended` or `p ≥ .995`.
5. Pause the clip, set the caseplate to opacity 1 (cancelling its animations), and hide the clip. The last frame and the caseplate are the same image, so the swap is invisible.

The transition clip is fetched whole into a Blob at load (`fetch → blob → URL.createObjectURL`), because Kling clips have one keyframe and streaming seeks stall. Set `transReady` on `loadeddata`; on a fetch error, fall back to the direct URL.

## 10. Arrive in case mode (`arriveCase`)

- Set mode `case` and add `body.is-case`:
  - the logo fades in;
  - the hint is hidden;
  - the nav-case buttons appear;
  - `.screen-hit` is enabled;
  - on mobile, the `t3`/`t4` tags get `visibility:hidden`.
- Keep the plate hidden and the cutout at opacity 0.
- Set `.screen` opacity to 1 and play a **flash** on it: opacity 0 → .55 → 0, 600 ms, ease-out.
- Video 1: `opacity 0, scale(1.06)` → `1, scale(1)`, 700 ms.
- `playOnly(0)` pauses every other video, rewinds and plays this one. **Only one screen video ever plays.**
- Call `caseIn(0, first)`:
  - ticket: `opacity 0, translateY(-60px) rotate(-6deg)` → (70%) `translateY(6px) rotate(1.2deg)` → none, 800 ms, delay 150. It drops in and settles like a hung tag;
  - description children: `opacity 0, translateY(14px)` → none, 600 ms, delay `250 + k·70`.
- Preload video 2. After 700 ms, release `busy` and remove `.glide`.

`fillCase(i)` writes the ticket title, the three rows, the key, the text and `NN / 03`, and toggles `.dim` on prev for `i === 0`.

## 11. Switching cases

- Next: wheel down, swipe up or left, `ArrowDown`, `PageDown`, `Space`, `ArrowRight`, the next button, or a click on the screen.
- Prev: wheel up, swipe down or right, `ArrowUp`, `PageUp`, `ArrowLeft`, or the prev button.
- Prev on case 1 calls `toHero()`. Next on case 3 wraps to case 1.

`swapTo(n)` runs these in order:
1. In parallel:
   - **caseOut**: the ticket goes to `opacity 0, translateY(-40px) rotate(4deg)` over 380 ms with `cubic-bezier(.5,0,.75,0)`; the description children go to `translateY(-10px)` and fade over 300 ms with stagger 40;
   - the old video fades over 350 ms.
2. Pause the old video.
3. Flash 0 → .35 → 0 over 420 ms.
4. The new video goes `opacity 0, scale(1.04)` → `1, scale(1)` over 500 ms.
5. `playOnly(n)`, `caseIn(n, false)` (ticket with no delay, description delay `80 + k·70`), and preload the next video.
6. Release `busy` after 520 ms.

## 12. Back to the hero (`toHero`)

Triggers: "my studio", the centre logo, or prev on case 1.

1. Run `caseOut`, pause all videos, and fade `.screen` out over 300 ms.
2. Remove `is-case`. Set `--glide:.9s` and `.glide`, then `place('hero')`.
3. Unhide the plate. Fade the cutout 0 → 1 over 700 ms, delay 150.
4. The caseplate goes `opacity 1, blur(0)` → `opacity 0, blur(12px)` over 800 ms with `cubic-bezier(.65,0,.35,1)`. At the same time the plate goes `scale(1.12) blur(8px)` → `scale(1) blur(0)` over 900 ms with `cubic-bezier(.2,.8,.2,1)`. Together they make a blurred zoom-out reveal.
5. After 250 ms, run **heroIn** (700 ms, fill forwards):
   - the wordmark rises from `translateY(40px)`;
   - the script writes on again (clip-path, delay 250);
   - the badge drops back in (`translateY(-110%) rotate(6deg)` → (70%) `translateY(0) rotate(-2deg)` → `rotate(0)`, 1100 ms), then the sway restarts.
6. Release `busy` after 1000 ms.

## 13. Small screens (≤ 820px)

- **Hidden from the frame**: the frame's wordmark, script and badge. Copies live in the fixed UI layer (`.m-only`).
- **Nav**: "my studio" top-left and "portfolio" top-right at 12px; "contacts" and "discuss a project" on a second row at `12px + 44n`. The tags are 13px, 30px tall, with 0 12px padding.
- **Mobile wordmark**: an SVG `viewBox 0 0 1440 240`, `text x=10 y=210 textLength=1420`, with the same gradient (bottom opacity .3). It sits at `left:3vw; width:94vw; top: 12px + 96n`.
- **Mobile script**: `right:6vw; top: 12px + 96n + 14vw`, 15vw, rotate −7deg, `text-shadow 0 2px 10px rgba(0,0,0,.2)`.
- **Mobile badge**: a `cloneNode` of the frame badge inside `.m-badge`. The box is `right:2vw; top: 12px + 96n + 9vw; width:27vw; height: 27vw·1030/582`, z −1. The inner badge stays 582×1030 internally with `scale: var(--mbs)` and `translate: calc(-288px + 13.5vw) 0`.
- **The man** is centred and bottom-anchored. The photo fades into the solid `#0b3b2a` from the top over 190 frame units, but the crisp cutout stays on top, so his hair is never faded.
- **Case mode**:
  - the logo is hidden;
  - the ticket is centred at `top:62px`, `width:min(86vw,360px)`, `padding 22px 26px 16px 36px`, with a 38px title, 11px rows and 15px holes;
  - the description is centred under the ticket at `top: 62px + var(--th) + 18px`, with a 15px key, 13.5px text and the counter hidden;
  - the laptop sits at the bottom;
  - the prev/next buttons form a row along the bottom (`bottom: safe-area + 2.2vh`): 42px circles, 20px arrows, single-line 12.5px labels (`<br>` hidden), prev at `left:6vw`, next at `right:6vw` mirrored.
- **Hint**: `bottom:18px`, 11px.

## 14. Reduced motion

`@media (prefers-reduced-motion:reduce)` sets `animation:none!important; transition:none!important` on everything. In JS (`RM`):
- the entrance just reveals everything;
- the sway and swings are skipped;
- the dive skips the clip and swaps the plates instantly;
- all other durations are multiplied by 0.

## 15. Copy and brand notes

All names are fictional: Haldoren, Vell, Vasari, Mina. The page carries no real logos (the laptop has no brand mark) and no real people.

Every string, exactly:
- **Nav and UI**: "my studio", "portfolio", "contacts", "discuss a project", "HALDOREN", "scroll into the work".
- **Hero**: "motion-design".
- **Badge card**: "DESIGNER CARD", "2026", "ART DIRECTOR // DESIGNER", "NAME", "E. HALDOREN", "FOCUS", "MOTION DESIGN", "TG", "@HALDOREN.MOTION", "EMAIL", "HI@HALDOREN.STUDIO".
- **Case buttons**: "previous case", "next case".
- **Cases**: the ticket and description strings from the table in §1.

Title: `Haldoren — Motion Design Portfolio`.
