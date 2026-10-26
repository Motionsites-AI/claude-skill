# Craft: the taste rules

These are the recurring decisions that separate gallery-grade pages from average AI output. They are defaults, not laws. Break one only on purpose, and say why in the spec.

## Composition
- **One idea per first screen.** Mark + nav + one headline + one sub + 1–2 CTAs + one media plane, plus at most one quiet strip (logos, stats or socials). Supporting material goes below the fold. No cards, stat grids or icon stacks in the first viewport unless they *are* the concept.
- **The media carries the design and the UI stays quiet.** 3–5 nav links at 12–15px, pill buttons, sparse text. Often the only "graphic" is the footage.
- **Anchor somewhere specific.** Choose one of:
  - **centred stack:** badge → H1 → sub → CTA;
  - **bottom-anchored:** headline bottom-left, a secondary element bottom-right, with a flex spacer above;
  - **left column:** vertically centred;
  - **editorial four corners:** labels in the corners around a big headline.

  Centred is the safe default, not the best one.
- **Text and subject never collide.** The subject takes the centre or right third and the text takes the other side or the empty band. Move the media to make room (`object-position`, oversize 110–120%, translate) before shrinking the text.
- **Negative space is real:**
  - sub max-width 28–42rem;
  - side blocks 240–320px wide;
  - bottom padding 40–80px on desktop;
  - gutters 20–24px on mobile, 48–64px on desktop.
- **Depth comes from layering, not decoration:**
  - a giant ghost word behind a cut-out subject;
  - a cut-out in front of the headline;
  - a foreground frame over video;
  - a spotlight mask revealing a second aligned image.
- **Inset-frame variant:** the hero sits in `padding: 16–24px` with a 24–40px-radius media container, a calm, expensive look.

## Typography
**Pairing archetypes** (pick one):
1. **Editorial serif display + neutral grotesk.** A high-contrast serif (often italic) for the headline, or just for 1–3 accent words inside a sans headline. Set the accent words in a muted colour, not a brighter one.
2. **Single grotesk system.** Headline at weight 400–500, never bold, with tight tracking; size and space do all the work.
3. **Heavy condensed display for mega words:** uppercase, 14–28vw, with a calm body face.
4. **Mono or dot-matrix** for tech personality, or as a micro-label system: 10–12px, uppercase, +0.15–0.3em tracking, 40–60% opacity, for indices (`01 / 05`), eyebrows and metadata.

| | Display / H1 | Mega type | Body | Labels |
|---|---|---|---|---|
| Size | 72–96px desktop, 36–48px mobile (`clamp()`) | 14–28vw | 14–18px | 10–13px |
| Line-height | 0.9–1.05 (0.95 is the sweet spot) | 0.75–0.88 | 1.5–1.6 | 1–1.3 |
| Tracking | −0.02 to −0.05em | −0.04 to −0.08em | 0 to −0.01em | +0.15 to +0.3em |
| Weight | 400–500 (300 for big numerals) | 800–900 | 300–400 | 500–600 |

- **Scale contrast does the work:** the H1 is 5–6× the body size.
- **Break headlines by hand** into 2–3 lines. Stop bad wraps on desktop (`white-space: nowrap` per line) and let the lines flow on mobile.
- **Gradient text is rare and controlled:** a subtle vertical silver on display type, or nothing at all.
- **Wordmarks** are tight-tracked text with a superscript ®/™, or a small custom inline-SVG mark. Never a generic icon next to a bold word.
- **At most 2 families,** plus an optional mono for labels. Load only the weights you use.

## Colour
- **Palette:** 1 background, 1 foreground, 1–2 greys, and at most 1 accent. Use the accent on no more than 3 element types (CTA fill, a dot, a glyph). Monochrome plus media is the most common winning palette.
- **Hierarchy comes from opacity, not new colours.** Over media, step the text through fg 100 → 80 → 60 → 40. Borders are 10–20% fg.
- **The page background equals the media's edge colour,** whether black footage on black, white studio on off-white, or a red backdrop on red. That's why great heroes need no overlay and never flash.
- **Use near-blacks and off-whites:**
  - dark: `#000`, `#050505`, `#0a0a0a`, `#0c0c0c`;
  - light: `#f0f0ee`, `#f7f5f0`, `#fcfcfc`.
- **Theme the selection colour.**
- **Banned by default:** purple/indigo gradients, glow orbs, blobs, radial-gradient backgrounds as "the visual", heavy drop shadows (use soft ones only, e.g. `0 4px 14px rgba(0,0,0,.16)`).

