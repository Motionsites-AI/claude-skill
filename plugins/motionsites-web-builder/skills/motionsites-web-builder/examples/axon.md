<!-- AXON · Portfolio · free MotionSites prompt -->
<!-- Preview: https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/6166d700-54bd-4de5-b095-b4dd3961f891.png · Source: https://motionsites.ai/?prompt=axon -->

# AXON — Motion research hub: recreation brief

Build a single full-screen dark page: a GPU particle cloud shaped like a sculpted logo form fills the viewport, stirred by the cursor through a fluid simulation, with a thin monospace UI layer on top (brand, tag chips, a scrollable column of video cards on the left, a text column on the right, a round counter top-right). Pure black background. No scrolling of the page itself.

## 1. Media

| Use | URL | Notes |
| --- | --- | --- |
| Card 1 video | https://pub-86dc5b5484314368ac5436a674b0d919.r2.dev/aaaf/oraciteslArea.mp4 | "Lattices / zone" |
| Card 2 video | https://pub-86dc5b5484314368ac5436a674b0d919.r2.dev/aaaf/facet-glass-hero.mp4 | "Prism / shell" |
| Card 3 video | https://pub-86dc5b5484314368ac5436a674b0d919.r2.dev/aaaf/stellarmind-hero.mp4 | "Nebular / loop" |
| Card 4 video | https://pub-86dc5b5484314368ac5436a674b0d919.r2.dev/aaaf/thedropthroughArea.mp4 | "Fall / forward" |
| Particle sprite matcap | 64×64 PNG, a soft grey sphere shading (a generic matcap). Any soft spherical matcap works; embed as a data URI. | Sampled per point sprite |
| three.js | https://cdn.jsdelivr.net/npm/three@0.150.1/build/three.min.js | UMD build, global `THREE` |

All videos: `autoplay muted loop playsinline preload="metadata"`, `object-fit: cover`.

## 2. Fonts

System monospace stack, no web font: `"SF Mono", "Menlo", "Consolas", "Liberation Mono", monospace`. All UI text is uppercase, 13 px, line-height 1.35, letter-spacing 0.02em.

## 3. Head and tokens

- `<title>AXON..</title>`
- `<meta name="description" content="AXON is a motion research studio: an open logbook of real-time rendering studies in particles, fluids and signed surfaces.">`
- Viewport meta, charset UTF-8.

```
--accent: #aa88ff   (headings, chip highlight)
--text:   #dddddd
--muted:  #8a8a8a
--chip:   #1c1c1c
--line:   #2a2a2a
body background #000, html/body height 100%, overflow hidden
```

## 4. Layers

1. `canvas#bg` fixed, full viewport, z-index 0. WebGL renderer, pixel ratio min(devicePixelRatio, 2), clear colour black.
2. `.ui` fixed inset 0, z-index 1, `pointer-events: none` (links and the card list re-enable pointer events). Text blocks use `mix-blend-mode: plus-lighter` so they glow over the particles; the video cards do not blend.

## 5. UI DOM, in order, desktop measurements

**Brand** `.brand` absolute top 24 left 24, flex row gap 14.
- A 40×40 SVG mark: 18.5 px radius circle stroke white 1.6, plus a white 8-point star polygon inside.
- Name "AXON" 20 px white; subtitle "Motion research" 11 px muted, margin-top 2.

**Counter** `.counter` absolute top 24 right 24: 44×44 circle, 1 px `--line` border, background #0a0a0a, text "07" 14 px white centred.

**Tags** `.tags` absolute top 120 left 24 width 320, flex wrap gap 6. Chips: background `--chip`, padding 5px 9px, 11 px, colour #cfcfcf. First chip "All" is active: background #e6e6e6, colour #000. Chips in order: All, Light, Physics, Fluids, Grid, Audio, Volumes, Particles, Capture, Render.

**Card list** `.list` absolute top 250 left 24 bottom 0 width 320, vertical scroll, scrollbar hidden. Each `.card`: padding 18px 0, 1 px top border `--line`.
- `.thumb` height 160, radius 2, background #0a0a0a, overflow hidden, video cover-fitted.
- `.meta` flex space-between gap 16, margin-top 10, 12 px. Left column white, right column muted and right-aligned; both two lines (`white-space: pre-line`).
- Cards: Lattices / zone · Ambient light / study — Prism / shell · Dispersion hero / render — Nebular / loop · Procedural hero / sequence — Fall / forward · Dolly track / study.

**Text column** `.about` absolute right 90, top 50% translateY(-50%), width 380. Blocks separated by 2.2em. Headings `h2` 13 px accent colour, margin-bottom 1em. Paragraphs justified, margin-bottom 1em. Lists `list-style: inside`. Links block-level, underlined, margin 4px 0, hover opacity .7 over 300 ms.

```
[info]
Studies are published as they are built and may not run on every device.

[aims]
An open logbook of real-time rendering research: surfaces, fluids, fields, and the little tools we build to shape them.
It is here to keep the work in view and to give each new project a place to grow.

[exploring]
• Signed surfaces  • Cursor turbulence  • Compute passes  • Type in 3D space

[connect]
Index -> AXON              (href "#")
Mail -> hello@axonlab.dev  (mailto)
```

## 6. Responsive

- ≤1100 px: text column right 24, width 320.
- ≤760 px: hide `.list` and `.tags`; text column becomes left 24 / right 24 / bottom 24, no transform, paragraphs left-aligned.

## 7. Particle system (the hero)

**Scene.** Perspective camera FOV 30, near 0.1, far 1000, base position (-1.17, 0, 6) looking at the origin. A group holds the points at position (0.343, 0.16, -1), rotation in degrees (-28.4, 390, 4.92), scale (5, 5, 6).

