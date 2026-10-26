# Video & media

Background footage, loops, scrubbing and the overlays that keep text legible on top of it.

**Conventions.** Every snippet runs in a single `index.html` with no build step. Code assumes `*,*::before,*::after{box-sizing:border-box}`, a dark page, and these shared tokens (paste once):
```css
:root{
  --ease-out-expo:cubic-bezier(.16,1,.3,1);   /* premium settle: entrances, panels */
  --ease-out-quint:cubic-bezier(.22,1,.36,1); /* carousels, fills, menus */
  --ease-material:cubic-bezier(.4,0,.2,1);    /* UI state changes */
}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
```
`VIDEO_URL.mp4`, `poster.jpg` etc. are placeholders. Encode backgrounds as H.264 MP4 with `-movflags +faststart` (add WebM as a second `<source>` if you have it). Keep background clips 6–12 s and ≤ 5–8 MB.

---

## 1. Cinematic background video layer (autoplay, HLS, off-screen pause, settle-in)

**What / when:** The default premium hero foundation: a muted looping clip fills the viewport and all UI floats over it. The video provides all the depth, so no decorative blobs are needed. Use it for any hero where footage carries the mood.

**Premium parameters**
- Full-bleed absolute video, `object-fit:cover`. The section background is `#000` (or the page bg, matching the clip's edge colour) so nothing flashes before the first frame.
- Always `muted autoplay loop playsinline` (all four are required for iOS autoplay), and set `video.muted = true` as a property too.
- `object-position: 70% center` (or wherever the subject is) so portrait crops keep the subject.
- Entrance: fade in from `opacity 0, scale(1.05)` to `1, scale(1)` over **1.8 s** `--ease-out-expo`. Or a **delayed reveal**: keep a still/blank hero during the type intro and fade the video in at ~**2.8 s**.
- Pause when off-screen (IntersectionObserver): a big battery and CPU win on long pages with several videos.
- HLS (`.m3u8`): Safari plays it natively; every other browser needs hls.js with `capLevelToPlayerSize: true` so phones never stream 4K.
- Text protection: pick one scrim from technique 4, or none when the footage has calm negative space behind the copy.

**Implementation**
```html
<section class="vhero">
  <video class="vhero__media vhero__media--settle" data-src="VIDEO_URL.mp4" poster="poster.jpg"
         autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>
  <div class="vhero__content">…nav, headline, CTAs…</div>
</section>
<!-- Only needed when a source is .m3u8 -->
<script src="https://cdn.jsdelivr.net/npm/hls.js@1.5.20/dist/hls.min.js"></script>
```
```css
.vhero{position:relative;min-height:100vh;min-height:100svh;overflow:hidden;background:#000;isolation:isolate;color:#fff}
.vhero__media{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;pointer-events:none}
.vhero__media--settle{opacity:0;transform:scale(1.05);transition:opacity 1.8s var(--ease-out-expo),transform 1.8s var(--ease-out-expo)}
.vhero__media--settle.is-ready{opacity:1;transform:none}
.vhero__content{position:relative;min-height:inherit;display:flex;flex-direction:column}
@media (prefers-reduced-motion:reduce){.vhero__media--settle{opacity:1;transform:none;transition:none}}
```
```js
function mountVideo(video, src, { revealDelay = 0 } = {}) {
  video.muted = true;               // some browsers ignore the attribute for autoplay
  video.playsInline = true;
  const isHls = /\.m3u8($|\?)/i.test(src);
  if (isHls && !video.canPlayType('application/vnd.apple.mpegurl') && window.Hls && Hls.isSupported()) {
    const hls = new Hls({ capLevelToPlayerSize: true });
    hls.loadSource(src); hls.attachMedia(video);
  } else {
    video.src = src;                // MP4 everywhere, or native HLS in Safari/iOS
  }
  const reveal = () => setTimeout(() => video.classList.add('is-ready'), revealDelay);
  video.readyState >= 2 ? reveal() : video.addEventListener('loadeddata', reveal, { once: true });
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    video.removeAttribute('autoplay'); video.pause();   // poster / first frame stays as a still
    return;
  }
  video.play().catch(() => {});     // autoplay can be refused (low-power mode): the poster remains
  new IntersectionObserver(([e]) => (e.isIntersecting ? video.play().catch(() => {}) : video.pause()))
    .observe(video);
}
document.querySelectorAll('video[data-src]').forEach((v) => mountVideo(v, v.dataset.src));
// Delayed reveal, letting the headline intro own the first ~3 s:
// mountVideo(el, el.dataset.src, { revealDelay: 2800 });
```

**React variant** (hls.js needs explicit cleanup):
```tsx
useEffect(() => {
  const v = ref.current!; let hls: Hls | undefined;
  if (v.canPlayType('application/vnd.apple.mpegurl')) v.src = SRC;
  else if (Hls.isSupported()) { hls = new Hls({ capLevelToPlayerSize: true }); hls.loadSource(SRC); hls.attachMedia(v); }
  return () => hls?.destroy();
}, []);
```

**Mobile / a11y:** use `100svh`/`100dvh` with a `100vh` fallback so browser chrome doesn't crop. Serve a lighter ≤720p encode to phones by picking `src` with `matchMedia('(max-width: 768px)')`. Reduced motion shows the poster or first frame as a still.

---

## 2. Seamless video loop with rAF opacity fades (manual loop, optional playlist)

**What / when:** A background video that fades in from black on load, fades out just before its last frame, and restarts after a short black beat. This hides the hard cut of a native `loop` (and any mismatch between first and last frame), so every loop reads as a cinematic "cut to black". The same mechanism cycles a playlist of clips.

**Premium parameters**
- Fade-in 500 ms; fade-out 500–550 ms, triggered when `duration − currentTime ≤ 0.55 s`.
- 100 ms of pure black between plays (`ended` → opacity 0 → wait 100 ms → `currentTime = 0` → play → fade in).
- Fades run on `requestAnimationFrame`, never a CSS `transition` on the video. Each new fade cancels the previous rAF and starts from the current opacity, so fades never snap or fight.
- A guard flag stops the fade-out from re-triggering on every `timeupdate`.
- Native `loop` is OFF. The video is `muted playsinline autoplay preload="auto"`. The section behind is pure `#000`, so the dip reads as intentional.

**Implementation**
```html
<section class="hero">
  <video class="hero-video" data-fade-loop muted playsinline autoplay preload="auto" src="VIDEO_URL.mp4" aria-hidden="true"></video>
  <div class="hero-content">…</div>
</section>
```
```css
.hero{position:relative;min-height:100vh;min-height:100dvh;overflow:hidden;background:#000}
.hero-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  opacity:0;            /* JS owns opacity: no CSS transition here */
  pointer-events:none;z-index:0}
.hero-content{position:relative;z-index:10}
```
```js
/** Manual loop with rAF fades. Returns a cleanup function. */
function fadeLoopVideo(video, { fadeMs = 500, fadeOutLead = 0.55, gapMs = 100, playlist = null } = {}) {
  let raf = 0, timer = 0, fadingOut = false, idx = 0;
  const fadeTo = (target, ms = fadeMs) => {
    cancelAnimationFrame(raf);
    const from = parseFloat(video.style.opacity) || 0;   // resume from wherever we are
    const t0 = performance.now();
    const tick = (now) => {
      const p = Math.min((now - t0) / ms, 1);
      video.style.opacity = String(from + (target - from) * p);
      if (p < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
  };
  const startPlayback = () => { fadingOut = false; video.play().catch(() => {}); fadeTo(1); };
  const onTimeUpdate = () => {
    const left = video.duration - video.currentTime;
    if (!fadingOut && left > 0 && left <= fadeOutLead) { fadingOut = true; fadeTo(0); }
  };
  const onEnded = () => {
    cancelAnimationFrame(raf);
    video.style.opacity = '0';
    timer = setTimeout(() => {
      if (playlist && playlist.length > 1) {
        idx = (idx + 1) % playlist.length;
        video.src = playlist[idx];             // 'loadeddata' fires again -> startPlayback
      } else { video.currentTime = 0; startPlayback(); }
    }, gapMs);
  };
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {   // still frame instead of motion
    video.removeAttribute('autoplay'); video.pause(); video.style.opacity = '1';
    return () => {};
  }
  video.loop = false; video.muted = true; video.playsInline = true;
  video.style.opacity = '0';
  if (playlist && playlist.length) video.src = playlist[0];
  video.addEventListener('loadeddata', startPlayback);
  video.addEventListener('timeupdate', onTimeUpdate);
  video.addEventListener('ended', onEnded);
  if (video.readyState >= 2) startPlayback();   // already loaded from cache
  return () => {
    cancelAnimationFrame(raf); clearTimeout(timer);
    video.removeEventListener('loadeddata', startPlayback);
    video.removeEventListener('timeupdate', onTimeUpdate);
    video.removeEventListener('ended', onEnded);
  };
}
document.querySelectorAll('video[data-fade-loop]').forEach((v) => fadeLoopVideo(v));
// Playlist: fadeLoopVideo(el, { playlist: ['a.mp4', 'b.mp4', 'c.mp4'] });
```
For `.m3u8` sources, attach them with the HLS branch of technique 1 instead of setting `video.src`.

**React variant** (only the lifecycle differs):
```tsx
function FadingVideo({ src, className }: { src: string | string[]; className?: string }) {
  const ref = useRef<HTMLVideoElement>(null);
  useEffect(() => fadeLoopVideo(ref.current!, { playlist: Array.isArray(src) ? src : null }), [src]);
  // put opacity:0 in the CSS class, not style={{}}, so a re-render never resets it
  return <video ref={ref} className={className} src={Array.isArray(src) ? undefined : src} muted playsInline autoPlay preload="auto" />;
}
```

**Mobile / perf:** iOS needs `muted` + `playsinline`. With several of these on one page, pause off-screen ones with an IntersectionObserver.

---

## 3. Background-video framing & art direction

**What / when:** Small geometry tricks that put the clip's subject exactly where the layout needs it, without re-editing the video. Use them whenever the focal point would collide with the copy, sit too low or high, or crop badly on portrait screens.

**Premium parameters / variants**
- **Oversize + top anchor:** `width:120%; height:120%`, centred horizontally, `top:0`, `object-position:top`. Keeps the top of the frame (sky, horizon, a planet) in view, trims edges and bottom, and reads slightly zoomed-in.
- **Vertical offset:** `translateY(15–20%)` on an `inset:0` cover video pushes the subject below the headline. Only works when the exposed band blends into the section bg (black clip edge, or a scrim from technique 4).
- **Lower band:** the video occupies only the area below the headline (from ~300 px / 30vh down). A `bg → transparent → bg` vertical gradient dissolves it into a light page.
- **Focal crop for portrait:** `object-position: 70% center` (or `right bottom` from ≥1024 px) keeps a right-side subject visible when a phone crops the sides.
- **Bleed scale:** `scale(1.05)` hides encoder edge lines and 1 px letterbox slivers.
- **Mobile in-flow:** on phones the video becomes a square block below the copy (`aspect-ratio:1/1`, `16/9` on tablet, absolute background again from ≥1024 px). Avoids text over busy video on small screens.
- **Light pages on mobile:** inset the video to `80% × 80%`, centred; it reads as a floating screen instead of a cropped mess.
- **Reuse trick:** the same clip flipped with `transform: scaleY(-1)` behind the footer or contact band, dimmed 60 %, reads as a new shot.

**Implementation**
```css
/* A. Oversize, top-anchored */
.video--oversize{position:absolute;left:50%;top:0;width:120%;height:120%;transform:translateX(-50%);object-fit:cover;object-position:top center}
/* B. Vertical offset */
.video--shift{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:translateY(17%)}
/* C. Lower band dissolving into a light page */
.video-band{position:absolute;left:0;right:0;bottom:0;top:clamp(180px,30vh,300px);z-index:0}
.video-band video{width:100%;height:100%;object-fit:cover}
.video-band::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(to bottom,var(--bg,#fff) 0%,transparent 50%,var(--bg,#fff) 100%)}
/* D. Focal crop */
.video--focal{object-position:70% center}
@media (min-width:1024px){.video--focal{object-position:right bottom}}
/* E. Bleed */
.video--bleed{transform:scale(1.05)}
/* F. In-flow block on mobile, background on desktop */
.split{display:flex;flex-direction:column;background:#fff}
.split__copy{order:1;position:relative;z-index:10;padding:48px 24px}
.split__media{order:2;position:relative;aspect-ratio:1/1;overflow:hidden}
.split__media video{width:100%;height:100%;object-fit:cover;object-position:right}
@media (min-width:768px){.split__media{aspect-ratio:16/9}}
@media (min-width:1024px){
  .split{display:block;position:relative;min-height:100vh}
  .split__copy{background:transparent;min-height:100vh;display:flex;flex-direction:column;justify-content:center}
  .split__media{position:absolute;inset:0;aspect-ratio:auto;z-index:0}
  .split__media video{object-position:right bottom}
}
/* G. Footer reuse */
.video--flipped{transform:scaleY(-1);filter:brightness(.4)}
```
```html
<section class="split">
  <div class="split__copy">…headline / form…</div>
  <div class="split__media"><video muted playsinline autoplay loop preload="auto" src="VIDEO_URL.mp4"></video></div>
</section>
```

**Mobile:** retest the focal point at 375×812. Usually you change `object-position` per breakpoint rather than the transform.

---

## 4. Edge-blend scrims & text protection over video

**What / when:** Gradient overlays that melt a video into the page colour and keep text legible without a flat dark tint that kills the footage. Eased bottom fade where the hero hands off to the next section; side letterboxing when the video has a capped width on ultra-wide screens; a directional scrim on portrait where text sits over the busiest part of the frame.

**Premium parameters**
- Eased bottom fade that starts late (~79 %) with many stops (a 2-stop gradient bands and looks cheap): 0 @78.8 % → .23 @79.6 → .45 @81.4 → .75 @83.3 → .84 @85.2 → .888 @88 → .905 @91 → .96 @95 → 1 @100.
- Simple menu of scrims (pick one, keep it subtle):
  - bottom fade into the page: `height 12–16rem`, `linear-gradient(to top, var(--bg), transparent)`;
  - top fade under a transparent nav: `height 180px`, `linear-gradient(#010103, transparent)`;
  - full vertical: `rgba(0,0,0,.30) → transparent 45 % → rgba(0,0,0,.60)`;
  - flat dim: `.20` hero, `.45` CTA band, `.60` when a clip is reused behind a footer;
  - light theme: `linear-gradient(to top, #fff 0%, rgba(255,255,255,.8) 50%, transparent 100%)` behind bottom copy.
- Side letterbox: solid page colour beyond the video's edges, feathered over ~70 px.
- Portrait text scrim, left→right `.86 → .66 @42 % → .20 @78 % → .10`; top→bottom `.72 → .34 @24 % → .34 @56 % → .80 @82 % → .97 @94 % → 1`.
- Media cards: `to top`, black 60 % → transparent at 50 %.
- Use the exact page colour (e.g. `#050505`), never a different black, or the seam shows.
- **No scrim at all** is often the strongest choice: the video at 100 %, contrast from glass chrome and from placing copy where the frame is naturally dark. Choose footage with a dark negative-space zone.

**Implementation**
```css
:root{--bg:#050505;--video-half:746px}  /* half the rendered video width, if capped */
.plate{position:absolute;inset:0;overflow:hidden;background:var(--bg)}
.plate video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.plate::after{content:"";position:absolute;inset:0;pointer-events:none;background:
  linear-gradient(to bottom,
    rgb(5 5 5/0) 78.8%, rgb(5 5 5/.23) 79.6%, rgb(5 5 5/.45) 81.4%, rgb(5 5 5/.75) 83.3%,
    rgb(5 5 5/.84) 85.2%, rgb(5 5 5/.888) 88%, rgb(5 5 5/.905) 91%, rgb(5 5 5/.96) 95%, var(--bg) 100%),
  linear-gradient(to right,
    var(--bg) calc(50% - var(--video-half)), transparent calc(50% - var(--video-half) + 70px),
    transparent calc(50% + var(--video-half) - 70px), var(--bg) calc(50% + var(--video-half)))}
/* Portrait: copy over the frame -> directional legibility scrim */
@media (max-aspect-ratio:11/10){
  .plate video{object-position:43% center}
  .plate::after{background:
    linear-gradient(to right,rgb(5 5 5/.86),rgb(5 5 5/.66) 42%,rgb(5 5 5/.20) 78%,rgb(5 5 5/.10)),
    linear-gradient(to bottom,rgb(5 5 5/.72),rgb(5 5 5/.34) 24%,rgb(5 5 5/.34) 56%,rgb(5 5 5/.80) 82%,rgb(5 5 5/.97) 94%,var(--bg))}
}
/* Simple scrims */
.scrim-vertical{position:absolute;inset:0;pointer-events:none;background:linear-gradient(to bottom,rgba(0,0,0,.3),transparent 45%,rgba(0,0,0,.6))}
.fade-bottom{position:absolute;left:0;right:0;bottom:0;height:16rem;pointer-events:none;background:linear-gradient(to top,var(--bg),transparent)}
.fade-top{position:absolute;left:0;right:0;top:0;height:180px;pointer-events:none;background:linear-gradient(#010103,transparent)}
/* Media card scrim */
.media-card{position:relative;overflow:hidden;border-radius:24px}
.media-card::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(to top,rgb(0 0 0/.6),transparent 50%)}
```

---

## 5. Progressive bottom blur (masked backdrop-filter)

**What / when:** Instead of darkening the footage, the bottom of the video goes out of focus and sharpens toward the middle: a camera-like depth-of-field band that protects bottom-aligned titles while keeping colours intact. Use it for bottom-anchored cinematic heroes.

**Premium parameters:** blur **24px**, mask `linear-gradient(to top, #000 0%, transparent 45%)`, no colour overlay. The stepped version stacks 2 / 4 / 8 / 16 px layers with shrinking masks so the blur compounds toward the bottom.

**Implementation**
```html
<div class="bottom-blur" aria-hidden="true"></div>
<!-- or: <div class="pblur" aria-hidden="true"><i></i><i></i><i></i><i></i></div> -->
```
```css
.bottom-blur{position:absolute;inset:0;z-index:1;pointer-events:none;
  -webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);
  -webkit-mask-image:linear-gradient(to top,#000 0%,transparent 45%);mask-image:linear-gradient(to top,#000 0%,transparent 45%)}
/* Smoother stepped version */
.pblur{position:absolute;left:0;right:0;bottom:0;height:55%;z-index:1;pointer-events:none}
.pblur>i{position:absolute;inset:0}
.pblur>i:nth-child(1){-webkit-backdrop-filter:blur(2px);backdrop-filter:blur(2px);-webkit-mask-image:linear-gradient(to top,#000,transparent 100%);mask-image:linear-gradient(to top,#000,transparent 100%)}
.pblur>i:nth-child(2){-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);-webkit-mask-image:linear-gradient(to top,#000,transparent 75%);mask-image:linear-gradient(to top,#000,transparent 75%)}
.pblur>i:nth-child(3){-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);-webkit-mask-image:linear-gradient(to top,#000,transparent 50%);mask-image:linear-gradient(to top,#000,transparent 50%)}
.pblur>i:nth-child(4){-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);-webkit-mask-image:linear-gradient(to top,#000,transparent 25%);mask-image:linear-gradient(to top,#000,transparent 25%)}
```

**Mobile:** `backdrop-filter` over full-screen video is GPU-heavy on low-end phones; prefer the single-layer version there.

---

## 6. Cursor-scrubbed video (delta scrub · split dual-video)

**What / when:** A paused clip whose timeline follows horizontal mouse movement: a character turns its head, a product spins on a turntable, an object opens. It feels like a live 3D object without WebGL. Desktop only; touch falls back to autoplay.
- **Delta scrub:** relative horizontal movement moves the playhead forward or back.
- **Split dual-video:** two clips; left of centre scrubs clip A, right of centre scrubs clip B; a dead zone at the centre holds frame 0.

**Premium parameters**
- Sensitivity **0.8**: crossing the full viewport width scrubs 80 % of the clip. `Δt = (Δx / innerWidth) × 0.8 × duration`, clamped to `[0, duration]`. Relative mapping, so the first mouse move never jumps.
- **Seek queue:** never assign `currentTime` while a seek is in flight. Store the target; on `seeked`, seek again only if the target moved. Without this the decoder floods and the image freezes.
- Split: dead zone `max(30px, width × 0.05)` either side of centre; progress = distance beyond the dead-zone edge ÷ remaining half-width; keep showing the last active side inside the dead zone.
- Disabled below 1024 px and on non-hover devices (autoplay loop there; the split version alternates the two clips on `ended`).
- `muted playsinline preload="auto"`, no autoplay on desktop, `object-position: 70% center`.
- Encode for scrubbing with tiny GOPs so seeks land instantly (the difference between silky and steppy):
  `ffmpeg -i in.mp4 -an -c:v libx264 -crf 20 -g 6 -keyint_min 6 -pix_fmt yuv420p -movflags +faststart scrub.mp4` (`-g 1` = all-intra, silkiest).
- For clips under ~15 MB, load the file fully before scrubbing so every seek is local: `fetch(url).then(r => r.blob()).then(b => { video.src = URL.createObjectURL(b); })`.

**Implementation (A: delta scrub)**
```html
<video class="scrub-video" muted playsinline preload="auto" src="TURNTABLE.mp4" aria-hidden="true"></video>
```
```css
.scrub-video{position:fixed;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% center;z-index:0}
```
```js
function mouseScrubVideo(video, { sensitivity = 0.8, query = '(min-width: 1024px) and (hover: hover)' } = {}) {
  const mq = matchMedia(query);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let prevX = null, target = 0, busy = false;
  video.muted = true; video.playsInline = true;
  const flush = () => {
    if (!mq.matches || reduce.matches) { busy = false; return; }   // ignore seeks caused by normal looping
    if (Math.abs(video.currentTime - target) < 1 / 60) { busy = false; return; }
    busy = true;
    video.currentTime = target;                 // 'seeked' fires when the frame is decoded
  };
  video.addEventListener('seeked', flush);
  addEventListener('mousemove', (e) => {
    if (!mq.matches || reduce.matches || !video.duration) return;
    if (prevX === null) { prevX = e.clientX; return; }
    const dx = e.clientX - prevX; prevX = e.clientX;
    target = Math.max(0, Math.min(video.duration, target + (dx / innerWidth) * sensitivity * video.duration));
    if (!busy) flush();
  }, { passive: true });
  const applyMode = () => {
    if (reduce.matches) { video.pause(); return; }                         // still frame
    if (mq.matches) { video.loop = false; video.pause(); target = video.currentTime; }
    else { video.loop = true; video.play().catch(() => {}); }             // touch / small screens
  };
  mq.addEventListener('change', applyMode);
  reduce.addEventListener('change', applyMode);
  applyMode();
}
mouseScrubVideo(document.querySelector('.scrub-video'));
```

**Implementation (B: split dual-video with dead zone)**
```html
<div class="dual" aria-hidden="true">
  <video class="dual__v" id="vidA" src="a.mp4" muted playsinline preload="auto"></video>
  <video class="dual__v" id="vidB" src="b.mp4" muted playsinline preload="auto"></video>
</div>
```
```css
.dual{position:fixed;inset:0;z-index:0;opacity:0;transition:opacity .3s ease;pointer-events:none;overflow:hidden}
.dual.is-ready{opacity:1}
.dual__v{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
@media (max-width:640px){.dual{top:220px;height:calc(100vh - 220px)}}  /* room for stacked copy */
```
```js
(() => {
  const wrap = document.querySelector('.dual');
  const A = document.getElementById('vidA'), B = document.getElementById('vidB');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const show = (v) => { A.style.visibility = v === A ? 'visible' : 'hidden'; B.style.visibility = v === B ? 'visible' : 'hidden'; };
  Promise.all([A, B].map((v) => (v.readyState >= 2 ? 0 : new Promise((r) => v.addEventListener('loadeddata', r, { once: true })))))
    .then(() => wrap.classList.add('is-ready'));
  if (matchMedia('(hover: none)').matches) {              // touch: alternate autoplay
    [A, B].forEach((v) => v.addEventListener('ended', () => {
      const next = v === A ? B : A; next.currentTime = 0; show(next); next.play().catch(() => {});
    }));
    show(A); if (!reduce) A.play().catch(() => {});
    return;
  }
  let mouseX = innerWidth / 2, active = B;
  show(active);
  addEventListener('mousemove', (e) => { mouseX = e.clientX; }, { passive: true });
  (function frame() {
    const w = innerWidth, c = w / 2, dz = Math.max(30, w * 0.05);
    let p = -1;
    if (mouseX < c - dz)      { active = A; p = (c - dz - mouseX) / (c - dz); }
    else if (mouseX > c + dz) { active = B; p = (mouseX - c - dz) / (w - c - dz); }
    show(active);
    if (active.duration && !active.seeking) {           // never seek while seeking
      const t = p < 0 ? 0 : Math.min(1, p) * (active.duration - 0.05);
      if (Math.abs(active.currentTime - t) > 0.02) active.currentTime = t;
    }
    requestAnimationFrame(frame);
  })();
})();
```

**Reduced motion:** variant A shows a still frame; B holds frame 0 on touch. The scrub itself is user-driven, so it may stay on for fine pointers.

---

## 7. Scroll-scrubbed video with canvas frame cache

**What / when:** The page scroll *is* the video timeline: a fixed full-bleed clip advances only as the user scrolls, smoothed with a lerp. Use it for abstract or 3D "transformation" footage behind a sparse editorial page (2–3 screens of text over it). Never also autoplay it.

**Premium parameters**
- Layers bottom→top: poster `<img>` → `<video>` (seek fallback) → `<canvas>` (cached frames). Crossfades `opacity 500ms`.
- `progress = scrollY / (scrollHeight − innerHeight)`, clamped; smoothing `smooth += (target − smooth) × 0.12` per rAF.
- Frame cache: `count = clamp(round(duration × 12), 24, 90)` frames, max width **960 px** (640 px on phones). Start extracting only after the visible video has `loadeddata` + **300 ms**, so the first paint isn't starved.
- Fallback before the cache is ready: seek the `<video>` to `smooth × (duration − 0.05)` only when `|Δ| > 0.04 s` and not already seeking. Encode with short GOPs (`-g 5`, or all-intra `-g 1`).
- Canvas DPR `min(devicePixelRatio, 2)`; draw with object-cover math.
- Give the scrub room: an `~80vh` spacer between content screens so the footage visibly transforms.
- Memory: 90 frames × 960×540 RGBA ≈ 190 MB; halve the width on mobile (≈ 47 MB).

**Implementation**
```html
<div class="scrubbg" aria-hidden="true">
  <img class="scrubbg__poster" src="poster.jpg" alt="">
  <video class="scrubbg__video" src="VIDEO_URL.mp4" muted playsinline preload="auto"></video>
  <canvas class="scrubbg__canvas"></canvas>
</div>
<div class="page">
  <section class="screen">…hero copy…</section>
  <div style="height:80vh" aria-hidden="true"></div>   <!-- scrub runway -->
  <section class="screen">…second scene…</section>
</div>
```
```css
.scrubbg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:#0a0a0a}
.scrubbg>*{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .5s ease}
.scrubbg__video,.scrubbg__canvas{opacity:0}
.scrubbg.has-video .scrubbg__video{opacity:1}
.scrubbg.has-video .scrubbg__poster{opacity:0}
.scrubbg.has-frames .scrubbg__canvas{opacity:1}
.scrubbg.has-frames .scrubbg__video{opacity:0}
.page{position:relative;z-index:1}
.screen{min-height:100vh;min-height:100svh;display:flex;flex-direction:column;justify-content:space-between}
```
```js
(() => {
  const root = document.querySelector('.scrubbg');
  const video = root.querySelector('video');
  const canvas = root.querySelector('canvas');
  const ctx = canvas.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const MAX_W = matchMedia('(max-width: 768px)').matches ? 640 : 960;
  let frames = [], target = 0, smooth = 0, lastIndex = -1;

  const resize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(innerWidth * dpr);
    canvas.height = Math.round(innerHeight * dpr);
    lastIndex = -1;                                     // force a redraw
  };
  const drawCover = (img) => {
    const cw = canvas.width, ch = canvas.height;
    const s = Math.max(cw / img.width, ch / img.height);
    const w = img.width * s, h = img.height * s;
    ctx.drawImage(img, (cw - w) / 2, (ch - h) / 2, w, h);
  };
  const progress = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    return max > 0 ? Math.min(1, Math.max(0, scrollY / max)) : 0;
  };
  const once = (el, ev) => new Promise((r) => el.addEventListener(ev, r, { once: true }));
  const seekTo = (v, t) => new Promise((r) => {
    const done = () => { clearTimeout(timer); r(); };
    const timer = setTimeout(done, 1000);               // safety net
    v.addEventListener('seeked', done, { once: true });
    v.currentTime = t;
  });
  async function buildFrameCache() {
    const v = document.createElement('video');
    v.muted = true; v.playsInline = true; v.preload = 'auto';
    v.src = video.currentSrc || video.src;
    v.play().then(() => v.pause()).catch(() => {});     // iOS ignores preload until play()
    if (v.readyState < 2) await once(v, 'loadeddata');
    const count = Math.max(24, Math.min(90, Math.round(v.duration * 12)));
    const scale = Math.min(1, MAX_W / v.videoWidth);
    const w = Math.round(v.videoWidth * scale), h = Math.round(v.videoHeight * scale);
    const out = [];
    for (let i = 0; i < count; i++) {
      await seekTo(v, (i / (count - 1)) * (v.duration - 0.05));
      const c = document.createElement('canvas');      // small canvases: no CORS/ImageBitmap quirks
      c.width = w; c.height = h;
      c.getContext('2d').drawImage(v, 0, 0, w, h);
      out.push(c);
    }
    return out;
  }
  function tick() {
    target = progress();
    smooth = reduce ? target : smooth + (target - smooth) * 0.12;
    if (frames.length) {
      const i = Math.round(smooth * (frames.length - 1));
      if (i !== lastIndex) { drawCover(frames[i]); lastIndex = i; }
    } else if (video.readyState >= 1 && video.duration) {
      const t = smooth * (video.duration - 0.05);
      if (!video.seeking && Math.abs(video.currentTime - t) > 0.04) video.currentTime = t;
    }
    requestAnimationFrame(tick);
  }
  resize();
  addEventListener('resize', resize);
  video.play().then(() => video.pause()).catch(() => {}); // prime decoding on iOS
  video.addEventListener('loadeddata', async () => {
    root.classList.add('has-video');
    await new Promise((r) => setTimeout(r, 300));
    try { frames = await buildFrameCache(); lastIndex = -1; root.classList.add('has-frames'); }
    catch (e) { /* keep the seek fallback */ }
  }, { once: true });
  requestAnimationFrame(tick);
})();
```

**Notes:** drawing a cross-origin video into a canvas only "taints" it (you can't read pixels back); drawing still works, so don't set `crossOrigin` unless the host sends CORS headers (otherwise the video fails to load). Reduced motion bypasses smoothing; the scrub is user-driven, so it stays.

---

## 8. Boomerang (ping-pong) video loop

**What / when:** The clip plays forward, then backward, then forward again, with no seam. Use it for any non-looping clip: a camera push-in, a flower opening, smoke rising. It reads like slow breathing.

**Premium parameters**
- **Preferred for production:** pre-render the boomerang as a file and loop it natively:
  `ffmpeg -i in.mp4 -filter_complex "[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0[out]" -map "[out]" -an -c:v libx264 -crf 20 -movflags +faststart boomerang.mp4`
- Runtime capture (when you can't pre-render): play at 30 fps; capture frames at most 960 px wide with `requestVideoFrameCallback` (exact per-frame, rAF fallback), skipping duplicate `currentTime` values. Show the live `<video>` during the first pass, then swap to a `<canvas>` with `object-fit:cover`.
- **Memory:** each 960×540 RGBA frame ≈ 2 MB, so 150 frames ≈ 300 MB. Keep clips 3–5 s, or capture at 640 px.
- Only add `crossorigin="anonymous"` if the video host sends CORS headers.

**Implementation (runtime capture)**
```html
<div class="boomerang">
  <video muted playsinline preload="auto" src="CLIP.mp4"></video>
  <canvas hidden></canvas>
</div>
```
```css
.boomerang{position:absolute;inset:0}
.boomerang video,.boomerang canvas{width:100%;height:100%;object-fit:cover;display:block}
```
```js
function boomerangVideo(root, { maxWidth = 960, fps = 30 } = {}) {
  const video = root.querySelector('video');
  const out = root.querySelector('canvas');
  const octx = out.getContext('2d');
  const frames = [];
  let capturing = true, lastT = -1;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;   // keep the first frame
  const grab = () => {
    if (!capturing || video.readyState < 2 || video.currentTime === lastT || !video.videoWidth) return;
    lastT = video.currentTime;
    const s = Math.min(1, maxWidth / video.videoWidth);
    const c = document.createElement('canvas');
    c.width = Math.round(video.videoWidth * s);
    c.height = Math.round(video.videoHeight * s);
    c.getContext('2d').drawImage(video, 0, 0, c.width, c.height);
    frames.push(c);
  };
  const hasVFC = 'requestVideoFrameCallback' in HTMLVideoElement.prototype;
  const loop = () => { grab(); if (!capturing) return; hasVFC ? video.requestVideoFrameCallback(loop) : requestAnimationFrame(loop); };
  video.addEventListener('ended', () => {
    capturing = false;
    if (!frames.length) return;
    out.width = frames[0].width; out.height = frames[0].height;
    video.hidden = true; out.hidden = false;
    let i = frames.length - 1, dir = -1, last = 0;
    const step = 1000 / fps;
    const render = (now) => {
      if (now - last >= step) {
        last = now;
        octx.drawImage(frames[i], 0, 0);
        i += dir;
        if (i >= frames.length - 1) { i = frames.length - 1; dir = -1; }
        else if (i <= 0) { i = 0; dir = 1; }
      }
      requestAnimationFrame(render);
    };
    requestAnimationFrame(render);
  }, { once: true });
  video.muted = true; video.loop = false;
  const start = () => { video.play().catch(() => {}); loop(); };
  video.readyState >= 1 ? start() : video.addEventListener('loadedmetadata', start, { once: true });
}
document.querySelectorAll('.boomerang').forEach((el) => boomerangVideo(el));
```

---

## 9. Crossfading multi-video scene switcher with adaptive text tone

**What / when:** 3–5 stacked looping clips (moods or locations) with a small text tab row to switch scenes; the active clip crossfades in. A transparent foreground cut-out (window frame, cockpit, interior) sits on top with a gentle bob, as if looking out of a moving vehicle. Use it for "choose your atmosphere" heroes (wellness, travel, focus apps).

**Premium parameters**
- Crossfade `opacity 1000ms ease-in-out`; lock input for the same 1000 ms so clicks can't stack. Pause the outgoing clip after the fade.
- Foreground bob: `translateY(0 → -6px)` **3 s ease-in-out infinite**, constant `scale(1.03)` so edges never show.
- Adaptive tone: when a bright clip is active, the hero copy switches to a deep ink (e.g. `#182C41`) over **700 ms**; nav and footer stats stay white.
- Tabs: active = full colour + 1 px bottom border; inactive `opacity .5`, hover `.8`.

**Implementation**
```html
<section class="vswitch" data-tone="light">
  <div class="vswitch__media">
    <video class="is-active" src="scene-1.mp4" autoplay muted loop playsinline></video>
    <video src="scene-2.mp4" muted loop playsinline preload="auto"></video>
    <video src="scene-3.mp4" muted loop playsinline preload="auto"></video>
  </div>
  <img class="vswitch__overlay" src="foreground-frame.png" alt="" aria-hidden="true">
  <div class="vswitch__content">
    <h1>…</h1>
    <div class="vswitch__tabs" role="tablist" aria-label="Scene">
      <button role="tab" aria-selected="true"  data-tone="light">Scene one</button>
      <button role="tab" aria-selected="false" data-tone="light">Scene two</button>
      <button role="tab" aria-selected="false" data-tone="dark">Scene three</button>
    </div>
  </div>
</section>
```
```css
.vswitch{position:relative;height:100vh;height:100svh;overflow:hidden;background:#000}
.vswitch__media video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1s ease-in-out}
.vswitch__media video.is-active{opacity:1}
.vswitch__overlay{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:1;pointer-events:none;animation:bob 3s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) scale(1.03)}50%{transform:translateY(-6px) scale(1.03)}}
.vswitch__content{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;transition:color .7s ease}
.vswitch[data-tone="dark"] .vswitch__content{color:#182C41}
.vswitch__tabs button{background:none;border:0;border-bottom:1px solid transparent;color:inherit;opacity:.5;padding:6px 2px;cursor:pointer;transition:opacity .3s,border-color .3s}
.vswitch__tabs button:hover{opacity:.8}
.vswitch__tabs button[aria-selected="true"]{opacity:1;border-bottom-color:currentColor}
@media (prefers-reduced-motion:reduce){.vswitch__overlay{animation:none;transform:scale(1.03)}.vswitch__media video{transition:none}}
```
```js
(() => {
  const root = document.querySelector('.vswitch');
  const vids = [...root.querySelectorAll('.vswitch__media video')];
  const tabs = [...root.querySelectorAll('[role="tab"]')];
  let active = 0, locked = false;
  tabs.forEach((tab, i) => tab.addEventListener('click', () => {
    if (i === active || locked) return;
    locked = true;
    const prev = vids[active], next = vids[i];
    next.play().catch(() => {});
    next.classList.add('is-active'); prev.classList.remove('is-active');
    tabs[active].setAttribute('aria-selected', 'false'); tab.setAttribute('aria-selected', 'true');
    root.dataset.tone = tab.dataset.tone || 'light';
    active = i;
    setTimeout(() => { prev.pause(); locked = false; }, 1000);   // matches the CSS crossfade
  }));
})();
```

**Mobile:** preload only the active clip (`preload="metadata"` on the rest) to save data; the others load on first tap.