## Surfaces and components
- **One material, reused everywhere.** Define it once (e.g. a liquid-glass or frosted class) and apply it to the nav, chips, cards and secondary buttons. No extra border classes on glass; the material provides the edge.
- **Buttons are pills.**
  - Primary is solid and inverse (white on dark, black on light): 14px, weight 500, padding 10–12px × 20–32px.
  - Secondary is glass, ghost or a text link with an icon.
  - An arrow (↗/→) often sits in a contrasting circle inside the pill and nudges 2px or rotates −45° on hover.
- **Radii stay consistent:** pills for actions, 20–40px for cards.
- **Micro-components that add credibility:**
  - an announcement badge with an inner chip ("New" + one line);
  - 3 overlapping avatars + one line of social proof;
  - 2–4 stats (big number + small muted label);
  - a logo strip at 40–50% opacity with edge fade;
  - an email pill (input + round submit).
- **Grain:** an SVG fractal-noise layer at 0.04–0.15 opacity, `pointer-events: none`, on top. It unifies video and UI and kills banding.

## Motion
- **Entrance choreography.**
  - Order: nav → eyebrow → H1 → sub → CTA → secondary strip.
  - Steps 0.1–0.2s apart, starting at 0–0.4s; the whole sequence is done by ~1.5s.
  - Base move: opacity 0→1 + translateY 20–30px, optionally blur 10px→0 or scale 0.96→1. Duration 0.6–1.1s (0.8s default).
- **Easing:**
  - entrances: `cubic-bezier(0.22,1,0.36,1)` or `cubic-bezier(0.16,1,0.3,1)`;
  - state changes: `cubic-bezier(0.4,0,0.2,1)`;
  - linear only for marquees.
- **Headline treatments** (pick one per page):
  - per-word blur-in (100ms stagger; add a word gap, since negative tracking eats spaces);
  - masked line rise from 110% inside `overflow: hidden`;
  - per-character slide (30ms stagger);
  - typewriter (35ms/char);
  - scramble.
- **Media entrance:** video fades in from 0 over ~500ms on `loadeddata`, and/or settles from scale 1.06 → 1 over 1.8s.
- **Scroll reveals:** in-view once, 10–25% threshold, y 20–40px, 0.6–0.9s, 0.1s stagger.
- **Hovers stay small:** scale ≤1.05, colour/opacity changes at 150–300ms, `:active` scale 0.97.
- **What is NOT animated, which is where the restraint shows:**
  - backgrounds and decorative layers;
  - no infinite pulsing or floating blobs;
  - no shimmer on headlines;
  - no CSS transitions on `<video>`.

  The media is the ambient motion.
- **Always add a `prefers-reduced-motion` branch** (final state, no smoothing). The rest state must be visible: if JS fails, nothing stays at opacity 0.

## Copy
- **Headline:** 3–9 words over 2–3 lines. Use a two-beat statement, a contrast pair, or a three-word staccato. Emphasise with italic serif or muted colour, never bold. Make it aspirational and specific, not salesy.
- **Sub:** 1–2 sentences, 15–30 words: a concrete benefit plus texture, in a muted colour.
- **Nav:** 3–5 links of 1–2 words. Warm labels beat defaults (Studio, Work, Journal, Inquire).
- **CTA:** 2–3 words, verb first. The primary is direct (Start, Book, Get); the secondary is softer (Watch the film, See how). Repeat the primary label in the nav.
- **Microcopy adds brand texture:** coordinates, a live local time, "Available for projects" with a pulsing dot, index numbers.
- **Never** lorem ipsum, "Your tagline here", generic "Feature 1/2/3", or emoji as icons.

## Failure modes to design against
| Failure | Guard |
|---|---|
| White flash | `html,body{background:…}` as the first CSS rule; media starts at opacity 0 and fades in on `loadeddata` |
| Visible loop seam | rAF fade loop, boomerang, crossfade, or loopable footage |
| Text unreadable over video | Footage with an empty zone; a bottom fade to bg; glass behind small UI; a soft text-shadow |
| Mobile 100vh clipping | `height:100vh; height:100dvh`; safe-area insets |
| Layout shift | Fixed-height lines for typed or rotating text; reserved media aspect ratios |
| Scrubbed-video jitter | Seek only when `!video.seeking`; lerp the target |
| Competing animations | Cancel the previous rAF; `isAnimating` locks (650–1000ms) |
| Blank page if animations fail | Rest state visible; JS forces the final state after 2 frames |
| Desktop-only interactions on touch | Disable hover/scrub effects under 1024px or on `(hover: none)` |
| Horizontal scroll | `overflow-x: clip` on the root; vw-sized mega type with nowrap and clipping |
| Menu leaves the page scrollable | Lock body scroll while it's open; close on link, Esc and resize |

## Extra craft details (values)

Recurring values from gallery-grade builds that go beyond the rules above. Working code for each pattern is in `references/techniques/`.

