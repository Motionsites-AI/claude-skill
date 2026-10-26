<!-- Neon Logic · Landing Page · 402 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=neon-logic · Source: https://motionsites.ai/?prompt=neon-logic -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a single-page landing site for "SynapseX" -- a futuristic neural-AI interface product. The entire site uses a black background with white text and full-viewport video backgrounds. The primary font is "Space Mono" (monospace) for all text. Use React + TypeScript + Vite + Tailwind CSS + Framer Motion.

### Fonts & External Assets

- **Primary font:** "Space Mono" (all weights: 400, 700, italic) from Google Fonts
- **Display font (background watermark only):** "Anton SC" from Google Fonts
- **Icons:** Bootstrap Icons CDN (`https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css`) -- used only for the Apple icon (`bi bi-apple`) in the download button
- **All Tailwind `fontFamily` keys** (`sans`, `serif`, `mono`) are overridden to `"Space Mono", monospace`

### Video URLs (CloudFront -- use exactly these)

1. **Hero (mouse-scrubbed, NOT autoplay):**
   `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_083515_290e5a10-0b95-41af-a5e2-32b6389baa4d.mp4`

2. **Second Section (autoplay, muted, loop):**
   `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_092455_089c54f8-3b03-4966-9df1-e9746063d0ef.mp4`

3. **Metrics Section (autoplay, muted, loop):**
   `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_095810_ecea3dd2-fc5e-4e41-8696-4219290b6589.mp4`

4. **Technology Section (autoplay, muted, loop):**
   `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_095750_32a52ce0-2005-45c9-9093-41f03fde9530.mp4`

5. **Footer (autoplay, muted, loop):**
   `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_080203_fd7f4f85-3a86-4837-8192-85e7bfe68e75.mp4`

### Dependencies

```json
"framer-motion": "^12.40.0",
"lucide-react": "^0.344.0",
"react": "^18.3.1",
"react-dom": "^18.3.1"
```

### Global CSS (`index.css`)

- Import Space Mono from Google Fonts
- Import Bootstrap Icons CSS
- Tailwind directives (`@tailwind base/components/utilities`)
- CSS variables: all `--font-*` set to `"Space Mono", monospace`
- Global reset: `* { margin: 0; padding: 0; box-sizing: border-box; }`
- `html, body`: `background: #000; color: #fff; overflow-x: hidden; overflow-y: auto; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`
- Lenis smooth scroll utility classes (`.lenis.lenis-smooth`, `.lenis.lenis-stopped`, `.lenis.lenis-scrolling iframe`)

### Custom Text Animation Components

