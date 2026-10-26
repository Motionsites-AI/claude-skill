<!-- PROMPT · Landing Page · 607 likes · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260715_020312_6a21f245-35e1-47c1-a730-090d3ebd518e.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=prompt-hero -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

### Overview

Build a full-screen, scroll-driven fashion/archive landing page for a brand called "prmpt". The page has two main phases:

1. **Hero phase** (first 100vh of scroll): Full-viewport video background with overlaid UI (logo, nav, product info, custom cursor). A black panel slides up from below covering the video.
2. **Gallery phase** (continues scrolling): The black panel contains a scattered grid of product images that scale in/out as they enter/exit the viewport. At the end, a white overlay fades in with a "view" CTA button.

---

### Tech Stack

- **React 19** + **TypeScript**
- **Vite 6** with `@vitejs/plugin-react`
- **Tailwind CSS v4** via `@tailwindcss/vite` plugin
- **GSAP 3.15** + `@gsap/react` (ScrollTrigger)
- **Motion (Framer Motion) 12** (`motion/react`)
- **Font**: "Inter Tight" (Google Fonts, weight 500) -- loaded via `<link>` or import

---

### Asset URLs

**Videos (CloudFront):**
- LEFT video: `https://d8j0ntlcm91z4.cloudfront.net/user_39ca84eAE1ODL9hbR5VhoEj8tBf/hf_20260625_154433_532a85d3-dabf-4265-b8bd-19ac6af31842.mp4`
- RIGHT video: `https://d8j0ntlcm91z4.cloudfront.net/user_39ca84eAE1ODL9hbR5VhoEj8tBf/hf_20260625_154401_a664f076-b971-4557-8728-40ef9ea4c49b.mp4`

