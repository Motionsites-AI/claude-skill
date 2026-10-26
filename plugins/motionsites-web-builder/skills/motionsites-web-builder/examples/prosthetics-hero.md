<!-- Prosthetics Hero · Hero · 419 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=prosthetics-hero · Source: https://motionsites.ai/?prompt=prosthetics-hero -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a React + TypeScript + Tailwind CSS single-page hero section using Vite. The entire page lives in `src/App.tsx`. No extra libraries beyond `react`, `react-dom`, `lucide-react`, and Tailwind.

**Background:**
- A fullscreen autoplaying, muted, looping, `playsInline` background `<video>` element absolutely positioned `inset-0 w-full h-full object-cover`.
- Video URL (exact): `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260508_215831_c6a8989c-d716-4d8d-8745-e972a2eec711.mp4`
- Root wrapper: `relative min-h-screen overflow-hidden bg-[#f0f0ee]`.
- Foreground content wrapper: `relative z-10 flex flex-col min-h-screen`.

**Logo (inline SVG component):**
- `width="18" height="18"`, `viewBox="0 0 256 256"`, `fill="none"`.
- Single path with `fill="rgb(84, 84, 84)"` and `d="M 160 88 L 194 34 L 216 0 L 256 0 L 256 40 L 221.5 93.5 L 200 128 L 256 128 L 256 256 L 96 256 L 96 168 L 64.246 220 L 40 256 L 0 256 L 0 216 L 34 162 L 56 128 L 0 128 L 0 0 L 160 0 Z"`.

**Navbar (centered, pill-style, two separate pills):**
- `<nav>` classes: `flex items-center justify-center pt-4 sm:pt-6 px-4 sm:px-8 gap-2 sm:gap-3`.
- Left circular logo container: `flex items-center justify-center rounded-full w-10 h-10 sm:w-11 sm:h-11 shrink-0`, inline style `backgroundColor: '#EDEDED'`, contains the Logo.
- Right pill container: `flex items-center gap-4 sm:gap-10 rounded-xl px-4 sm:px-8 py-2.5 sm:py-3`, inline style `backgroundColor: '#EDEDED'`.
- Nav links array: `['Story', 'Products', 'Help', 'Support']`. Each anchor: `text-[12px] sm:text-[14px] font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200`.

**Hero content (bottom-left aligned):**
- Outer: `flex-1 flex items-end pb-10 sm:pb-16 lg:pb-20 px-6 sm:px-12 md:px-20 lg:px-28`.
- Inner: `max-w-xs`. Four stacked elements, each with `mb-3`:

1. Badge link: `inline-flex items-center gap-1.5 text-[11.5px] font-medium text-blue-500 hover:text-blue-600 transition-colors mb-3 group`. Text: `Seen on Shark Tank in India` followed by an arrow `→` in a span with `inline-block transition-transform duration-200 group-hover:translate-x-0.5`.

2. Headline `<h1>`: `text-[1.5rem] sm:text-[1.75rem] leading-[1.15] font-medium text-gray-900 tracking-tight mb-3`. Text: `Simple, smart prosthetics made for people who keep fighting.`

3. Subtext `<p>`: `text-[13px] text-gray-400 font-normal mb-3`. Text: `Reclaim your movement now.`

4. CTA anchor: `inline-flex items-center gap-2 text-[13px] font-medium text-blue-500 border border-blue-400 rounded-full px-5 py-2.5 hover:bg-blue-500 hover:text-white hover:border-blue-500 transition-all duration-200 group`. Text: `Try a free fitting` plus arrow `→` in span with `transition-transform duration-200 group-hover:translate-x-0.5`.

**Animations / micro-interactions:**
- Arrow spans translate right by `0.5` on group hover (`group-hover:translate-x-0.5`).
- CTA fills blue on hover (bg + text + border transitions, 200ms).
- Nav links shift from gray-700 to gray-900 on hover.

**Fonts:** Default Tailwind sans-serif system font stack (no custom font). All sizes are exact pixel/rem values above (`11.5px`, `12px`, `13px`, `14px`, `1.5rem`, `1.75rem`).

**Colors:** Page background `#f0f0ee`; pill backgrounds `#EDEDED`; accent `blue-500/600/400`; text `gray-900/700/400`.

Do not add any other sections, no Supabase wiring, no routing. Only the single hero page as described.