**Gaze camera.** Each frame the target position is base + (mouse.x mapped 0..width → -1..1) × (-1) on x and (mouse.y mapped 0..height → -1..1) × 2 on y; the camera lerps to it at 0.05 and looks at the origin.

**Count.** 262,144 points on desktop (512×512 position texture), 16,384 on mobile. Each point has a `random` vec4 attribute in 0..1 and looks up its position from a float RGBA texture using `position.xy` as UV.

**Simulation (ping-pong float render target, one fullscreen pass per frame).** Inputs: current position texture, origin texture (initial random positions uniform in [-1,1]³), random attribs, `time` (s), `HZ` (= dt × 60), fluid velocity texture, fluid density texture, projection matrix (camera projection × inverse camera world), model matrix (group world), normal matrix (camera world). Per particle:

```
if (length(pos) > 0.7) pos /= 2.0;
pos += curlNoise(pos * 0.1 + time * 0.05) * 1.0 * 0.0002 * HZ;        // uCurlNoiseScale 1, uCurlTimeScale 0.5, uCurlNoiseSpeed 1
vec3 gradient = sdfNormal(pos);   // central differences, step 0.001
float sdf = sdfShape(pos);
pos += cross(normalize(pos), normalize(gradient)) * 0.0005;           // swirl along the surface
pos += -gradient * sdf * 0.5;                                          // pull onto the surface
pos += (origin - pos) * 0.0002 * HZ;                                   // spring back to origin
// mouse fluid
vec2 screenUV = project(model * pos) → 0..1
vec3 flow = vec3(texture(fluidVelocity, screenUV).xy, 0.0) rotated by the camera's world rotation
pos += flow * 0.0001 * HZ * 0.4 * texture(fluidDensity, screenUV).r;  // uMouseStrength 0.4
```

**Shape.** A smooth, organic sculpted form about 0.7 units across: a bent, hollow ring/torus-like mass with one large opening and softer lobes, defined as a signed distance function. (The original uses a small sine-network SDF; any closed, smooth, slightly twisted ring with one big hole gives the same read. Before evaluating, mirror the depth axis: `p.z = sqrt(p.z*p.z + 0.0215) - sqrt(0.012)` so the form is symmetric front/back with a soft seam, and rotate `p` by the quaternion (0.5, 0.5, 0.5, 0.5). Outside radius 0.8 return `length(p) - 0.7`.)

**Curl noise.** Analytic curl of three sine-sum potentials (Bridson-style), normalized.

**Point rendering.** Additive blending, transparent, depth test on, depth write off. Vertex: `pos *= mix(1.0, 1.5, pow(random.y, 150.0))`; `scale = smoothstep(3, 15, distToCamera) * mix(0.5, 1.0, random.z)`; `gl_PointSize = 0.04 * DPR * 2.0 * scale * (1000 / viewDistance)`. Fragment: discard outside a circle; discard when scale < 0.1; base colour `mix(0.0, 0.2, random.x)` grey, mixed to lavender (0.6, 0.45, 1.0) by `pow(random.z, 100)`; sparkle `0.5 + (0.4 + sin(time*4 + random.y*20)) * pow(random.z, 10) * 2.5`; matcap sampled with the sprite UV rotated by `sin(time + random.z*20)*0.5 + 1`, blended soft-light 0.8 then overlay 0.2; alpha 1.

## 8. Fluid simulation (drives the cursor interaction)

Classic GPU fluid (curl → vorticity → divergence → pressure → gradient subtract → advect velocity → advect density → display), half-float ping-pong targets.

| Setting | Value |
| --- | --- |
| Sim resolution | 256 × 256 |
| Dye resolution | 512 × 512 |
| Velocity dissipation | 0.98 |
| Density dissipation | 0.97 |
| Pressure dissipation | 0.95 |
| Pressure iterations | 5 |
| Curl | 30 |
| dt | 1/60 |

**Mouse input each frame.** `len` = cursor distance moved since last frame (px). Splat radius = clamp-map(len, 0..5 → 0..60) × 0.6 (× 0.8 on mobile); force multiplier = clamp-map(len, 0..15 → 0..10). When len > 0.01: splat a line from the previous point to the current with colour (dx × mult, -dy × mult, 1) into velocity (additive) and white into density, radius/200 in UV units, aspect-corrected. If more than 50 ms passed since the last splat, the line starts at the current point.

The density texture, rendered to a viewport-sized target with alpha = max(r, g, b), is the mask that limits the push to where the cursor has been.

## 9. Interactions and motion summary

- Cursor move anywhere: fluid splat → particles swirl and drift along the flow, then heal back onto the shape within ~1–2 s.
- Cursor move also pans the camera slightly (gaze).
- Touch: `touchstart`/`touchmove` feed the same mouse position.
- Resize: renderer, camera aspect and the fluid mask target follow the window.
- Links: hover fades to 70 % over 300 ms.
- No entrance animation; the cloud forms from random positions over the first ~3 s of simulation.

## 10. Acceptance checklist

- [ ] Black page, no scrollbars, canvas fills the viewport at any size.
- [ ] A dense white-grey particle cloud with sparse lavender points forms a hollow, twisted ring form, centred slightly right of the UI columns.
- [ ] Moving the cursor across the cloud visibly stirs it; it settles back within two seconds.
- [ ] Camera drifts a little with the cursor.
- [ ] Brand, counter, 10 chips, 4 video cards (all playing, muted), and the four text blocks with the exact copy above.
- [ ] Headings in #aa88ff; text blends additively over the particles; videos are opaque.
- [ ] Below 760 px the chips and cards hide and the text column sits at the bottom.
- [ ] No console errors; all four video URLs return 200.
