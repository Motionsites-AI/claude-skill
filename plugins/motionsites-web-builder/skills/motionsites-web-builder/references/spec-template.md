# The build spec

Quality is decided here, before any code. A gallery-grade spec reads like a precise brief from a senior designer to a developer: every visible element has real values, every asset a real URL, every motion a delay, duration and easing. Aim for 600–1,200 words for a hero and 1,200–2,500 for a multi-section page. The examples you opened in step 2 are your calibration; match their density.

## Precision rules
- **No adjective stands alone.** "Cinematic", "premium" and "glassy" must be followed by the values that produce them: blur px, alpha, gradient stops, durations.
- **Every visible element gets a full style line:** size at each breakpoint (3–5 tiers or `clamp()`), weight, line-height, tracking, colour with opacity, max-width and margins.
- **Colour:** hex/HSL tokens only, with opacity steps for hierarchy (100 / 80 / 60 / 40).
- **Motion:** per element, give the trigger, delay, duration, easing and from→to values. Write stagger formulas out (`delay = 0.3 + i*0.12s`).
- **Media:** exact URL, element and attributes, fit, focal point (`object-position`, oversize, offsets), playback mode, plus one sentence on what the footage shows, where its subject sits and where the empty zone is.
- **Logic:** algorithms in steps, with constants (lerp factor, locks in ms, thresholds) and cleanup.
- **Absolute positions are explicit** (`top: 18%; left: 6vw`). Grids are explicit (`grid-template-columns: 26% 1fr 48%`).
- **Verbatim blocks** for anything that must be exact: CSS classes, keyframes, SVG paths, the font `<link>`.

## Consistency pass (before building)
Check the spec against itself:
- every asset has a reachable URL or a declared placeholder;
- no conflicting classes or values on one element;
- every "do not" agrees with the asset list and layout;
- every font named is actually loaded;
- the page background equals the hero media's edge colour.

## Template
Fill every `{{ }}`. Write "none" rather than leaving a block blank, and delete blocks that truly don't apply.

````markdown
# {{Brand}} · {{one-line concept}}

## 0. Brief
Build {{a single full-viewport hero | an N-section landing page: Hero, …}} for **{{Brand}}**, {{what it is, for whom}}.
Aesthetic: {{3–6 words}}.
Signature idea (the ONE thing this page is remembered for): {{…}}.
Fidelity: build exactly as specified; add no sections, cards, badges, gradients or decorations not listed here.

## 1. Stack & files
{{single index.html, inline CSS/JS, CDN libs pinned (e.g. gsap@3.12.5) | React 18 + Vite + TS + Tailwind 3.4 + motion}}; icons: {{inline SVG | lucide: ArrowUpRight, Menu, X}}.

## 2. Fonts
| Role | Family | Weights/style | Used on |
|---|---|---|---|
| Display | {{…}} | {{…}} | {{H1, accent words, big numbers}} |
| Body/UI | {{…}} | {{400/500}} | {{nav, body, buttons}} |
| Labels (optional) | {{mono or body}} | {{…}} | {{eyebrows, indices, metadata}} |
Load: `{{exact Google Fonts URL}}`. Fallback stack: `{{…}}`.

## 3. Colour tokens
```css
:root{
  --bg: {{…}};      /* equals the hero media's edge colour */
  --fg: {{…}};
  --muted: {{…}};
  --line: {{…}};
  --accent: {{one hue or none}};  /* only on: {{≤3 element types}} */
}
html,body{background:var(--bg);color:var(--fg)}   /* first rule: no white flash */
```
Text hierarchy over media: {{fg 100 headline / 80 nav / 60 body / 40 labels}}.

## 4. Global utilities (verbatim)
{{material class (e.g. glass), grain, keyframes, reduced-motion block}}

## 5. Assets
| Slot | Type | URL | Element & attributes | Fit & focal point | Behaviour | Fallback |
|---|---|---|---|---|---|---|
| hero-bg | {{MP4 loop}} | `{{exact URL}}` | `<video autoplay muted loop playsinline preload="auto">` | `object-fit:cover; object-position:{{…}}` | {{native loop | rAF fade loop}} | bg colour; fade in on `loadeddata` |
Art direction: {{what the media shows, where the subject sits, where the empty zone is, dominant colours, motion speed}}.
Overlay policy: {{none | bottom fade to --bg | edge vignette}}.

