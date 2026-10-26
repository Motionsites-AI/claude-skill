<!-- Intelligent Operations · Agency · 387 likes · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260730_075859_52d1611f-168a-44ed-8222-ba56da2755fa.png&w=1920&q=85 · Source: https://motionsites.ai/?prompt=intelligent-operations -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

# Exact recreation prompt — NovaAI landing page

Recreate this page **pixel-faithfully**. Stack: React + TypeScript + Vite + Tailwind CSS + lucide-react. Do not invent alternate copy, layout, fonts, colors, or effects.

---

## Page identity

- **Title:** `NOVA_AI — Today AI Aligns With Bold Dreams`
- **Brand:** lowercase `novaai` with a Lucide `Hexagon` icon (size 24, strokeWidth 1.5) to the left
- **Overall feel:** dark cinematic AI marketing site; full-viewport scroll-scrubbed video background; white typography with drop shadows; frosted glass UI chips; sparse editorial layout; no purple gradients, no cream paper look, no card grids of icons

---

## Assets (use these exact URLs)

**Hero scroll video (CloudFront — required):**
```
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260729_102822_0e6c87e8-c141-4744-bf32-ad30db296371.mp4
```
Video content: abstract 3D forms (hanging white cables with glowing gold tips → organic white spherical / brain-like folds with warm orange core), soft blue-grey mist / grain background, floating bokeh particles. 1920×1080.

**Optional local mirrors for reliability:** `/hero.mp4` (same file) and `/hero-poster.jpg` (first-frame still). Prefer CloudFront URL in production code; local copy is fine for offline/dev.

**Portrait (“Talk with Mitha”) — exact URL:**
```
https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260728_050334_5b076e26-0ce7-4898-b432-d764190e448f.png&w=1280&q=85
```
Display as `h-24 w-20` (`96×80px`), `rounded-lg`, `object-cover`. Alt: `Mitha, co-founder of NovaAI`.

---

## Fonts

- Load Google Fonts Inter weights **400, 500, 600, 700**
- Body: `font-family: 'Inter', system-ui, sans-serif`
- Tailwind: both `font-sans` and `font-mono` map to Inter (mono labels still use `font-mono` class but render Inter)
- Antialiased text; selection color `rgba(255,255,255,0.2)`
- Page bg: `#0a0a0a`; default text white

---

## Global structure

```
relative root
  ScrollVideo (fixed inset-0 z-0, pointer-events-none)
  relative z-10 wrapper
    Navbar (fixed top)
    main
      SectionOne (min-h-screen / 100svh)
      spacer div h-[80vh] (aria-hidden)  ← critical for scroll video length
      SectionTwo (min-h-screen / 100svh)
```

Horizontal padding rhythm everywhere: `px-5 sm:px-8 md:px-12`.  
Section top padding under fixed nav: `pt-24 sm:pt-28`.  
Bottom padding: `pb-12 md:pb-16`.

---

## Scroll-scrubbed video background (exact behavior)

Fixed full-bleed layer `z-0`, bg `#0a0a0a`, `overflow-hidden`, `pointer-events-none`.

**Layers (bottom → top):**
1. Poster `<img>` — full cover; fades out (`opacity-0`, 500ms) once video has a decoded frame or frame cache is ready
2. `<video>` — muted, playsInline, preload=auto, object-cover; visible only while video has a frame and canvas frame-cache is not ready; then fade out
3. `<canvas>` — full cover; draws scrubbed frames; fades in when ready

**Scroll mapping:**
- `progress = scrollY / (scrollHeight - innerHeight)`, clamped 0–1
- Smooth with lerp: `smoothed += (target - smoothed) * 0.12` each `requestAnimationFrame`
- Draw with **object-cover** math (scale max, center crop)

**Frame cache (preferred smooth path):**
- Offscreen video loads same URL
- Extract up to **90** frames (or `duration * 12`, min 24), max width **960px**
- Wait until visible video has `loadeddata` + 300ms yield before extraction starts
- On ready, canvas draws cached `ImageBitmap`s by smoothed progress index