#### 1. `ScrambleIn` -- entrance reveal animation
- Props: `text: string`, `delay: number` (ms before start), `triggered: boolean`
- Character set: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~|}{[]:;?><`
- On trigger (after delay): runs interval every 25ms, revealing characters left-to-right at 0.5 chars/frame
- Characters not yet revealed show random chars (up to 3 ahead of the reveal cursor); characters beyond that are empty
- Spaces always show as spaces
- Before triggered: renders `&nbsp;`

#### 2. `ScrambleText` -- hover-driven scramble
- Props: `text: string`, `isHovered: boolean`, `className?: string`
- On hover: scrambles all chars with random chars, then reveals left-to-right at 4 frames/char, interval 25ms
- On unhover: immediately resets to original text

### Custom SVG Logo (`SynapseXLogo`)

A 4-fold rotationally symmetric abstract shape rendered in an SVG with `viewBox="-50 -50 100 100"`. Each quadrant is the same path rotated 0/90/180/270 degrees:

```
M 1.5,23 L 1.5,33 C 1.5,38.5 6,43 11.5,43 L 16.5,43 C 22,43 26.5,38.5 26.5,33 Q 28,28 33,26.5 C 38.5,26.5 43,22 43,16.5 L 43,11.5 C 43,6 38.5,1.5 33,1.5 L 23,1.5 Q 12,12 1.5,23 Z
```

### Animated Hamburger (`SquashHamburger`)

- 3 horizontal bars (absolute positioned spans)
- Desktop: container 18x12px, bar height 1.5px
- Mobile: container 15x10px, bar height 1.2px
- On open: top bar rotates 45deg + translates down to center; middle bar fades/scales out; bottom bar rotates -45deg + translates up to center
- Spring animation: stiffness 300, damping 20

---

### Page Sections (in order)

---

#### SECTION 1: Hero (full viewport height)

- **Background:** Video #1, `object-cover`, paused on load. Controlled by mouse-scrub: horizontal mouse movement across viewport scrubs the video timeline forward/backward. Sensitivity factor: `0.8`. Uses `seeked` event to chain seeks without dropping frames.
- **Entrance animation:** After 800ms delay, `entranceComplete` state becomes true -- all hero content fades in (opacity 0 -> 1, duration 1s).
- **Dot grid overlay:** `radial-gradient(#ffffff 1px, transparent 1px)` with 24x24px grid, opacity 0.05, pointer-events-none
- **Large background watermark text:** The word "TRANSCENDENCE" in "Anton SC" font, centered vertically (offset +50px from center), `clamp(120px, 30vw, 521px)` font size, uppercase, letter-spacing -4px. Opacity 0.10. Color achieved via `radial-gradient(circle, rgba(142,127,148,0) 0%, #8E7F94 70%)` as `background-clip: text` with transparent fill.
- **Layout:** Flexbox column, padding `px-4 sm:px-6 md:px-8 pt-20 sm:pt-24 pb-8 sm:pb-12`. Content is pushed to the bottom using `flex-1` spacer.
- **Bottom row:** `flex-col gap-6 md:flex-row md:items-end md:justify-between`
  - **Left column** (`flex flex-col gap-4`):
    - **h1** "Brain" / "And Body" (two lines via `<br>`): `text-white font-light leading-[0.95] tracking-[-0.03em] text-[clamp(40px,10vw,100px)]`. Each line uses `ScrambleIn` with delays 200ms and 500ms.
    - **Description paragraph** (motion.p): fade-up animation (y:25->0, opacity 0->1, duration 0.9s, cubic-bezier ease `[0.215, 0.610, 0.355, 1.000]`, delay 0.2s). Text: "Built at the intersection of neuroscience and artificial intelligence. SynapseX continuously maps neural pathways, cognitive load, and physiological states into a single adaptive intelligence layer." Style: `max-w-sm text-[13px] sm:text-[15px] text-white/60 leading-relaxed`
  - **Right h1** "One" / "Network": Same styling as left h1 but with `text-left md:text-right`. ScrambleIn delays: 700ms and 1000ms.

---

#### NAVBAR (fixed, z-50)

- Fixed to top, height 80px (h-20), transparent background, full width
- Fades in with `entranceComplete` (opacity 0->1, duration 0.8s)

**Desktop (hidden below `sm`):**
- Left group: two pills side by side with gap-2
  - **Logo pill:** h-12, px-5, `bg-white/15 backdrop-blur-md rounded-[14px]`. Contains SynapseXLogo (18x18px white) + "SynapseX" text (16px font-medium tracking-tight white). WhileHover: scale 1.02 + bg rgba(255,255,255,0.22). WhileTap: scale 0.98. Hides on `sm` when menu open (`hidden md:flex`), shows normally otherwise.
  - **Expanding menu pill:** Animates width from 48px (closed) to 290px (open) with spring (stiffness 350, damping 28). h-12, `rounded-[14px]`, `bg-white/15 backdrop-blur-md`. Contains:
    - Hamburger button: when closed = 48x48px rounded-[14px]; when open = 36x36px rounded-[11px] with `bg-white/10 hover:bg-white/20 ml-1.5`
    - Nav links (fade in when open, offset x:15->0): "About" and "Metrics" with ScrambleText on hover. 16px font-normal text-white/85 hover:text-white. Smooth-scroll to `window.innerHeight` and `window.innerHeight * 2` respectively.
- Right: **Download button** -- `h-12 px-6 bg-white rounded-full`, black text. Apple icon + "Download" with ScrambleText on hover. WhileHover: scale 1.03 + bg #e2e2e6. WhileTap: scale 0.97.

**Mobile (visible below `sm`):**
- Scaled-down version: h-9 pills, rounded-[10px], smaller text (13px), logo pill animates to width 0 when menu open (spring stiffness 350, damping 28). Menu capsule expands to 100% width when open. Download button: h-9 px-3.5 rounded-full.

---

#### SECTION 2: Cinematic Text (full viewport height)

- **Background:** Video #2, autoplay muted loop, object-cover
- **Top gradient overlay:** 180px height, linear-gradient from `#010103` to transparent, z-10
- **Content:** Centered large paragraph in a `max-w-5xl` container with 3D perspective (400px)
  - Framer Motion: `rotateX(24deg) translateY(${yScaleValue}px) translateZ(15px)` where `yScaleValue` transforms from 60 to -120 based on smooth scroll progress (spring: stiffness 15, damping 32, mass 1.8). Opacity fades in from 0 to 1 between scroll progress 0.3-0.5.
  - Text: "A neural-AI interface built on the architecture of the human nervous system. SynapseX translates synaptic activity into computational intelligence. Every signal becomes measurable, structured, and visible. It continuously reconstructs internal state as a dynamic neural map. Biological noise is filtered into actionable cognitive patterns."
  - Style: `font-sans font-normal text-[22px] sm:text-[30px] md:text-[36px] lg:text-[42px] text-white leading-[1.35] tracking-[-0.02em] select-none px-6 sm:px-12 text-center`

---

#### SECTION 3: Metrics (min-h-screen)

- **Background:** Video #3, autoplay muted loop, object-cover
- **Layout:** Centered content, `pt-32 pb-32 px-6`, max-w-6xl
- **Subtitle:** "Performance Metrics" -- `text-white/40 text-[13px] sm:text-[14px] tracking-[0.2em] uppercase mb-20 text-center`. Fades in on scroll (whileInView, duration 1.2s, once, amount 0.3).
- **Metrics grid:** 3 columns on md, 1 on mobile, gap-16 md:gap-8. Each metric fades up (y:30->0, opacity, duration 0.8s, staggered 0.15s delay per item):
  - "2.4ms" -- Synaptic Latency
  - "99.7%" -- Signal Accuracy
  - "140B" -- Neural Parameters
  - Value: `text-white text-[clamp(48px,10vw,96px)] font-light tracking-[-0.04em] leading-none`
  - Label: `text-white/40 text-[13px] sm:text-[15px] mt-4 tracking-wide`

---

#### SECTION 4: Technology / Adaptive Intelligence (full viewport height)

- **Background:** Video #4, autoplay muted loop, object-cover
- **Layout:** Flexbox column, `px-8 sm:px-12 md:px-16 py-12 sm:py-16`
- **Top area:** flex-col md:flex-row md:justify-between md:items-start gap-6
  - **Left heading:** "Adaptive / Intelligence" (two lines), `text-white font-light text-[clamp(36px,8vw,72px)] leading-[0.95] tracking-[-0.03em]`. Fades up (y:40->0, duration 1.0s, whileInView once amount 0.3).
  - **Right paragraph:** "The system learns your neural baseline within 72 hours. From there, every cognitive state is mapped, predicted, and optimized in real time." `text-white/50 text-[13px] sm:text-[15px] leading-relaxed max-w-xs md:text-right md:pt-2`. Fades up (y:20->0, duration 1.0s, delay 0.2s).
- **Spacer** (`flex-1`)
- **Bottom grid:** 2 cols on mobile, 4 cols on md, gap-8 md:gap-6. Fades in on scroll (duration 1.0s, delay 0.3s). Each item staggered (y:20->0, duration 0.7s, delay i*0.1):
  1. "Cortical Mapping" -- "Real-time spatial reconstruction of active neural regions."
  2. "Signal Isolation" -- "Separates cognitive intent from biological noise."
  3. "State Prediction" -- "Anticipates cognitive transitions before they occur."
  4. "Loop Feedback" -- "Closed-loop adjustment based on outcome correlation."
  - Title: `text-white text-[14px] sm:text-[16px] font-normal mb-2`
  - Desc: `text-white/40 text-[12px] sm:text-[14px] leading-relaxed`

---

#### SECTION 5: Architecture (min-h-screen, pure black background, no video)

- Centered content, max-w-3xl, `px-6 py-32`
- **Heading block** (fades up y:30->0, duration 1.0s, whileInView once amount 0.4):
  - Subtitle: "Architecture" -- `text-white/40 text-[13px] sm:text-[14px] tracking-[0.2em] uppercase mb-8`
  - Heading: "Three layers. Zero friction." -- `text-white font-light text-[clamp(28px,6vw,56px)] leading-[1.15] tracking-[-0.02em] mb-10`
  - Description: "Sensor layer captures raw bioelectric signals. Processing layer isolates intent. Interface layer delivers structured output to any connected system." -- `text-white/45 text-[15px] sm:text-[17px] leading-relaxed max-w-xl mx-auto`
- **Layer cards** (fade in, duration 1.2s, delay 0.4s, whileInView once amount 0.4): 3 stacked cards, `mt-20 flex-col items-center gap-4`. Each card: `max-w-md h-[72px] border border-white/10 rounded-lg flex items-center justify-between px-6`
  - Left: "Layer 1/2/3" -- `text-white/30 text-[12px] tracking-[0.15em] uppercase`
  - Right: "Capture" / "Process" / "Interface" -- `text-white text-[16px] sm:text-[18px] font-light`

---

#### FOOTER

- Black background, overflow hidden
- Two-column layout (stacked on mobile): `flex-col md:flex-row min-h-[400px]`
- **Left:** Video #5, `object-cover`, fills half width (h-[300px] on mobile, auto height on md)
- **Right:** Flex column justify-between, `p-10 sm:p-16`
  - Top: SynapseXLogo (18x18px, text-white/70) + "SynapseX" text (15px font-medium text-white/70 tracking-tight), mb-8. Below: "The next evolution of human-machine interaction. Built for those who refuse to be limited by biology alone." `text-white/40 text-[14px] sm:text-[15px] leading-relaxed max-w-sm`
  - Bottom: "(c) 2026 SynapseX Labs. All rights reserved." `text-white/25 text-[12px] mt-12`

---

### Key Technical Details

- The entire app wrapper has inline style: `fontFamily: '"Space Mono", monospace'`
- All `h-screen` elements also have `h-[100dvh]` for mobile viewport compatibility
- The hero video is NOT autoplay -- it starts paused at time 0 and is scrubbed by horizontal mouse movement (delta-based, not absolute position). The seek logic chains via `seeked` event to avoid frame-dropping.
- Framer Motion `useScroll` tracks the second section with offset `["start end", "end start"]`, piped through `useSpring` (stiffness 15, damping 32, mass 1.8) then `useTransform` and `useMotionTemplate` for the 3D text rotation effect.
- No external state management, no routing, no database -- pure single-page React app.

---
