<!-- Email Landing Page · Landing page · 544 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=email-landing-page · Source: https://motionsites.ai/?prompt=email-landing-page -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a premium, AI-native email client landing page called "Aura" using **React 18 + TypeScript + Vite + Tailwind CSS + motion/react (framer motion) + lucide-react**. The aesthetic is dark (bg `#0c0c0c`), cinematic, glassy, with a looping fullscreen background video, a shiny gradient headline, a macOS-style menu bar, a realistic inbox mockup, and a custom "liquid-glass" card treatment.

## Stack / setup

- `package.json` dependencies: `react`, `react-dom`, `@supabase/supabase-js`, `motion` (v12+, import from `motion/react`), `lucide-react`.
- Tailwind config extends colors with `brand: '#3D81E3'` and fontFamily sans with `['Inter','system-ui','sans-serif']`.
- Font: Google Fonts Inter weights 400, 500, 600, 700, 800, 900. Import in `index.css` via `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');`.
- `html,body { font-family: 'Inter', system-ui, sans-serif; -webkit-font-smoothing: antialiased; }`.
- Background color base `#0c0c0c`, text white, selection `bg-brand/30`.

## Global background video (fixed, behind everything)

Inside the root wrapper (`relative min-h-screen overflow-x-hidden bg-[#0c0c0c] text-white`), render a fixed full-screen video:

```
<div className="fixed inset-0 z-0 pointer-events-none">
  <video autoPlay loop muted playsInline
    className="w-full h-full object-cover pointer-events-none"
    src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260508_064122_c4750c0e-7476-4b44-94a2-a85a65c63bf2.mp4" />
</div>
```

Also render two hidden-on-mobile fixed vertical guide lines at the 36rem container edges:
```
<div className="hidden md:block pointer-events-none fixed inset-y-0 left-1/2 -translate-x-[calc(50%+36rem)] w-px bg-white/10 z-[5]" />
<div className="hidden md:block pointer-events-none fixed inset-y-0 left-1/2 translate-x-[calc(-50%+36rem)] w-px bg-white/10 z-[5]" />
```

## Global SVG noise filters (two, both id `c3-noise`)

- One at root level (subtle grain, multiply blend) for the shiny headline.
- One inside the pricing section (fractal noise, overlay blend) for the watermark.

Root filter:
```
<filter id="c3-noise">
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" />
  <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.35 0" />
  <feComposite in2="SourceGraphic" operator="in" result="noise" />
  <feBlend in="SourceGraphic" in2="noise" mode="multiply" />
</filter>
```

Pricing filter:
```
<filter id="c3-noise">
  <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="2" stitchTiles="stitch" />
  <feComponentTransfer><feFuncA type="linear" slope="0.075" /></feComponentTransfer>
  <feComposite in2="SourceGraphic" operator="in" result="noise" />
  <feBlend in="SourceGraphic" in2="noise" mode="overlay" />
</filter>
```

## Shared primitives

**AppleLogo** — inline SVG Apple mark, `viewBox="0 0 384 512"`, `fill="currentColor"`, default `w-4 h-4`. Path:
`M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z`.

**LogoMark** — abstract 4-quadrant curve mark, `viewBox="0 0 256 256"`, default `w-8 h-8`, white fill. Path:
`M 0 128 C 70.692 128 128 185.308 128 256 L 64 256 C 64 220.654 35.346 192 0 192 Z M 256 192 C 220.654 192 192 220.654 192 256 L 128 256 C 128 185.308 185.308 128 256 128 Z M 128 0 C 128 70.692 70.692 128 0 128 L 0 64 C 35.346 64 64 35.346 64 0 Z M 192 0 C 192 35.346 220.654 64 256 64 L 256 128 C 185.308 128 128 70.692 128 0 Z`.

**AppleButton** — rounded-full white pill, Apple logo + "Download Aura" label + ChevronRight. Chevron translates `+1px` on group hover. Classes: `group inline-flex items-center justify-center gap-2 rounded-full bg-white text-black font-medium text-sm px-5 py-3 transition-all hover:bg-white/90 active:scale-[0.98]`. Accepts `label` and `full` props.

