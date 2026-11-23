<!-- Shelf Hero · Portfolio · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261029_012401_8f947ed0-7b82-47d6-bdcd-b1ce1af0bf5f.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=vasari-vhs-hero -->

# Prompt: Leon Vasari, VHS filmography shelf hero

## What it is

Build a single-screen **filmography hero** for a fictional film director, Leon Vasari. Use plain HTML, CSS and vanilla JavaScript in one file, with no framework, no build step and no libraries.

The page is a warm off-white sheet of paper. Across its middle runs a long, endless shelf of worn VHS tape boxes standing side by side, spine out. One tape, the active film, is pulled out of the shelf and **physically turned in 3D** so its illustrated front cover faces you. It is tilted a few degrees, lifted slightly and pushed towards the viewer.

- **Changing film:** click any spine, the arrows, a decade tab, scroll, drag or use the keyboard. The shelf slides, the open tape turns back into a spine, and the new one turns out to show its cover.
- **Caption:** the film's title, romanised Japanese title, kanji title and year sit under the shelf and slide up through a mask whenever the film changes.
- **Cursor:** a large custom ring cursor follows the mouse. It shrinks over spines and becomes a filled cobalt "OPEN / 開く" disc over the active cover.
- **Opening a film:** click the cover, the play ring or press Enter. A sheet of paper grows out of the cover, rotating from the cover's tilt to straight, until it fills the screen. It becomes a detail page whose poster bleeds in like ink blots spreading on paper, while each line of text rises out of its own mask.

Everything is driven by one `requestAnimationFrame` loop plus the Web Animations API, with no CSS keyframes. There is no opacity fade anywhere; every reveal is a mask slide, a clip or a scale.

## Media: every asset URL

All 24 images come from **four Higgsfield GPT Image 2.5 generation sheets** with transparent backgrounds. Each sheet is loaded through the Higgsfield image proxy as WebP, and the alpha is kept. The art is fictional, unbranded VHS art, with no real studios or logos.

Never use separate image files. Each spine and cover is a **rectangle cut out of one of these sheets** with CSS background cropping, using the exact pixel boxes below.

### Sheets

| Sheet id | Size (px) | Contents | URL |
|---|---|---|---|
| covers | 1744 × 2336 | all 12 covers in a 4 × 3 grid | https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261029_010644_837e04ca-2418-45c1-b8e0-0233265c4cd5.png&w=1744&q=85 |
| spines | 2688 × 1152 | 12 spines in one row (9 are used: all except river, observer and storm) | https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261029_010738_a3e47ead-18f2-4974-9468-06d16a25edc5.png&w=2688&q=85 |
| fix | 1520 × 2688 | re-drawn spines; the first one, RIVER OF SALT, is used | https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261029_010831_3ebb874b-93dc-433e-87ed-6299aba720f0.png&w=1520&q=85 |
| fix2 | 1520 × 2688 | re-drawn spines THE OBSERVER and LIGHT IN THE STORM | https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261029_092020_f96bc094-db7b-46de-9298-074a24e0a3b8.png&w=1520&q=85 |

### Crop boxes

The boxes are in sheet pixels, as `x, y, w, h`.

- **Spines:** a tall, narrow worn cardboard box side, about 1:6. It has a small illustration at the top, the title running vertically in a condensed serif, then "VASARI" and a boxed "VHS" badge at the bottom.
- **Covers:** about 1:1.95. Each is the front of the same box: "A LEON VASARI FILM" at the top, a big condensed serif title, a duotone screen-print illustration in ink black, cobalt, vermilion and cream, and a "VHS" badge bottom right.

| Film id | Spine sheet | Spine box | Cover sheet | Cover box |
|---|---|---|---|---|
| valley | spines | 266, 31, 189, 1089 | covers | 497, 72, 344, 659 |
| bluehour | spines | 492, 31, 189, 1089 | covers | 914, 72, 342, 659 |
| river | fix | 197, 54, 324, 2566 | covers | 1332, 72, 344, 659 |
| summer | spines | 937, 31, 188, 1089 | covers | 74, 813, 344, 676 |
| green | spines | 1157, 31, 185, 1090 | covers | 497, 815, 344, 674 |
| noon | spines | 44, 32, 184, 1088 | covers | 74, 72, 347, 659 |
| observer | fix2 | 371, 15, 349, 2655 | covers | 915, 815, 342, 675 |
| birds | spines | 1573, 31, 183, 1089 | covers | 1331, 815, 345, 675 |
| storm | fix2 | 808, 15, 347, 2656 | covers | 74, 1571, 345, 681 |
| tide | spines | 2012, 31, 188, 1089 | covers | 496, 1577, 343, 678 |
| war | spines | 2236, 31, 189, 1089 | covers | 913, 1579, 343, 676 |
| door | spines | 2462, 31, 188, 1089 | covers | 1331, 1579, 344, 677 |

