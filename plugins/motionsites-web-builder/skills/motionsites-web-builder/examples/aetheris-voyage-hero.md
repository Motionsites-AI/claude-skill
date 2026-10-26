<!-- Aetheris Voyage · Hero Section · 859 likes · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260715_020834_841011fb-d336-4dcd-bbe6-493a895e4eb4.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=aetheris-voyage-hero -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build Prompt: Cinematic Space-Travel Landing Page
Build a single-page landing site with two full-height sections (Hero + Capabilities), both using looping background videos with custom JS crossfade, a shared liquid-glass design system, and Framer Motion entrance animations.

Tech stack (pinned, CDN-only)
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/react@18.3.1/umd/react.development.js" integrity="sha384-hD6/rw4ppMLGNu3tX5cjIb+uRZ7UkRJ6BPkLpg4hAu/6onKUg4lLsHAs9EBPT82L" crossorigin="anonymous"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" integrity="sha384-u6aeetuaXnQ38mYT8rp6sbXaQe3NL9t+IBXmnYxwkUI2Hw4bsp2Wvmx4yRQF1uAm" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" integrity="sha384-m08KidiNqLdpJqLq95G/LEi8Qvjl/xUYll3QILypMoQ65QorJ9Lvtp2RXYGBFj1y" crossorigin="anonymous"></script>
<script src="https://unpkg.com/framer-motion@11.11.17/dist/framer-motion.js"></script>
<script>window.Motion = window.FramerMotion;</script>
Body is bg: #000. Page is a React app mounted on #root, all components are <script type="text/babel"> files exporting via window.X = X.

Fonts
Google Fonts:

family=Instrument+Serif:ital@0;1&family=Barlow:wght@300;400;500;600
Tailwind config adds:

font-heading → 'Instrument Serif', serif (always italic in use)
font-body → 'Barlow', sans-serif
Default border radius override: DEFAULT: "9999px" (so bare rounded → pill).

Liquid-glass utilities (exact CSS, in a <style> block)
Two variants — .liquid-glass (subtle, for nav/chips/cards) and .liquid-glass-strong (heavier blur, for primary CTA):

.liquid-glass {
background: rgba(255,255,255,0.01);
background-blend-mode: luminosity;
backdrop-filter: blur(4px);
-webkit-backdrop-filter: blur(4px);
border: none;
box-shadow: inset 0 1px 1px rgba(255,255,255,0.1);
position: relative;
overflow: hidden;
}
.liquid-glass::before {
content: "";
position: absolute; inset: 0;
border-radius: inherit;
padding: 1.4px;
background: linear-gradient(180deg,
rgba(255,255,255,0.45) 0%,
rgba(255,255,255,0.15) 20%,
rgba(255,255,255,0) 40%,
rgba(255,255,255,0) 60%,
rgba(255,255,255,0.15) 80%,
rgba(255,255,255,0.45) 100%);
-webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
-webkit-mask-composite: xor;
mask-composite: exclude;
pointer-events: none;
}
.liquid-glass-strong { /* same but: */
backdrop-filter: blur(50px);
box-shadow: 4px 4px 4px rgba(0,0,0,0.05), inset 0 1px 1px rgba(255,255,255,0.15);
}
.liquid-glass-strong::before { /* same but 0.5 / 0.2 / 0 / 0 / 0.2 / 0.5 stops */ }
FadingVideo component (custom JS crossfade, no CSS transitions)
Wraps a <video autoPlay muted playsInline preload="auto"> starting at opacity: 0. Behavior:

