<!-- USD Halo · Landing Page · 382 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=halo-usd-landing · Source: https://motionsites.ai/?prompt=halo-usd-landing -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a premium, fintech-style landing page for a stablecoin product called "Halo / USD Halo" using React + TypeScript + Vite + Tailwind CSS, with lucide-react for icons. No other UI libraries. Background color of the page is #F5F5F5.

Global Setup
Use TT Norms Pro as the primary font, loaded via @font-face from /fonts/tt-norms-pro-regular.woff2 (weight 400) and /fonts/tt-norms-pro-semibold.woff2 (weight 600), with font-display: swap. Apply it to html, body, and inherit on *.
Tailwind base + components + utilities at the top of src/index.css.
Page wrapper: flex flex-col bg-[#F5F5F5]. The first section (Navbar + Hero) is wrapped in a h-screen flex flex-col overflow-hidden container.
Inner content max width across sections: max-w-[88rem] mx-auto.
Custom Logo Icon
Create an SVG component LogoIcon using currentColor, viewBox 0 0 256 256, with this path (a stylized "halo" mark made of two interlocking rounded squares):


M 128.005 191.173 C 128.448 156.208 156.93 128 192 128 L 192 64 L 128 64 C 128 99.346 99.346 128 64 128 L 64 192 L 128 192 Z M 192 256 L 64 256 C 28.654 256 0 227.346 0 192 L 0 64 L 64 64 L 64 0 L 192 0 C 227.346 0 256 28.654 256 64 L 256 192 L 192 192 Z
1. Navbar (absolute, transparent over hero)
nav is absolute top-0 left-0 right-0 z-20 px-6 py-5.
Inner row: flex items-center justify-between.
Left: LogoIcon (w-7 h-7, black) + word "Halo" (text-2xl font-medium tracking-tight text-black).
Center (hidden below md): links Network · Ecosystem · Rewards · Help · News, gap-8, text-base text-gray-700 hover:text-black font-medium transition-colors duration-200.
Right: black pill button "Open Wallet" — bg-black text-white text-base font-medium px-7 py-2.5 rounded-full hover:bg-gray-800 transition-colors duration-200.
2. Hero Section
Outer: flex-1 px-6 pt-20 pb-6 flex items-end.
Inner card: relative w-full rounded-2xl overflow-hidden, inline style height: calc(100vh - 96px).
Background video (autoplay, muted, loop, playsInline, object-cover absolute inset-0 w-full h-full): 
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260423_161253_c72b1869-400f-45ed-ac0c-52f68c2ed5bd.mp4

Content overlay: relative z-10 flex flex-col items-start justify-start h-full p-12 pt-36.
h1: "Your Wealth\nWorks" (with <br/>) — text-black text-5xl md:text-6xl font-medium leading-tight max-w-xl mb-4, inline letterSpacing: '-0.04em'.
p: "An automated, reward-powered digital dollar built for native passive earnings and effortless connection into DeFi." — text-black/70 text-base md:text-lg max-w-md mb-8 leading-relaxed, inline fontFamily: "'Inter', ui-sans-serif, system-ui, sans-serif".
Pill button "Join us" with arrow circle: inline-flex items-center gap-3 bg-black text-white text-base md:text-lg font-medium pl-8 pr-2 py-2 rounded-full hover:bg-gray-800. Trailing arrow inside bg-white rounded-full p-2, using ArrowRight w-5 h-5 text-black from lucide-react.
Followed by the Brand Marquee below.
Brand Marquee (inside hero, below button)
Container: mt-24 w-full max-w-md overflow-hidden.
Inject scoped <style> with keyframes marquee translating 0 → -50%, applied to .marquee-track { display:flex; width:max-content; animation: marquee 22s linear infinite; }.
Render the brand list twice (so it loops seamlessly).
Each item: mx-7 shrink-0 text-black/60 whitespace-nowrap with these inline styles:
Stripe — Georgia serif, weight 700, letterSpacing -0.02em, fontSize 15px
Coinbase — Arial sans, weight 900, letterSpacing 0.08em, fontSize 13px, uppercase
Uniswap — Trebuchet MS, weight 600, letterSpacing 0.01em, fontSize 15px, italic
Aave — Courier New monospace, weight 700, letterSpacing 0.12em, fontSize 13px, uppercase
Compound — Palatino, Book Antiqua, weight 400, letterSpacing -0.01em, fontSize 16px
MakerDAO — Impact, Arial Narrow, weight 400, letterSpacing 0.04em, fontSize 14px
Chainlink — Verdana, weight 700, letterSpacing -0.03em, fontSize 13px
3. Info Section ("Meet USD Halo.")
section bg-[#F5F5F5] px-6 py-24.
Row 1: 2-col grid (grid-cols-1 md:grid-cols-2 gap-12 mb-16 items-start).
Left: h2 "Meet USD Halo." — text-black text-4xl md:text-5xl font-medium leading-tight mb-8, letterSpacing -0.03em. Below it, black pill "Discover it" button with white arrow circle (same pattern as "Join us" but text-base).
Right: paragraph "USD Halo is a reward-earning dollar coin that lets your savings grow while remaining tied to the U.S. dollar." — text-black/70 text-2xl md:text-3xl leading-relaxed.
Row 2 — 4-col card grid (grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4):
Card 1 (spans 2 cols on lg): rounded-2xl with background image: 
https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260423_164207_f243351d-ed59-48ec-83a0-a5e996bdbe3c.png&w=1280&q=85

 backgroundSize: cover; backgroundPosition: center. Inside: p-7 min-h-80 flex flex-col justify-between. Title (top): "Savings that bloom" — text-black text-2xl font-medium leading-snug letterSpacing -0.02em. Body (bottom): "Gain steady returns as your dollar tokens are routed into top-performing DeFi strategies." — text-black/70 text-base max-w-xs.
Card 2: solid #2B2644, rounded-2xl, p-7, min-h-80, flex-col-justify-between. White heading "Always fluid,\nalways pegged." text-2xl font-medium, body "Keep fully dollar-anchored with on-demand access to funds — no lockups or waits." text-white/60 text-base.
Card 3: same #2B2644 styling. Heading "Fully\nautomated". Body "Skip the task of tuning positions yourself. USD Halo runs in the background for you."
4. Backed By Section (marquee row)
section bg-[#F5F5F5] px-6 with inner max-w-[88rem] mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 items-center.
Left col (1/4): text-black/70 text-base leading-relaxed — "Funded by premier partners\nand forward-thinking leaders."
Right col (3/4): infinite marquee (same pattern as hero marquee but 30s linear infinite, class .backers-track, keyframes backers-marquee). Items use mx-10 shrink-0 text-black/50 whitespace-nowrap with these inline styles:
Fundamental Labs — Times New Roman serif, 400, ls 0.02em, 14px
KUCOIN — Arial Black, 900, ls 0.08em, 16px
NGC — Impact, 700, ls 0.05em, 18px
NxGen — Georgia, 600, ls -0.02em, 17px
Matter Labs — Helvetica, 700, ls -0.01em, 15px
DEXTools — Verdana, 700, ls 0.06em, 14px, uppercase
NGRAVE — Courier New, 700, ls 0.18em, 14px
Polychain — Palatino, 500, ls 0.03em, 15px
Render brands twice for the loop.
5. Use Cases Section
section bg-[#F5F5F5] px-6 py-24. Inner: 2-col grid grid-cols-1 md:grid-cols-2 gap-8 items-start.
Left column (md:pr-12 md:pt-2):
Eyebrow: "USD Halo in Practice" — text-black/60 text-sm mb-2.
h2 "Use modes" — text-5xl md:text-6xl font-medium leading-none mb-6, ls -0.04em.
Paragraph: "USD Halo powers a wide range of modes for builders, companies and treasuries wanting safe and rewarding stablecoin integrations plus more" — text-black/60 text-base leading-relaxed max-w-sm.
Right column: large relative rounded-3xl overflow-hidden min-h-[720px] with background video (autoplay/muted/loop/playsInline, object-cover absolute inset-0): 
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260423_183428_ab5e672a-f608-4dcb-b319-f3e040f02e2d.mp4

Overlay content relative z-10 p-10 md:p-12:
h3 "Commerce" — text-4xl md:text-5xl font-medium leading-tight mb-5, ls -0.03em.
Paragraph: "Lift customer retention by offering USD Halo, a trusted dollar-backed stablecoin with strong yields, letting your patrons earn with zero effort on your platform." — text-black/70 text-base max-w-md mb-8.
Inline-flex link "Know more" with leading circular icon: w-9 h-9 rounded-full bg-white/80 backdrop-blur flex items-center justify-center group-hover:bg-white transition-colors containing ArrowRight w-4 h-4 text-black.
Animations & Interactions
Two CSS keyframe marquees (22s for hero brands, 30s for backers), both translating 0 → -50% on a duplicated track for seamless looping.
All buttons use transition-colors duration-200 with hover state hover:bg-gray-800 (or hover:bg-white for the white circle).
Nav links transition on hover from text-gray-700 to text-black.
Videos autoplay muted with playsInline for mobile compatibility.
Composition
App renders, in order:

h-screen overflow-hidden wrapper containing Navbar (absolute) + HeroSection.
InfoSection
BackedBySection
UseCasesSection
All section backgrounds are #F5F5F5. All headings use negative letter-spacing for the tight, modern fintech feel. Use font-medium (600) as the heaviest weight throughout.
