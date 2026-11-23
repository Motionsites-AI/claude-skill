<!-- Reelmark · Creator Platform · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261021_033850_f6a98168-2aa6-47b5-8fa8-6d28a9992580.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=reelmark-v2 -->

# Prompt: Reelmark hero

Build a single-file, one-screen **landing hero for a short-form video creator marketplace**, **Reelmark** ("Captivate Crowds with Snackable Reels"). Use plain HTML, CSS and vanilla JS, with no framework and no build step. The look is soft mint studio: a warm off-white page `#F5F8EF`, deep forest-green accents `#08482D`, a mint badge `#DAE7C7`, a big bold black headline, and an arched row of seven tall video cards playing bright sage-green product clips, with hand-drawn green notes and arrows.

## Frame

- **Frame:** one **1440×1080** frame, contained and centred: `--u = min(100vw/1440, 100vh/1080)`. Every element is placed in frame units.

## Type

- **Headline:** **Inter Tight 700**, 88u on a 92u line, tracking −0.035em (−0.022em on line 2), ink `#101410`.
- **UI:** **Inter** 400/500. The subline is `#5E5E61`.
- **Notes:** **Caveat 600** for the hand-drawn notes, in forest green.

## Layout (1440×1080)

- **Top bar:**
  - **Logo:** a green leaf mark with "Reelmark", at (37, 36).
  - **Nav:** Brands · Creators · Pricing · Use Cases · Contact, Inter 16.4u, starting at x = 505 with a 31u gap.
  - **Buttons:** a white "Log in" pill, 92×40 at (1211, 29), and a forest-green "Sign up" pill, 97×40 at (1304, 29).
- **Badge:** a mint pill, 292×37 at (575, 115): "Trusted by 120,000+ indie makers", Inter 500 16.6u in green.
- **Headline:** centred, top 176: **"Captivate Crowds / with Snackable Reels"**.
- **Subline:** centred, top 394, 20.8u / 32u, three lines: "Grow your brand with short, snappy product clips by / our handpicked video makers. Our crew is ready to / lift your next launch higher."
- **Notes:**
  - a "//" doodle at (263, 377)
  - a handwritten "Be seen / with clips" rotated 16° at (1212, 310), with a long curving arrow down to the cards
  - "Zero cost" rotated 24° at (521, 937), with a small arrow pointing to the button
  - the doodle strokes draw themselves in
  - the "Be seen" arrow starts **below** the note (it never crosses the words) and curls down to the cards
- **Card row: a curved video carousel.** Ten tall cards scroll continuously **right → left** (about 50u per second, looping seamlessly). The row is draggable with the pointer or touch: it follows the drag 1:1, coasts with momentum after release (velocity decays about 95% per second), then the slow auto-scroll carries on. The cursor is grab / grabbing.
  - **Curve:** each card's geometry comes from its x position relative to the centre, like the inside of a cylinder.
    - Normalised distance d = |x − 720| / 706.
    - Width = (170 + 48·d²)u. Cards sit on an even 196u pitch, then each centre is pushed outward: x = 720 + t·(1 + 0.083·(t/706)²), where t is the unpushed offset from the centre. This keeps about a 26u gap even at the edges.
    - Each vertical edge's height = (280 + 92·q^2.6)u, where q is that edge's own normalised distance.
    - The vertical centre sits at (687 − 12·d²)u.
  - **Result:** centre cards are upright 170×280 rectangles, and cards near the screen edges grow to about 370u tall with their outer edge taller than the inner edge.
  - **Drawing:** each card is a rounded quad (`clip-path: path()`, 15u corners) recomputed every frame.
  - **Details:** no drop shadow, a small frosted round play icon at each card's bottom-left, and cards clipped by the frame edges.
- **Button:** a forest-green "Make a Reel" pill (172×58) inside a dashed green outline ring (190×74) at (626, 901).

## Card media (one video for all ten)

- **Grid:** all card clips live in ONE 16:9 **5×2 grid** (10 tiles of 384×540, edge to edge):
  - **Still poster:** `https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/b7ebb74a-8c8a-4f7e-8f80-55e2d74ecd05.webp`
  - **Loop:** `https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/04fd3d5f-99d7-476e-98a4-46c08518ffb3.mp4` (1280×720, 5s, muted, loops)
- **Tiles** (row-major) are the sneaker, skincare splash, latte pour, headphones, plant shop, florist bouquet, pottery wheel, serum splash, latte top-down and headphones on a stand. Each tile animates on its own.
- **Each card:** shows its own tile, cover-fitted. Inside the clipped card, place a `<video>` and a poster layer sized 5 × tile width by 2 × tile height, offset to that tile, where the tile height is max(card height, card width / 0.7111).
- **Sync:** every card uses the same src, so it downloads once. Keep all ten on the same timestamp, and fade each in when its first frame is ready.
- **Clock:** drive the carousel from a long-running Web Animations clock (`document.documentElement.animate(…, {duration: 1e9})`) so the scroll is time-based.

## Motion (UI)

- **Entrance:** a one-time Web Animations sequence.
  - The nav drops in, the badge pops, each headline line rises out of a blur, then the subline.
  - The card row rises in, the button scales in, the doodle strokes draw, and the notes fade in.
- **Reduced motion:** no entrance and no video.

## Phones (≤ 820px)

- **Top:** the logo and a Sign up pill.
- **Copy:** stacked and centred: the badge, the headline (clamp 38–56px) and the subline.
- **Cards:** the same auto-scrolling, draggable curved carousel, scaled to the screen width (640-unit scale), in a 250px-tall band.
- **Bottom:** the button and the "Zero cost" note.

## Acceptance check (1440×1080)

- The headline sits centred above the arched card row, matching the coordinates above.
- The card row keeps drifting left and can be flung by dragging.
- Each card plays a different clip in motion, and the edge cards are taller and lean like the inside of a cylinder.
- **Content:** no real brand logos.