### How the images are used

Put the two tables into JS as `SHEET[id] = [url, W, H]` and `CROP['spine-<id>' | 'cover-<id>'] = [sheet, x, y, w, h]`.

- **Spines and covers** are drawn as a cropped background on the box faces. For a box `x, y, w, h` on a sheet of size `W × H`, set:
  - `background-image: url(sheet)`
  - `background-size: (W/w·100)% (H/h·100)%`
  - `background-position: (x/(W−w)·100)% (y/(H−h)·100)%`

  The crop is stretched to fill the face exactly, so the spine is exactly `--ws` wide and the cover exactly `--d` wide.
- **The detail poster** is an SVG `<image>` of the cover's sheet, inside a `<g clip-path>` with a 474 × 900 rect, so the ink mask can still be applied.
  - Set the image's `href` to the sheet URL, with `x = −x·474/w`, `y = −y·900/h`, `width = W·474/w` and `height = H·900/h` (`preserveAspectRatio="none"`).
  - Only the cover's box then shows, stretched to 474 × 900.
- **Preloading:** preload the four sheet URLs as `Image()` objects on start, so the first turn never shows an empty face.

## Fonts

Self-host all five. The single-file version embeds them as base64 WOFF2 data URLs.

| Family | Weight / style | Use | Source |
|---|---|---|---|
| Newsreader (variable, optical size 6–72) | 400 regular, plus 400 italic | Caption title, detail title, synopsis, italic credit line | https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400 and `ital,opsz,wght@1,6..72,400` (Latin subset) |
| Inter Tight (variable) | 500 and 600 | Every small uppercase label, tab, button, year, meta line | https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600 (Latin subset) |
| Noto Sans JP | 500 | Every Japanese character in labels and titles; second in the sans stack | https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500&text=… subset to exactly the kana and kanji used on the page (about 14 KB) |
| Noto Serif SC | 700 | The logo characters 莱昂·瓦萨里 only | https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@700&text=莱昂·瓦萨里 (about 2 KB) |

- **Sans stack:** `"Inter Tight", "Noto Sans JP", system-ui, sans-serif`.
- **Serif stack:** `"Newsreader", Georgia, serif`.
- **Japanese subset:** the subset string must contain every kana and kanji in the film data and UI. That is 戻る, すべて, 閉じる, 開く, 監督作品, 映画を見る, 年, 〜, the twelve kanji titles, and the right single quote. Romanised titles are written without macrons (SHOGO, SENSO), so the Latin subset is enough.

## Palette and tokens

| Token | Value | Used for |
|---|---|---|
| `--paper` | `#EDEBE6` | Page background |
| `--sheet` | `#F4F2ED` | Detail sheet background (slightly lighter paper) |
| `--ink` | `#141414` | All text, borders, cursor ring |
| `--muted` | `#6D6A63` | Detail meta line and italic credit |
| `--cobalt` | `#1F3FB0` | Logo, tab indicator, subtitles, play ring, OPEN cursor, Watch button |
| `--rule` | `rgba(20,20,20,.9)` | 1px borders of every boxed label |
| `--ease` | `cubic-bezier(.2,.8,.2,1)` | Every CSS transition and text slide |
| `--H` | `min(46vh, 31vw)` on desktop, `min(60vw, 40svh)` on mobile | Height of every tape; all geometry scales from it |

### Paper grain

A fixed, full-screen layer (`z-index 40`, `pointer-events none`) sits above the shelf and caption, under the detail sheet.
- **Pattern:** a 220 × 220 inline SVG tile, made from `feTurbulence` fractalNoise (baseFrequency `.85`, 3 octaves, stitchTiles) through an `feColorMatrix` that maps it to warm grey `rgb(.45,.42,.38)` at alpha `.22`.
- **Blend:** `mix-blend-mode: multiply` at `opacity .55`. The whole page reads as printed paper and the tapes pick up the grain too.

