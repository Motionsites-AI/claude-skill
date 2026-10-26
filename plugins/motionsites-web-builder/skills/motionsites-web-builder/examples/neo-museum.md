<!-- Neo Museum · Website · 395 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=neo-museum · Source: https://motionsites.ai/?prompt=neo-museum -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Project Setup

Stack: React 19 + Vite 6 + Tailwind CSS 4 + Motion (Framer Motion) + Lucide React icons + TypeScript

package.json dependencies:
- `react`, `react-dom` ^19.0.1
- `vite` ^6.2.3
- `@tailwindcss/vite` ^4.1.14, `tailwindcss` ^4.1.14
- `motion` ^12.23.24
- `lucide-react` ^0.546.0
- `@vitejs/plugin-react` ^5.0.4
- `typescript` ~5.8.2

Fonts (loaded via Google Fonts in `index.css`):
- Sans: Inter (weights: 300, 400, 500, 600)
- Mono: JetBrains Mono (weights: 400, 500)

```css
/* index.css */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
@import "tailwindcss";

@theme {
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
}

@layer utilities {
  .text-mega {
    font-size: 21vw;
    line-height: 0.75;
    letter-spacing: -0.04em;
  }
}
```

Global styling: Background `#fcfcfc`, text `#111`, selection color `bg-black text-white`, `overflow-x-hidden`, `font-sans` (Inter).

---

DATA

```tsx
const chaptersData = [
  { name: "Age of Dinosaurs", image: "https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624247/01_udnber.png" },
  { name: "Fossils of Ancient Life", image: "https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624374/02_pmvxxl.png" },
  { name: "Reptiles of the Mesozoic", image: "https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624236/03_hcp3jc.png" },
  { name: "Marine Fossil Gallery", image: "https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624256/04_get63z.png" },
  { name: "Prehistoric Giants", image: "https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624251/05_kz1tyu.png" }
];
```

---

STATE

```tsx
const [showVideo, setShowVideo] = useState(false);
const [activeChapter, setActiveChapter] = useState(2); // starts at "Reptiles of the Mesozoic"
const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
```

- `showVideo` flips to `true` after a 2800ms delay (setTimeout)
- `activeChapter` auto-cycles every 3500ms via setInterval, wrapping `(prev + 1) % 5`

---

ANIMATION VARIANTS

```tsx
const fadeUp = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
};

const letterBlock = {
  initial: { y: 120, opacity: 0 },
  animate: { 
    y: 0, 
    opacity: 1, 
    transition: { duration: 1.2, ease: [0.16, 1, 0.3, 1] } 
  }
};
```

---

SECTION 1: HERO (full viewport height)

Container: `relative w-full min-h-screen flex flex-col overflow-hidden`

1A. HEADER (NHM Logo)

- `motion.header` with `staggerChildren: 0.1, delayChildren: 0.1`
- Padding: `pt-6 px-6 md:px-16`, `z-20`
- The "NHM" logo is a custom inline SVG with `viewBox="0 0 840 100"`, `fill-[#111]`, full width
- The SVG is wrapped in `motion.h1` with `variants` that animate from `scale: 1.03` to `scale: 1` with `staggerChildren: 0.06, delayChildren: 0.1`
- Each polygon of each letter uses the `letterBlock` variant (slides up from `y: 120`)
- Letter N (translate 0,0): Three polygons -- left vertical `0,0 14,0 14,100 0,100`, right vertical `200,0 214,0 214,100 200,100`, diagonal `0,0 33,0 214,100 181,100`
- Letter H (translate 280,0): Three polygons -- left vertical `0,0 14,0 14,100 0,100`, right vertical `200,0 214,0 214,100 200,100`, crossbar `14,43 200,43 200,57 14,57`
- Letter M (translate 560,0): Four polygons -- left vertical `0,0 14,0 14,100 0,100`, right vertical `266,0 280,0 280,100 266,100`, left diagonal `0,0 26,0 153,100 127,100`, right diagonal `254,0 280,0 153,100 127,100`

1B. SUB-NAV BAR

- Below the SVG logo, `flex justify-between items-start mt-8`
- Font: `text-[10px] md:text-[11px] font-mono tracking-[0.2em] uppercase`
- Uses `fadeUp` variant with `duration: 0.8, ease: "easeOut"`

Left column (15% width): Three lines -- "Natura" / "History" / "Museum"

Arrow separator (5% width, hidden on mobile): `ArrowRight` from lucide, size 14, strokeWidth 1, `text-gray-400`