## 6. Layers & root
Root: {{position, height 100vh then 100dvh, overflow}}.
z-ladder: media 0 → fades 1 → content 10 → nav 20 → menu 50 → grain 100 (pointer-events none).
Skeleton: {{e.g. flex column: nav / flex-1 stage with content pinned bottom-left / bottom strip}}.

## 7. Navbar
Container: {{…}}. Left: {{wordmark}}. Centre: {{3–5 links, style}}. Right: {{CTA, style}}.
Mobile: {{burger → full-screen menu, timing, stagger, closes on link/Esc/resize}}.

## 8. Hero content (reading order)
| Element | Copy | Tag | Font | Size (base→md→lg) | Wt | Leading | Tracking | Colour | Box/spacing | Motion |
|---|---|---|---|---|---|---|---|---|---|---|
| Eyebrow | {{≤8 words}} | span | … | … | … | … | … | … | … | … |
| H1 | {{3–8 words, line breaks marked /}} | h1 | display | {{clamp(…)}} | … | {{0.9–1.05}} | {{−0.02 to −0.05em}} | … | … | … |
| Sub | {{15–30 words}} | p | body | … | … | 1.5–1.6 | … | {{fg/60}} | {{max-width}} | … |
| Primary CTA | {{verb + object}} | a | body | … | … | … | … | … | … | … |
| Secondary | {{softer action}} | a | … | … | … | … | … | … | … | … |

## 9. Sections (repeat per section)
### {{Name}}
Background {{…}}; padding {{…}}; container {{…}}. Eyebrow · Heading · Body (each with full style lines). Grid {{…}}. Card {{radius, padding, material, inner layout}}. Media {{…}}. Reveal {{in-view config}}.

## 10. Motion table
Default easing `cubic-bezier(0.22,1,0.36,1)`.
| Element | Trigger | Delay | Duration | From → To |
|---|---|---|---|---|
The entrance completes by {{≤1.5s}}. Hovers: {{…}}. NOT animated: {{…}}.
Reduced motion: {{final state shown, no smoothing/scrub}}.

## 11. Interaction & state
State, handlers, constants, algorithm in steps, cleanup, touch fallback.

## 12. Responsive
| Element | <640 | ≥768 | ≥1024 |
|---|---|---|---|
Use 100dvh and safe-area insets; no horizontal scroll at 375px; add a short-viewport rule (max-height 720px) when the hero is dense.

## 13. Constraints & acceptance
Do not: {{…}}.
Must: {{…}}.
Acceptance (first viewport): {{one paragraph describing exactly what's visible and where}}.
````

## Add-on modules
Append the one(s) that match the brief.
- **Video hero.**
  - Loop mode: native, rAF fade loop, crossfade between clips, mouse-scrub, scroll-scrub or boomerang.
  - Focal point and oversize.
  - Overlay policy.
  - Poster image.
  - Behaviour on touch devices.
- **Cut-out / 3D showcase.**
  - Per-role transform table (centre/left/right/back: position, height %, scale, blur, opacity, z).
  - One shared transition with an animation lock.
  - Preloading.
  - Ghost mega-word behind the subject.
  - For real 3D (Three.js/GLB): camera, framing maths, lights, interaction model and loading state.
- **Editorial / mega type.**
  - Display size in vw.
  - Line-height 0.75–0.9.
  - Tracking −0.04 to −0.08em.
  - Overflow clipping.
  - Which words sit in front of or behind the media.
  - A mono micro-label system.
- **SaaS.**
  - Product mock-up anatomy (window chrome, columns, realistic rows).
  - Logo strip (opacity, edge mask).
  - Pricing (material, toggle).
- **Portfolio.**
  - The name as a display element.
  - Work grid spans.
  - Hover reveals.
  - Availability microcopy.
  - Marquee speed.
- **Scroll story.**
  - Sticky stage height.
  - Segment ranges.
  - Per-frame variables.
  - smoothstep/lerp helpers.
  - Choreography listed by scroll range.
