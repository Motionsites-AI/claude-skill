<!-- Digital Experiences · Landing Page · 462 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=digital-experiences · Source: https://motionsites.ai/?prompt=digital-experiences -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

## Prompt

Build a single-page React + Vite + TypeScript + Tailwind CSS site with exactly two full-screen sections (Hero and Capabilities). The page is a dark, cinematic web design agency landing page with "liquid glass" morphism UI elements and smooth blur/fade animations using Framer Motion.

---

### Fonts (Google Fonts)

Load via `<link>` in `index.html`:
- **Instrument Serif** (italic) -- used for all headings (`font-heading`)
- **Barlow** (weights 300, 400, 500, 600) -- used for body text (`font-body`)

Tailwind config extends `fontFamily`:
```js
heading: ["'Instrument Serif'", 'serif'],
body: ["'Barlow'", 'sans-serif'],
```

Base CSS: `html, body { background: #000; color: #fff; font-family: 'Barlow', sans-serif; }`

---

### Liquid Glass CSS (in index.css)

Two variants defined as plain CSS classes:

**`.liquid-glass`** (subtle):
- `background: rgba(255, 255, 255, 0.01)` with `background-blend-mode: luminosity`
- `backdrop-filter: blur(4px)` / `-webkit-backdrop-filter: blur(4px)`
- No border; `box-shadow: inset 0 1px 1px rgba(255,255,255,0.1)`
- `position: relative; overflow: hidden`
- `::before` pseudo-element creates a gradient stroke border:
- `position: absolute; inset: 0; border-radius: inherit; padding: 1.4px`
- `background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%, rgba(255,255,255,0) 40%, rgba(255,255,255,0) 60%, rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%)`
- Masked with `-webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude;`
- `pointer-events: none`

**`.liquid-glass-strong`** (bolder):
- Same structure but `backdrop-filter: blur(50px)`
- `box-shadow: 4px 4px 4px rgba(0,0,0,0.05), inset 0 1px 1px rgba(255,255,255,0.15)`
- `::before` gradient uses 0.5 alpha at edges, 0.2 at 20%/80%

---

### FadingVideo Component

A reusable `<video>` component accepting `src` (string or string[]), `className`, and `style`. It:
1. Starts with `opacity: 0`
2. On `loadeddata`, fades in over 500ms using `requestAnimationFrame`
3. On `timeupdate`, when remaining time <= 0.55s, fades out over 550ms
4. On `ended`, if single source: resets `currentTime` to 0, replays, fades back in. If array: advances to next index (cycling).
5. Video is `autoPlay`, `muted`, `playsInline`, `preload="auto"`

---

### BlurText Component

A word-by-word staggered blur-in animation component using Framer Motion:
- Splits `text` prop by spaces
- Each word is a `motion.span` with `display: inline-block`, `marginRight: 0.28em`
- Triggers on IntersectionObserver (threshold 0.1)
- Each word animates: `filter` from `blur(10px)` to `blur(0px)`, `opacity` 0 to 1, `y` from 50 to 0
- Duration 0.7s per word, stagger delay of 100ms per word index
- Container uses `display: flex; flexWrap: wrap; justifyContent: center; rowGap: 0.1em`

---

### Section 1: Hero

- Full viewport height (`h-screen`), `overflow-hidden`, `bg-black`
- **Background video**: Single `<FadingVideo>` with:
- `src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260619_191346_9d19d66e-86a4-47f7-8dc6-712c1788c3b2.mp4"`
- Positioned: `absolute left-1/2 top-0 -translate-x-1/2 object-cover object-top z-0`
- Inline style: `width: 120%; height: 120%`

- **Content** (`relative z-10, flex flex-col h-full`):

**Navbar** (fixed, `top-4 left-0 right-0 z-50`, flex between, `px-8 lg:px-16`):
- Left: `liquid-glass` circle (h-12 w-12 rounded-full) with italic "a" in `font-heading text-2xl`
- Center (hidden on mobile, `md:flex`): `liquid-glass rounded-full px-1.5 py-1.5` pill containing links ["Work", "Studio", "Services", "Journal", "Contact"] as `px-3 py-2 text-sm font-medium text-white/90 font-body` + a white CTA button "Start a Project" with ArrowUpRight icon
- Right: empty `h-12 w-12` spacer div

**Main content** (centered, `flex-1 flex flex-col items-center justify-center pt-24 px-4 text-center`):
- **Badge** (motion.div, delay 0.4): `liquid-glass rounded-full` pill with a white "New" badge inside + text "Booking Q3 2026 engagements -- limited capacity"
- **Headline** (mt-6, max-w-3xl): `<BlurText>` with text "Crafted Digital Experiences Built to Outlast Trends", classes: `text-6xl md:text-7xl lg:text-[5.5rem] font-heading italic text-white leading-[0.8] tracking-[-4px]`
- **Subtext** (motion.p, delay 0.8, mt-4): "We are a small studio of designers and engineers shaping brand-defining websites for ambitious companies. Precise typography, cinematic motion, and code you can be proud of." -- `text-sm md:text-base text-white max-w-2xl font-body font-light leading-tight`
- **CTA buttons** (motion.div, delay 1.1, mt-6, flex gap-6): "Start a Project" in `liquid-glass-strong rounded-full px-5 py-2.5` with ArrowUpRight + "Watch Showreel" plain text with Play icon
- **Stats cards** (motion.div, delay 1.3, mt-8, flex gap-4): Two `liquid-glass p-5 w-[220px] rounded-[1.25rem]` cards:
- Card 1: ClockIcon, "6 Weeks", "Average End-to-End Launch Time"
- Card 2: GlobeIcon, "140+", "Brands Shipped Across Four Continents"
- Numbers: `text-4xl font-heading italic tracking-[-1px] leading-none mt-4`

