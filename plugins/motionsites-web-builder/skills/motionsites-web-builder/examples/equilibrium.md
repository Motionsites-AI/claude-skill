<!-- Equilibrium · Hero · 466 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=equilibrium · Source: https://motionsites.ai/?prompt=equilibrium -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a full-screen, single-page React + TypeScript + Vite + Tailwind CSS hero section with a "liquid glass" aesthetic on top of a looping background video. Use `lucide-react` for icons. No other UI libraries.

**Font & Global CSS (`src/index.css`):**
- Import Geist from Google Fonts: `https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&display=swap`
- Apply `Geist` globally via `* { font-family: 'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }`
- Include `@tailwind base; @tailwind components; @tailwind utilities;`
- Define a `.liquid-glass` class:
  - `background: rgba(255,255,255,0.01);`
  - `background-blend-mode: luminosity;`
  - `backdrop-filter: blur(4px);` plus `-webkit-backdrop-filter`
  - `border: none;`
  - `box-shadow: inset 0 1px 1px rgba(255,255,255,0.1);`
  - `position: relative; overflow: hidden;`
- Add a `.liquid-glass::before` pseudo-element creating a gradient border via mask compositing:
  - `content:''; position:absolute; inset:0; border-radius:inherit; padding:1.4px;`
  - `background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%, rgba(255,255,255,0) 40%, rgba(255,255,255,0) 60%, rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%);`
  - `-webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude; pointer-events:none;`

**Component (`src/App.tsx`):**
- Import from `lucide-react`: `ChevronDown`, `Infinity`, `Menu`, `X`. Import `useState` from React.
- Constant `BG_VIDEO = 'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260511_230229_7c9bc431-46cf-489a-948d-e8144d8eb5d4.mp4'`
- `navLinks` array: `{ label: 'Home', active: true }`, `{ label: 'Wellness', dropdown: true }`, `{ label: 'Routine' }`, `{ label: 'Our Team' }`.
- `menuOpen` state via `useState(false)`.

**Layout:**
- Root: `<div class="relative w-full h-screen overflow-hidden">`.
- Background `<video>` absolutely positioned, `w-full h-full object-cover`, `autoPlay muted loop playsInline`, `src={BG_VIDEO}`.

**Navbar** (`absolute top-0 left-0 right-0 z-20 flex items-center justify-between px-5 sm:px-8 py-5`):
- Logo (left): flex with `gap-2 text-white font-medium text-base`. `<Infinity size={22} strokeWidth={1.5} />` followed by `<span>Equilibrium</span>`.
- Nav pill (center, `hidden md:flex`): `liquid-glass items-center gap-1 rounded-xl px-2 py-2`. Map `navLinks`. Each button: `flex items-center gap-0.5 px-3 py-1.5 rounded-md text-sm transition-colors`; active gets `bg-white/15 text-white`, others `text-white/70 hover:text-white`. Dropdown items render a `<ChevronDown size={13} class="mt-px" />`.
- CTAs (right, `hidden md:flex items-center gap-3`):
  - "Log in": `liquid-glass text-white text-sm font-medium px-4 py-2.5 rounded-full hover:bg-white/5 transition-colors`
  - "Begin Now": `bg-white text-black text-sm font-medium px-4 py-2.5 rounded-full hover:bg-white/90 transition-colors`
- Mobile toggle (`md:hidden`): `liquid-glass text-white p-2 rounded-lg`; shows `X` when open else `Menu` (size 18).

**Mobile menu** (when `menuOpen`): `absolute top-[72px] left-4 right-4 z-30 md:hidden liquid-glass rounded-2xl p-4 flex flex-col gap-1`. Same nav links as buttons `flex items-center justify-between w-full px-4 py-3 rounded-lg text-sm`. Bottom CTA row: `flex gap-2 mt-2 pt-3 border-t border-white/10` with two `flex-1` buttons ("Log in", "Begin Now") matching desktop styles.

**Hero content (bottom-left)** `absolute bottom-0 left-0 z-20 px-6 sm:px-12 pb-10 sm:pb-16 max-w-2xl`:
- `<h1>`: `text-white text-4xl sm:text-5xl lg:text-6xl font-medium leading-tight tracking-tight mb-4` — text: `Live Better, Feel Whole Every Day`.
- `<p>`: `text-white/60 text-sm leading-relaxed mb-7 max-w-md` — text: `Take charge of how you feel with a companion built for your journey—build routines, follow your growth, and unlock tailored insights for a steadier, more vibrant life each day.`
- Buttons row `flex flex-wrap items-center gap-3`:
  - "Start Today": `bg-white text-black text-sm sm:text-base font-medium px-6 sm:px-7 py-3 rounded-full hover:bg-white/90 transition-colors`
  - "Discover How": `liquid-glass text-white text-sm sm:text-base font-medium px-6 sm:px-7 py-3 rounded-full hover:bg-white/5 transition-colors`

**Animations/interactions:** all buttons use Tailwind `transition-colors`; liquid-glass effect uses `backdrop-filter: blur(4px)` plus the animated-looking gradient border pseudo. No additional keyframe animations. The background video itself provides motion.

**Dependencies:** `react`, `react-dom`, `lucide-react`, `tailwindcss`, `vite`, `@vitejs/plugin-react`, TypeScript. Tailwind configured with default content globs for `./index.html` and `./src/**/*.{ts,tsx}`.