Center column (flex-1 on mobile, 30% on desktop): "Exploring the story of life on earth through science, discovery and wonder." -- Split differently on desktop (3 lines) vs mobile (4 lines). `text-gray-800 leading-relaxed font-mono`

Arrow separator (5% width, hidden on mobile): Same as above

Right column (15% width, hidden on mobile): Nav links list -- Visit, Exhibitions, Discover, Learn, About. `text-gray-800`, `hover:text-black hover:underline`

Hamburger button (far right, z-60): Two horizontal lines (`w-8 h-[1.5px] bg-black`), `gap-[6px]`. Hover: first line shrinks to `w-6`, second expands to `w-10`. When open: first rotates 45deg + translateY, second rotates -45deg + translateY (forming an X). Transition: `duration-300`.

1C. MOBILE MENU OVERLAY

- `AnimatePresence` wrapping a `motion.div`
- Appears below the header, slides in from `y: -20`, `opacity: 0` to `y: 0, opacity: 1`
- `bg-[#fcfcfc] border-b border-gray-200 shadow-xl`, only visible on `md:hidden`
- Contains the same nav links as the desktop version, `text-sm font-mono tracking-[0.2em] uppercase`, `space-y-6`

1D. BACKGROUND VIDEO

- Appears after 2800ms delay (controlled by `showVideo` state)
- `absolute top-0 left-0 w-full h-full pointer-events-none z-0`
- Video: `autoPlay loop muted playsInline`, `w-full h-full object-cover`
- Video URL: `https://res.cloudinary.com/dsdxaxkiz/video/upload/v1779624998/magnific_use-img-2-as-the-exact-ba_Piu3X0W42C_wnrc8f.mp4`

1E. LEFT SIDEBAR CONTENT

- `motion.div` with `staggerChildren: 0.15, delayChildren: 0.6`
- Position: `px-10 md:px-16`, `mt-20 sm:mt-28 md:mt-32`, `w-[320px]`, `z-10`

Section indicator: `01` + horizontal line (`w-16 h-[1.5px] bg-black/20`), `text-xs font-mono`

Headline: "TIMELESS WONDERS" -- `text-[3.5rem] md:text-[5rem] font-normal tracking-tight leading-[1]`. Line break between "TIMELESS" and "WONDERS".

Description: "Step into the natural world and / discover the stories written / millions of years ago." -- `text-[13px] md:text-[14px] text-gray-700 w-[240px] leading-[1.6]`

CTA Button ("Explore Now"):
- Container: `bg-[#1a1a1a] px-6 py-3.5 border border-[#1a1a1a] rounded-md shadow-sm`
- Hover: slides up 0.5px, adds `shadow-[3px_3px_0px_rgba(17,17,17,0.5)]`
- Active: resets translate and shadow
- Has a sliding background panel: `bg-[#fcfcfc]` that slides from `-translate-x-[101%]` to `translate-x-0` on hover, `duration-700 ease-[cubic-bezier(0.16,1,0.3,1)]`
- Icon: Custom SVG leaf/plant shape (4 paths forming a stylized leaf), white by default, turns `#111` on hover with `scale-110 -rotate-12 -translate-y-1` transform
- Text: "Explore Now", `text-[15px] font-medium`, white turning to `#111` on hover

1F. RIGHT SIDEBAR (hidden on mobile)

- `motion.div` with `staggerChildren: 0.15, delayChildren: 0.9`
- Position: `w-[200px] mt-12 md:mt-20`, `hidden md:flex`

Specimen info: "Tyrannosaurus Rex" heading (`text-[10px] font-bold font-mono tracking-widest uppercase`), subtext "Late Cretaceous period / 68-66 million years ago" (`text-[12px] text-gray-600 leading-[1.6]`)

Stats: "Length" label + "12.3 m" value, "Height" label + "4.0 m" value. Labels: `text-[10px] font-mono tracking-widest uppercase text-gray-500`. Values: `text-[13px] font-medium`.

View Details button: Circle (`w-10 h-10 rounded-full border border-gray-400`) with `Plus` icon (size 16, strokeWidth 1.5), text "View Details" (`text-[10px] font-mono uppercase tracking-widest font-bold`). Hover: circle gets `border-black bg-[#111]`, icon turns white.

1G. BOTTOM-LEFT "SCROLL TO EXPLORE"