**SectionEyebrow** — `<span className="w-1.5 h-1.5 rounded-full bg-white" />` + label, optional tag pill with `px-2 py-0.5 rounded-full border border-white/10 text-white/50`.

**gradientStyle** used on the headline word "Revitalized":
```
backgroundImage: 'linear-gradient(to right, #091020 0%, #0B2551 12.5%, #A4F4FD 32.5%, #00d2ff 50%, #0B2551 67.5%, #091020 87.5%, #091020 100%)'
backgroundSize: '200% auto'
WebkitBackgroundClip: 'text' (+ backgroundClip text)
color: 'transparent'; WebkitTextFillColor: 'transparent'
filter: 'url(#c3-noise)'
```

Shiny animation (`.animate-shiny`): 6s linear infinite, keyframes shiny `{0%: background-position: -200% center; 100%: 200% center;}`.

## Liquid-glass utility (used across cards)

```
.liquid-glass {
  background: rgba(255,255,255,0.01);
  background-blend-mode: luminosity;
  backdrop-filter: blur(4px);
  border: none;
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.1);
  position: relative; overflow: hidden;
}
.liquid-glass::before {
  content: ''; position: absolute; inset: 0; border-radius: inherit;
  padding: 1.4px;
  background: linear-gradient(180deg,
    rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%,
    rgba(255,255,255,0) 40%, rgba(255,255,255,0) 60%,
    rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
  pointer-events: none;
}
```

## Section 1 — Navbar

Max-width `max-w-6xl mx-auto px-6`. Motion nav fades/slides down (opacity 0 -> 1, y -10 -> 0, 0.6s easeOut). Left: just the `LogoMark` (NO "Aura" word). Center (`hidden md:flex gap-8`): links `['Solutions','Pricing','Blog','Documentation','Careers']` each `text-white/70 text-sm font-medium hover:text-white` with staggered y animation (delay 0.1 + i*0.05). Right desktop: `<AppleButton />` default label "Download Aura". Mobile right: `w-10 h-10 rounded-full border border-white/10 bg-white/5` Menu icon button.

## Section 2 — Hero

Centered section, `pt-16 md:pt-28 pb-20 text-center flex flex-col items-center`.
Motion h1 (delay 0.3, 0.8s cubic-bezier(.22,1,.36,1)), classes `text-4xl md:text-7xl font-semibold tracking-tight leading-[0.9]`:
- Line 1: "Your email." (white)
- Line 2: "Revitalized" — apply `animate-shiny` and the `gradientStyle` inline.

Then motion paragraph (delay 0.5): `mt-8 text-white/60 max-w-md text-base leading-[1.5]`:
> "Aura is the premier inbox platform for the current era. It leverages powerful AI to organize, prioritize, and refine your messages into total clarity."

Then motion div (delay 0.7) with `<AppleButton />` and `text-xs text-white/40` "Download for Intel / Apple Silicon".

## Section 3 — macOS menu bar strip

Full-width bar `h-10 bg-black/40 backdrop-blur-md border-t border-b border-white/10`. Inside `max-w-6xl mx-auto px-6 h-full flex items-center justify-between text-xs`. Left: `AppleLogo w-3.5 h-3.5`, bold white "Aura", then menu items `['File','Edit','View','Go','Window','Help']` (progressive hiding: index>2 `hidden sm:inline`, index>3 `hidden md:inline`). Right: `Search w-3.5 h-3.5` + "Wed May 6 1:09 PM". Enters with delay 0.9.

## Section 4 — Inbox mockup

`max-w-6xl mx-auto px-6 py-16 md:py-24`. Outer container `relative rounded-2xl overflow-hidden border border-white/10 bg-[#0e1014]/90 backdrop-blur-2xl`. Motion enters from y:40 at delay 1.1.

Title bar: three traffic lights `#ff5f57`, `#febc2e`, `#28c840` (each `w-3 h-3 rounded-full`); center label "Aura — Inbox" `text-xs text-white/50`.

Body `grid grid-cols-12 h-[520px]`:

