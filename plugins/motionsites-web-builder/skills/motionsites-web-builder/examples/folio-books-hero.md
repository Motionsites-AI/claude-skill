<!-- Bookshop · Portfolio · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261030_004358_8ba84f4d-10fa-48f5-9ef1-306e689e4734.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=folio-books-hero -->

# Prompt: Folio, 3D bookshop hero with a rising row of books

## What it is

Build a single-screen hero for a fictional independent press and bookshop, **Folio**. Use one HTML file with plain HTML and CSS plus a Three.js module (r160 from jsDelivr through an import map: `three` and `three/addons/`).

- **Page:** pure black, with a giant thin high-contrast serif wordmark "Folio" across the upper middle.
- **Books:** a long diagonal row of 32 real 3D hardcover books stands on edge, running from the bottom-right corner off the left edge, covers facing the camera at a slight angle and heavily overlapping.
- **Covers:** every book wears its own fully designed cover.
- **Wave:** books near the cursor rise in a smooth, springy wave, with neighbours tapering off. Raised books pass in front of the wordmark.
- **Smoothness:** every book has its own spring, sub-stepped each frame, so the motion stays smooth at any frame rate.

## Media: every asset URL

The covers come from two Higgsfield GPT Image 2.5 sheets (2336 × 1744 px each), 6 columns × 3 rows of 2:3 covers separated by black gutters. Load them through the Higgsfield image proxy, which sends `access-control-allow-origin: *` so they can be WebGL textures:

- **sheetA:** https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261030_003447_7862e2d0-751c-4d7c-9c8a-e682415d908f.png&w=2336&q=90
- **sheetB:** https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261030_003448_95f1eed5-2ae5-4736-a53c-f3b3f87acd3b.png&w=2336&q=90

All titles and authors are fictional. Each cover is a texture clone of its sheet:

- Trim 3px from every side to drop the gutter.
- `repeat = ((w−6)/2336, (h−6)/1744)`, `offset = ((x+3)/2336, 1 − (y+h−3)/1744)`.
- `colorSpace = SRGBColorSpace`, `anisotropy = max`.

### Sheet A cells

| # | Box x, y, w, h | Spine colour | Cover |
|---|---|---|---|
| 0 | 6, 0, 386, 575 | `#2c4f63` | THE LAST HARBOR / Elise Moreau — painted seascape with a lighthouse |
| 1 | 401, 0, 376, 575 | `#195433` | Bright Rivers / Hana Sato — green and cream abstract river |
| 2 | 787, 0, 377, 575 | `#c62420` | The Quiet Room / Lila Hart — red, black potted-plant silhouette |
| 3 | 1175, 0, 379, 575 | `#f4f3ef` | STILL LIFE / Juno Reed — white Swiss type, black vase |
| 4 | 1564, 0, 377, 575 | `#2d86cf` | The Salt Between Us / Lila Barron — blue watercolour |
| 5 | 1949, 0, 383, 575 | `#f7d547` | THE BRIGHTER SIDE / Cassia Wren — yellow with black organic shapes |
| 6 | 6, 583, 386, 573 | `#494e68` | City of Ash / Tomás Reyes — dusk skyline photo |
| 7 | 401, 583, 376, 573 | `#f2ecde` | The Weight of Tomorrow / Eliot Grant — cream with a red circle |
| 8 | 787, 583, 377, 573 | `#7893a3` | Vanishing Light / Marlowe Pierce — misty mountain lake |
| 9 | 1175, 583, 379, 573 | `#0c0b0b` | THE GLASS GARDEN / Adelaide Cross — black, white engraved flower |
| 10 | 1564, 583, 377, 573 | `#ddd0c1` | Fragments of Us / Nova Keller — collage portrait |
| 11 | 1949, 583, 383, 573 | `#013eb0` | Blue Hours / Jasper Lane — cobalt Bauhaus shapes |
| 12 | 6, 1164, 386, 578 | `#f2f1ed` | THE SILENT BELL / Kai Mori — white, black vertical lines |
| 13 | 401, 1164, 376, 578 | `#0a291c` | All That Remains / Iris Vale — dark pine forest |
| 14 | 787, 1164, 377, 578 | `#c61111` | The Red Departure / Pesse Hall — red, black bird |
| 15 | 1175, 1164, 379, 578 | `#7f7263` | A Brighter Tomorrow / Mira Lowe — sunlit coastal cliffs |
| 16 | 1564, 1164, 377, 578 | `#ae4716` | NORTH OF NOWHERE / Sam Ortega — orange desert highway |
| 17 | 1949, 1164, 383, 578 | `#021f42` | Paper Moons / Ada Finch — navy, gold moon phases |