### Global behaviour
- `body` hides overflow and uses `user-select: none` and antialiased smoothing.
- On fine pointers (`@media (pointer:fine)`) the native cursor is hidden on html, body, buttons and links.

## Label system

- **`.lbl`:** Inter Tight 600, 10.5px, line height 1, letter-spacing `.09em`, uppercase.
- **`.box`:** inline-flex, 21px tall, 0 8px padding, 1px `--rule` border. It looks like the small boxed tags in printed film catalogues.

## Layout, top to bottom (desktop)

Everything is `position: fixed` and positioned from the centre of the viewport using `--H`, so the composition is identical at any desktop size.

### 1. Top bar

- **Bar:** 84px tall, 32px side padding, a 3-column grid `1fr auto 1fr`, items centred vertically.
- **Left:** a boxed label link "BACK / 戻る", aligned to the start, ink colour, no underline.
- **Centre, the logo:** a two-line stack centred with a 5px gap, all cobalt.
  - Line 1: "莱昂·瓦萨里" in Noto Serif SC 700, 22px, letter-spacing `.04em`.
  - Line 2: "LEON VASARI" in Inter Tight 600, 9px, letter-spacing `.34em`, with matching left padding so it is optically centred.
- **Right:** "CAREER 1958年〜1989年" as a `.lbl`, aligned to the end.

### 2. Decade tabs

- **Position:** centred horizontally, top at `50% − H/2 − 86px`, so they float just above the shelf.
- **Buttons:** five boxed `.lbl` buttons in a row, each 23px tall with 0 11px padding and a 1px border. `margin-left: −1px` makes neighbours share one border. Labels: "ALL / すべて" (written "All / すべて" and uppercased by the label style), "1950s", "1960s", "1970s", "1980s". Labels never wrap.
- **Indicator:** a cobalt block, absolutely positioned behind the buttons. It is the full 23px tall, and its `width` and `transform: translateX()` are set to the active tab's `offsetWidth` and `offsetLeft`. Both transition over `.6s var(--ease)`, so the cobalt block slides and stretches from decade to decade.
- **Active tab:** its text turns white via a `.45s` colour transition.
- **Which tab is active:** always the decade of the active film. For example, Noon in Ashes (1971) highlights "1970s". "ALL" is never highlighted.

### 3. The shelf (3D stage)

- **Section:** full width; top at `50% − H/2 − 40px`; height `H + 80px`.
- **Perspective:** `perspective: 2200px`, `perspective-origin: 50% 50%`, `touch-action: pan-y`.
- **Stage:** a zero-size `.stage` at `left 50%; top 50%` with `transform-style: preserve-3d`, holding every tape.
- **Tape element:** `.tape` is a zero-size box at the stage origin, with `transform-style: preserve-3d`, `will-change: transform` and two faces.

**Box dimensions**, measured from the real `--H` at load and on resize. Measure it by inserting an off-screen probe element with `height: var(--H)` and reading its height.

| Name | Value | Meaning |
|---|---|---|
| H | resolved `--H` in px | Tape height |
| ws | `H × 142 / 840` (≈ 0.169 H) | Spine width (front face) |
| d | `H × 474 / 900` (≈ 0.527 H) | Cover width = box depth |
| gap | `H × 0.03` | Gap between spines |

`ws` and `d` are written onto the stage as the CSS variables `--ws` and `--d`.

**Faces.** Each face is absolutely positioned, `H` tall, top at `−H/2`, with `backface-visibility: hidden` and a 2px radius.
- **Spine face `.sp`:** width `--ws`, left `−ws/2`, `transform: translateZ(d/2)`. This is the front of the cuboid.
- **Cover face `.cv`:** width `--d`, left `−d/2`, `transform: rotateY(90deg) translateZ(ws/2)`. This is the right-hand side of the cuboid. It also has `box-shadow: 0 30px 60px −28px rgba(20,16,10,.55)` so the pulled-out tape casts a soft shadow on the paper.
- **Shading:** each face has an `::after` overlay of solid black whose opacity comes from a `--shade` variable. As the box turns, the spine darkens to 55 % and the cover brightens from 50 % dark to fully lit. It reads as light falling across a turning object.

**Endless shelf.**
- **Copies:** render the 12 films **three times**, 36 tapes with virtual index `v = copy × 12 + i`. Wrapping then always happens far off-screen.
- **Relative position:** each tape's position comes from its relative index `r` to the current scroll value `s`. Take `(v − s)` modulo 36 into the range −18 … +18.
- **Culling:** tapes whose computed x is more than `W/2 + 1.5 d` from centre get `visibility: hidden` and are skipped.