**Sidebar (col-span-3, border-r, bg-black/30, p-4):**
- White "Compose with Aura" button with `Sparkles` icon (`rounded-lg bg-white text-black text-xs font-semibold px-3 py-2`).
- Nav items (icon + label + optional count): Inbox (12, active), Starred (3), Sent, Drafts (2), Archive, Trash. Active uses `bg-white/10 text-white`, others `text-white/60 hover:bg-white/5`.
- Labels section: uppercase tracking "Labels" small title, then 4 color dots: Work `#00d2ff`, Personal `#A4F4FD`, Travel `#f59e0b`, Finance `#10b981`.

**Message list (col-span-4, border-r):**
- Search header: `Search` icon + placeholder "Search mail".
- 6 messages with name, subject, preview, time, unread/active flags:
  - Linear — "Weekly product digest" — "Your team shipped 23 issues this week..." — 9:41 AM — unread + active
  - Sophia Chen — "Re: Q3 roadmap review" — "Thanks for sending the deck over. I had a few thoughts..." — 8:12 AM — unread
  - Figma — "Marcus commented on your file" — "Love the new direction on the landing hero." — Yesterday
  - Stripe — "Payout of $12,480.00 sent" — "Your payout is on its way to your bank..." — Yesterday
  - Vercel — "Deployment ready for aura-web" — "Preview is live at aura-web-g3f.vercel.app" — Mon
  - GitHub — "[aura/core] PR #482 approved" — "david-lim approved your pull request." — Mon

**Reader (col-span-5):**
- Toolbar with Reply, Forward, Archive, Trash2 icon buttons (each `w-7 h-7 rounded-md hover:bg-white/5`) and a MoreHorizontal on the right.
- Header: "Weekly product digest"; sender avatar gradient bubble `w-7 h-7 rounded-full bg-gradient-to-br from-[#00d2ff] to-[#0B2551]` with "L"; "Linear" + "to me · 9:41 AM"; "Work" pill.
- Body:
  - Card with `Sparkles` icon (color `#A4F4FD`) labeled "Summary by Aura" and text "Your team closed 23 issues, merged 14 PRs, and shipped 2 features. Top contributor: Marcus. No action needed."
  - Paragraphs: "Hi team,", "Here is your weekly digest of everything happening across your projects. This was a strong week with significant progress on the Q3 roadmap.", "Twenty-three issues were closed, fourteen pull requests were merged, and two customer-facing features went out. The velocity trend continues to climb.", "Let me know if you would like a deeper breakdown by project or contributor.", "— The Linear team" (`text-white/50`).
  - Attachment pill with `Paperclip` icon: "digest-may-6.pdf".

## Section 5 — FeatureTriage

`max-w-6xl mx-auto px-6 py-20 md:py-28`, two-column grid `grid md:grid-cols-2 gap-10 md:gap-16 items-start`.

Left column motion (y 20 -> 0, 0.7s): `SectionEyebrow label="Triage" tag="AI-native"`, h2 `mt-5 text-3xl md:text-5xl font-semibold tracking-tight leading-[1.02]`: "Clear your inbox" <br/> "in a single pass.". Paragraph `mt-6 text-white/60 text-base leading-[1.6] max-w-md`: "Aura reads every message, understands intent, and routes the noise away from the signal. Focus on what moves your day forward — the rest handles itself." Chips row (`text-xs text-white/70 px-3 py-1.5 rounded-full border border-white/10 bg-white/[0.03]`): "Auto-categorize", "Snooze for later", "Silent newsletters", "One-tap unsubscribe".

Right column: `liquid-glass rounded-2xl p-5` card. Eyebrow text: "Today · 42 messages triaged". Four sub-cards (each `liquid-glass rounded-lg p-3`):
- Priority (4) `#ffffff` — items: "Sophia Chen — Q3 review", "David Lim — contract signoff"
- Follow-up (7) `#e5e5e5` — items: "Marcus — design review", "Figma — comment thread"
- Updates (18) `#a3a3a3` — items: "Vercel — deploy ready", "GitHub — PR #482 merged"
- Archived (13) `#525252` — items: "Stripe payout · Newsletter · Receipts"

## Section 6 — LogoCloud

`max-w-6xl mx-auto px-6 py-16 md:py-20`. Centered kicker `text-xs uppercase tracking-widest text-white/40`: "Trusted by the world's most thoughtful teams". Grid `mt-10 grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-6`, each logo name as `text-sm font-semibold tracking-tight text-white/50 hover:text-white`. Names: Linear, Vercel, Figma, Stripe, Ramp, Notion, Loom, Arc. Each fades in with stagger 0.05.

