<!-- Smoothie Slider · Food & Drink · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261117_061855_3cc0b3cc-0cea-4370-a06e-1cb37e2b5898.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=smoothie-slider -->

# Blendy — smoothie flavour slider hero: exact recreation prompt

Build a single-screen landing hero for a fictional smoothie brand called Blendy. It is a full-viewport product slider with four flavours: Berry, Kiwi, Banana and Strawberry. Each flavour floods the whole screen with one flat pastel colour. A huge white flavour word sits behind one centred smoothie bottle, and real fruit pieces float around the bottle at different depths, with two large blurred pieces in the bottom-left and top-right corners. A tiny white nav sits on top, a tracked "SHOP NOW" label at the bottom centre and thin arrows in the bottom corners. Changing flavour plays a measured panel wipe: the current slide is covered from its right edge towards the left while its content drifts left, and the next flavour's word, bottle and fruit slide in from the right with parallax. Everything must match the measurements below exactly. Use one HTML file with inline CSS and vanilla JavaScript, no frameworks and no build step.

## 1. Assets

All product imagery comes from four transparent PNG "cut-out sheets", one per flavour. Each sheet is 2048 × 2048 px with transparency, laid out as an invisible 2 × 2 grid: the top-left cell holds the bottle (with its two green leaves attached), and the other three cells hold three different fruit pieces. Load each sheet through the images.higgs.ai proxy as WebP. The exact URL form is `https://images.higgs.ai/?default=1&output=webp&w=2048&q=85&url=` followed by the URL-encoded original link.

| Flavour | Original sheet URL (transparent PNG, 2048 × 2048) |
|---|---|
| Berry | https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261117_053958_8803e421-29b1-4c24-8efd-54cae3f479b4.png |
| Kiwi | https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261117_053958_b5695e60-72da-4b5b-bfb7-a091d528af75.png |
| Banana | https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261117_053958_6cf14029-4bce-4c9a-b9fc-1c5b185082e3.png |
| Strawberry | https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261117_055135_cbfb5a8d-c52b-4358-a6ee-d941c6c42285.png |

So, for example, the Berry sheet is loaded from https://images.higgs.ai/?default=1&output=webp&w=2048&q=85&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261117_053958_8803e421-29b1-4c24-8efd-54cae3f479b4.png, and the other three follow the same pattern with their own file names.

Never slice the sheets into separate files. Every bottle and fruit piece is a CSS background crop of its sheet. These are the exact item boxes inside each sheet, as [x, y, width, height] in sheet pixels:

| Sheet | Item 0: bottle with leaves | Item 1 | Item 2 | Item 3 |
|---|---|---|---|---|
| Berry | 233, 60, 598, 917 | raspberry: 1209, 272, 569, 573 | blueberry: 265, 1230, 579, 572 | blackberry: 1192, 1192, 626, 641 |
| Kiwi | 217, 90, 610, 874 | kiwi round half: 1204, 257, 619, 601 | kiwi wedge: 250, 1197, 619, 522 | kiwi round slice: 1200, 1186, 633, 650 |
| Banana | 194, 76, 579, 873 | banana coin, angled: 1205, 228, 596, 597 | peeled banana chunk: 230, 1181, 624, 648 | banana coin, face-on: 1193, 1182, 646, 659 |
| Strawberry | 226, 88, 594, 887 | whole strawberry: 1190, 216, 561, 653 | strawberry half: 257, 1168, 604, 662 | whole strawberry, tilted: 1240, 1169, 632, 686 |

How to crop: to show item [bx, by, bw, bh] at a target width W (design px), use the scale s = W / bw. The element is W wide and bh × s tall. Its background-size is (2048 × s) by (2048 × s), and its background-position is (−bx × s, −by × s), with background-repeat no-repeat.

## 2. Fonts

Use Google Fonts, self-hosted as latin WOFF2 files with font-display swap.

| Family | Weight | Used for | Google Fonts source |
|---|---|---|---|
| Poppins | 500 | nav tabs, Cart, Register | https://fonts.gstatic.com/s/poppins/v24/pxiByp8kv8JHgFVrLGT9Z1xlFQ.woff2 |
| Poppins | 600 | SHOP NOW | https://fonts.gstatic.com/s/poppins/v24/pxiByp8kv8JHgFVrLEj6Z1xlFQ.woff2 |
| Poppins | 700 | the giant flavour word | from https://fonts.googleapis.com/css2?family=Poppins:wght@700 (latin subset) |
| Baloo 2 | 800 | the "Blendy" logo | https://fonts.gstatic.com/s/baloo2/v23/wXK0E3kTposypRydzVT08TS3JnAmtdiayppo_lc.woff2 |