**Horizontal placement.**
- **Formula:** the centre of a tape at relative index `r` sits at `x = F(r) = r·(ws + gap) + (d − ws + 1.6·gap)·B(r)`.
- **The smooth step `B(r)`:** for `|r| < 1` it is `(r + sin(πr)/π) / 2`, otherwise `±0.5`.
- **Effect:** spines step by spine width plus gap, and the open cover pushes neighbours apart by exactly half its extra width on each side. Because `B` is continuous, a fractional `s` slides everything smoothly with no jumps.

**Turning a tape.**

| Quantity | Formula |
|---|---|
| Openness `o` | `smoothstep(max(0, 1 − |r|))`, where smoothstep(x) = x²(3 − 2x). 1 for the active tape, 0 for spines; in between while the shelf moves, so tapes the shelf passes half-open and close |
| rotateY | `−90°·o + tiltY·o` (the box turns left until its right side, the cover, faces front) |
| rotateX | `tiltX·o` |
| rotateZ | `−4.5°·o` (the pulled-out cover leans slightly anticlockwise, like the reference) |
| translateZ | `o · 0.2 H` (pulled towards the viewer, so it looks bigger than the spines) |
| translateY | `−o · 0.025 H − lift · 0.045 H` (raised slightly; hovered spines rise more) |
| Transform order | `translate3d(x, y, z) rotateZ() rotateX() rotateY()` |
| z-index | `round(100 − |r|·4)`, so nearer tapes stack on top |
| `--shade` | Spine face: `o × .55`. Cover face: `(1 − o) × .5` |

**Hover lift.**
- **When it lifts:** hovering any tape that is not the active one (`|r| > .5`) sets that tape's lift target to 1. It eases towards the target at `1 − e^(−12·dt)` per frame, so the spine rises by 4.5 % of H, like a finger pulling it halfway out.
- **Tracking:** hover is tracked with `pointerenter` / `pointerleave` on each tape.

**Tilt towards the cursor.**
- **When the cursor is "on the cover":** within `0.55 d` horizontally of screen centre, within `0.55 H` vertically of the shelf centre, not in the detail view, and the shelf almost settled (`|T − s| < .3`).
- **On the cover:** `tiltY` targets `(mx − W/2) / (0.55 d) × 9°` and `tiltX` targets `−(my − cy) / (H/2) × 6°`.
- **Elsewhere:** `tiltY` drifts to `(mx − W/2)/W × 5°` and `tiltX` to 0.
- **Smoothing:** both ease at `1 − e^(−7·dt)`. The open cover leans gently towards the mouse like a card held in the hand.

### 4. Play ring

- **Shape:** a fixed 42px circle with a 1px cobalt border, cobalt colour, `rgba(237,235,230,.75)` fill, and a 12px solid play triangle nudged 2px right.
- **Position:** centred on the active cover's lower-left corner, at `left = W/2 − 0.5 d − 6px` and `top = shelf centre + 0.36 H`.
- **Scale:** `smoothstep(max(0, 1 − |T − s|·3))`. It pops in once the shelf settles and shrinks to 0 while the shelf moves or the detail is open.
- **Action:** clicking it opens the detail.

### 5. Caption

- **Position:** a centred stack, top at `50% + H/2 + 30px`, 9px gap, `pointer-events none`.
- **Masked lines:** each line is an `overflow: hidden` mask, `width: min(92vw, 760px)`, centred text.
  - **Title:** Newsreader 400, 31px, line height 1.12, letter-spacing −.01em (e.g. "Noon in Ashes").
  - **Subtitle:** a `.lbl` in cobalt at weight 500: romaji, " / ", kanji (e.g. "HAI NO SHOGO / 灰の正午").
  - **Year:** Inter Tight 500, 11px, letter-spacing .08em (e.g. "1971").
- **Swap animation, whenever the active film changes:**
  - A new span is appended. Its siblings are absolutely positioned over the first, so the two overlap inside the mask.
  - The new span slides from `translateY(dir × 105%)` to 0.
  - Every older span that is not already leaving slides from its current transform to `translateY(−dir × 105%)` and is removed when done.
  - Timing: 650ms, `cubic-bezier(.2,.8,.2,1)`, `fill: both`.
  - `dir` is the direction of travel: +1 going right, so text comes up from below; −1 going left, so it comes down from above.
  - When you flip quickly through several films, each intermediate title passes through the mask in turn.
  - Calling setActive also updates the decade indicator.

