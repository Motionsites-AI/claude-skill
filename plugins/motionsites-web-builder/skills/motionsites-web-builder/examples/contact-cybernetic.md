<!-- Contact Cybernetic · Hero · 605 likes · free MotionSites prompt -->
<!-- Preview: https://motionsites.ai/?prompt=contact-cybernetic · Source: https://motionsites.ai/?prompt=contact-cybernetic -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

Build a modern, interactive hero section using React, Tailwind CSS, and Framer Motion (motion/react). Ensure you follow these precise architecture and styling instructions:
1. Fonts & Global Animations
Import the Inter font from Google Fonts.
In your CSS setup, configure Tailwind to use it by default (--font-sans: 'Inter', ...).
Create a keyframe animation in CSS named blink for the typewriter cursor:
code
CSS
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
.animate-blink { animation: blink 1s step-end infinite; }
2. General Page Structure
Wrap the entire application in a container div with the following classes: relative bg-white text-neutral-900 font-sans selection:bg-[#EAECE9] selection:text-[#1C2E1E] antialiased overflow-x-hidden flex flex-col lg:block lg:min-h-screen.
3. Background Video Component (with Native Scrubbing)
Container element: Add a div containing the background video with classes: order-last lg:order-none relative lg:absolute lg:inset-0 lg:z-0 overflow-hidden pointer-events-none w-full aspect-square md:aspect-video lg:aspect-auto lg:h-full bg-neutral-50 lg:bg-transparent.
Video element: Use <video> with muted, playsInline, preload="auto".
Video Source URL: https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260601_110537_3a579fa0-7bbc-4d94-9d25-0e816c7840f5.mp4
Classes: w-full h-full object-cover object-right lg:object-right-bottom.
Scrubbing/Playback Logic via useEffect hooks:
Desktop Mouse Scrubbing Hook: Listen to the window mousemove event. If window.innerWidth < 1024, ignore (disable scrubbing). Store the mouse 'previous X' coordinate to calculate the delta against 'current X'. Update the target scrub time based on (delta / window.innerWidth) * 0.8 * video.duration. Clamp the time between 0 and duration. Set video.currentTime = targetTime. Bind a seeked event listener to ensure smooth tracking frame to frame.
Mobile Autoplay Hook: Because scrubbing is disabled on mobile frames, trigger normal playback for screens < 1024 width: video.autoplay = true and video.play().
4. Interactive Navbar
Header wrapper: Wrap the Navbar in <header className="fixed top-0 inset-x-0 z-10 px-5 sm:px-8 py-4 sm:py-5 flex flex-row justify-between items-center bg-transparent">
Logo (Left side): Flex row with gap-3.
Text: Mainframe&reg; (using the ® symbol). Classes: text-[21px] sm:text-[26px] tracking-tight text-black font-medium select-none.
Icon block right beside it: An asterisk &#10033;. Classes: text-[25px] sm:text-[30px] text-black select-none tracking-[-0.02em] font-medium leading-none mb-1.
Desktop Nav Links (Center): Flex row, hidden md:flex, text-[23px] text-black. Links are "Labs", "Studio", "Openings", "Shop" separated by <span className="opacity-40">,&nbsp;</span> dividers. Hover states should use hover:opacity-60 transition-opacity.
Desktop CTA (Right): Hidden on mobile. A link reading "Get in touch" mapped with text-[23px] text-black underline underline-offset-2 hover:opacity-60 transition-opacity.
Mobile Menu Logic:
Hamburger <button> visible below md. Has three w-6 h-[2px] bg-black spans.
Hook it to a local state isMobileMenuOpen. When open, animate the burger into an 'X' (top bar rotate-45 translate-y-[7px], middle bar opacity-0, bottom bar -rotate-45 -translate-y-[7px]). All spans need transition-all duration-300.
Create a full screen Mobile Navigation Overlay div hidden on Desktop. Fixed inset-0 z-[9] with bg-white/95 backdrop-blur-sm. Apply opacity-100 pointer-events-auto when isMobileMenuOpen is true; otherwise, opacity-0 pointer-events-none.
5. Content Layout Container
Below the background video and relative to it, add a content grouping layer: <div className="relative z-10 flex flex-col order-first lg:order-none w-full bg-white lg:bg-transparent pb-8 lg:pb-0 lg:min-h-screen">
Inside that, the overarching layout engine: <main id="spade-hero" className="w-full max-w-7xl mx-auto px-6 py-12 flex-1 flex flex-col justify-center">
6. Typewriter Hook and Headline
Implement a custom useTypewriter(text, speed = 38, startDelay = 600) React hook. It uses setTimeout and setInterval to iteratively build a string slice by slice. It must return an object: { displayed: string, done: boolean }.
Run the hook with the string "we'd love to\nhear from you!".
Wrap the headline securely in a motion.div configured to drop-in (initial: opacity: 0, y: 20, animate: opacity: 1, y: 0, transition duration 0.6).
Render your hook text inside <h1 className="text-5xl md:text-6xl lg:text-[76px] font-normal tracking-tight text-black leading-[1.08] mb-8 select-none w-full whitespace-pre-wrap">.
While typing (!done), output a <span className="inline-block w-[2px] h-[1.1em] bg-black align-middle ml-[2px] animate-blink" /> cursor at the end of the displayed text string.
7. Secondary Description Text
Another motion.div (delay 0.1s from the headline).
Content: <p> tag that reads: Whether you have questions, feedback, <br /> drop us a message and we'll get back to you as soon as possible.
Classes: text-lg md:text-xl text-[#5A635A] leading-relaxed font-normal mb-14 max-w-2xl.
8. Interactive Multi-Select Service Pills
Using setServices track an array ["Brand", "Digital", "Campaign", "Other"].
The prompt Title: "What sort of service?" (text-2xl font-medium tracking-tight mb-2). Subtitle: "Select all that apply" (opacity-85 text-[#738273] mb-8).
Iterate over the options natively outputting motion.button wrapper tags allowing multiple selections inside a flex wrap container.
Pill active traits classes: bg-[#1C2E1E] text-white shadow-md shadow-emerald-950/5 transform. Show a check icon (lucide-react) dropping in using type: "spring", stiffness: 300, damping: 20.
Pill inactive traits classes: bg-white text-[#1C2E1E] border border-[#F1F3F1] hover:bg-[#F1F3F1]/55.
Contingent Feedback Status Banner: Underneath your service pills, write an <AnimatePresence mode="wait"> that tracks user state array length:
Empty: Show a generic placeholder indicating "Please click to select services above." at fifty percent opacity (opacity: 0.5, italic, text-xs).
Active Selection: Swap cleanly into a container <motion.div> that springs height gracefully (height: "auto"). Inside, display an acknowledgment banner reading "Ready to inquire about: [array.join(", ")]" combined with an arrow call-to-action button "Let's Go" (text-[#4D6D47] uppercase text-xs). Style the banner with bg-[#FAFBF9] border rounded-2xl.