### Sheet B cells

| # | Box x, y, w, h | Spine colour | Cover |
|---|---|---|---|
| 0 | 3, 2, 383, 574 | `#d1cd8c` | The Orchard Year / Clara Bell — pastel orchard |
| 1 | 394, 2, 381, 574 | `#000621` | SIGNAL / Theo Marsh — neon blue grid on black |
| 2 | 784, 2, 381, 574 | `#b8acd3` | Small Hours / June Park — lilac clock |
| 3 | 1172, 2, 381, 574 | `#e6bd7e` | The Cartographer's Daughter / Ines Duarte — sepia map |
| 4 | 1562, 2, 381, 574 | `#076368` | WILD SALT / Rory Quinn — teal woodcut waves |
| 5 | 1952, 2, 382, 574 | `#ad8357` | Low Tide / Mae Okafor — footprints in sand |
| 6 | 3, 586, 383, 572 | `#cfa94d` | The Long Field / Owen Hale — golden wheat field |
| 7 | 394, 586, 381, 572 | `#497f9d` | Houses of Glass / Vera Lind — modernist house photo |
| 8 | 784, 586, 381, 572 | `#02878a` | OPEN WATER / Lena Ruiz — swimmer from above |
| 9 | 1172, 586, 381, 572 | `#170402` | Nine Lanterns / Mei Tanaka — red lanterns at night |
| 10 | 1562, 586, 381, 572 | `#09150b` | The Understory / Ash Kerr — dark ferns |
| 11 | 1952, 586, 382, 572 | `#f57664` | Velvet Static / Remy Cole — pink-orange grainy gradient |
| 12 | 3, 1167, 383, 574 | `#f3f3f3` | Lessons in Gravity / Noor Haddad — falling figure on white |
| 13 | 394, 1167, 381, 574 | `#2a2929` | THE ARCHIVE / Felix Brandt — brutalist type |
| 14 | 784, 1167, 381, 574 | `#3fb1b9` | Summer, Elsewhere / Isla Grey — sunlit pool |
| 15 | 1172, 1167, 381, 574 | `#6b1405` | Ember & Bone / Kit Morrow — fire illustration |
| 16 | 1562, 1167, 381, 574 | `#ceba9f` | A Map of Quiet Things / Sol Rivera — paper collage |
| 17 | 1952, 1167, 382, 574 | `#1c565e` | Northern Lights Hotel / Hugo Berg — snowy hotel under aurora |

**Order:** books use cover index n (0 to 17 from sheet A, 18 to 35 from sheet B) in this order, front to back:

`0, 22, 5, 30, 9, 13, 26, 2, 19, 11, 33, 7, 15, 24, 4, 28, 17, 21, 1, 31, 14, 8, 25, 35, 3, 18, 10, 29, 16, 23, 6, 34`

## Fonts and colour

- **Fonts:** Google Fonts **Libre Caslon Display** 400 for the wordmark and logo, **Inter** 400 and 500 for the UI.
- **Colours:** background `#000`, text white. The logo mark is a `#b8a58a` rounded tile with a `#16120d` bar. The pill is white with black text.

## Layout (all fixed, the page never scrolls)

### Nav (z 5)

- **Box:** left 23.3vw, right 23.4vw, top 4.6vh, height 4.4vh; font `max(11px, .78vw)` Inter 500.
- **Logo:**
  - A 2.1vw × 2.4vw tile with a dark vertical bar (left 32%, 24% wide, 64% tall).
  - Next to it, "Folio" in Libre Caslon Display `max(17px, 1.55vw)`, with "independent press" in Inter `max(8px, .6vw)` at 70% under it.
- **Centre links**, 2.3vw apart, starting 11.4vw after the logo: "Books ⌄", "Authors", "Journal", "More ⌄". The chevrons are small stroked svgs, and the links sit at 88% opacity, going to 100% on hover.
- **Right side**, 2.4vw apart:
  - "Sign in".
  - A white pill "Start reading": radius .4vw, padding .55vw 1vw, lifting 1px on hover.

