<!-- AI Workflow Hero · Hero · 404 likes · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260721_114043_a70b6aa4-73d7-4b38-9595-baa6a5bad2d3.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=ai-workflow -->
<!-- Free sample. 500+ premium prompts like this: https://motionsites.ai/unlimited?utm_source=claude-skill&utm_medium=skill&utm_campaign=web-builder&utm_content=example-file -->

### Stack

- **Vite** + **React 18** + **TypeScript**
- **Tailwind CSS 3.4**
- **lucide-react** for icons (`LogIn`, `UserPlus`, `Play`, `Sparkles`, `Menu`, `X`)
- No Framer Motion -- all animations are CSS `transition-*` classes

---

### Fonts (loaded in `index.html`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link href="https://db.onlinewebfonts.com/c/6e47ef470dd19698c911332a9b4d1cf4?family=Neue+Haas+Grotesk+Text+Pro" rel="stylesheet" />
<link href="https://db.onlinewebfonts.com/c/dec0d9b4e22ca588dc20e1e2e09a59b5?family=Neue+Haas+Grotesk+Display+Pro+55+Roman" rel="stylesheet" />
```

Body/root font stack (in `index.css`):

```css
html, body, #root {
  height: 100%;
  margin: 0;
  font-family: 'Neue Haas Grotesk Display Pro 55 Roman', 'Neue Haas Grotesk Text Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
```

---

### Video URL (CloudFront)

```
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260511_131941_d136af49-e243-493a-be14-6ff3f24e09e6.mp4
```

---

### Color Palette

| Token | Hex |
|-------|-----|
| Dark green (text, buttons) | `#1f2a1d` |
| Medium dark green | `#2d3a2a` |
| Button hover | `#2a3827` |
| Body text green | `#4b5b47` |
| Heading primary | `#336443` |
| Heading accent | `#85AB8B` |
| Bottom-left text | `#3d5638` |
| Bottom-left button bg | `#3d5638`, hover `#2d4228` |

---

### Architecture

Two files:

1. **`BoomerangVideoBg.tsx`** -- captures video frames into canvas, then plays them forward/backward in a seamless boomerang loop at 30fps (960px max capture width).
2. **`App.tsx`** -- the full hero section.

---

### `BoomerangVideoBg.tsx` (exact)

```tsx
import { useEffect, useRef, useState } from 'react';

type Props = {
  src: string;
  className?: string;
};

export default function BoomerangVideoBg({ src, className }: Props) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const displayCanvasRef = useRef<HTMLCanvasElement>(null);
  const [framesReady, setFramesReady] = useState(false);
  const framesRef = useRef<HTMLCanvasElement[]>([]);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    const frames: HTMLCanvasElement[] = [];
    let capturing = true;
    let lastTime = -1;
    const MAX_WIDTH = 960;

    const captureFrame = () => {
      if (!capturing || video.readyState < 2) return;
      if (video.currentTime === lastTime) return;
      lastTime = video.currentTime;

      const vw = video.videoWidth;
      const vh = video.videoHeight;
      if (!vw || !vh) return;

      const scale = Math.min(1, MAX_WIDTH / vw);
      const w = Math.round(vw * scale);
      const h = Math.round(vh * scale);

      const canvas = document.createElement('canvas');
      canvas.width = w;
      canvas.height = h;
      const ctx = canvas.getContext('2d');
      if (!ctx) return;
      ctx.drawImage(video, 0, 0, w, h);
      frames.push(canvas);
    };

    type VFCVideo = HTMLVideoElement & {
      requestVideoFrameCallback?: (cb: () => void) => number;
    };
    const vfcVideo = video as VFCVideo;
    const hasVFC = typeof vfcVideo.requestVideoFrameCallback === 'function';

    let rafId = 0;
    const rafLoop = () => {
      captureFrame();
      if (capturing) rafId = requestAnimationFrame(rafLoop);
    };

    const vfcLoop = () => {
      captureFrame();
      if (capturing && vfcVideo.requestVideoFrameCallback) {
        vfcVideo.requestVideoFrameCallback(vfcLoop);
      }
    };

    const onEnded = () => {
      capturing = false;
      if (frames.length > 0) {
        framesRef.current = frames;
        setFramesReady(true);
      }
    };

    const onLoaded = () => {
      video.play().catch(() => {});
      if (hasVFC) {
        vfcVideo.requestVideoFrameCallback!(vfcLoop);
      } else {
        rafId = requestAnimationFrame(rafLoop);
      }
    };

    video.addEventListener('loadedmetadata', onLoaded);
    video.addEventListener('ended', onEnded);
    if (video.readyState >= 1) onLoaded();

    return () => {
      capturing = false;
      cancelAnimationFrame(rafId);
      video.removeEventListener('loadedmetadata', onLoaded);
      video.removeEventListener('ended', onEnded);
    };
  }, [src]);

  useEffect(() => {
    if (!framesReady) return;
    const canvas = displayCanvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    const frames = framesRef.current;
    if (frames.length === 0) return;

    const first = frames[0];
    canvas.width = first.width;
    canvas.height = first.height;

    let index = 0;
    let direction = 1;
    let last = performance.now();
    const interval = 1000 / 30;
    let rafId = 0;

    const render = (now: number) => {
      if (now - last >= interval) {
        last = now;
        ctx.drawImage(frames[index], 0, 0);
        index += direction;
        if (index >= frames.length - 1) {
          index = frames.length - 1;
          direction = -1;
        } else if (index <= 0) {
          index = 0;
          direction = 1;
        }
      }
      rafId = requestAnimationFrame(render);
    };
    rafId = requestAnimationFrame(render);
    return () => cancelAnimationFrame(rafId);
  }, [framesReady]);

  return (
    <div className={className ?? 'absolute inset-0 w-full h-full'}>
      <video
        ref={videoRef}
        src={src}
        className="w-full h-full object-cover"
        style={{ display: framesReady ? 'none' : 'block' }}
        muted
        playsInline
        preload="auto"
        crossOrigin="anonymous"
      />
      <canvas
        ref={displayCanvasRef}
        className="w-full h-full object-cover"
        style={{ display: framesReady ? 'block' : 'none' }}
      />
    </div>
  );
}
```