- `absolute bottom-10 left-[2.5rem] md:left-[4rem]`, `hidden md:flex`
- Fade up animation: `delay: 1.2`
- Circle (`w-12 h-12 rounded-full border border-gray-300`) containing two thin vertical lines (`w-[1px] h-[12px] bg-gray-600`, `gap-[4px]`) representing a pause icon
- Text: "Scroll to explore" -- `text-[10px] font-mono tracking-widest uppercase text-gray-500 font-semibold`

---

SECTION 2: "EXPLORE OUR WORLD"

Container: `relative w-full min-h-[75vh] md:min-h-screen bg-[#fcfcfc]`, flex column centered, `pt-24 md:pt-32 pb-0 z-20`

2A. SECTION LABEL

`[ 02 ] Explore Our World` -- `text-[10px] md:text-[11px] font-mono tracking-[0.2em]`, `mb-12`. "02" in `text-gray-500`, "Explore Our World" in `text-gray-900 font-bold uppercase`.

2B. MAIN HEADING

"Unearth the stories of our planet's past through fossils, minerals, and ancient wonders." -- `text-[2.2rem] md:text-[3.5rem] lg:text-[4.2rem] leading-[1.1] font-medium tracking-tight text-[#111]`, max-width 1000px, text-center. Line break on desktop after "past". Animates with `whileInView` from `y: 40, opacity: 0` to `y: 0, opacity: 1`, `once: true`, margin `-100px`.

2C. ACTION PILLS

Five pill buttons in a flex-wrap row, `gap-3 md:gap-4`, `mb-10 md:mb-24`. Staggered reveal animation (`staggerChildren: 0.1, delayChildren: 0.3`). Each pill: `rounded-full border border-gray-300 text-[11px] font-medium uppercase tracking-wider bg-white/50 backdrop-blur-sm text-gray-800`. Hover: `border-black bg-black text-white`. Icons from lucide (size 14, strokeWidth 2):

1. `Bone` + "Dinosaurs"
2. `Dna` + "Ancient Life"
3. `Gem` + "Minerals"
4. `Leaf` + "Fossils"
5. `BookOpen` + "Learn More"

2D. SPACER

`min-h-[220px] md:min-h-[450px]` -- provides room for the pterodactyl image from Section 3 to overlap upward.

2E. BOTTOM TEXT

Absolute positioned at bottom, `px-8 md:px-16 pb-8 md:pb-12`, `pointer-events-none`. Two text elements at `justify-between`:
- Left: "WE DON'T JUST TELL STORIES."
- Right: "PALEONTOLOGY (C) 2026"
- Both: `text-[10px] font-mono tracking-widest uppercase text-gray-500 font-medium`, hidden on mobile.

---

SECTION 3: "ANCIENT COLLECTION" (Dark Section)

Container: `relative w-full bg-[#0a0a0a] text-white flex flex-col z-30`

3A. PTERODACTYL IMAGE (Overlapping)