**Fallback:** seek the visible `<video>` to `smoothed * (duration - 0.05)` when frames aren’t ready (seek if delta > 0.04s)

**Canvas DPR:** `min(devicePixelRatio, 2)`

Do **not** autoplay as a normal looping background — motion is **scroll-driven only**.

---

## Reveal animation (every text/UI block)

IntersectionObserver, threshold `0.15`.  
Hidden: `translate-y-8 opacity-0`  
Visible: `translate-y-0 opacity-100`  
Transition: `all 700ms ease-out`, `will-change-transform`  
Per-element `transition-delay` in ms as specified below.

---

## Glass / material system (exact tokens)

Reuse these consistently:

| Token | Classes |
|--------|---------|
| Glass panel | `bg-white/15 backdrop-blur-md` (or `bg-white/10` for larger panels) |
| Glass border | `border border-white/15` or `border-white/20` or `border-white/25` |
| Left-accent badge | `border-l-2 border-white bg-white/15 px-3 py-1.5 backdrop-blur-md` + mono uppercase label |
| Primary CTA | solid white pill/rounded, black text, hover `bg-white/85` |
| Secondary CTA | glass border + `bg-white/10` or `bg-white/15`, white text |
| Text over video | white + `drop-shadow-md` / `drop-shadow-lg` |
| Mono labels | `font-mono text-[10px]` or `text-[11px]` or `text-xs`, `uppercase`, `tracking-[0.15em]` |

---

## Navbar (fixed, z-50)

- Full width, `border-b border-white/15`
- Row: logo left | center nav (md+) | CTA right
- Logo: Hexagon + `novaai` (`text-lg sm:text-xl font-medium tracking-tight`)
- Links (hidden below md): `Projects` with superscript `6` (`font-mono text-[10px] text-white/60`), `About`, `Blog`, `Contact` — `text-sm text-white/85`, hover `text-white`, gap `gap-8 lg:gap-10`
- CTA: `Get Free Consultation` — `rounded-md border border-white/20 bg-white/15 backdrop-blur-md px-4 py-2 text-xs sm:px-5 sm:text-sm`, hover `bg-white/25`
- Reveal delays: logo 0; links `100 + i*100` ms; CTA `500` ms

---

## Section One — Hero

Full viewport flex column `justify-between`.

**Top row** (`flex-col gap-8` → `sm:flex-row justify-between`):

**Left — service list** (gap-2), each reveal delay `150 + i*120`:
```
/ AI AUTOMATION
/ AI INTEGRATION
/ AI AGENT DEVELOPMENT
```
Style: `font-mono text-xs uppercase tracking-[0.15em] text-white/90 drop-shadow-md`

**Right — intro** (`max-w-xs sm:text-right`, delay 300):
> We design automation that brings clarity, precision, and efficiency to the way your company operates.  
`text-lg sm:text-xl leading-relaxed text-white drop-shadow-md`

**Bottom row** (`flex-col gap-8` → `md:flex-row items-end justify-between`):

**Left:**
1. Badge delay 150: `We Automate 100+ Businesses` — left-accent glass badge, `font-mono text-[11px] uppercase tracking-[0.15em]`, `mb-5`
2. H1 delay 280:
```
Clear. Precise.
Automated.
```
`text-5xl sm:text-6xl lg:text-7xl font-normal leading-[1.05] tracking-tight text-white drop-shadow-lg`

**Right — glass contact card** (delay 420):
- Container: `flex items-center gap-4 rounded-xl bg-white/15 p-3 backdrop-blur-md`
- Image: portrait URL above, `h-24 w-20 rounded-lg object-cover`
- Text column (`gap-1.5 pr-2`):
  - `Talk with Mitha` — `text-sm font-medium text-white`
  - `Co-founder of NovaAI` — mono `text-[10px] uppercase tracking-[0.15em] text-white/60`
  - Button: `Book 15-mins call` + Lucide `ChevronRight` size 14 — `rounded-full bg-white px-4 py-2 text-xs font-medium text-black`, hover `bg-white/85`, `mt-1.5`