### 6. Arrows

- **Buttons:** two 44px buttons at the caption title's height (`top: 50% + H/2 + 40px`), 20px in from each side.
- **Icons:** 18 × 10 SVG arrows, a 1.2px stroke in currentColor. Left: a chevron `M5 1 L1 5 L5 9` plus a shaft to x 17. Right: the mirror image.
- **Action:** each moves the target one film left or right.

### 7. Footer

- **Position:** fixed 32px from the sides and 26px from the bottom, `justify-content: space-between`.
- **Left:** "© LEON VASARI. ALL RIGHTS RESERVED."
- **Right:** "FB / TW", where FB and TW are links in ink with no underline.
- Both are `.lbl`.

### 8. Custom cursor

- **Element:** 58 × 58px, fixed, centred on the pointer with −29px margins, `z-index 100`, shown only on fine pointers.
- **Parts:**
  - A 1.5px ink ring (border radius 50 %).
  - A 6px ink centre dot.
  - A hidden label "OPEN" over "開く" in Inter Tight 600, 10px, line height 1.25, letter-spacing .1em, white, centred.
- **Movement:** it follows the mouse with exponential smoothing, `1 − e^(−16·dt)` per frame, positioned with `translate3d`.

| State | When | Ring | Dot | Label |
|---|---|---|---|---|
| default | anywhere else | scale 1, ink border, transparent | scale 1 | hidden (scale 0) |
| `.spine` | over a non-active tape | scale .72 | 1 | hidden |
| `.btn` | over any button or link outside the shelf | scale .55 | scale 0 | hidden |
| `.open` | over the open cover (the tilt test above) | scale 1.75, cobalt fill, cobalt border | scale 0 | scale 1 |

- **Transitions:** the ring's transform, background colour and border colour run over `.5s / .4s / .4s var(--ease)`. The dot and label scale over `.4s / .45s`. Entering the cover, the ring swells into a cobalt disc and "OPEN / 開く" pops out of its centre.

## Data: the twelve films (chronological shelf order)

| # | id | Title | Romaji | Kanji | Year | Genre | Minutes | Synopsis |
|---|---|---|---|---|---|---|---|---|
| 0 | valley | The Silent Valley | SHIZUKANA TANI | 静かな谷 | 1958 | Drama | 104 | A schoolteacher returns to the mountain village that exiled her father, and finds the valley has kept every one of its secrets. |
| 1 | bluehour | The Blue Hour | AO NO TOKI | 青の刻 | 1962 | Romance | 97 | Over one long evening in a harbour town, a widow and a stranger trade small lies until the light runs out. |
| 2 | river | River of Salt | SHIO NO KAWA | 塩の川 | 1964 | Drama | 121 | Two brothers drag a salt barge downriver to a city that no longer wants anything they carry. |
| 3 | summer | The Last Summer | SAIGO NO NATSU | 最後の夏 | 1966 | Drama | 109 | The summer before the dam floods their village, three friends set fire to everything they cannot take with them. |
| 4 | green | The Green Road | MIDORI NO MICHI | 緑の道 | 1969 | Mystery | 101 | A surveyor mapping a forest road keeps finding the same footprints, always one day ahead of him. |
| 5 | noon | Noon in Ashes | HAI NO SHOGO | 灰の正午 | 1971 | Western | 112 | A rider crosses a white desert to settle an old debt, and learns too late who sent him. |
| 6 | observer | The Observer | KANSATSUSHA | 観察者 | 1973 | Thriller | 96 | A night watchman begins to suspect that the building he guards has started watching him back. |
| 7 | birds | The Fallen Birds | OCHITA TORI | 落ちた鳥 | 1975 | Drama | 118 | When the birds stop singing over a frontier town, the mayor's daughter is the only one who goes looking for the reason. |
| 8 | storm | Light in the Storm | ARASHI NO HI | 嵐の灯 | 1978 | Drama | 127 | A lighthouse keeper and his son wait out a three-day storm with a shipwrecked sailor who will not give his name. |
| 9 | tide | The Long Tide | NAGAI SHIO | 長い潮 | 1981 | Drama | 99 | A fisherman's wife counts the tides on the harbour wall while her husband's boat fails to come home. |
| 10 | war | A Quiet War | SHIZUKANA SENSO | 静かな戦争 | 1985 | Comedy | 103 | Two neighbours fight a silent war over a garden wall for thirty years, and neither will say how it began. |
| 11 | door | Red Door | AKAI TOBIRA | 赤い扉 | 1989 | Thriller | 114 | A projectionist follows a reel of unknown film through the corridors of a cinema on its final night. |