The body font stack is Poppins, then system-ui, then sans-serif. All text is pure white #FFFFFF and antialiased.

## 3. Head and colour tokens

The page title is "Blendy — Real fruit smoothies". Use a standard viewport meta (width=device-width, initial-scale=1). html and body are 100% tall with overflow hidden (the page never scrolls), and body background is #C2B0DC. body has touch-action pan-y so horizontal swipes reach the script.

| Flavour | Backdrop colour | Word |
|---|---|---|
| Berry | #C2B0DC (soft lilac) | Berry |
| Kiwi | #B4D58A (soft mint green) | Kiwi |
| Banana | #F3DA8A (butter yellow) | Banana |
| Strawberry | #F2AFC0 (pastel strawberry pink) | Strawberry |

Every small UI text element carries the text-shadow 0 1px 6px rgba(90,70,40,0.18), so the white stays legible on the yellow and pink backdrops.

## 4. Scaling system

Everything inside a slide is drawn on one 1440 × 900 design frame. One unit, --u, is set on the root element by script: u = min(viewportWidth / 1440, viewportHeight / 900). The frame is 1440u wide and 900u tall and centred in the viewport (left = 50% − 720u, top = 50% − 450u + fy, where fy is 0 on desktop). The backdrop colour fills the whole viewport outside the frame, so fitting rather than covering never shows an edge.

The nav and bottom controls do not use --u. They use their own unit, --n = clamp(0.5px, min(100vw / 1440, 100vh / 900), 1.3px), and are pinned to the viewport edges.

## 5. DOM and desktop measurements

A fixed full-viewport stage (overflow hidden, user-select none) holds four stacked slide sections, one per flavour. Each section is absolutely positioned at inset 0 with overflow hidden and its flavour backdrop colour. Each slide holds one frame, and the frame holds five full-size layers in this stacking order (bottom to top): word, shadow, bottle, fruit, corner. Each layer moves as a unit during transitions.

### 5.1 The flavour word (word layer)

The word is centred horizontally across the 1440-wide frame, set in Poppins 700 with line-height 1, white-space nowrap and pure white. Its size is computed by script:

- Default size is 445 design px with letter-spacing 0.005em. At that size the cap height is 0.698 × 445 ≈ 311 px.
- If the word's ink width at 445 px would exceed 1330 design px, letter-spacing changes to −0.035em and the size becomes the largest that makes the ink width 1400 design px (capped at 445). Ink width is measured with a canvas measureText of the word in 700-weight Poppins at 100 px, using actualBoundingBoxLeft + actualBoundingBoxRight.
- Vertical placement keeps every word centred on the same cap line: baseline = 403.5 + 0.698 × F / 2, and the element's top = baseline − 0.85 × F (0.85em is Poppins' baseline offset at line-height 1).
- At 1440 × 900 this gives Berry and Kiwi at 445 px (box top 181), Banana at about 372 px (box top 217) and Strawberry at about 257 px (box top 275).

### 5.2 Floor shadows (shadow layer)

There are four soft ellipses, the same on every slide. Each is a radial-gradient (closest-side) from rgba(60,40,80,0.22) to transparent, with border-radius 50% and a blur of 4u. The values are centre x, centre y, width, height in design px:

| Shadow | cx | cy | w | h |
|---|---|---|---|---|
| under left fruit | 345 | 650 | 170 | 24 |
| under bottle | 720 | 708 | 320 | 30 |
| under right fruit | 1318 | 638 | 160 | 22 |
| under bottom-right fruit | 1045 | 760 | 150 | 22 |

### 5.3 Bottle (bottle layer)

Each bottle is item 0 of its sheet, placed at left x, top y and width w in design px, with height following the sheet ratio. The bottle never bobs.

| Flavour | x | y | w |
|---|---|---|---|
| Berry | 518 | 138 | 372 |
| Kiwi | 504 | 135 | 403 |
| Banana | 512 | 135 | 383 |
| Strawberry | 512 | 135 | 386 |

