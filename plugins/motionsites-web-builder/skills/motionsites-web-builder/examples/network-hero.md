<!-- Network Hero · Hero · 384 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=network-hero · Source: https://motionsites.ai/?prompt=network-hero -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Create a single-page React + Vite landing page for "Marketeam" -- a marketing talent platform. Use Inter (400, 500, 600, 700) and Urbanist (600, 700) from Google Fonts. The page is a full-viewport hero with a header, left content area, right animated circles visualization, and a bottom logo ticker strip.

---

### Background

Full-page background image covering the entire viewport:
```
https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260624_111401_56af5012-2263-45d3-849a-8688084d7c2a.png&w=1280&q=85
```
Applied as `background: url(...) center center / cover no-repeat` on the root `.app` container.

---

### Header

- Flexbox row, `justify-content: space-between`, padding `24px 64px`, max-width `1920px`, centered.
- **Left side**: Logo image + nav links
  - Logo: `<img>` with height 32px from: `https://polo-pecan-73837341.figma.site/_assets/v11/17ae538989a509947a8de3892c644664895e69b1.png`
  - Nav links: "Your Team", "Solutions", "Blog", "Pricing" -- color `#000000`, 15px, font-weight 400, with underline animation on hover (scaleX from 0 to 1, transform-origin left, 0.3s ease).
- **Right side**: "Log In" link + "Join Now" button
  - Log In: color `#ffffff`, 15px, weight 500, same underline hover as nav but white.
  - Join Now: pill button (border-radius 50px), black bg (`#000000`), white text, padding `12px 26px`, 15px, weight 500. On hover a `#A068FF` fill slides in from left using `::after` with `translateX(-100%)` to `translateX(0)`, cubic-bezier(0.22, 1, 0.36, 1), 0.4s. Button uses `overflow: hidden`.
  - The button is wrapped in a `.btn-border-wrap` div that has a rotating conic-gradient border using `::before` with `inset: -3px`, `padding: 3px`, mask technique for border-only effect. The gradient is: `conic-gradient(from var(--border-angle), #A068FF, #070319, #A068FF, #070319, #A068FF)`. It rotates via CSS `@property --border-angle` from `0deg` to `360deg` in 3s linear infinite.

---

### Hero Left

- `flex: 0 1 600px`, `padding-top: 40px`
- **Heading**: Typewriter effect, font Urbanist, 64px, weight 600, line-height 64px, letter-spacing -1.5px. Text: "Unlock Top Marketing Talent You Thought Was Out of Reach -- Now Just One Click Away!". The first 67 characters are colored `#000000`, the rest `#ffffff`. A blinking purple cursor (`#A068FF`) appears during typing. Typing speed: 35ms per character, starts after 400ms delay.
- **"Start Project" button**: Same pill style as Join Now but slightly larger (padding `14px 28px`, 16px), bg `#060218`. Has a right-arrow chevron SVG icon (18x18). Hover fill slides from right (`translateX(100%)` to `translateX(0)`). Also wrapped in `.btn-border-wrap` with the same rotating gradient border. Appears after typing finishes (animation-delay 3.2s).
- **Cursor element**: A purple cursor icon (SVG: pointer arrow filled `#A068FF`) + "David" label (pill badge, bg `#A068FF`, white text, 16px, weight 500, padding `8px 16px`, border-radius 20px). Positioned `margin-left: 290px`, `margin-top: 40px`. Appears with animation-delay 3.6s.

---

### Hero Right -- Circles Visualization

- Container: `720x720px`, centered.
- 4 concentric circles (orbits), each rotating slowly:
  - Orbit 1 (innermost): 353px diameter, spins left (counterclockwise) 30s
  - Orbit 2: 501px diameter, spins right 40s
  - Orbit 3: 649px diameter, spins right 50s
  - Orbit 4 (outermost): 797px diameter, spins left 60s
