<!-- Wild Pil · Travel · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261027_025011_1abf0073-f4d1-4855-ab7b-6bf9838ea04d.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=wild-pill-hero -->

# Prompt: Wild pill hero

Build a single-file, one-screen **travel hero for a fictional rental brand, Wild**. Use plain HTML, CSS and vanilla JS with no framework and no build step.

The page opens on white with the word **WILD** and a hairline between the I and the L. That line opens into a slit, then a circle, then a wide stadium-shaped pill that pushes "WI" and "LD" apart. The pill shows a looping video of a floating island with a waterfall over sunset clouds. As the pill opens, a soft paper background with flowing white lines fades in, the nav drops in from the top and the footer bar rises from the bottom.

## Media

- **Scene video:** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/175fbbcd-e50a-480c-bab2-ca16d4678322.mp4
  - 1280×720, 60 fps, 4.25 s, muted.
  - It loops seamlessly with a hard loop: no crossfade, no reverse.
  - The island sits centred with sky above and clouds below. The waterfall pours, clouds drift, birds glide and the small islands bob.
- **Poster (first frame):** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/726b168c-da47-4682-a255-cc3e02f89bae.jpg
- **Display:** the video sits inside the pill at full pill height, centred horizontally, at least 4.2 em wide, so it cover-crops at every pill width. The focal point is the top of the scene: `object-fit: cover; object-position: center top` (the poster too). It is always fully opaque; only the pill's own width and clip reveal it.

## Type and colour

- **Font:** Inter (variable, 400–800), self-hosted.
- **Word:** "WILD" in weight 800, tracking −0.045 em, line-height 0.8.
- **Colours:**
  - page `#ffffff` at the start, then paper `#f2f2f1`
  - ink `#1d1d1d`, secondary text `#3a3a3a`
  - rule `#a9a9a6`
  - button `#1b1b1b` with white text

## Scale

- **Unit:** one type unit, `--fs = min(19.6vh, 13.2vw)` on desktop, which is the font size of the word. Everything in the hero is sized from it.
- **Phone (≤ 720 px):** the word stacks, with "WI" over the pill over "LD". See *Phone* below.

## Layout

- **Hero:** centred 43 % from the top. The row is `WI · pill · LD` in a flex row, with the gap animating between the parts.
- **Pill:**
  - height 1.81 em, fully rounded, overflow hidden, placeholder fill `#d8d3cf`
  - final width 3.62 em on desktop, about a 2:1 stadium
  - a tiny white line icon near each end, at about 85 % opacity: a breeze icon on the left, a speaker icon on the right that toggles its sound waves
- **Background:** a paper layer with about 15 long white strokes sweeping up and to the right as soft S-curves (stroke 1.2–3.9 px, opacity 0.55–0.85), drawn in an SVG stretched to the viewport.
- **Nav (top):**
  - left links "Home · Features · Templates · Contact Us", right links "Instagram · Facebook" as plain text (no logos)
  - size max(12 px, 0.072 em), weight 450
  - padding 0.14 em top, 0.27 em sides
- **Footer (bottom):** a row aligned to the bottom.
  - Left: a paragraph 1.42 em wide, size 0.066 em, line-height 1.45, with a drop-cap "E" (2.35× size, weight 650): "Embark on a wild ride around the world with our travel rental service. Discover breathtaking landscapes and hidden gems on your unforgettable journey."
  - Middle: a 1 px rule filling the space.
  - Right: a black pill button "Let's Get Wild".

## Motion: the reveal

One Web Animations timeline, 2.1 s, starting once fonts are ready.

- **Pill width** (fs = word size):
  - 0.012 fs (a hairline) at 0 %, held to 14 %
  - 0.16 fs (a slit) at 30 %
  - 1.81 fs (a circle) at 58 %
  - the final width at 100 %
  - easings: `(.5,0,.3,1)`, `(.45,0,.3,1)`, `(.4,0,.2,1)`
- **Pill clip:** grows vertically from `inset(50% 0)` to `inset(0)` over 0–14 %, so the hairline draws from the middle out.
- **Hairline:** a grey overlay (`#b9b9b9`) on the pill shows the line as grey, then fades out between 14 % and 30 % as the image appears. This fade is on the overlay, never on the video.
- **Word gap:** 0.026 em until 14 %, 0.05 em at 58 %, then 0.085 em. "WI" and "LD" are pushed outward by the opening pill.
- **Background:** the paper and lines fade in between 45 % and 78 %.
- **Nav:** slides down from −140 % between 50 % and 86 %, with easing `(.2,.8,.2,1)`.
- **Footer:** rises from +160 % between 52 % and 90 %.
- **Rule:** draws from the centre (scaleX 0 → 1) between 40 % and 95 %.
- **Icons:** fade in after 80 %.

## Interaction

- **"Let's Get Wild":** replays the reveal. It plays the same timeline in reverse, collapsing the pill back to the hairline with everything leaving, then opens it again.
- **Resize:** finishes any running animation and resets the pill width.
- **Speaker icon:** toggles its waves. The clip is silent.
- **Reduced motion:** shows the final state with the video paused on the poster.

## Recording mode (`?rec=1`)

- The reveal plays at 0 s and the reverse collapse starts at 4.9 s, matching the reference loop.
- `window.__recVideo(t)` returns `(t mod duration) + 1/120`, so a frame-by-frame recorder seeks the clip to a fresh frame every step.

## Phone (≤ 720 px)

- **Type:** `--fs = min(34vw, 16.5vh)`, side margin 20 px.
- **Hero:** the hero column is centred 47 % from the top: "WI", then the pill, then "LD", with gaps of 0.03 → 0.1 em.
- **Pill:** full width (`100vw − 40px`), with a final height of width ÷ 1.85.
  - It opens **vertically**: a horizontal grey hairline draws from the centre outwards (clip `inset(0 50%)` → 0), then grows 1.5 px → 10 % → 55 % → 100 % of its height on the same 2.1 s curve.
  - The halves are pushed apart vertically.
  - The video inside is full pill width and the final pill height, centred vertically, anchored top.
- **Nav:** the four links only, at 12.5 px.
- **Footer:** the paragraph at full width (13 px / 1.5), then a row with the rule and a 38 px black button. Even 20 px margins.

## Acceptance check (1440×960)

- The hairline draws between I and L, opens into a slit, a circle, then a wide pill, while the halves glide apart. The nav drops in, the footer rises and the rule draws.
- The island video keeps moving inside the pill and loops with no jump.
- "Let's Get Wild" collapses the hero to the line and reopens it.
- **Content:** no real brands or logos.