**Type**
- Tracking by size: condensed caps −.02em; large sans/serif −.025 to −.035em; big sans −.045 to −.05em (italic serif at ~88px ≈ −4px); vw wordmarks −.07em; stat numbers −.025em; UI and body −.01 to −.015em.
- Line-height by role: mega/serif titles .75–.78; vw wordmarks .85; italic serif display .8–.9; stacked caps .88–.92; two-line sans headlines 1.05–1.12; a sub under an italic display can be 1.25.
- Sizes: lede 15.5–18px; nav and buttons 13–15px; badges and eyebrows 11–13.5px; compact stats 18–26px with 9–12.5px labels, big metrics `clamp(48px,10vw,96px)` at weight 300. Fluid examples: hero `clamp(28px,6.2vw,80px)`, section title `clamp(3rem,12vw,160px)`, stacked statement `clamp(2rem,9vw,9rem)`, h2 `clamp(1.5rem,4vw,3.2rem)`.
- Weight 300 at huge sizes on dark backgrounds reads expensive; 500 for big sans wordmarks.
- Pairings that recur: Instrument Serif italic + Inter or Barlow; Inter + Outfit; Geist alone; Manrope alone; Kanit 300–900 alone; Anton + Inter (poster); Poppins + Source Serif 4 italic; Helvetica Now / Neue Haas (Swiss); a dot-matrix or pixel display face + Inter for UI.
- Two-tone headline: the first phrase in the primary, the rest in a lighter tint of the same hue (`#336443` → `#85AB8B`); or muted-tone words without italics.
- Logo craft: a 10px ®/™; a ✳︎ or ✦ glyph after the logotype; one lowercase italic serif letter in a 48px glass disc; an SVG mark with a metallic multi-stop gradient.
- Micro-label formats: `// Capabilities` (14px, 80 %), `[ 02 ] Section`, `01 ——` with a 64×1.5px rule, `/ SERVICE NAME` lists, an eyebrow led by a 32px hairline or a 6px dot, counts as superscripts on nav items (`Projects⁶`, mono 10px at 60 %). Mapping a mono class to the sans keeps the tracked look without a third font.
- Inline icon circles inside a headline (56px, 1px border, 22px icon, nudged −4px) work as ornaments that invert on hover. All-lowercase copy suits calm tech brands.
- Rendering: `-webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale`; `font-variant-numeric:tabular-nums` on changing numbers; `font-display:swap` + `preconnect` to fonts.gstatic.com (`crossorigin`). Card copy max 32ch; ledes max 28rem (~470px).

**Colour**
- Palettes that recur: warm cream on black (`#DEDBC8` / `#E1E0CC`, cards `#101010`–`#212121`); paper on photography (`#fdf1e1`, ink `#111411`); light pages `#fcfcfc` / `#f0f0ee` / `#EFEFEF` / `#f9fafb` with ink `#111` or deep navy `#051A24` / `#0D212C`; dark cards `hsl(0 0% 5–8%)`, borders `hsl(0 0% 12–20%)`, muted text `hsl(0 0% 53–65%)` or `#9a9a9a` / `#8e8e8e` / `#6F6F6F`.
- Define tokens as HSL triplets (`--fg: 0 0% 100%`) so `hsl(var(--fg) / .6)` opacity steps work.
- Selection: `rgba(255,255,255,.2)` on dark, or the brand at 30 % alpha.

**Text over media**
- Text-shadow instead of boxes: body `0 2px 18px rgba(0,0,0,.42)`, display `0 16px 38px rgba(0,0,0,.32)`, nav `0 2px 16px rgba(0,0,0,.2)`. Never a flat 50 % black wash.

**Buttons, pills, cards**
- Sizes: nav CTA 20×10px at 14px; hero CTA 24–32×12px; minimal heroes go large (56×20px, 16px). Tech and metal styles use a crisp 6–7px radius instead of pills.
- Announcement badge: inner white chip 12px semibold, padding 4×12px; message 14px at 90 % white. Email capture: submit inside the pill, pill padding `8px 8px 8px 24px`.
- Light-page physical button shadow: `0 1px 2px rgba(5,26,36,.1), 0 4px 4px rgba(5,26,36,.09), 0 9px 6px rgba(5,26,36,.05), 0 17px 7px rgba(5,26,36,.01), 0 26px 7px rgba(5,26,36,0), inset 0 2px 8px rgba(255,255,255,.5)`; secondary `0 0 0 .5px rgba(0,0,0,.05), 0 4px 30px rgba(0,0,0,.08)`; cards `0 4px 16px rgba(0,0,0,.08)` at radius 32–40px. Hover glow in the accent at ~30 %.
- Circular icon buttons 40–64px (2px white border or glass); a row of three glass social circles (16px padding, 20px icons) can close a hero.
- Tag pills: min-height 38–42px, padding 0 16–25px, paper colour on photos with `0 12px 30px rgba(0,0,0,.18)`; on dark, mono 9–10px outline tags that invert on hover. Numbered section badge: a 24–28px dark circle + a bordered 12–13px pill label.
- Media cards: 16/9, radius 24px, media zooms 1.05 over 700ms on hover, bottom scrim, a glass ↗ disc. Portfolio image tiles use 40–60px radii.