- Each circle has a 1px gradient border: `linear-gradient(180deg, rgba(217, 161, 255, 0) 0%, rgba(217, 161, 255, 1) 43%, rgba(217, 161, 255, 0) 100%)` applied via the mask technique.
- **Center circle (orbit-1)**: Displays an animated count-up number "20k+" (Urbanist 64px, weight 500) and "Specialists" label (Urbanist 16px, weight 600). Counter-rotates to stay upright.
- **Avatars** placed on orbits using `transform: translate(-50%, -50%) rotate(Xdeg) translate(radius) rotate(-Xdeg)`:
  - Avatar images (58px default, some 78px/88px) from these URLs:
    - `https://polo-pecan-73837341.figma.site/_assets/v11/aa51718fb3af3637e6d666b6543fc27a175fada6.png` (orbit 1, at 270deg, 177px radius, square with border-radius 20px, purple glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/ca755f7f93c1126fb8bdbf99ab364a33aa9ab272.png` (orbit 2, at 60deg, 251px, round, yellow glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/dc01064c7093dcc32674876ee3cf5e41c4a485c6.png` (orbit 2, at 180deg, 251px, 78px, pink glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/d5470a58b02388336141575048720f19a50de832.png` (orbit 2, at 300deg, 251px, square border-radius 20px, blue glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/018736aa5d0275c4ce56cfebaf2ae3007d81ca1e.png` (orbit 3, at 130deg, 325px, 88px, pink glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/c76d8a0b99676de31c014344bfaf75bad090758d.png` (orbit 4, at 30deg, 399px, purple glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/7b1b5f039de7b54cc9913e96c1923c3b15a157fa.png` (orbit 4, at 95deg, 399px, 88px, square border-radius 24px, orange glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/9ae171d8895199349755c43fbff00e122221a027.png` (orbit 4, at 220deg, 399px, 88px, square border-radius 24px, pink glow)
    - `https://polo-pecan-73837341.figma.site/_assets/v11/926c9eb7b4bc1df846fa0e39f0b0dc3fefd80671.png` (orbit 4, at 320deg, 399px, purple glow)
  - Each avatar has a staggered fly-in animation (scale 0.3 + rotate -180deg + blur -> normal), delays from 0.6s to 2.3s.

---

### Logo Ticker (Bottom)

- Horizontal infinitely scrolling strip of partner logos, `gap: 64px`, 20s animation.
- Fade masks on left/right edges (linear-gradient mask).
- 5 unique SVG logos repeated 4x for seamless loop:
  - `https://polo-pecan-73837341.figma.site/_assets/v11/1e7b0e6fcc016cd28aec5c68990118b8c54c35a5.svg`
  - `https://polo-pecan-73837341.figma.site/_assets/v11/3eac03c183db2ae080d910159211c14843398b61.svg`
  - `https://polo-pecan-73837341.figma.site/_assets/v11/17705a4c0023a0e5a99154dfb10582adbbf4260b.svg`
  - `https://polo-pecan-73837341.figma.site/_assets/v11/0e5f442b09dc5c248e3e60d40a65505fb1887228.svg`
  - `https://polo-pecan-73837341.figma.site/_assets/v11/63f99030ceb459e3c9ab9e429cfa2353491d3816.svg`
- Each logo: `width: 137px`, `height: 40px`, `object-fit: contain`.

---

### Entrance Animations

- Header: fade-down (translateY -20px to 0, 0.8s)
- Hero left: fade-up (translateY 40px to 0, 1s)
- Hero right circles: scale-in (scale 0.85 to 1 + opacity, 1.2s, delay 0.3s)
- Logos section: fade-up, delay 0.6s
- All using `cubic-bezier(0.22, 1, 0.36, 1)` easing.

---

### Responsive Breakpoints

- **1280px**: circles scale 0.85
- **1024px**: stack layout (flex-direction column), heading 48px, circles scale 0.7, nav gap shrinks
- **768px**: hide nav, heading 36px, circles scale 0.5
- **480px**: heading 28px, circles scale 0.4, smaller buttons/logos

---

### Key Colors

- Primary accent: `#A068FF`
- Background dark: `#060218` / `#070319`
- Text dark: `#000000`
- Text light: `#ffffff`
- Body bg fallback: `#0a0a0a`

---

### Technical Details

- React (useState, useEffect, useRef), Vite build
- Custom `useCountUp` hook: animates 0 to 20 over 2s with easeOutCubic, starts after 1.2s delay
- `TypewriterHeading` component: types char by char at configurable speed
- CSS `@property --border-angle` for the animated border gradient
- No external animation libraries -- pure CSS animations + JS for typewriter/counter
