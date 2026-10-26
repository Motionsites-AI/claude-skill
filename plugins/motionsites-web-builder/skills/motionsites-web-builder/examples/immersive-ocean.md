<!-- Immersive Ocean · Hero · 689 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=immersive-ocean · Source: https://motionsites.ai/?prompt=immersive-ocean -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Create a fullscreen hero landing page for a creative studio called "Foldcraft" using React, Tailwind CSS, and Lucide React icons. The page is a single viewport-height section with a looping background video, a responsive navbar, a mobile menu, and staggered-animated hero text.

**Video Background:**
- URL: `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_204221_5339e40b-e73d-4ab0-9c65-79c18c66fd50.mp4`
- Attributes: autoPlay, muted, loop, playsInline
- Styling: absolute positioned, full width/height, object-cover, object-position at 70% horizontal center
- The video sits behind all content (no z-index or z-0)

**Font:**
- Google Fonts: Geist (weights 300-700), loaded via `<link>` in index.html
- Tailwind config extends fontFamily with `geist: ['Geist', 'sans-serif']`
- Applied as `font-geist` on the root container
- Body CSS: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale`

**Root Container:**
- `relative h-screen w-full overflow-hidden bg-black font-geist`

**Navbar (z-30):**
- Flex, space-between, padding: `px-6 py-5 md:px-12 lg:px-16`
- Left side: Logo text "Foldcraft" (`text-lg font-semibold tracking-tight text-white sm:text-xl`) followed by desktop nav links (hidden on mobile, flex on md+)
- Nav links: Home, Projects, Studio, Reach Us (`text-sm text-white/80 hover:text-white transition-colors`)
- Right side (desktop): "Let's Talk" button (`rounded-lg bg-white px-5 py-2 text-sm font-medium text-black hover:scale-105 transition-transform`)
- Right side (mobile): hamburger toggle button (40x40, z-50) with animated Menu/X icons from lucide-react. Menu rotates 90deg out and X rotates in with opacity and scale transitions (duration-300). Button has `active:scale-90`.

**Mobile Menu (z-20):**
- Absolute, `inset-x-0 top-0`, full-screen overlay with `bg-black/98 backdrop-blur-xl`
- Transition: `duration-500 ease-[cubic-bezier(0.16,1,0.3,1)]` toggling between `h-screen opacity-100` and `h-0 opacity-0 pointer-events-none`
- Inner content: centered vertically (`flex h-full flex-col justify-center px-8`), with a delayed fade + translate animation (delay-100, translate-y-8)
- Links: Home, Projects, Studio, Reach Us (`text-3xl font-medium text-white/90 hover:text-white`)
- Button: "Let's Talk" (`mt-6 rounded-full bg-white px-8 py-3.5 text-base font-medium text-black hover:scale-105`)
- All links/button call `setMobileMenuOpen(false)` on click

**Hero Content (z-10):**
- Flex column, justify-between, fills remaining height: `h-[calc(100vh-80px)]`
- Padding: `px-6 pb-10 pt-12 sm:pb-12 sm:pt-16 md:px-12 md:pb-16 md:pt-20 lg:px-16`

**Top Section (max-w-3xl):**
- Badge: "Brand & Visual Storytelling" (`text-xs sm:text-sm text-white/90`), with `animate-[fadeSlideUp_0.8s_ease_0.2s_both]`, margin-bottom 4 (sm:6)
- Heading h1: "Shaping visual / narratives, / one pixel at a time." with `<br/>` line breaks
  - Sizing: `text-3xl sm:text-5xl md:text-6xl lg:text-7xl`
  - Style: `font-medium leading-[1.1] tracking-tight text-white`
  - Animation: `animate-[fadeSlideUp_0.8s_ease_0.4s_both]`

**Bottom Section:**
- Paragraph: "Turning vision into reality through craft, motion, and an endless pursuit of beauty."
  - Style: `text-sm sm:text-base md:text-lg leading-relaxed text-white/60 max-w-sm sm:max-w-lg mb-5 sm:mb-6`
  - Animation: `animate-[fadeSlideUp_0.8s_ease_0.7s_both]`
- CTA Button: "Explore Work" with ArrowRight icon (size 16)
  - Style: `rounded-lg bg-white px-5 py-2.5 sm:px-6 sm:py-3 text-sm font-medium text-black hover:scale-105 transition-transform inline-flex items-center gap-2`
  - Animation: `animate-[fadeSlideUp_0.8s_ease_0.9s_both]`

**CSS Animation (in index.css):**
```css
@keyframes fadeSlideUp {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**CSS Reset (in index.css):**
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
```

**Dependencies:** React, lucide-react (ArrowRight, Menu, X), Tailwind CSS, Google Fonts Geist.