## Section 7 — Testimonials

`max-w-6xl mx-auto px-6 py-20 md:py-28 border-t border-white/10`. 3-col grid of `liquid-glass rounded-2xl p-6` figures. Each: blockquote `text-sm text-white/80 leading-[1.6]` wrapped in quotes, `figcaption mt-6 pt-5 border-t border-white/10` with name `text-sm font-semibold`, role `text-xs text-white/50`, company uppercased `text-xs text-white font-semibold tracking-wide`.
- "Aura gave our leadership team four hours of their week back. It reads like email from the future." — Parker Wilf, Group Product Manager, MERCURY
- "The command palette alone has changed how I process messages. I can't imagine going back to a traditional client." — Andrew von Rosenbach, Senior Engineering Program Manager, COHERE
- "Triage that actually understands context. Our team stopped dreading Monday morning inboxes." — Mathies Christensen, Engineering Manager, LUNAR

## Section 8 — Pricing

Uses custom CSS classes (not Tailwind) for cinematic typography.

Outer `<section className="c3-pricing-section">` with its own `<svg>` defining the `c3-noise` pricing filter described earlier.

Watermark (giant hero headline as backdrop):
```
<div className="c3-watermark-container">
  <div className="c3-watermark-main">
    <span className="c3-watermark-line-1">Your email.</span>
    <span className="c3-watermark-line-2">Revitalized</span>
  </div>
</div>
```

State: `yearly` boolean toggle. Three plans:
- **Free** — "Free" — "For creators taking their first steps with Forma." — Up to 3 projects in the cloud / Image export up to 1080p / Basic editing tools / Free templates and icons / Access via web and mobile app.
- **Standard** — monthly "$9,99/m" yearly "$99,99/y" — "For freelancers and small teams who need more freedom and flexibility." — Up to 50 projects in the cloud / Export up to 4K / Advanced editing toolkit / Team collaboration (up to 5 members) / Access to premium template library.
- **Pro** (`c3-card-pro`) — monthly "$19,99/m" yearly "$199,99/y" — "For studios, agencies, and professional creators working with brands." — Unlimited projects / Export up to 8K + animations / AI-powered content generation tools / Unlimited team members / Brand customization.

Each card renders: `c3-tier-small` (tier), `c3-tier-large` (price), `c3-desc`, `c3-list` of checkmark rows (white circle `c3-check` with white SVG check), `c3-btn` "Choose Plan".

Below: `c3-toggle-wrap` with "Yearly" label and a pill toggle (white knob black when off; when `.active`, background `rgba(255,255,255,0.2)`, knob white, translated 24px).

