<!-- Facet Glass · 3D · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261026_045953_479b439c-09fa-4701-ba5e-4ff534c67858.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=facet-glass-hero -->

# Prompt: Facet "Designed in glass" hero

Build a one-screen **WebGL hero for a fictional real-time material studio, Facet**. The page is a dark website shattered into **thick smoked-glass shards** floating on black. The content is printed on the shards. The whole slab tilts toward the cursor, the shard under the pointer lifts and tips, and "Read paper →" shatters the page to reveal a second view. Use plain HTML, CSS and JS with three.js 0.169.0 from jsDelivr (import map, plus `RoomEnvironment` from the addons). No build step and no images: all content is drawn in code. Font: Inter (variable woff2, 400–600).

## Scene and scale

- **Background:** #050507.
- **Camera:** perspective, fov 30°, placed so that 1 world unit = 1 CSS px at z = 0.
- **Renderer:** ACES filmic tone mapping, DPR capped at 2.
- **Environment:** PMREM RoomEnvironment, `environmentIntensity` .42, plus a soft white-blue key light from the top-left.
- **Page block:** centred, with side margins of 5.5 % of the width and top/bottom margins of 8.5 % of the height (16 px on phones).
  - The block is a **nav slab** (10.8 % of the block height) above a **14 px gap** and a **shard panel** (the rest).
  - Layout scale: S = blockWidth / 1730.

## The glass

- **Construction:** every piece is an `ExtrudeGeometry` of a rounded polygon.
  - Corner radius 20·S, depth 13·S, bevel 2.6·S with 3 segments.
  - The outline is inset by half the gap, so pieces sit 14·S apart.
- **Material:** MeshPhysicalMaterial.
  - color #17171b, roughness .36, clearcoat .7, clearcoatRoughness .12, specularIntensity .7.
  - Iridescence .55 (IOR 1.3, thickness 250–650 nm), rising to 1.0 together with envMapIntensity 1 → 1.9 while a piece is hovered.
  - The result: dark charcoal faces, soft studio gradients, thin bright rims, and a green/violet sheen when a piece tips toward the light.
- **Cursor glow:** a soft lavender emission injected into the glass shader via `onBeforeCompile`: `vec3(.42,.37,.62) · .16 · exp(−1.6·(d/300S)²)` around the pointer's world position. It fades in and out with the pointer.

## The cut pattern (live)

- **Cells:** five cells measured from the reference, in panel-normalised coordinates (x right, y down).
  - Edge points: top .22, .515, .84; bottom .34, .865.
  - Inner junctions: J0 (.385,.72), J1 (.48,.62), J2 (.716,.49).
  - A = TL·tAB·J0·bAD·BL (hero), B = tAB·tBC·J1·J0, C = tBC·tCE·J2·J1, D = J0·J1·J2·bDE·bAD, E = tCE·TR·BR·bDE·J2.
- **Drift:** every point drifts on its own slow sine (x ±.03; junctions also y ±.05; periods ≈10–20 s).
- **Cursor push:** points within .6 of the pointer are pushed away by up to .05, so the cell under the cursor grows.
- **Rebuild:** geometry is rebuilt about 45×/s.
- **Portrait screens:** the pattern is transposed so the hero cell sits on top.

## Content printed on the glass

- **Page image:** one canvas (DPR ≥1.5) of the whole panel. Each cell carries a `ShapeGeometry` of its own outline just above its top face, with UVs mapped to its original page position. A lifted or flying shard takes its slice of the text with it, and the seams read like refraction.
- **Panel content:**
  - Eyebrow "REAL-TIME MATERIAL STUDIO": 11·S px, tracking .2em, 38 % white, at 13.5 % of the height.
  - Headline "Designed / in glass.": Inter 500, size min(7.8 % of panel width, 20 % of height), tracking −.045em, leading .97, a #dcdce0→#bdbdc3 vertical gradient.
  - Two-line sub "Author dispersion, transmission, and refraction in the browser. Live / previews, real materials.": 55 % white.
  - "Open studio" light pill (116×40·S, radius 6). It **turns green #36d67e on hover**.
  - "Read paper →" link (underlines on hover).
  - "© Facet Lab" bottom-left and "KHR_materials_dispersion" bottom-right, 11·S px at 34 % white.
- **Nav slab:** square mark + "Facet", links "Studio · Materials · Pricing" (60 % white, brighten on hover), "Sign in" right.
- **Text layer:** a transparent DOM copy of all text is mapped onto the tilted panel with a homography (`matrix3d` from the panel's four projected corners). Text is selectable (blue selection box) and buttons and links are real hit areas.

## Interaction

- **Global tilt:** the block rotates as if pressed at the pointer: rotateY = x·7° − 1.2°, rotateX = −y·5.5° + .8°. It is smoothed with a 0.3 s exponential and eases back when the pointer leaves the window.
- **Hover:** a raycast picks the piece under the pointer (cells and nav). It springs (k 170, c 19) up 50·S toward the camera (nav 32·S) and tips up to ±.24 rad, with the edge nearest the pointer dipping away. Neighbours stay put.
- **Shatter (click "Read paper →"):**
  - Every piece, nav first, flies off in 0.72 s with ease-in cubic, with a small stagger per piece.
  - Each piece gets an outward and downward velocity plus 420–800·S toward the camera, gravity, and 2.0–3.6 rad of tumble about a random axis. The printed text rides along.
  - From 0.28 s the definitions view fades in on black over 0.4 s. Its type scales with viewport width, measured from the reference:
    - The column starts at 32.4 % W and is 33.9 % W wide. The title baseline sits at 35.9 % H.
    - Title "Real-time glass, in five terms.": Inter 650, 1.36 vw, tracking −.022em, white.
    - Five paragraphs (Iridescence, Index of refraction, Dispersion, Transmission, Roughness): .73 vw on a 1.72 line height, 60 % white, with the bold term in white + an em dash. Gaps are 1.05 vw.
  - The **"← Back" sliver** is a thin dark smoked-glass shard, the same material as the cells with iridescence .35 and no cursor glow.
    - Outline: viewport fractions (.147,.243) (.252,.169) (.287,.277) (.151,.258), with rounded corners, an 11·k extrusion and a bright bevel (k = W/1918).
    - It leans in 3D: rotateY −.16 (left end further away) and rotateX .08. It has a slow idle wobble (±.03–.04 rad at ≈1 Hz) and tips up to .14 rad toward the pointer on hover.
    - "← Back" is .66 vw Inter 500, white, centred at (.219 W, .238 H). It turns lavender #b9abff on hover.
    - It grows in from .3 s after the click and shrinks away on Back.
- **Back:** the definitions fade out in 0.25 s and the sliver shrinks away. The pieces fly back along the same paths in 0.72 s with ease-out-back (a slight overshoot), nav first, then a 30 ms stagger.
- **Load:** the page enters with the same fly-in.
- **Reduced motion / no WebGL:** a static styled HTML version.

## Acceptance check (1440×960)

- The dark glass shards and nav slab look thick, with bright hairline rims and black gaps. The headline is printed across the cuts.
- Moving the mouse tilts the whole slab, and the hovered shard lifts, tips, gains a sheen and glows lavender under the cursor.
- The cut lines slowly breathe.
- "Read paper →" shatters everything, with the text flying on the shards, into the five-terms view. "← Back" reassembles it.
- **Content:** no real brands or logos.