---

## Mid spacer

`div` with `h-[80vh]` between sections so scroll progress has room to scrub the video between hero and section two.

---

## Section Two — Capability

Same full-viewport flex `justify-between` shell.

**Top row:**

**Left badge** delay 120: `Insight On Demand` — same left-accent glass badge as hero.

**Right copy** delay 220 (`max-w-sm sm:text-right`):
> Our AI doesn't just respond — it interprets, sharpens, and delivers the signal you need.  
`text-lg sm:text-xl leading-relaxed text-white drop-shadow-md`

**Bottom area** (`flex-1 justify-end`, `flex-col gap-12` → `md:flex-row items-end justify-between gap-16`):

**Left column** (`max-w-xl`):
1. H2 delay 180:
```
Learn to see
brilliantly.
```
Same headline scale as H1 (`text-5xl sm:text-6xl lg:text-7xl … drop-shadow-lg`)
2. Body delay 320 (`mt-6 max-w-md text-sm sm:text-base text-white/80 drop-shadow-md`):
> From the first sketch to the final render, Nova turns raw intent into decisions your team can act on — quietly, precisely, at speed.
3. CTAs delay 420 (`mt-8 flex flex-wrap gap-3`):
   - Primary pill: `Run the demo` + ChevronRight 14 — `rounded-full bg-white px-5 py-2.5 text-xs sm:text-sm font-medium text-black`, hover `bg-white/85`
   - Secondary: `Free consultation` — `rounded-full border border-white/25 bg-white/10 backdrop-blur-md px-5 py-2.5 text-xs sm:text-sm`, hover `bg-white/20`

**Right — frosted capability panel**  
`w-full max-w-md rounded-2xl border border-white/15 bg-white/10 backdrop-blur-md px-5 sm:px-6`

Three rows (dividers `border-b border-white/15` except last), each `flex gap-5 py-5`, reveal delay `300 + i*110`:

| # | Title | Body |
|---|--------|------|
| 01 | Real-time vision | Reads context as it happens and surfaces what matters before you ask. |
| 02 | Layered insight | Moves from rough outline to sharp output without losing the thread. |
| 03 | Adaptive speed | Learns your cadence and tightens every pass as you work. |

- Index: `font-mono text-[11px] tracking-[0.15em] text-white/55`
- Title: `text-base sm:text-lg font-medium text-white` + ChevronRight 16 (`text-white/40`, hover: translate-x-0.5 + `text-white`)
- Body: `mt-1.5 text-sm leading-relaxed text-white/70`

---

## Interactions / motion checklist

1. Scroll scrub maps page scroll → video timeline (smoothed)
2. Staggered fade-up reveals on enter viewport (700ms, per-delay)
3. Button / link color transitions `duration-300`
4. Capability chevrons nudge right on hover
5. Poster → video → canvas opacity crossfades `duration-500`
6. No looping autoplay of hero video

---

## Responsive rules

- Nav links hidden below `md`
- Hero/section stacks vertically on mobile; side-by-side from `sm`/`md` as specified
- Prefer `supports-[height:100svh]:min-h-[100svh]` plus `min-h-screen`
- Touch: video `playsInline` + muted

---

## Do not

- Do not replace Inter with another display font
- Do not use a different video URL than the CloudFront URL above
- Do not use the old Pexels portrait
- Do not rebuild section two as icon card stacks
- Do not put opaque solid backgrounds over the video (only glass / transparent wrappers)
- Do not remove the `80vh` spacer

---

## Acceptance

Top of page: fixed glass nav + service list + intro + “Clear. Precise. Automated.” + Mitha glass card over scroll video.  
Scrolling scrubbing advances the CloudFront video smoothly.  
After spacer: “Insight On Demand” + “Learn to see brilliantly.” + dual CTAs + three-item frosted capability panel.  
Visual match to current NovaAI page at `localhost:5199`.