**Bottom trust bar** (motion.div, delay 1.4, flex-col items-center gap-4 pb-8):
- `liquid-glass rounded-full` pill: "Trusted by founders, operators, and creative directors worldwide"
- Logo names in a flex row (gap-12 md:gap-16): ["Aeon", "Vela", "Apex", "Orbit", "Zeno"] each as `font-heading italic text-2xl md:text-3xl tracking-tight`

- **All motion elements** use shared initial/animate: `{ filter: 'blur(10px)', opacity: 0, y: 20 }` -> `{ filter: 'blur(0px)', opacity: 1, y: 0 }`, duration 0.8s, easeOut

---

### Section 2: Capabilities

- `min-h-screen`, `overflow-hidden`, `bg-black`, relative
- **Background video**: `<FadingVideo>` with:
- `src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_093722_ccfc7ebf-182f-419f-8a62-2dc02db7dd9d.mp4"`
- `absolute inset-0 w-full h-full object-cover z-0`

- **Content** (`relative z-10 px-8 md:px-16 lg:px-20 pt-24 pb-10 flex flex-col min-h-screen`):
- **Header** (mb-auto):
- Label: `text-sm font-body text-white/80 mb-6` -- "// Capabilities"
- Heading: `font-heading italic text-6xl md:text-7xl lg:text-[6rem] leading-[0.9] tracking-[-3px]` -- "Studio craft,\nend to end"

- **Cards grid** (mt-16, `grid grid-cols-1 md:grid-cols-3 gap-6`), three cards:
1. **Design** -- Icon: ImageIcon (filled image icon), Tags: ["Brand Systems", "Art Direction", "Visual Identity", "Motion"], Body: "We shape identities and interfaces that feel unmistakably yours -- typographic systems, component libraries, and art-directed pages that scale without losing soul."
2. **Engineering** -- Icon: MovieIcon (film/clapboard), Tags: ["React", "Next.js", "Headless CMS", "Edge-Ready"], Body: "Production-grade front-ends built on modern stacks. Performant, accessible, and instrumented -- with code your team will enjoy extending long after launch."
3. **Growth** -- Icon: LightbulbIcon, Tags: ["SEO", "Analytics", "A/B Testing", "Retention"], Body: "Launch is the starting line. We partner with your team on conversion, content, and iteration loops that turn a beautiful site into a compounding asset."

- Each card: `liquid-glass rounded-[1.25rem] p-6 min-h-[360px] flex flex-col`
- Top row: icon in a nested `liquid-glass h-11 w-11 rounded-[0.75rem]` square + tags (flex-wrap, gap-1.5) right-aligned, each tag is `liquid-glass rounded-full px-3 py-1 text-[11px] text-white/90 font-body whitespace-nowrap`
- Spacer: `flex-1`
- Bottom: title in `font-heading italic text-3xl md:text-4xl tracking-[-1px] leading-none` + body in `text-sm text-white/90 font-body font-light leading-snug max-w-[32ch]`

---

### Custom SVG Icons (no external icon library needed for these)

- **ArrowUpRight**: 24x24, stroke, paths "M7 17L17 7" and "M7 7h10v10"
- **Play**: 24x24, filled polygon "6 4 20 12 6 20 6 4"
- **ClockIcon**: 24x24, stroke (1.5), circle r=9 + "M12 7v5l3 2"
- **GlobeIcon**: 24x24, stroke (1.5), circle r=9 + horizontal line + two arc paths
- **ImageIcon**: 24x24, filled Material-style image icon
- **MovieIcon**: 24x24, filled Material-style movie icon
- **LightbulbIcon**: 24x24, filled Material-style bulb icon

---

### Dependencies

- react, react-dom
- framer-motion
- tailwindcss, postcss, autoprefixer
- vite, @vitejs/plugin-react
- typescript

---

### Key Design Principles

- Everything is on a pure black (#000) background
- All text is white; subtle text uses `white/80` or `white/90`
- Liquid glass elements have near-invisible fills with gradient-stroke borders via CSS masks
- Videos cover sections as atmospheric backgrounds, fading in/out smoothly
- Typography: heading font is always italic with very tight tracking (negative), body font is light weight
- Responsive: nav links hidden on mobile, grid collapses to single column, text sizes scale with breakpoints
- Animations: staggered blur-in on load for hero content, intersection-triggered for BlurText