Pricing CSS (key values, include exactly):
- `.c3-pricing-section { position: relative; padding: 40px 20px 80px; display: flex; flex-direction: column; align-items: center; overflow-x: hidden; }`
- `.c3-watermark-container { position: relative; width: 100%; max-width: 1100px; text-align: center; margin-top: 40px; z-index: 2; }`
- `.c3-watermark-main { font-size: 9rem; font-weight: 800; line-height: 0.9; letter-spacing: -0.05em; filter: url(#c3-noise); display: flex; flex-direction: column; align-items: center; }`
- `.c3-watermark-line-1 { color: #fff; }`
- `.c3-watermark-line-2 { background: linear-gradient(to right, #091020 0%, #0B2551 25%, #A4F4FD 65%, #00d2ff 100%); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; }`
- `.c3-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; width: 100%; max-width: 1100px; margin-top: 60px; transform: translateX(20px); position: relative; z-index: 3; }`
- `.c3-card { background: linear-gradient(135deg, rgba(0,0,0,0.7), rgba(0,0,0,0.4)); backdrop-filter: blur(14px) brightness(0.91); border: 1px solid rgba(255,255,255,1); border-radius: 44px; padding: 50px 24px; min-height: 580px; display: flex; flex-direction: column; transition: all 0.6s cubic-bezier(.22,1,.36,1); overflow: hidden; position: relative; }`
- `.c3-card::before { content:''; position:absolute; inset:0; border-radius:inherit; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 50%); pointer-events:none; }`
- `.c3-card:hover { background: rgba(15,15,15,0.6); border-color: rgba(34,211,238,0.7); transform: translateY(-12px) scale(1.01); }`
- `.c3-card-pro { background: linear-gradient(135deg, rgba(0,0,0,0.85), rgba(0,0,0,0.55)); }`
- `.c3-tier-small { font-size: 1.1rem; font-weight: 400; color: rgba(255,255,255,0.6); }`
- `.c3-tier-large { font-size: 2.8rem; font-weight: 500; letter-spacing: -0.02em; color: #fff; margin-top: 8px; }`
- `.c3-desc { font-size: 0.88rem; color: rgba(255,255,255,0.45); min-height: 3.2em; margin-top: 16px; margin-bottom: 40px; line-height: 1.5; }`
- `.c3-list li { display:flex; align-items:flex-start; gap: 14px; font-size: 0.92rem; color: rgba(255,255,255,0.8); margin-bottom: 18px; line-height: 1.4; }`
- `.c3-check { width:28px; height:28px; border-radius:50%; background: rgba(255,255,255,0.15); display:inline-flex; align-items:center; justify-content:center; flex-shrink:0; }`
- `.c3-btn { background:#fff; color:#000; padding: 10px 32px; border-radius: 100px; font-weight:600; font-size: 0.88rem; margin-top:auto; border:none; cursor:pointer; align-self:center; transition: all 0.3s cubic-bezier(.22,1,.36,1); }`
- `.c3-btn:hover { background:#f5f5f5; transform:scale(1.02); box-shadow: 0 8px 24px rgba(255,255,255,0.15); }`
- `.c3-toggle-wrap { display:flex; align-items:center; justify-content:flex-end; gap:12px; width:100%; max-width:1100px; margin-top:32px; padding-right:20px; }`
- `.c3-toggle { width:52px; height:28px; background:#fff; border-radius:100px; position:relative; cursor:pointer; border:none; transition: background 0.3s cubic-bezier(.4,0,.2,1); padding:0; }`
- `.c3-toggle-knob { width:20px; height:20px; background:#000; border-radius:50%; position:absolute; top:4px; left:4px; transition: all 0.3s cubic-bezier(.4,0,.2,1); }`
- `.c3-toggle.active { background: rgba(255,255,255,0.2); }`
- `.c3-toggle.active .c3-toggle-knob { transform: translateX(24px); background:#fff; }`
- Media query `(max-width:1024px)`: `.c3-watermark-main { font-size: 3.5rem; filter:none; }`, `.c3-watermark-line-2 { background:none; -webkit-text-fill-color:#00d2ff; color:#00d2ff; }`, `.c3-grid` becomes horizontal scroll-snap flex (`display:flex; overflow-x:auto; scroll-snap-type:x mandatory; transform:none; width:100vw; padding:0 20px; gap:16px; scrollbar-width:none`), cards `flex: 0 0 320px; scroll-snap-align:center`, `.c3-grid::-webkit-scrollbar{display:none}`, `.c3-toggle-wrap { justify-content:center; padding-right:0; }`.

## Section 9 — FinalCTA

`max-w-6xl mx-auto px-6 py-20 md:py-32`. Motion `liquid-glass relative overflow-hidden rounded-3xl px-8 py-16 md:py-24 text-center`. Radial glow overlay: `radial-gradient(600px circle at 50% 0%, rgba(255,255,255,0.15), transparent 70%)` at opacity 0.3.
- h2 `text-4xl md:text-6xl font-semibold tracking-tight leading-[1.02]`: "Close the tabs." / "Open your day.".
- Paragraph `mt-6 text-white/60 max-w-md mx-auto text-sm leading-[1.6]`: "Join thousands of builders, founders, and operators who treat email like a tool — not an obligation."
- Buttons: `<AppleButton label="Download Aura" />` and `rounded-full border border-white/15 text-white text-sm font-medium px-5 py-3 hover:bg-white/5` "Talk to sales" + ChevronRight.


Reproduce exactly — fonts, gradient stops, noise filters, copy strings, animation delays, and the CloudFront video URL `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260508_064122_c4750c0e-7476-4b44-94a2-a85a65c63bf2.mp4`.
