# Technique library: index

58 tested recipes in 7 files. Each recipe has what/when, the premium parameter values, a vanilla single-file implementation, a React/Framer variant where it differs meaningfully, and reduced-motion and mobile notes. Every file opens with its conventions and the shared easing tokens its code uses.

## How to choose a signature

Pick **one signature technique per page**: the single idea the page will be remembered for (a real 3D object, a scrubbed film, a giant word behind a cut-out, a pinned cinematic stage). Then add **2–4 supporting techniques** that stay quiet: an entrance (blur-rise), one material (liquid glass), one type move (a serif accent), and a reveal for the sections below. **Never stack five effects** in one viewport; if two techniques compete for the same attention (spotlight + magnet + parallax), cut one. Allow at most **one heavy** technique per page and let the media or the signature carry the motion: everything else should feel inevitable, not busy. Typical sets:
- **Cinematic video hero:** background video layer + edge-blend scrim + liquid glass + blur-rise + serif accent.
- **Product object:** 3D model hero + floating pill nav + blur-rise + count-up stats.
- **Editorial portfolio:** giant display type + split-text entrance + magnetic hover + scroll-linked word reveal + stacking cards.

## Techniques

| Technique | File | Use it when | Cost |
|---|---|---|---|
| Cinematic background video layer (autoplay, HLS, settle-in) | video-and-media.md | Footage carries the mood; the default foundation of a video hero | medium |
| Seamless video loop with rAF opacity fades | video-and-media.md | A looping clip shows a hard cut or mismatched first/last frame | light |
| Background-video framing & art direction | video-and-media.md | The clip's subject collides with the copy or crops badly on phones | light |
| Edge-blend scrims & text protection | video-and-media.md | Copy needs contrast over footage, or the hero must melt into the next section | light |
| Progressive bottom blur | video-and-media.md | Bottom-anchored titles over footage whose colours must stay untouched | medium |
| Cursor-scrubbed video (delta · split dual) | video-and-media.md | A turntable or head-turn clip should feel like a live 3D object (desktop) | medium |
| Scroll-scrubbed video with canvas frame cache | video-and-media.md | Scrolling should drive a transformation clip behind sparse copy | heavy |
| Boomerang (ping-pong) video loop | video-and-media.md | A non-looping clip (push-in, bloom, smoke) must loop seamlessly; pre-render it (runtime capture is heavy) | light |
| Crossfading multi-video scene switcher | video-and-media.md | Visitors pick an atmosphere or location from 3–5 moods | heavy |
| Liquid-glass surface | surfaces-and-buttons.md | UI floats over moving footage: nav, chips, cards, secondary CTAs | light |
| Frosted glass UI kit (chips, badge, numbered panel, contact card) | surfaces-and-buttons.md | Text must sit *on* glass over video and stay legible | light |
| Premium button finishes (liquid metal, halo, jewel) | surfaces-and-buttons.md | The CTA itself should feel machined or glow on a dark hero | light |
| Text-roll button with rotating arrow chip | surfaces-and-buttons.md | A studio or agency CTA needs a tactile hover | light |
| Sliding-fill buttons (+ hard offset shadow) | surfaces-and-buttons.md | Editorial or playful pages want a colour-wipe hover | light |
| Animated gradient border ring | surfaces-and-buttons.md | One CTA must pull the eye without changing the layout | light |
| Media card hover (icon-to-label pill, zoom, veil) | surfaces-and-buttons.md | Case-study and work grids | light |
| Texture overlays (grain, noise type, halftone, dot grid) | surfaces-and-buttons.md | Flat colour, gradients or video banding look too digital | light |
| Staggered blur-rise load choreography | type-and-text-motion.md | Every hero entrance (the default) | light |
| Fail-safe entrance system with a motion vocabulary | type-and-text-motion.md | Rich single-file choreography that must never leave a blank page | light |
| Word-by-word blur-in headline | type-and-text-motion.md | A big italic-serif headline over video should "exhale" in | light |
| Split-text entrances (masked lines/words, char cascade) | type-and-text-motion.md | Giant display words or stacked statements rising out of a slot | light |
| Serif-italic accent words | type-and-text-motion.md | Almost any headline with a natural key phrase | light |
| Gradient-clipped text (metallic, shine sweep) | type-and-text-motion.md | Name-as-hero metal type, or one "magic" word in a headline | light |
| Scramble / decode text | type-and-text-motion.md | AI, tech or sci-fi brands with monospace type | light |
| Typewriter with zero-reflow caret + depth-of-field lead-in | type-and-text-motion.md | An assistant/persona voice or a typed contact headline | light |
| Rotating word slot | type-and-text-motion.md | One word in a sentence should cycle (roles, verbs, places) | light |
| Scroll-linked word/char opacity reveal | type-and-text-motion.md | A manifesto or About paragraph read at scroll pace | medium |
| Giant display type as image (ghost word, wordmark, watermark, scattered) | type-and-text-motion.md | A word should be architecture: behind a cut-out, edge-to-edge, or as a backdrop | light |
| Geometric SVG wordmark assembly | type-and-text-motion.md | An institution or studio header with a constructed mark | light |
| Count-up stats & counter preloader | type-and-text-motion.md | Proof numbers, or a portfolio intro loader | light |
| Depth carousel with role slots + colour crossfade | depth-and-interaction.md | 3–6 products or characters, each with its own colour | medium |
| Magnetic hover | depth-and-interaction.md | A hero subject or primary CTA should feel weighted and alive | light |
| Pointer parallax depth layers | depth-and-interaction.md | A layered still (cut-outs over a backdrop) needs depth | light |
| Cursor-following spotlight reveal mask | depth-and-interaction.md | Two aligned images where the hidden one is the point (x-ray, night, render) | medium |
| Cursor image trail | depth-and-interaction.md | A closing CTA block should spray portfolio thumbnails | medium |
| Exclusion-blend overlay UI & custom cursor | depth-and-interaction.md | Fixed UI must stay legible as the page goes video → black → white | light |
| Orbit rings with counter-rotating avatars | depth-and-interaction.md | A community, talent network or integrations visual | medium |
| Sand-dissolve image transition + auto-cycling index | depth-and-interaction.md | Cycling collection or chapter images with an archival feel | heavy |
| Viewport-triggered staggered reveal (+ corner decor) | scroll.md | Every section below the hero | light |
| Sticky cinematic stage with CSS-variable choreography | scroll.md | Layered photography tells a story across one long pinned scroll | heavy |
| Panel slide-over + viewport-scaled scattered gallery + blend outro | scroll.md | Fashion or archive pages with many tall images | medium |
| Pinned heading with counter-drifting parallax columns | scroll.md | A gallery "playground" orbiting a pinned title | medium |
| Sticky stacking cards that scale down | scroll.md | 3–5 case studies or process steps | medium |
| Scroll-linked opposing marquee rows | scroll.md | A wall of work right after a portfolio hero | medium |
| 3D tilted text crawl (spring-smoothed) | scroll.md | A manifesto paragraph over video should feel like a film opening | medium |
| Hero composition patterns | layout-and-ui.md | Deciding where copy sits over a full-bleed visual | light |
| Viewport-locked single-frame hero | layout-and-ui.md | A poster hero that must look identical on every screen size | light |
| Floating pill navigation | layout-and-ui.md | The nav for most premium heroes (glass, frosted, white, dock, editorial) | light |
| Expanding glass capsule menu | layout-and-ui.md | Minimal heroes where a full link row would be noise | light |
| Mobile menu (burger morph, overlay / drawer / bottom sheet) | layout-and-ui.md | Every page with navigation, below 768–1024 px | light |
| Overlapping avatar trust cluster | layout-and-ui.md | Compact social proof above a SaaS or AI headline | light |
| Selectable chip group with spring check | layout-and-ui.md | Contact, enquiry or onboarding forms that should feel conversational | light |
| In-page product UI mockup | layout-and-ui.md | SaaS, dev tools or dashboards, instead of a screenshot | light |
| Desktop grid → mobile scroll-snap rail | layout-and-ui.md | 3–4 large cards (pricing, plans, features) | light |
| Seamless infinite marquee (logos, images, giant text) | layout-and-ui.md | A logo strip, image strip or giant text band | light |
| Infinite looping card slider | layout-and-ui.md | Locations, testimonials or case studies in a carousel | light |
| Real 3D model hero (Three.js + GLB) | 3d-and-webgl.md | The object is the story and you have (or can generate) a GLB | heavy |
| Animated shader backdrop (swirl, chroma blob, fluted glass) | 3d-and-webgl.md | A light agency hero with a living, refractive background | heavy |

**Cost** is the runtime weight on a mid-range phone: *light* = CSS or a little JS; *medium* = per-frame work, filters or extra media; *heavy* = WebGL, large frame caches, several videos or SVG filters on bitmaps. Every recipe already handles `prefers-reduced-motion` and touch; keep those branches when you adapt them.