### Wordmark (z 1)

- **Text:** "Folio", centred, `--fs: min(46vh, 32vw)`, `font: 400 var(--fs)/1 Libre Caslon Display`, letter-spacing −.02em.
- **Position:** `top: calc(46.5vh − var(--fs)·.8)`, so its baseline sits at about 46vh.

### Link row (z 1)

- **Box:** top 51.1vh, centred, gap 2.1vw, Inter 500 `max(10px, .74vw)`.
- **Links:** "New Releases, Bestsellers, Fiction, Nonfiction, Poetry, Classics, Independent Voices, Gift Cards".

### Canvas (z 2)

A full-screen transparent WebGL canvas above the wordmark and links and below the nav.

## Three.js scene

### Renderer

- `antialias`, `alpha`, pixel ratio `min(dpr, 2)`.
- ACESFilmic tone mapping at exposure 1.05, sRGB output.

### Lighting

- **Environment:** `PMREMGenerator.fromScene(new RoomEnvironment(), .04)` with `environmentIntensity .55`.
- **Key:** DirectionalLight `#fff3e4`, 2.4, at (−4, 6, 6).
- **Rim:** `#bfd2ff`, 1.1, at (6, 3, −4).
- **Ambient:** white, .12.

### Camera

- PerspectiveCamera with fov 19.5 (40 when width < height) at (3.6, 2.15, 7.4), looking at (−1.4, .05, −.6).

### Books

- **Geometry:** one shared `BoxGeometry(1, 1.5, .2)`. Face materials in order +x, −x, +y, −y, +z, −z:
  1. **Fore-edge:** MeshStandard, roughness .9, with a 256px canvas of cream `#efe7d6` and 1px brown lines every 2px (alpha .05 to .17), horizontal.
  2. **Spine:** MeshPhysical in the cover's spine colour ×.62, roughness .55, clearcoat .3.
  3. **Top** and 4. **Bottom:** the same page texture with vertical lines.
  5. **Cover:** MeshPhysical with the cover texture, roughness .42, clearcoat .55, clearcoatRoughness .35.
  6. **Back:** spine colour ×.62, roughness .6.
- **Groups:** each book is a mesh inside a group.
  - Group position: `(1.55 + i·(−.5), −1.12, .9 + i·(−.2))` with `rotation.y = .32`, where i = 0 is the front book at the bottom right.
  - The mesh moves inside the group for the lift.

## Motion

### Pointer wave

- **Projection:** each frame, project the point (0, .1, 0) of each book mesh to screen pixels (sx, sy).
- **Influence:** with `s = max(innerWidth, innerHeight)·.085`, `influence = exp(−((sx−x)² + ((sy−y)·.55)²) / s²)`.
- **Target lift:** `.78·influence`, or 0 when the pointer has left the window or the window is blurred.

### Springs

Every book has a vertical spring and a forward spring (target `lift·.35` in local z), both with `K = 70`, `C = 12.5`.

- Integrate in 4 sub-steps per frame, with `dt` capped at .05s: `v += ((target − y)·K − v·C)·h; y += v·h`.
- `mesh.rotation.x = −v·.012`, so a book leans slightly while it moves.

### Intro

- **Books:** start at y = −3. Each one's target stays −3 until `t > .25 + (32 − i)·.035` seconds, so the row rises from the back to the front, each book springing up.
- **Wordmark:** Web Animations API, 1400ms after a 150ms delay: opacity 0 → 1, translateY(4vh) → 0, blur(14px) → 0, with `cubic-bezier(.2,.8,.2,1)`.
- **Nav:** fades down from −1.2vh at 700ms (900ms long).
- **Link row:** fades up from 1.2vh at 850ms (900ms long).

### Touch and idle

On `(pointer: coarse)`, or after 4s without pointer movement, a virtual cursor sweeps along the row with `u = (sin(t·.45) + 1)/2`, between book 29 and book 1 projected to the screen.

## Phones (≤760px)

- **Nav:** left and right 5vw, top 2.5vh. Only the logo and the pill stay.
- **Wordmark:** `--fs: 36vw` at top 14vh.
- **Link row:** wraps at top 36vh with 8vw side padding.
- **Camera:** fov 40.