- Absolute positioned at top, centered horizontally (`left-1/2 -translate-x-1/2`)
- Width: `w-[160vw] md:w-[1100px]`
- Image URL: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779625001/ChatGPT_Image_May_23_2026_12_24_44_PM_1_lv1dne.png`
- Animates with `whileInView` from `y: "-65%", opacity: 0` to `y: "-78%", opacity: 1`, `duration: 1.4, ease: "easeOut"`, viewport margin `100px`
- `pointer-events-none z-0`, `mix-blend` not applied here

3B. HEADING AREA

- Padding: `px-8 md:px-16 pt-32 md:pt-48 mb-16`, `z-10`
- Two-column layout on xl (`flex-col xl:flex-row justify-between`)

Left -- Main heading: "Curated from millions of years of wonder [3 circle icons] & discovery." -- `text-[1.8rem] md:text-[3rem] lg:text-[3.8rem] xl:text-[4rem] leading-[1.15] font-medium tracking-tight text-white`. The three circle icons are inline (`inline-flex gap-2 md:gap-3 align-middle mx-2 md:mx-4 translate-y-[-4px]`), each `w-10 h-10 md:w-14 md:h-14 rounded-full border border-gray-600 bg-black text-gray-400`. Hover: `bg-white text-black border-white`. Icons: `Bone`, `Dna`, `Leaf` (size 22).

Right -- Tagline + pills:
- Tagline: "WE DON'T JUST DISPLAY FOSSILS / WE SHARE EARTH'S STORY" -- `text-[9px] md:text-[10px] font-mono tracking-widest text-gray-400 uppercase mb-6 leading-relaxed`
- Three pills: "Educational", "Authentic", "Inspiring" -- `px-5 py-2 rounded-full border border-gray-600 text-[9px] font-mono tracking-widest uppercase text-gray-300`. Hover: `bg-white text-black border-white`.

3C. TWO-COLUMN PANEL

Separated by `h-[1px] bg-gray-800` line. Flex row on desktop, column on mobile.

Left panel (35% width):
- `border-r border-gray-800` on desktop, `border-b` on mobile
- `min-h-[400px] md:min-h-[500px]`
- Top: `***` text (`text-gray-500 text-xl tracking-[0.3em]`)
- Center: Chapter image using `SandTransitionImage` component (SVG filter-based sand/dissolve transition). Image: `absolute inset-0 w-[80%] h-[80%] m-auto object-contain mix-blend-lighten`. Uses `AnimatePresence mode="wait"`.
- Bottom: Chapter counter `01 / 05` style, with animated number (`motion.div` slides vertically). `text-[10px] font-mono tracking-widest text-[#888] uppercase`. Counter numeral color `#888`, divider `text-[#333]`.

Right panel (65% width):
- Top bar: "Explore the past. Understand the present." + animated "Chapter 0X" label. `border-b border-gray-800 p-8 text-[10px] font-mono text-gray-400 tracking-widest`.
- Chapter list: 5 items, each `border-b border-gray-800/80 py-8`. Active: `text-white`, inactive: `text-[#444] hover:text-[#999]`. Chapter name: `text-2xl md:text-[2rem] font-medium tracking-tight`. Active item shows `ArrowUpRight` icon (size 22, strokeWidth 1, `text-gray-400`) that animates in/out.
- Clicking a chapter sets `activeChapter`.

3D. BOTTOM FOOTER

- `h-[1px] bg-gray-800` divider
- Text: "DIGGING INTO OUR PLANET'S PAST" -- `px-8 py-8 text-[10px] font-mono tracking-widest text-gray-500 uppercase bg-[#0a0a0a]`

---

SandTransitionImage COMPONENT

A custom component that creates a sand/particle dissolve effect using SVG filters:

```tsx
function SandTransitionImage({ src, alt, className }) {
  // Uses usePresence() from motion/react for AnimatePresence awareness
  // Unique filterId per instance via useRef
  // requestAnimationFrame loop over 900ms
  // Easing: entering = quartic ease-out (1 - Math.pow(1-t, 4)), exiting = cubic (Math.pow(t, 3))
  // SVG filter chain:
  //   1. feTurbulence: fractalNoise, baseFrequency 1.8, numOctaves 4
  //   2. feDisplacementMap: scale up to 150 based on progress
  //   3. feOffset: dy up to -80 (enter) or 120 (exit), dx up to -30/+30
  //   4. feGaussianBlur: up to 6px
  //   5. feColorMatrix: opacity fades (1 - progress * 1.2)
  // Image has crossOrigin="anonymous" and referrerPolicy="no-referrer"
}
```

---

ALL EXTERNAL ASSET URLs

Video:
- `https://res.cloudinary.com/dsdxaxkiz/video/upload/v1779624998/magnific_use-img-2-as-the-exact-ba_Piu3X0W42C_wnrc8f.mp4`

Images:
- Chapter 1: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624247/01_udnber.png`
- Chapter 2: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624374/02_pmvxxl.png`
- Chapter 3: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624236/03_hcp3jc.png`
- Chapter 4: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624256/04_get63z.png`
- Chapter 5: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779624251/05_kz1tyu.png`
- Pterodactyl: `https://res.cloudinary.com/dsdxaxkiz/image/upload/v1779625001/ChatGPT_Image_May_23_2026_12_24_44_PM_1_lv1dne.png`

(Note: these are Cloudinary URLs, not CloudFront. The project uses Cloudinary for all hosted media assets.)

---

KEY DESIGN DETAILS

- Color palette: `#fcfcfc` (off-white bg), `#111` / `#1a1a1a` (near-black), `#0a0a0a` (dark section bg). Gray scale via Tailwind: `gray-300` through `gray-800`.
- No purple/indigo anywhere. Strictly monochrome black/white/gray.
- Typography hierarchy: Large display headings (3.5-5rem), mono labels (10-11px), body text (13-14px).
- Spacing: 8px base system throughout.
- Transitions: Most hover transitions 300-700ms. Button slide effect uses `cubic-bezier(0.16, 1, 0.3, 1)`. Letter animations use same cubic bezier.
- The page is entirely a single `App.tsx` component plus the `SandTransitionImage` helper function in the same file.