---

### `App.tsx` (exact)

```tsx
import { useState, useEffect } from 'react';
import { LogIn, UserPlus, Play, Sparkles, Menu, X } from 'lucide-react';
import BoomerangVideoBg from './BoomerangVideoBg';

const BG_VIDEO =
  'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260511_131941_d136af49-e243-493a-be14-6ff3f24e09e6.mp4';

function App() {
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    if (menuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [menuOpen]);

  const navLinks = [
    { href: '#mission', label: 'Purpose' },
    { href: '#how', label: 'The Process' },
    { href: '#pricing', label: 'Tariffs' },
  ];

  return (
    <section className="relative w-full min-h-screen sm:h-screen overflow-hidden">
      <BoomerangVideoBg src={BG_VIDEO} className="absolute inset-0 w-full h-full" />
      <nav className="absolute top-0 left-0 right-0 z-30 flex items-center justify-between px-4 sm:px-6 md:px-10 py-4 sm:py-6">
        <div className="flex items-center gap-2 text-[#2d3a2a]">
          <span className="text-lg sm:text-xl md:text-2xl font-semibold tracking-tight">
            LinkFlow<sup className="text-[10px] sm:text-xs font-medium">TM</sup>
          </span>
        </div>

        <div className="hidden lg:flex items-center gap-1 bg-white/70 backdrop-blur-md rounded-full pl-6 pr-1 py-1 shadow-sm border border-white/60">
          {navLinks.map((link, i) => (
            <a
              key={link.href}
              href={link.href}
              className={`text-sm px-3 py-2 transition-colors ${
                i === 0 ? 'font-semibold text-[#1f2a1d]' : 'font-medium text-[#4b5b47] hover:text-[#1f2a1d]'
              }`}
            >
              {link.label}
            </a>
          ))}
          <button className="ml-2 bg-[#1f2a1d] hover:bg-[#2a3827] text-white text-sm font-medium px-5 py-2.5 rounded-full transition-colors">
            Try it Live
          </button>
        </div>

        <div className="flex items-center gap-3 sm:gap-6 text-[#2d3a2a]">
          <a href="#signup" className="hidden sm:flex items-center gap-2 text-sm font-medium hover:opacity-80 transition-opacity">
            <UserPlus className="w-4 h-4" />
            Sign Me Up!
          </a>
          <a href="#login" className="hidden sm:flex items-center gap-2 text-sm font-medium hover:opacity-80 transition-opacity">
            <LogIn className="w-4 h-4" />
            Enter
          </a>
          <button
            onClick={() => setMenuOpen((v) => !v)}
            className="lg:hidden relative flex items-center justify-center w-10 h-10 rounded-full bg-white/70 backdrop-blur-md border border-white/60 text-[#1f2a1d] transition-all duration-300 hover:bg-white/90"
            aria-label={menuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={menuOpen}
          >
            <Menu
              className={`w-5 h-5 absolute transition-all duration-300 ${
                menuOpen ? 'opacity-0 rotate-90 scale-50' : 'opacity-100 rotate-0 scale-100'
              }`}
            />
            <X
              className={`w-5 h-5 absolute transition-all duration-300 ${
                menuOpen ? 'opacity-100 rotate-0 scale-100' : 'opacity-0 -rotate-90 scale-50'
              }`}
            />
          </button>
        </div>
      </nav>

      {/* Mobile menu overlay */}
      <div
        className={`lg:hidden fixed inset-0 z-20 transition-opacity duration-300 ${
          menuOpen ? 'opacity-100 pointer-events-auto' : 'opacity-0 pointer-events-none'
        }`}
        onClick={() => setMenuOpen(false)}
      >
        <div className="absolute inset-0 bg-[#1f2a1d]/40 backdrop-blur-sm" />
      </div>

      {/* Mobile menu drawer */}
      <div
        className={`lg:hidden fixed top-0 right-0 bottom-0 z-20 w-[85%] max-w-sm bg-white/95 backdrop-blur-xl shadow-2xl transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)] ${
          menuOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div className="flex flex-col h-full pt-24 px-8 pb-8">
          <div className="flex flex-col gap-1">
            {navLinks.map((link, i) => (
              <a
                key={link.href}
                href={link.href}
                onClick={() => setMenuOpen(false)}
                className={`text-2xl font-semibold text-[#1f2a1d] py-4 border-b border-[#1f2a1d]/10 transition-all duration-500 ${
                  menuOpen ? 'translate-x-0 opacity-100' : 'translate-x-8 opacity-0'
                }`}
                style={{ transitionDelay: menuOpen ? `${150 + i * 70}ms` : '0ms' }}
              >
                {link.label}
              </a>
            ))}
          </div>

          <div
            className={`mt-8 flex flex-col gap-4 transition-all duration-500 ${
              menuOpen ? 'translate-x-0 opacity-100' : 'translate-x-8 opacity-0'
            }`}
            style={{ transitionDelay: menuOpen ? '400ms' : '0ms' }}
          >
            <a href="#signup" className="flex items-center gap-2 text-sm font-medium text-[#2d3a2a] sm:hidden">
              <UserPlus className="w-4 h-4" />
              Sign Me Up!
            </a>
            <a href="#login" className="flex items-center gap-2 text-sm font-medium text-[#2d3a2a] sm:hidden">
              <LogIn className="w-4 h-4" />
              Enter
            </a>
            <button className="mt-2 bg-[#1f2a1d] hover:bg-[#2a3827] text-white text-sm font-semibold px-5 py-3 rounded-full transition-colors">
              Try it Live
            </button>
          </div>
        </div>
      </div>

      {/* Hero copy */}
      <div className="relative z-10 flex flex-col items-center text-center pt-24 sm:pt-28 md:pt-32 px-4 sm:px-6">
        <h1
          className="font-normal leading-[0.95] text-[#336443] text-[2rem] sm:text-4xl md:text-5xl lg:text-[4.75rem] xl:text-[5.25rem] max-w-5xl"
          style={{ fontFamily: '"Neue Haas Grotesk Display Pro 55 Roman", "Neue Haas Grotesk Text Pro", "Helvetica Neue", Helvetica, Arial, sans-serif', letterSpacing: '-0.035em' }}
        >
          Close the rift{' '}
          <span className="text-[#85AB8B]">
            linking
            <br className="hidden sm:block" /> signals and action
          </span>
        </h1>
        <p className="mt-6 sm:mt-8 text-[#4b5b47] text-sm sm:text-base md:text-lg leading-relaxed max-w-md px-2">
          Shape scattered signals into meaningful outcomes via AI-driven workflows.
        </p>
      </div>

      {/* Bottom-left CTA block */}
      <div className="absolute left-4 right-4 sm:right-auto sm:left-6 md:left-10 bottom-6 sm:bottom-8 md:bottom-10 z-10 max-w-sm">
        <div className="flex items-center gap-2 text-[#3d5638] sm:text-white/95 mb-3">
          <Sparkles className="w-4 h-4" />
          <span className="text-sm font-semibold sm:font-medium">
            FluxEngine<sup className="text-[10px]">TM</sup>
          </span>
        </div>
        <p className="text-[#3d5638]/90 sm:text-white/85 text-xs leading-relaxed mb-6 max-w-xs font-medium sm:font-normal">
          LinkFlow smoothly unites your company systems, streamlining data paths between services without having to write custom scripts.
        </p>
        <div className="flex items-center gap-4 flex-wrap">
          <button className="bg-[#3d5638] sm:bg-white hover:bg-[#2d4228] sm:hover:bg-white/90 text-white sm:text-[#1f2a1d] text-sm font-semibold px-5 sm:px-6 py-2.5 sm:py-3 rounded-full transition-colors shadow-sm">
            Try it Live
          </button>
          <button className="text-[#3d5638] sm:text-white text-sm font-semibold sm:font-medium hover:opacity-80 transition-opacity">
            Know More.
          </button>
        </div>
      </div>

      {/* Bottom-right video link */}
      <div className="hidden sm:flex absolute right-6 md:right-10 bottom-8 md:bottom-10 z-10 items-center gap-2 text-white/90 text-sm">
        <button className="flex items-center justify-center w-6 h-6 rounded-full bg-white/20 backdrop-blur-sm hover:bg-white/30 transition-colors">
          <Play className="w-3 h-3 fill-white text-white ml-0.5" />
        </button>
        <span className="font-medium">How we build?</span>
        <span className="text-white/60">1:35</span>
      </div>
    </section>
  );
}