**Gallery Images (10 total, in order):**
1. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_104530_521b2f85-c0f3-4d0e-9704-b578315b4cb9.png&w=1920&q=85`
2. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103711_76ccdb8b-5043-4f47-9c54-4379713393ea.png&w=1920&q=85`
3. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103728_394f6a1b-85e2-4386-a4f6-408472a0a5b7.png&w=1920&q=85`
4. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103739_86743e0e-16a7-4bee-bf38-dd67985344dc.png&w=1920&q=85`
5. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103748_b2215dc8-a3a7-470d-b19a-5b87fa7d0c37.png&w=1920&q=85`
6. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103758_e919ce72-5c9d-4b87-9be6-d7647b34825c.png&w=1920&q=85`
7. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103808_013583d0-3386-4547-9832-37c7d8edb3ac.png&w=1920&q=85`
8. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103937_a0c49d0a-33eb-4ead-aea6-c1baf241acbc.png&w=1920&q=85`
9. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_103956_d18ed8fd-7b6f-4b86-91f9-20010fe38670.png&w=1920&q=85`
10. `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260629_104034_ba5a9963-87ff-4008-a545-6bd686c088b5.png&w=1920&q=85`

---

### SECTION 1: Hero (Video Background + Overlaid UI)

#### Root Container
- `id="scroll-spacer"`, `position: relative`, `user-select: none`, `background: white`
- Height is dynamically calculated (initially `500vh`, then overridden by GSAP to `vh + maxScroll + 2*vh`)
- Custom cursor hidden on desktop (`cursor: none`), default on touch devices

#### 1A. Custom Cursor (Desktop Only)
- Hidden on mobile/tablet (< 1024px)
- A `fixed`, `pointer-events-none`, `z-index: 50` div that follows `mousemove`
- Positioned via direct DOM manipulation (`style.left/top = clientX/clientY`)
- `transform: translate(-50%, -50%)` to center on pointer
- `mix-blend-mode: exclusion`
- Contains a 48x48 SVG: a circle with stroke (r=22.75, strokeWidth=2.5) containing a custom Japanese/decorative glyph path, all filled white

#### 1B. Logo (Top Left)
- `position: fixed`, `pointer-events-none`, `z-index: 20`
- `mix-blend-mode: exclusion`
- Responsive width: 124px (mobile < 640), 266px (tablet 640-1024), 355px (desktop)
- Position: `top: 16px, left: 16px` (mobile), `top: 32px, left: 32px` (desktop)
- Motion animation: fade in + slide up (`opacity: 0->1, y: 12->0`), duration 0.6s, ease `[0.25, 0.1, 0.25, 1]`, delay 0s
- SVG viewBox `0 0 355 110`, contains the "prmpt" wordmark + circled "R" mark, all paths filled white

#### 1C. Caption (Below Logo, Left Side)
- `position: fixed`, `pointer-events-none`, `z-index: 20`
- `mix-blend-mode: exclusion`
- Position: `left: 32px` (desktop), `left: 16px` (mobile)
- Top: 244px (desktop), 180px (tablet), 118px (mobile)
- Width: 692px (desktop), `calc(50vw - 48px)` (tablet), `calc(100vw - 32px)` (mobile)
- Font: Inter Tight, weight 500, size 12px, line-height 140%, letter-spacing -0.04em, color #FFFFFF
- Motion animation: same as logo but delay 0.3s
- Text content: "When switching between videos near the center, do not reset currentTime to 0 abruptly. Add a small dead zone: if cursor is within +/-50px of center, keep both videos at currentTime = 0 and show whichever was last active."

#### 1D. Header Navigation (Top Right)
- `position: fixed`, `z-index: 20`, `pointer-events-none`
- `mix-blend-mode: exclusion`
- Position: `top: 32px, right: 32px` (desktop), `top: 16px, right: 16px` (mobile)
- Width: 330px (desktop), auto (mobile)
- Height: 30px
- Flex row, justify-content: space-between, align-items: center
- Motion animation: same easing, delay 0.15s
- Contains:
  - "ABOUT" text (hidden on mobile): Inter Tight, 500, 15px, uppercase, white
  - A flex row with gap 50px (desktop) / 20px (mobile):
    - Hamburger SVG icon: viewBox `0 0 40 40`, two horizontal lines (`M0 14H40` and `M0 26H40`), stroke white, strokeWidth 2.5. Size: 30x30 (desktop), 24x24 (mobile)
    - "[ CART ]" text: Inter Tight, 500, 15px (desktop) / 13px (mobile), white

#### 1E. Product Info (Bottom Right)
- `id="outro-info"`, `position: fixed`, `pointer-events-none`, `z-index: 20`
- `mix-blend-mode: exclusion`
- **Desktop**: right: 32px, bottom: 80px, width: 330px, flex-column, align center
- **Mobile**: left: 0, right: 0, bottom: 48px, flex-column, align center
- Motion animation: opacity 0->1, delay 0.45s
- `data-outro-offset`: 166 (desktop), 132 (mobile) -- used by scroll animation
- Contains:
  - Top block (flex-column, align flex-start, width 100% desktop / 252px mobile, margin-bottom 32px desktop / 12px mobile):
    - Circle icon: relative div (30x30 desktop, 20x20 mobile) containing:
      - SVG circle (cx=20, cy=20, r=18.75, stroke white, strokeWidth 2.5 desktop / 2 mobile)
      - `<span id="circle-symbol">` centered inside, shows "8" initially, changes to random symbol from `['8', '$', '^^', '%', '/']` on scroll (throttled 80ms)
      - Font: Inter Tight, 500, 15px (desktop) / 10px (mobile), letter-spacing -0.04em, uppercase, white
    - Collection label: Inter Tight, 500, 30px (desktop) / 20px (mobile), line-height 100%, text-align center, letter-spacing -0.04em, uppercase, white. Content: `ARCHIVE COLLECTION` + line break + `"PROMPT"`
  - Price: Inter Tight, 500, 80px (desktop) / 60px (mobile), line-height 100%, text-align center, letter-spacing -0.04em, white. Content: `$97,33`

#### 1F. "View" Button (Bottom Right, Initially Hidden)
- `id="outro-buy"`, `position: fixed`, `pointer-events-none`, `z-index: 20`
- `mix-blend-mode: exclusion`
- **Desktop**: right: 32px, bottom: 32px, width: 330px, height: 174px
- **Mobile**: left: 16px, right: 16px, bottom: 60px, height: 100px
- `transform-origin: right bottom`, `transform: scale(0)` (starts hidden, scales to 1 via scroll)
- Background: #fff, border-radius: 1335px (pill shape)
- Flex center
- Text "view": Inter Tight, 500, 110px (desktop) / 72px (mobile), letter-spacing -0.04em, color #fff, `mix-blend-mode: exclusion`

#### 1G. Video Container
- `id="main-canvas"`, `pointer-events-none`
- **Desktop**: `position: fixed, inset: 0, width: 100%, height: 100%, z-index: 0`
- **Mobile**: `position: fixed, left: 0, top: 220px, width: 100vw, height: calc(100vh - 220px), z-index: 0`
- Opacity transition: 0 -> 1 when both videos loaded (`opacity 0.3s ease`)
- `overflow: hidden`
- Contains two `<video>` elements (muted, playsInline, preload="auto"), absolutely positioned to fill container, `object-fit: cover`
- Left video starts `display: none`, right starts `display: block`


**Desktop (non-touch):**
- Videos are NOT auto-played. They are scrubbed based on cursor X position via `requestAnimationFrame`.
- Dead zone: `Math.max(30, width * 0.05)` pixels from center
- If cursor is in dead zone, keep current video at `currentTime = 0`
- If cursor moves left of dead zone: show RIGHT video, scrub it based on distance from center-left-edge to left edge
- If cursor moves right of dead zone: show LEFT video, scrub it based on distance from center+deadzone to right edge
- `activeSideRef` tracks which side was last active, only changes when cursor exceeds dead zone
- Progress calculation: `(distance from dead zone edge) / (available range)` mapped to `0...video.duration`
CRITICAL: Only update currentTime when !video.seeking -- this prevents jittery playback by waiting for the browser to finish rendering the previous seek before requesting a new one.
#### 1H. Video Interaction Logic

**Mobile/Tablet (touch):**
- Videos auto-play alternately: left plays first, on `ended` event switches to right, on right `ended` switches back to left
- Respects `prefers-reduced-motion`

#### 1I. White Overlay
- `id="outro-overlay"`, `position: fixed, inset: 0`, `pointer-events-none`, `z-index: 12`
- Background: #fff, opacity: 0 (controlled by scroll)

#### 1J. Footer
- `id="outro-footer"`, `position: fixed`, `pointer-events-none`
- Left: 16px, bottom: 32px (desktop) / 24px (mobile)
- `mix-blend-mode: exclusion`, opacity: 0 (controlled by scroll)
- Flex row, gap: 80px (desktop) / space-between (mobile)
- Two spans: "PRMPT (R) 2026" and "PRIVACY POLICY"
- Font: Inter Tight, 500, 13px (desktop) / 11px (mobile), letter-spacing -0.02em, uppercase, white

---

### SECTION 2: Black Panel (Gallery)

#### Container
- `position: fixed, inset: 0`, background: black, `z-index: 10`
- Initially translated `translateY(100vh)` (off-screen below)
- Slides up to `translateY(0)` during first 100vh of scroll via GSAP ScrollTrigger (scrub: true, ease: none)

#### Inner Wrapper
- `width: 100%`, `padding-top: min(400px, 40vh)`

#### Grid Layout Algorithm
- Responsive columns: 2 (< 640px), 3 (640-1024px), 4 (>= 1024px)
- Each cell has `aspect-ratio: 2/3`
- Layout function `buildLayout(count, cols)` creates rows:
  - For each row `r`, compute primary column: `a = (r * 2 + (r % 2)) % cols`
  - Place one image at column `a`
  - Every 3rd row (`r % 3 === 0`), place a second image at `b = (a + 2) % cols` (or `(a+1)%cols` if same as a)
  - Empty cells get `-1` (rendered as empty spacer divs)

#### Card Behavior
- Each card has class `bp-card`, `will-change: transform`
- `transform: scale(0)` initially
- `transform-origin`: cards in left half of grid get `right bottom`, right half get `left bottom`
- Scale is computed per-frame in RAF based on card's vertical position:
  - **Enter**: `Math.min(1, (vh - top) / (vh * 0.6))` -- scales from 0 to 1 as it enters viewport
  - **Exit**: `Math.min(1, bottom / (vh * 0.4))` -- scales from 1 to 0 as it exits top
  - Final scale: `Math.min(enter, exit)`
  - If card is fully off-screen (bottom <= 0 or top >= vh): `scale(0)`

#### Scroll Phases (RAF-based, NOT scroll events)
- **Phase 1** (scrollY 0 to vh): Panel slides up. Cards are computed with panelOffset = `vh - scrollY`
- **Phase 2** (scrollY > vh): Panel is fixed at top. Inner wrapper translates up: `translateY(-(scrollY - vh))`. Cards recomputed with phase2 offset.
- **Outro** (scrollY > vh + maxScroll): White overlay fades in, product info slides up by `outroOffset` px, "view" button scales from 0 to 1, footer fades in. Progress: `(scrollY - vh - maxScroll) / (vh - 100)`

#### Spacer Height Calculation
- Set dynamically: `vh + maxScroll + 2 * vh` where `maxScroll = wrapScrollHeight - vh`

---

### CSS (index.css)

```css
@import "tailwindcss";

.bp-card {
  will-change: transform;
}

@media (prefers-reduced-motion: reduce) {
  .bp-card {
    will-change: auto;
  }
}
```

---

### Responsive Breakpoints
- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: >= 1024px

---

### Key Design Principles
- All text overlays use `mix-blend-mode: exclusion` to remain visible against both light and dark backgrounds
- No visible scroll bar interaction -- entirely RAF-driven position tracking
- `pointer-events-none` on all overlaid UI elements
- `user-select: none` on root container
- Videos hidden (`visibility: hidden`) once scroll passes first viewport height
- Circle symbol randomizes on scroll (throttled to 80ms)
- Entry animations staggered: logo (0s), nav (0.15s), caption (0.3s), product info (0.45s)
