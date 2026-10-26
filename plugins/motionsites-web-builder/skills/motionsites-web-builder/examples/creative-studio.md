<!-- Creative Studio · Agency · 426 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=creative-studio · Source: https://motionsites.ai/?prompt=creative-studio -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a full-screen hero section using React, Tailwind CSS, Framer Motion, and Lucide React icons. Use the Inter font. The page is fully mobile-responsive. Here are the exact specifications:

---

**BACKGROUND:**
- A full-screen autoplaying, looping, muted video covering the entire viewport as a background.
- Video URL: `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260517_222138_3e3205be-3364-417b-a64a-bfe087acbec4.mp4`
- The video is positioned absolute, inset-0, with `object-cover` to fill the viewport.

---

**COLOR:**
- Accent color: `#5E0ED7` (deep purple). Used for the logo dot, the "+" symbols in stats, and the CTA link text.
- All body text is black (#000).

---

**FONT:**
- Font family: `'Inter', sans-serif` applied to the root container.
- All text is uppercase with wide letter-spacing (`tracking-widest` or `tracking-wide`).
- Font weights: 600 (semibold) throughout.

---

**LAYOUT (flex column, min-h-screen):**
The page is a flex column with three vertical sections:
1. **Nav** (top, fixed height)
2. **Stats row** (flex-1, vertically centered, right-aligned)
3. **Bottom content** (pinned to bottom with padding)

---

**NAVIGATION BAR:**
- Horizontal flex, items centered, justified between. Padding: `px-5 sm:px-8 md:px-12 pt-5 md:pt-6`.
- **Left:** A circular logo — 32px round div with 2px border in accent color, containing a 10px solid circle in accent color.
- **Center (hidden on mobile, visible md+):** Four nav links: "Story", "Expertise", "Studios", "Feedback". Text: 14px, font-semibold, tracking-widest, uppercase, black.
- **Right:** A 36px round black button with three horizontal white lines (hamburger icon — three `span` elements, each `w-4 h-0.5 bg-white` with `gap-1`). This opens the mobile menu on click.

---

**MOBILE MENU OVERLAY:**
- Triggered by hamburger click. Fixed, full-screen, z-50, white background.
- Top row: same logo (left) and a 36px round black close button with an X icon (right).
- Below: vertical list of the 4 nav links at `text-3xl`, font-semibold, tracking-widest, uppercase, with `gap-8` and `mt-16`.
- Bottom (mt-auto): "Work With Us" CTA in accent color with ArrowUpRight icon, `text-xl`.

---

**STATS ROW (middle section):**
- Container: `flex-1 flex items-center justify-end`, with same horizontal padding. `py-8 md:py-0`.
- Three stat items in a horizontal row with `gap-5 sm:gap-8 md:gap-10`, each right-aligned:
  - **+300** / CRAFTED BRANDS
  - **+200** / DIGITAL PRODUCTS
  - **+100** / VENTURES FUNDED
- Number styling: `fontSize: clamp(1.5rem, 5vw, 3.5rem)`, weight 600. The "+" is rendered separately in accent color at 0.5em size. The number is black.
- Label: `text-[10px] sm:text-xs md:text-sm`, font-semibold, tracking-widest, uppercase, black, `whitespace-pre-line leading-tight` (each label has a line break between the two words).

---

**BOTTOM SECTION:**
- Padding: `px-5 sm:px-8 md:px-12 pb-8 md:pb-12`. Flex column with `gap-6 md:gap-12`.

**Row A (tagline + CTA):**
- Flex row, items-center, justify-between, gap-4.
- **Left:** Small uppercase tagline paragraph: "Shaping Bold / Visions Into Power / For Your Tribe" (with `<br />` line breaks). Text: `text-[10px] sm:text-xs md:text-sm`, font-semibold, tracking-widest, max-width `130px sm:160px md:max-w-xs`.
- **Right:** CTA link "Work With Us" with ArrowUpRight icon. Text: `text-base sm:text-xl md:text-2xl`, accent color, weight 600, `whitespace-nowrap`. Icon: 18px on mobile, 22px on sm+.

**Row B (description + main heading):**
- Flex row, `items-end`, justify-between, `gap-3 sm:gap-4`.
- **Left:** A fixed-width container (`w-[120px] sm:w-[180px] md:w-[280px]`, shrink-0) containing a paragraph: "Creative Studios Built Around Elevating Your Vision Into Striking Reality". Text: `text-[9px] sm:text-xs md:text-sm`, font-semibold, tracking-widest, uppercase, `text-left md:text-right`.
- **Right:** The main heading — three words stacked vertically: "Fearless", "Vision", "Delivered". Each word in its own `overflow-hidden` wrapper. Text: `fontSize: clamp(2rem, 9vw, 9rem)`, `lineHeight: 0.88`, weight 600, uppercase, black, text-right.

---

**ANIMATIONS (Framer Motion):**

All animations fire on page load (initial -> animate).

1. **fadeDown variant** (nav elements):
   - From: `{ opacity: 0, y: -20 }`
   - To: `{ opacity: 1, y: 0 }`
   - Each element has a custom stagger index. Delay: `index * 0.1s`. Duration: 0.5s. Ease: `[0.22, 1, 0.36, 1]`.
   - Applied to: logo (custom=0), each nav link (custom=1-4), hamburger (custom=5).

2. **fadeUp variant** (stats + bottom content):
   - From: `{ opacity: 0, y: 32 }`
   - To: `{ opacity: 1, y: 0 }`
   - Delay: `index * 0.12s`. Duration: 0.6s. Ease: `[0.22, 1, 0.36, 1]`.
   - Applied to: each stat card (custom=2,3,4), tagline paragraph (custom=5), CTA link (custom=6), description block (custom=7).

3. **Heading slide-up** (main heading words):
   - Each word slides up from `y: "110%"` to `y: 0` within its overflow-hidden parent (clip reveal effect).
   - Delay: `0.4 + wordIndex * 0.14` (so 0.4s, 0.54s, 0.68s). Duration: 0.7s. Ease: `[0.22, 1, 0.36, 1]`.

---

**RESPONSIVE BREAKPOINTS:**
- Mobile-first. Three tiers: default (mobile), `sm:` (640px), `md:` (768px).
- Nav links hidden on mobile, shown md+.
- Spacing, font sizes, and widths scale up at each breakpoint.
- Mobile menu provides full navigation on small screens.

---

**DEPENDENCIES:**
- React 18
- Tailwind CSS 3
- framer-motion
- lucide-react (ArrowUpRight, X icons)