The page opens on **Noon in Ashes** (index 5, in the middle copy, so `s = 5 + 12 = 17`).

## Motion engine

### State
- `s`: the current scroll position in tape units.
- `T`: the target.
- `hover`: the hovered virtual index, or −1.
- `active`: the film index currently in the caption.
- `mx, my`: the raw pointer; `cx, cy`: the smoothed cursor.
- `tiltX, tiltY`, `onCover`, `isOpen`.

### Each frame
- **Time step:** `dt` is clamped to 50ms.
- **Spring:** `s += (T − s) × (1 − e^(−k·dt))`, with `k = 5.2` normally and `18` while dragging. It snaps when within 1e−4. A one-step move settles in about 0.9s, and multi-step jumps glide through every tape in between.
- **Normalising:** if `s` drifts beyond ±4 full loops, both `s` and `T` shift by whole loops.
- **Caption:** the active film is `round(s) mod 12`. When it changes, run the caption swap with `dir = sign(T − s)`.

### Inputs
- **Click a tape:** if it is the active one (`|r| < .5`), open the detail. Otherwise set `T = round(T + r)`, so the shelf glides that tape to the centre.
- **Arrows:** `T = round(T) ± 1`.
- **Keyboard:** Left and Right do the same. Enter opens the detail when focus is on the body. Escape closes it.
- **Decade tabs:** jump to the first film of that decade by the shortest way round the loop. "ALL" jumps to The Silent Valley.
- **Wheel:** both axes; use whichever delta is larger. `T += delta / (ws + gap) × 0.5`. After 160ms of no wheel input, `T` snaps to the nearest integer. Wheel input is ignored while the detail is open.
- **Drag:**
  - `pointerdown` on the shelf records the start x and `T`.
  - Once the pointer moves more than 5px it becomes a drag: `T = T0 − dx / (ws + gap)`, with the faster spring.
  - `pointerup` snaps `T` to the nearest integer.
  - A drag suppresses the click on the tape it ended over.

## Opening a film: paper sheet and ink reveal

The detail is a fixed full-screen `.detail` dialog (`z-index 60`, `--sheet` background, `visibility hidden` until opened).
- **Grid:** two equal columns with a `4vw` gap and padding `110px 6vw 56px 7vw`.

### Contents

- **Close button:** a boxed `.lbl` "CLOSE / 閉じる" at the top left (32px, 31px).
- **Logo:** a copy of the cobalt logo, centred in an 84px top band.
- **Left column**, centred vertically, `max-width 520px`, 18px gap, top to bottom. Every line is wrapped in its own overflow mask:
  1. The cobalt subtitle `.lbl`, "ROMAJI / kanji".
  2. The title, Newsreader 400, `clamp(44px, 5.4vw, 84px)`, line height 1, letter-spacing −.025em.
  3. The meta `.lbl` in muted grey, "YEAR / GENRE / N MIN" (e.g. "1971 / WESTERN / 112 MIN").
  4. The synopsis, Newsreader 400, 17px, line height 1.5, `max-width 42ch`.
  5. An italic credit, Newsreader italic, 15px, muted: "Written and directed by Leon Vasari. 監督作品".
  6. A 44px boxed button, cobalt border and text, 0 20px padding, 10px top margin: "WATCH THE FILM / 映画を見る".
- **Right column: the poster.** Height `min(100%, 78vh)` with aspect ratio 474/900, centred.
  - It is an inline SVG with viewBox `0 0 474 900` holding one clipped `<image>` of the film's cover crop (see Media), masked by an ink mask.
  - **The ink mask:** a `<mask>` in user space (−200, −200, 874 × 1300) containing a group of seven white circles.
  - **Ink filter on that group:** `feTurbulence` fractalNoise, baseFrequency .011, 3 octaves, seed 7, feeding an `feDisplacementMap` with scale 120 on the R and G channels. The circles' edges become ragged, bleeding blots.

