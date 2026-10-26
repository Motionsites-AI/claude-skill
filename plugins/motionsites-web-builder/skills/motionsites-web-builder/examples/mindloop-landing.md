<!-- Mindloop Landing · Landing Page · 409 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=mindloop-landing · Source: https://motionsites.ai/?prompt=mindloop-landing -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a dark monochrome landing page called Mindloop — a newsletter/content platform. Use React + Vite + TypeScript + Tailwind CSS + shadcn/ui + Framer Motion. Fonts: Inter (sans) and Instrument Serif (serif, used for italic accent words). The entire theme is pure black (#000) background with white foreground — no colors or gradients beyond monochrome. Install hls.js and framer-motion.

Design System (index.css)
All CSS variables in HSL (no hsl() wrapper in the variable, just the values):

--background: 0 0% 0%
--foreground: 0 0% 100%
--card: 0 0% 5%
--card-foreground: 0 0% 100%
--primary: 0 0% 100%
--primary-foreground: 0 0% 0%
--secondary: 0 0% 12%
--secondary-foreground: 0 0% 85%
--muted: 0 0% 15%
--muted-foreground: 0 0% 65%
--accent: 170 15% 45%
--accent-foreground: 0 0% 100%
--border: 0 0% 20%
--input: 0 0% 18%
--ring: 0 0% 40%
--hero-subtitle: 210 17% 95%
Liquid Glass Effect (global CSS class .liquid-glass)

.liquid-glass {
  background: rgba(255, 255, 255, 0.01);
  background-blend-mode: luminosity;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border: none;
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}
.liquid-glass::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.4px;
  background: linear-gradient(180deg,
    rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%,
    rgba(255,255,255,0) 40%, rgba(255,255,255,0) 60%,
    rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
Animation Pattern
All sections use a reusable fadeUp helper with staggered delays:

const fadeUp = (delay: number) => ({
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true, margin: "-100px" },
  transition: { duration: 0.6, delay, ease: "easeOut" },
});

Page Structure (top to bottom)
1. Navbar (fixed, transparent)
Left: Logo (concentric circles icon — outer w-7 h-7 with border-2 border-foreground/60, inner w-3 h-3 with border border-foreground/60) + "Mindloop" bold text.
Center-left: Nav links ["Home", "How It Works", "Philosophy", "Use Cases"] separated by • dots. Links are text-muted-foreground hover:text-foreground.
Right: 3 social icons (Instagram, Linkedin, Twitter from lucide-react) in liquid-glass circular buttons (w-10 h-10 rounded-full).
No background — fully transparent, fixed top-0 z-50, padding px-8 md:px-28 py-4.

2. Hero Section (full viewport height)
Background: autoplaying looping muted MP4 video covering the entire section.
Video URL: https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260325_120549_0cd82c36-56b3-4dd9-b190-069cfc3a623f.mp4
Bottom gradient: h-64 bg-gradient-to-t from-background to-transparent for smooth fade to black.
Content (centered, z-10, pt-28 md:pt-32):
Avatar row: 3 overlapping circular avatars (-space-x-2, w-8 h-8 rounded-full border-2 border-background) + "7,000+ people already subscribed" in text-muted-foreground text-sm.
Heading: text-5xl md:text-7xl lg:text-8xl font-medium tracking-[-2px] — "Get Inspired with Us" where "Inspired" is font-serif italic font-normal.
Subtitle: text-lg in hsl(var(--hero-subtitle)) color — "Join our feed for meaningful updates, news around technology and a shared journey toward depth and direction."
Email form: liquid-glass rounded-full p-2 max-w-lg container with email input and a white bg-foreground text-background rounded-full px-8 py-3 "SUBSCRIBE" button with whileHover scale 1.03 and whileTap scale 0.98.

3. "Search has changed" Section
Top padding pt-52 md:pt-64, bottom padding pb-6 md:pb-9.
Heading: text-5xl md:text-7xl lg:text-8xl — "Search has changed. Have you?" with "changed." in serif italic.
Subtitle: text-muted-foreground text-lg max-w-2xl mx-auto mb-24.
3 platform cards (grid md:grid-cols-3 gap-12 md:gap-8 mb-20): Each card has a 200x200 icon image centered, platform name (font-semibold text-base), and description (text-muted-foreground text-sm).
ChatGPT icon: local asset icon-chatgpt.png
Perplexity icon: local asset icon-perplexity.png
Google AI icon: local asset icon-google.png
Bottom tagline: "If you don't answer the questions, someone else will." in text-muted-foreground text-sm text-center.

4. Mission Section
Padding pt-0 pb-32 md:pb-44.
Video: Large 800x800 looping autoplaying muted video centered.
Video URL: https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260325_132944_a0d124bb-eaa1-4082-aa30-2310efb42b4b.mp4
Scroll-driven word-by-word reveal using useScroll and useTransform from framer-motion:
Paragraph 1 (text-2xl md:text-4xl lg:text-5xl font-medium tracking-[-1px]): "We're building a space where curiosity meets clarity — where readers find depth, writers find reach, and every newsletter becomes a conversation worth having." Words "curiosity", "meets", "clarity" are highlighted in --foreground, rest in --hero-subtitle.
Paragraph 2 (text-xl md:text-2xl lg:text-3xl font-medium mt-10): "A platform where content, community, and insight flow together — with less noise, less friction, and more meaning for everyone involved."
Each word transitions opacity from 0.15 to 1 based on scroll progress.

5. Solution Section
Padding py-32 md:py-44, border-t border-border/30.
Label: "SOLUTION" in text-xs tracking-[3px] uppercase text-muted-foreground.
Heading: text-4xl md:text-6xl — "The platform for meaningful content" (serif italic on "meaningful").
Video: Rounded rounded-2xl, aspect-[3/1] object-cover.
Video URL: https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260325_125119_8e5ae31c-0021-4396-bc08-f7aebeb877a2.mp4
4-column feature grid (md:grid-cols-4 gap-8): Curated Feed, Writer Tools, Community, Distribution — each with title (font-semibold text-base) and description (text-muted-foreground text-sm).

6. CTA Section
Padding py-32 md:py-44, border-t border-border/30, overflow-hidden.
Background video (HLS via hls.js): absolute inset-0 object-cover z-0.
HLS URL: https://stream.mux.com/8wrHPCX2dC3msyYU9ObwqNdm00u3ViXvOSHUMRYSEe5Q.m3u8
Uses Hls.isSupported() check with fallback to native HLS for Safari.
Overlay: absolute inset-0 bg-background/45 z-[1].
Content (z-10, centered):
Concentric circles logo icon (w-10 h-10 outer, w-5 h-5 inner).
Heading: "Start Your Journey" (serif italic).
Subtitle in text-muted-foreground.
Two buttons: "Subscribe Now" (bg-foreground text-background rounded-lg px-8 py-3.5) and "Start Writing" (liquid-glass rounded-lg).

7. Footer
Simple py-12 px-8 md:px-28 footer.
Left: "© 2026 Mindloop. All rights reserved." in text-muted-foreground text-sm.
Right: Privacy, Terms, Contact links in text-muted-foreground text-sm hover:text-foreground.

Key Dependencies
framer-motion for all animations
hls.js for the CTA background video streaming
@fontsource/inter (400, 500, 600, 700)
@fontsource/instrument-serif (400, 400-italic)
lucide-react for icons
tailwindcss-animate plugin

Assets Needed
3 avatar images (avatar-1.png, avatar-2.png, avatar-3.png)
3 platform icons (icon-chatgpt.png, icon-perplexity.png, icon-google.png)