**Layout & spacing**
- Content max-width 64–80rem (or 1440px); hero copy 860–980px; lede 440–540px. Horizontal rhythm 20 / 32 / 48px by breakpoint; airy transparent navs go to ~112px side padding on desktop.
- Section padding 128–176px vertical; ~96px under section subtitles. Safe areas: `padding-bottom:max(36px, env(safe-area-inset-bottom))`.
- Sheet transitions between sections: the next section gets `border-radius:40–60px 40–60px 0 0`, `margin-top:-40…-56px`, `position:relative; z-index:10`, alternating near-black and white.
- Grids: 12-column bottom grid under giant type (8 + 4); bento spans 7/5/5/7; asymmetric about grid `26% / 1fr / 48%`, images aligned end, text start.
- Architectural guide lines: fixed 1px `rgba(255,255,255,.1)` verticals at the container edges (desktop, just above the background video).
- Ambient light (never "the visual"): `radial-gradient(ellipse at top, rgba(255,255,255,.03), transparent 70%)` behind dark sections; a CTA card's top glow `radial-gradient(600px circle at 50% 0%, rgba(255,255,255,.15), transparent 70%)` at opacity .3.

**Navigation**
- Floating split pills: logo in its own 40–44px circle, links in a separate pill (`#EDEDED` on light, `neutral-900/90` + blur on video), solid CTA pill right.
- A pill wrapping logo · 1×20px divider · links · divider · CTA that gains a shadow after `scrollY > 100`. Active item in a glass pill nav: `rgba(255,255,255,.2)` + blur + a `rgba(255,255,255,.3)` border, 16×6px padding.
- "Hanging tab" nav: a solid black pill attached to the top edge of an inset hero (bottom radius 16–24px, links 10 → 14px). Or a fixed floating bottom pill (24px from the bottom, centred, white, layered shadow) with a monogram + CTA.
- Link underline grows from the left on hover: `::after` `scaleX(0 → 1)`, origin left, .3s. Live time as `HH:MM in City`; links separated by `•` dots.

**Social proof & data**
- Avatar stack: 3 × 32px, −8px overlap, a 2px ring in the page colour, plus one 14px muted line.
- Pipe-separated stat strip pinned to the bottom (12–14px at 70 %, pipes hidden on mobile); definition-list facts with serif numerals `4.2rem/.9` and 86px gaps; glass stat cards (220px wide, 20px padding, outline icon top, italic-serif number ~36px at −1px, 12px light label); a star row (five 20px stars + "5/5") beside a testimonials heading.

**Motion**
- More easings: `cubic-bezier(.25,.1,.25,1)` scroll reveals and button text rolls; `(.34,1.56,.64,1)` spring overshoot (checks, pops); `(.32,.72,0,1)` bottom sheets; `(.215,.61,.355,1)` body fade-ups.
- Durations: hovers 150–350ms; button rolls 500ms; panel wipes 400–700ms; menus 280–500ms; carousels 640–800ms; crossfades 1s; count-ups 1.5–2s; video fades 500ms; media settles 1.8s; shine sweeps 600–650ms.
- Stagger: 30ms characters, 50ms nav items, 60–80ms words and blocks, 100–150ms cards and stats.
- Lerp factors: .1 cursor spotlight; .12 pointer parallax and scroll-scrubbed video; .14 pinned scroll stages; .04 shader blob momentum.
- Ambient loops stay slow: orbits 30–60s, marquees 20–40s (~40–60px/s), bob 3s, gradient border 3s, gradient shift 6s.
- Direction: the nav enters from above, content from below, secondary items sideways; logos and fine print only fade. Release transforms once an entrance ends (`animation:none` or an `.is-in` class) so hover transforms still work.
- Reduced motion: scroll-driven pieces keep the mapping but drop smoothing; pointer effects turn off; `(hover:none)` gets an autonomous or static alternative.

**Mobile**
- Stat grids 4 → 2×2; footer stat rows become columns; hero actions stack with full-width buttons at ≤560px.
- Height breakpoints (`max-height: 850px / 720px`) keep single-frame heroes intact on short laptops.
- Background video either stays full-bleed with a portrait `object-position` and a stronger directional scrim, or moves in-flow below the copy.