FADE_MS = 500, FADE_OUT_LEAD = 0.55 seconds.
fadeTo(target, duration) uses requestAnimationFrame; reads current opacity from http://video.style.opacity so each new fade resumes from wherever the last one left off. Each call calls cancelAnimationFrame on the previous rAF id before starting.
On loadeddata: set opacity 0, play(), fadeTo(1).
On timeupdate: if fadingOutRef not set and duration - currentTime <= 0.55 and > 0, flip the ref and fadeTo(0).
On ended: set opacity 0; after setTimeout(100ms) reset currentTime = 0, play(), clear fadingOutRef, fadeTo(1).
loop attribute is OFF (we implement looping manually via ended).
Cleanup on unmount: cancel rAF, remove listeners.
Section 1 — Hero (full viewport, black bg)
Background video (120% width/height, top-aligned, centered horizontally — focal point is the top of frame):

src: https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260418_080021_d598092b-c4c2-4e53-8e46-94cf9064cd50.mp4
class: absolute left-1/2 top-0 -translate-x-1/2 object-cover object-top z-0
style: { width: "120%", height: "120%" }
No overlay. z-10 layer holds: Navbar → Hero content (flex-1, centered) → Partners.

Navbar (fixed top-4, px-8 / lg:px-16, z-50)
Left: 48×48 liquid-glass circle with italic serif lowercase "a" (Instrument Serif).
Center (desktop only): liquid-glass pill, px-1.5 py-1.5, holding 5 text links — Home, Voyages, Worlds, Innovation, Plan Launch — each px-3 py-2 text-sm font-medium text-white/90 font-body. Followed by a white pill button Claim a Spot + ArrowUpRight icon (bg-white text-black, whitespace-nowrap).
Right: 48×48 invisible spacer to balance logo.
Hero content (centered, pt-24 px-4)
All animated with Framer Motion, initial: {filter: blur(10px), opacity: 0, y: 20}, easeOut.

Badge (delay 0.4s): liquid-glass rounded-full pill. Contains white pill chip "New" (bg-white text-black px-3 py-1 text-xs font-semibold) + text "Maiden Crewed Voyage to Mars Arrives 2026" (text-sm text-white/90, pr-3).
Headline — BlurText component (word-by-word animation, see below). Text: "Venture Past Our Sky Across the Universe". Classes: text-6xl md:text-7xl lg:text-[5.5rem] font-heading italic text-white leading-[0.8] max-w-2xl justify-center tracking-[-4px].
Subheading (delay 0.8s, mt-4 text-sm md:text-base text-white max-w-2xl font-body font-light leading-tight): "Discover the universe in ways once unimaginable. Our pioneering vessels and breakthrough engineering bring deep-space exploration within reach—secure and extraordinary."
CTAs (delay 1.1s, flex items-center gap-6 mt-6):
Primary: liquid-glass-strong rounded-full px-5 py-2.5 text-sm font-medium text-white with "Start Your Voyage" + ArrowUpRight (h-5 w-5).
Secondary: bare text link, "View Liftoff" + Play icon (h-4 w-4, filled).
Stats row (delay 1.3s, flex items-stretch gap-4 mt-8): two liquid-glass cards, p-5 w-[220px] rounded-[1.25rem], each:
Top: white 28×28 outline SVG icon (clock for card 1, globe for card 2).
Bottom: large number in Instrument Serif italic white (text-4xl tracking-[-1px] leading-none): "34.5 Min" / "2.8B+". Label below (text-xs text-white font-body font-light mt-2): "Average Videos Watch Time" / "Users Across the Globe".
Partners (bottom of hero, delay 1.4s)
flex flex-col items-center gap-4 pb-8:

liquid-glass rounded-full chip (px-3.5 py-1 text-xs font-medium text-white): "Collaborating with top aerospace pioneers globally".
Row of 5 names in Instrument Serif italic white, text-2xl md:text-3xl tracking-tight, gap-12/md:gap-16: Aeon · Vela · Apex · Orbit · Zeno.
BlurText component (word-by-word blur-in)
IntersectionObserver triggers on 10% visibility. Splits text by spaces. Each word is a motion.span with:

initial: {filter: 'blur(10px)', opacity: 0, y: 50}
3-step keyframes to {filter: 'blur(5px)', opacity: 0.5, y: -5} → {filter: 'blur(0px)', opacity: 1, y: 0}
duration: 0.7 (stepDuration 0.35 × 2), times: [0, 0.5, 1], ease: easeOut
Stagger: delay = (i * 100) / 1000 seconds
display: inline-block, marginRight: 0.28em (not non-breaking-space — letter-spacing -4px eats nbsp).
Parent <p> is display: flex; flexWrap: wrap; justifyContent: center; rowGap: 0.1em.
Section 2 — Capabilities (min-h-screen, black bg)
Background video (full-bleed, no 120% scale):

src: https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260418_094631_d30ab262-45ee-4b7d-99f3-5d5848c8ef13.mp4
class: absolute inset-0 w-full h-full object-cover z-0
Same FadingVideo treatment. No overlay.

Content (relative z-10 px-8 md:px-16 lg:px-20 pt-24 pb-10 flex flex-col min-h-screen):

Header (mb-auto):

Kicker: text-sm font-body text-white/80 mb-6 → // Capabilities
Heading: font-heading italic text-white text-6xl md:text-7xl lg:text-[6rem] leading-[0.9] tracking-[-3px]:
Production
evolved
(two lines, <br/> between).
Three cards (grid grid-cols-1 md:grid-cols-3 gap-6 mt-16): each is liquid-glass rounded-[1.25rem] p-6 min-h-[360px] flex flex-col.

Top row of each card (flex items-start justify-between gap-4):

Left: 44×44 nested liquid-glass square (rounded-[0.75rem]) with a white Material Icons SVG (fill currentColor, h-6 w-6 text-white). Use random Material icons — these three used:
AI Scenery: image icon — path M5 21q-.825 0-1.412-.587T3 19V5q0-.825.588-1.412T5 3h14q.825 0 1.413.588T21 5v14q0 .825-.587 1.413T19 21H5Zm1-4h12l-3.75-5-3 4L9 13l-3 4Z
Batch Production: movie icon — path M4 6.47 5.76 10H20v8H4V6.47M22 4h-4l2 4h-3l-2-4h-2l2 4h-3l-2-4H8l2 4H7L5 4H4c-1.1 0-1.99.89-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V4Z
Smart Lighting: lightbulb icon — path M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1Zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7Z
Right: flex flex-wrap justify-end gap-1.5 max-w-[70%] — 4 small liquid-glass pill tags (rounded-full px-3 py-1 text-[11px] text-white/90 font-body whitespace-nowrap):
Card 1: Natural Context · Photo Realism · Infinite Settings · Eco-Vibe
Card 2: Scale Fast · Visual Consistency · Time Saver · Ready to Post
Card 3: Ray Tracing · Physical Shadows · Studio Quality · Sunlight Sync
Middle: flex-1 spacer.

Bottom of each card (mt-6):

Title h3: font-heading italic text-white text-3xl md:text-4xl tracking-[-1px] leading-none — "AI Scenery" / "Batch Production" / "Smart Lighting"
Body p (mt-3 text-sm text-white/90 font-body font-light leading-snug max-w-[32ch]):
"AI analyzes your product to create indistinguishable natural environments — from Icelandic cliffs to misty forests."
"Style your entire product line in minutes. Create a unified visual identity for catalogues and social media without weeks of retouching."
"Automatic lighting and material adjustment. Achieve flawless integration with realistic shadows and sunlight."
Icons (inline lucide-style SVGs, currentColor stroke)
ArrowUpRight: 24×24, M7 17L17 7 + M7 7h10v10, strokeWidth 2, round caps.
Play: 24×24 filled polygon 6 4 20 12 6 20 6 4.
Notes
All text white; no green, no gradient backgrounds.
No CSS transitions on the videos — fades must be rAF-driven per the FadingVideo spec.
Videos are full-bleed with no dark overlay; contrast comes from the liquid-glass chrome.
Framer Motion dev warnings about list keys can be suppressed with a console.error filter wrapper — they're benign.
The detailed prompt above captures every element, style, animation, video URL, and font to recreate the landing page exactly.
