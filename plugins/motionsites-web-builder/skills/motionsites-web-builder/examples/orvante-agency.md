<!-- Orvante Agency · Agency · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261027_053930_87ab1421-7fc4-4597-a7ae-7039d2527f8b.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=orvante-agency -->

# Prompt: Orvante branding-agency page (three sections)

Build a single-file, three-section landing page for a fictional branding agency, **Orvante**. Use plain HTML, CSS and vanilla JS, with no framework and no build step. The look is a strict monochrome editorial layout. A light grey hero with a large black-and-white photo of an Asian man seen from behind is followed by a black manifesto section whose words fill from grey to white, then a bordered "Trusted by" panel with stat cards.

## Media (exact URLs, all on Higgsfield CloudFront)

- **Hero photo:** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/7dc8b8f3-4ccb-4599-8ce4-7f7c7881bad9.webp. A black-and-white studio photo of an East Asian man seen from behind, head turned slightly to his right, in a dark technical jacket, on a flat #dadada background.
- **230+ card photo:** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/a9d3641f-d629-46e5-8d2d-5f75386b803d.webp. A young man in a black cap, low-key, dark background.
- **Q Industrial card:** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/9340eb08-877d-4d08-91fb-b70754541d98.webp. An abstract motion-blurred monochrome fashion shot with a sharp white angular shape.
- **Portrait card:** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/addecc7d-666f-4342-8290-ed7f7cbbffd6.webp. A side profile in a white t-shirt on a blue-grey gradient.
- **Avatars:** eight round black-and-white headshots, 240 × 240.
  - Avatar 1: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/300f41b1-3de5-4153-afde-06e15e753ad0.webp
  - Avatar 2: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/bfff4cdf-4fda-4491-ada6-62f3b6236492.webp
  - Avatar 3: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/943b121e-fe72-479f-93ae-aa8cd1650f69.webp
  - Avatar 4: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/c673306f-2b81-4c3d-a7d2-3df61d481abb.webp
  - Avatar 5: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/2e4fcf11-d0fc-4f31-8f7a-dfe751777141.webp
  - Avatar 6: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/ab458fcd-4c2c-426f-8213-21cc3c7274be.webp
  - Avatar 7: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/c1fcd833-5ac9-41e9-9352-fead7e64fa24.webp
  - Avatar 8: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/4c2b3307-e555-4633-949c-efd3b7e09d82.webp