### 5.4 Fruit pieces (fruit and corner layers)

Each slide has seven pieces: five sharp mid-size ones in the fruit layer and two large blurred ones in the corner layer (filter blur 9u). The columns are the sheet item, left x, top y, width in design px, base rotation in degrees, and whether the outer element is mirrored with scaleX(−1).

Berry:

| Piece | Item | x | y | w | Rotation | Mirror | Layer |
|---|---|---|---|---|---|---|---|
| blueberry, top-left | 2 | 383 | 178 | 104 | 0 | no | fruit |
| blackberry, upper right of the bottle | 3 | 960 | 232 | 118 | 0 | no | fruit |
| raspberry, mid-left | 1 | 295 | 478 | 129 | −8 | no | fruit |
| raspberry, far right | 1 | 1247 | 455 | 123 | 15 | no | fruit |
| blueberry, lower right | 2 | 968 | 590 | 110 | 30 | no | fruit |
| raspberry, blurred, bottom-left corner | 1 | −15 | 590 | 255 | 0 | no | corner |
| blackberry, blurred, top-right corner | 3 | 1282 | 40 | 200 | 0 | no | corner |

Kiwi:

| Piece | Item | x | y | w | Rotation | Mirror | Layer |
|---|---|---|---|---|---|---|---|
| wedge, top-left | 2 | 376 | 170 | 144 | −150 | yes | fruit |
| round slice, upper right | 3 | 960 | 228 | 152 | 0 | no | fruit |
| round half, mid-left | 1 | 303 | 460 | 168 | 0 | no | fruit |
| wedge, far right | 2 | 1187 | 462 | 148 | −25 | no | fruit |
| wedge, lower right | 2 | 946 | 606 | 150 | 10 | yes | fruit |
| round half, blurred, bottom-left corner | 1 | −10 | 575 | 260 | 0 | no | corner |
| round slice, blurred, top-right corner | 3 | 1285 | 30 | 200 | 0 | no | corner |

Banana:

| Piece | Item | x | y | w | Rotation | Mirror | Layer |
|---|---|---|---|---|---|---|---|
| angled coin, top-left | 1 | 387 | 147 | 123 | 0 | no | fruit |
| chunk, upper right | 2 | 970 | 223 | 136 | −10 | yes | fruit |
| face-on coin, mid-left | 3 | 298 | 483 | 132 | 15 | no | fruit |
| chunk, far right | 2 | 1245 | 462 | 150 | 20 | no | fruit |
| face-on coin, lower right | 3 | 950 | 582 | 130 | −12 | no | fruit |
| face-on coin, blurred, bottom-left corner | 3 | 0 | 585 | 235 | 0 | no | corner |
| angled coin, blurred, top-right corner | 1 | 1280 | 30 | 190 | 0 | no | corner |

Strawberry:

| Piece | Item | x | y | w | Rotation | Mirror | Layer |
|---|---|---|---|---|---|---|---|
| whole, top-left | 1 | 372 | 142 | 128 | 0 | no | fruit |
| half, upper right | 2 | 955 | 225 | 117 | 20 | no | fruit |
| tilted whole, mid-left | 3 | 290 | 455 | 140 | −10 | no | fruit |
| tilted whole, far right | 3 | 1250 | 432 | 135 | 15 | no | fruit |
| half, lower right | 2 | 962 | 558 | 146 | −15 | no | fruit |
| whole, blurred, bottom-left corner | 1 | −10 | 555 | 245 | 0 | no | corner |
| whole, blurred, top-right corner | 1 | 1285 | 35 | 200 | 20 | no | corner |

Each piece is an outer element (position, size, optional mirror) that holds an inner element, which carries the background crop and the idle bob animation. The base rotation is applied inside the bob, so the mirror and the rotation never fight.

### 5.5 Nav (fixed UI, --n units)

The UI layer is fixed at inset 0 with z-index 10 and pointer-events none. Only links and buttons take pointer events, and they have no background, no border, white text and an inherited font.