| Blob | cx | cy | Delay (ms) |
|---|---|---|---|
| 1 | 150 | 330 | 0 |
| 2 | 340 | 600 | 120 |
| 3 | 250 | 120 | 220 |
| 4 | 90 | 760 | 300 |
| 5 | 400 | 250 | 360 |
| 6 | 260 | 860 | 420 |
| 7 | 230 | 470 | 180 |

### Open sequence (`openDetail`)

1. **Prepare.**
   - Snap `T` to an integer and fill the detail texts from the active film.
   - Point the poster `<image>` at its cover's sheet, positioned so only its crop box shows (see Media).
   - Reset all blob radii to 0.
   - Read the screen rect of the active tape's cover face (`getBoundingClientRect`, which gives the projected 3D box).
2. **The sheet grows out of the cover.**
   - Make the dialog visible and set its `transform-origin` to the cover's centre.
   - Animate it with the Web Animations API over **1050ms**, `cubic-bezier(.76,0,.18,1)`, `fill both`.
   - From `clip-path: inset(top right bottom left round 3px)`, matching the cover rect, with `transform: rotate(−4.5deg)`.
   - To `clip-path: inset(0 0 0 0 round 0)` with `rotate(0)`.
   - A blank rectangle of paper the exact size and tilt of the cover straightens and expands until it covers the screen.
3. **Text rises.** Every masked line slides from `translateY(110%)` to 0 over **900ms**, `cubic-bezier(.2,.8,.2,1)`. Delays are `620ms + index × 75ms`, so the lines arrive one after another.
4. **The poster bleeds in.**
   - Starting 520ms after open, a rAF loop grows each circle's radius from 0 to 720 over **1250ms** after its own delay, with an ease-out cubic `1 − (1 − p)³`.
   - The cover appears as spreading ink blots that merge into the full poster.
   - The loop stops after 2.4s.
5. **Hide the rest.** The play ring scales to 0, and the cursor drops its OPEN and spine states while over the sheet.

### Close (`closeDetail`: the Close button or Escape)

- Animate the sheet back from full screen to the current cover rect, with `rotate(−4.5deg)`, over **850ms** with the same ease.
- When it finishes, hide the dialog and cancel all its animations so the next open starts fresh.

## Responsive (≤ 767px)

- `--H: min(60vw, 40svh)`. Every tape dimension follows from it.
- **Top bar:** 64px tall, 16px padding. The logo becomes 17px over 7.5px. Labels are 9px. **The career label is hidden.**
- **Tabs:** sit at `50% − H/2 − 70px`, with 0 7px padding and 9px text.
- **Caption title:** 24px.
- **Arrows:** 6px from the edges.
- **Footer:** 16px sides, 18px bottom, 9px labels.
- **Detail:** a single column that scrolls vertically.
  - Padding `84px 22px 40px`, 24px gap.
  - The poster moves first and is `46svh` tall.
  - Title 42px, synopsis 16px. The Close button sits at 16px, 21px, and the logo band is 64px.
- **Touch:** the custom cursor is not shown. Dragging the shelf with a finger scrubs it, because the shelf uses `touch-action: pan-y`.

## Reduced motion

With `prefers-reduced-motion: reduce`:
- The scroll spring and hover lift become instant (k = 1), so tapes snap between states.
- Caption swaps replace the text without sliding.
- The sheet open, close and text rises run with 1ms duration and no delay.
- The ink starts 5s in the past, so the poster is fully visible at once.

## Accessibility

- The tabs are a `<nav aria-label="Decades">` and the shelf is a `<section aria-label="Filmography shelf">`.
- The caption container is `aria-live="polite"`, so film changes are announced.
- Arrow and play buttons have `aria-label`s ("Previous film", "Next film", "Open film").
- The detail is `role="dialog" aria-modal="true"`. The poster SVG is `aria-hidden`.
- All controls are real `<button>`s and links.

## Acceptance checklist

- On load, Noon in Ashes is turned out at the centre: tilted −4.5°, lifted and casting a shadow. The other eleven spines repeat endlessly on both sides, about 13 visible at 1440px.
- Clicking a spine two places to the right glides the shelf: the open tape turns back into a spine while the next ones turn out in passing, and the caption rolls through each title.
- The cobalt tab block slides to the new decade.
- The cursor ring shrinks over spines and becomes a cobalt "OPEN / 開く" disc over the cover, which leans towards it.
- Clicking the cover grows a tilted sheet of paper out of it to full screen. The detail text rises line by line, and the poster bleeds in as ragged ink blots.
- There are no opacity fades anywhere.