- **Fonts:** Inter Tight (variable, 100–900) for UI and body. Archivo with a variable width axis (wdth 62–125) for the display title, the brand plate and the bar labels. Both are self-hosted latin woff2 (Google Fonts: https://fonts.googleapis.com/css2?family=Inter+Tight:wght@100..900&family=Archivo:wdth,wght@62..125,100..900&display=swap).

## Scale

- **Units:** everything is drawn on a 1440-px artboard. `u = min(100vw / 1440, 1.333px)`, and every size below is in u.
- **Hero:** 938u tall. The black bar is 111u. The statement section uses 170u top and 230u bottom padding. The trust section ends with 150u padding. The full page is about 2598u.

## Colours and type

- **Colours:**
  - hero paper #dadada, ink #111
  - lower sections pure black #000
  - text #f4f4f4
  - statement grey #6f6f6f filling to #f4f4f4
  - hairlines white at 14–28 %
- **"PURE DESIGN":** Archivo at width 104 %, weight 640, 90u, line-height 0.86, tracking −0.06em.
- **UI:** Inter Tight, 13–15u, weight 500.

## Hero (1440 × 938u)

- **Photo:** placed at left 338u, top −86u, 764 × 1024u, object-fit cover. The left and right edges are masked to transparent over 6 %, so it melts into the paper. The man's head top sits about 85u from the top, and his back is cut off by the hero's bottom edge.
- **Nav:** at (57, 61). A white segmented pill, 48u tall, with Home (active, on a black sliding pill), Studio, Works and Blog. The black pill slides to the hovered link.
- **Top right:**
  - date "Sunday / 17.06 – 27 June 2026" at (1038, 70)
  - a black "Contact Us ↗" button, 144 × 46u, at (1237, 63)
- **Title:** "PURE / DESIGN" at (57, 246), with "(’25)" at (339, 272).
- **About:** "● (ABOUT)" at y 458, then two lines of 14u copy, "Building stunning website that every brand deserves to be seen.", then a black "Book A Call ↗" button at y 584.
- **Stats frame:** at (57, 693), 341 × 208u, light grey #cdcdcd.
  - A dark card: "400+ / Trusted Partner", six tiny fictional partner marks (Halcyon, Ostra, Fenwick, Monolo, Kitefly, Arbor, each with a simple glyph), and a white "Book a call ↗" bar.
  - A photo card (cap photo) with "Studio Feed · 05/06" and a hairline at the top, and "230+ / Projects successfully launched worldwide" bottom right.
- **Right column:**
  - a frosted "True Growth" pill with a black check disc at (1216, 258)
  - "We’re available / ● for you", right-aligned, at y 442
  - "Out Now / Q Industrial / [2025]" with a 196u-tall image card (Q Industrial image, scaled 1.55 from 62 % 45 %), a frosted round arrow button and a progress line (white at 35 % with a white fill)
- **Brand plate:** a dark glass plate over the man's back at (532, 444), 364 × 73u, with a two-part triangular mark, "ORVANTE" in wide Archivo 25u, and a two-line menu icon.
- **Logos:** a row of fictional white wordmarks, "Lumon · Paperfold · Northwind", at y 864 across the jacket.

## Bar and statement

- **Bar:** black, 111u, with a bottom hairline. "EST 2019" on the left (the year in grey), "SCROLL DOWN" with a white round arrow in the middle, and "LIVE IN DETAILS" (grey) on the right. Wide Archivo, 14u.
- **Statement:** centred, 830u wide, 52u, line-height 1.33, tracking −0.028em, five lines: "We believe the strongest brands are / built through strategy, not just / aesthetics. Every campaign is designed / to capture attention, inspire action, and / create lasting business growth."
  - Every word is its own span. As the section scrolls through the viewport, the words fill from grey #6f6f6f to white in reading order, with a 3-word soft edge.
- **Sub-line:** two lines, 23u, 150u below: "Performance-driven marketing, from / strategy to execution. *Built for growing brands.*" (the last sentence in grey).

## Trust panel

- **Panel:** 1302 × 429u, centred, with a 1px border (white at 28 %) and a 14u radius.
- **Left:** "Trusted by / Hundreds of / Growing / Businesses", 55u, weight 500, plus a three-line 14.5u paragraph. Two frosted glass icon tiles (88u, 12u radius, backdrop blur) overlap the heading: an asterisk tile top right of line 1, and a four-dot tile over "Businesses".
- **Cards:** 326u tall, 8u radius.
  - Avatar card, light grey #d6d6d6, 293u: eight round 48u avatars in a 4 × 2 grid, "56M+" at 43u and "Global Collaborations".
  - Awards card, #262626, 298u: "10+ / Industry Awards", an SVG laurel badge "BEST GROWTH PARTNER 2026" and a two-line note.
  - Portrait card, 200u, cut off by the panel's right edge.

## Motion

- **Load (Web Animations):**
  - The title lines rise out of their masks, 1 s, staggered 110 ms.
  - The photo rises 40px, un-blurs and fades in over 1.3 s.
  - The nav drops in.
  - Every other hero element rises 14px and fades in, staggered 55 ms.
  - The Q Industrial progress line draws in.
  - "400+" and "230+" count up over 1.4 s.
- **Scroll:**
  - The hero photo drifts at 0.12× scroll.
  - The statement fills grey → white.
  - When the trust panel enters, "56M+" and "10+" count up and the avatars pop in (scale 0.4 → 1, staggered).
- **Hover:**
  - Nav pill slide.
  - Buttons lift 1px.
  - Trust cards lift 6u.
  - The Q Industrial image zooms and its arrow rotates 45°.
- **Recorder (?rec=1):** the whole page is captured in one frame, so the scroll-driven parts run on time instead.
  - Statement fill: 1.3–4.2 s.
  - Trust counters and avatars: 3.5–5.2 s.
  - Awards card lift: 5.3 s.
  - The photo drifts slowly throughout.
- **Reduced motion:** no transitions; everything is shown filled and counted.

## Phone (≤ 760px)

- **Unit:** `u = 100vw / 390`.
- **Layout:** one column.
  - The nav pill is on the left and "Contact Us" becomes a 40u square arrow button.
  - The title, (ABOUT) copy and Book A Call come next, then the full-width photo (470u) with the brand plate and logos over it.
  - Then True Growth, the stats frame (two columns) and Out Now.
- **Statement:** 28u.
- **Trust panel:** stacks its heading, paragraph and cards, and the second glass tile is hidden.
- **Overflow:** no sideways scroll.

## Acceptance check (1440 wide)

- **Hero:** the hero matches the reference layout, with the man centred and the ORVANTE plate on his back.
- **Statement:** the words fill to white as you scroll.
- **Trust panel:** the counters and avatars animate in when it appears.
- **Content:** no real brands or logos.