- **Header row:** from 50n to the left and right edges, 26n from the top, 50n tall, flex with items centred vertically.
- **Logo:** "Blendy" in Baloo 2 800 at 51n, letter-spacing −0.02em, line-height 1, linking to #. At 1440 wide it measures about 156 × 51 px at x 50, y 26.
- **Flavour tabs:** absolutely centred in the header (left 50%, translateX −50%), flex with gap 88n, in Poppins 500 at 21n. The buttons read Berry, Kiwi, Banana, Strawberry, each with 6n vertical padding. At 1440 wide their left edges sit at 440, 583, 713 and 884 px.
- **Underline:** one 2 px white bar with 2 px radius, absolutely positioned 2n below the tab row. It always takes the active tab's width and its offsetLeft as translateX, and moves over 0.6 s with cubic-bezier(0.65, 0, 0.35, 1) on both transform and width. The active tab gets aria-current true.
- **Account links:** pushed to the right with margin-left auto, flex with gap 22n, in Poppins 500 at 21n: "Cart", a "|" separator at 0.9 opacity, then "Register".

### 5.6 Bottom controls (fixed UI)

- **SHOP NOW:** a link centred horizontally (left 50%, translateX −50%), 36n from the bottom, in Poppins 600 at 21n with letter-spacing 0.2em, and 10n × 16n padding. At 1440 × 900 its box is about 181 × 51 px at y 813.
- **Arrows:** a previous button 36n from the left and a next button 36n from the right, both 30n from the bottom. Each is 52n square with its icon centred. The icons are 28n square SVGs in a 28 × 28 viewBox, white stroke 2 with round caps and joins. The previous arrow is the path M24 14H4 M12 6l−8 8 8 8, and the next arrow is M4 14h20 M16 6l8 8−8 8. Their aria-labels are "Previous flavour" and "Next flavour".

## 6. Idle motion

Every fruit piece (not the bottle) bobs forever: an alternate infinite ease-in-out keyframe from translateY(−7u) with rotate(base − 3°) to translateY(+7u) with rotate(base + 3°). Each piece gets a random duration between 3.2 s and 5.0 s and a random negative delay between 0 and −4 s, so no two pieces move in step.

## 7. Flavour change (measured from the reference)

Only one slide is visible at rest; it has z-index 2 and the others are hidden. When changing from slide A to slide B in direction dir (+1 for next, −1 for previous):

1. Slide B becomes visible under A at z-index 1, and A stays on top at z-index 2.
2. A runs for 970 ms. At time fraction t (0 to 1), its coverage c = cover(t) comes from this measured table, with smoothstep (3k² − 2k³) between neighbouring points. The values are t → c:

| t | 0 | 0.031 | 0.134 | 0.206 | 0.278 | 0.34 | 0.412 | 0.485 | 0.546 | 0.583 | 0.62 | 0.69 | 0.79 | 0.85 | 0.93 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c | 0 | 0.006 | 0.012 | 0.023 | 0.047 | 0.07 | 0.105 | 0.158 | 0.246 | 0.55 | 0.825 | 0.9 | 0.94 | 0.956 | 0.975 | 1 |

   This gives a slow start (about half the time to cover the first quarter), a rush through the middle and a long soft settle.
3. **Covering A:** going forward, A is clipped with clip-path inset(0 c×100% 0 0), so its right edge sweeps from the right of the screen to the left. Going back, it is clipped with inset(0 0 0 c×100%) instead.
4. **A drifts away:** all five of A's layers translate on x by −dir × c × 0.14 × the frame width.
5. **B arrives with parallax:** B's layers start pushed towards the incoming side and settle to 0. The offset is dir × (1 − k) × factor × the frame width, where k = easeOutQuad of (t − 0.5) / 0.42, clamped to 0–1, and t keeps counting past 1 until k reaches 1. So B's content starts moving halfway through the sweep and lands about 0.9 s after the click. The factors make the fruit travel farther than the word: word 0.40, shadow 0.30, bottle 0.15, fruit 0.55, corner 0.75.
6. **Finish:** B becomes the current slide, every clip and transform is cleared, and the other slides are hidden. Clicks during a transition are ignored.
7. **Ordering:** next from Strawberry wraps to Berry and still plays the forward (right-to-left) direction; previous from Berry goes to Strawberry. Clicking a tab goes forward when the target is to the right of the current tab and backward when it is to the left. The underline starts moving the moment a change begins.

## 8. Opening sequence

Once document.fonts.ready resolves, the word and the slide layers are laid out again. Then:

| Element | Animation | Delay | Duration | Easing |
|---|---|---|---|---|
| Berry word layer | translateX from +0.40 × frame width to 0 | 0 | 900 ms | cubic-bezier(0.22, 0.8, 0.3, 1) |
| Berry shadow layer | from +0.30 × frame width to 0 | 0 | 900 ms | same |
| Berry bottle layer | from +0.15 × frame width to 0 | 0 | 900 ms | same |
| Berry fruit layer | from +0.55 × frame width to 0 | 0 | 900 ms | same |
| Berry corner layer | from +0.75 × frame width to 0 | 0 | 900 ms | same |
| Logo | opacity 0 → 1 and translate 0 14px → 0 | 250 ms | 1000 ms | same |
| Tabs | the same rise | 330 ms | 1000 ms | same |
| Cart / Register | the same rise | 410 ms | 1000 ms | same |
| Previous arrow | the same rise | 490 ms | 1000 ms | same |
| SHOP NOW | the same rise | 570 ms | 1000 ms | same |
| Next arrow | the same rise | 650 ms | 1000 ms | same |

Use the separate `translate` property for the UI rise, not transform, so the centring transforms on the tabs and SHOP NOW are untouched. Add a 3 s failsafe that finishes any reveal still pending and removes the hidden state.

## 9. Controls

- **Autoplay:** every 2600 ms, if the page is visible and no one has interacted in the last 6 s, go to the next flavour (forward).
- **Tabs:** go to that flavour.
- **Arrows:** previous and next.
- **Keyboard:** ArrowLeft and ArrowRight do the same as the arrows.
- **Swipe and drag:** on pointerdown over the stage, record x and y. On pointerup anywhere, if the horizontal distance is over 45 px and larger than the vertical distance, a swipe left goes forward and a swipe right goes back.
- Every user action pauses autoplay for 6 s.

## 10. Tablet and mobile

The mobile layout applies when the viewport is 820 px wide or less, or taller than it is wide.

- **Scene scale:** u = min(width / 640, (height − 200) / 620), and the frame is nudged 8 px down. This shows the central part of the design frame: the bottle, the inner fruit and the word. The two blurred corner pieces fall outside the view.
- **Word on mobile:** the word fits 92% of the visible frame width (visible width = min(1440, viewportWidth / u) × 0.92), with the same long-word letter-spacing rule. It stays centred on the same cap line, behind the bottle.
- **UI on mobile:** --n becomes 1px.
  - The header sits 20 px from each side and 16 px from the top, 40 px tall.
  - The logo is 34 px.
  - Cart and Register are 15 px with a 10 px gap.
  - The tabs move to a second row, top 52 px, centred, with a 22 px gap at 15 px.
  - SHOP NOW is 15 px, 22 px from the bottom.
  - The arrows are 48 px buttons with 24 px icons, 12 px from the bottom and 8 px from the sides.
- Short landscape phones (for example 844 × 390) keep the desktop layout. The fit-to-height scale keeps the whole composition visible, and --n bottoms out at 0.5px.
- Nothing scrolls sideways at any size, and every control stays visible and tappable.

## 11. Reduced motion

With prefers-reduced-motion: reduce, the fruit pieces stop bobbing and hold their base rotation. Flavour changes swap instantly with no wipe or parallax, the underline jumps, there is no opening sequence (everything is visible at once), and autoplay still advances the flavours.

## 12. Acceptance checklist

- At 1440 × 900 the Berry slide shows the lilac backdrop; the "Berry" word at 445 px with its cap line centred at y 403.5; the bottle at 518, 138 and 372 wide; and the seven berry pieces exactly as tabled, with the two corner pieces blurred.
- Words never overflow the screen; "Banana" and "Strawberry" get smaller with tighter tracking.
- The flavour change takes 970 ms with the slow, fast, soft rhythm of the coverage table. The old slide drifts left and stays as a shrinking strip at the left edge. The new content slides in from the right with the fruit travelling farther than the word.
- The underline glides to the active tab.
- Autoplay cycles Berry → Kiwi → Banana → Strawberry → Berry every 2.6 s and pauses for 6 s after any click, key or swipe.
- Swiping works on touch screens, and the arrows and tabs work everywhere.
- The phone layout at 390 × 844 and 360 × 640 shows the nav on two rows, the bottle and word centred, and SHOP NOW with both arrows at the bottom, with no sideways scroll.
- All images load from images.higgs.ai, and the fonts load from local WOFF2 files (or embedded base64 in the standalone version).