export default App;
```

---

### Animation Details (all CSS, no Framer Motion)

| Element | Property | Values |
|---------|----------|--------|
| Hamburger Menu/X icon swap | `transition-all duration-300` | Open: Menu gets `opacity-0 rotate-90 scale-50`, X gets `opacity-100 rotate-0 scale-100`. Closed: reverse. |
| Mobile overlay backdrop | `transition-opacity duration-300` | Open: `opacity-100 pointer-events-auto`. Closed: `opacity-0 pointer-events-none`. |
| Mobile drawer slide | `transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)]` | Open: `translate-x-0`. Closed: `translate-x-full`. |
| Mobile nav links stagger | `transition-all duration-500` | Open: `translate-x-0 opacity-100`, delay per item: `150ms + i * 70ms`. Closed: `translate-x-8 opacity-0`, delay `0ms`. |
| Mobile CTA group | `transition-all duration-500` | Open: `translate-x-0 opacity-100`, delay `400ms`. Closed: `translate-x-8 opacity-0`, delay `0ms`. |
| Nav buttons | `transition-colors` | Default Tailwind duration (150ms). |
| Opacity links | `transition-opacity` | `hover:opacity-80`. |

---

### Key Layout/Spacing Notes

- Root section: `relative w-full min-h-screen sm:h-screen overflow-hidden`
- Navbar padding: `px-4 sm:px-6 md:px-10 py-4 sm:py-6`
- Desktop pill nav: `bg-white/70 backdrop-blur-md rounded-full pl-6 pr-1 py-1 shadow-sm border border-white/60`
- Hero heading: `pt-24 sm:pt-28 md:pt-32`, font sizes `text-[2rem] sm:text-4xl md:text-5xl lg:text-[4.75rem] xl:text-[5.25rem]`, `leading-[0.95]`, `letterSpacing: '-0.035em'`
- Bottom-left block: `absolute left-4 right-4 sm:right-auto sm:left-6 md:left-10 bottom-6 sm:bottom-8 md:bottom-10`
- Bottom-right video: `absolute right-6 md:right-10 bottom-8 md:bottom-10`

---

### Dependencies (package.json)

```json
{
  "dependencies": {
    "lucide-react": "^0.344.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.1",
    "autoprefixer": "^10.4.18",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "typescript": "^5.5.3",
    "vite": "^5.4.2"
  }
}
```
