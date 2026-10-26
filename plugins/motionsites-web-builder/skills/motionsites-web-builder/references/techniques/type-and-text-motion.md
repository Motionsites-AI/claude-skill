# Type & text motion

Entrance choreography, headline effects, display type as image, and animated numbers.

**Conventions.** Single-file, no build step, dark page unless stated. Shared tokens and helpers (paste once):
```css
:root{
  --ease-out-expo:cubic-bezier(.16,1,.3,1);
  --ease-out-quint:cubic-bezier(.22,1,.36,1);
  --ease-out-cubic:cubic-bezier(.215,.61,.355,1);
}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
```
Golden rule for every entrance: the **rest state is visible**. Hide only through `animation-fill-mode: both` or a `.js` class, so a failed script never leaves a blank page.

---

## 1. Staggered blur-rise load choreography (+ settle-zoom media)

**What / when:** The hero's first second. Each element rises a few px out of a blur into focus in a deliberate reading order (nav → eyebrow → headline lines → body → CTAs → proof strip) while the background media settles from a slight zoom. The blur is what separates premium from a plain fade-up. The default entrance for any hero.

**Premium parameters**
- Blur-rise: `opacity 0, translateY(20–28px), blur(6–12px)` (optionally `scale(.98)`) → rest, **0.85–1.1 s**, `--ease-out-expo` or `cubic-bezier(.22,1,.36,1)`. Heavier variant: `blur(20px), y 40px`, 1 s ease-out.
- The nav comes **down** from `-10…-20px` (0.5–0.8 s); content comes **up**; secondary items may slide in sideways.
- Plain rise (no blur) for paragraphs: `y 20–24px`, 0.8–1 s. `filter: blur()` on huge text is costly, so keep blur for headline lines and a few chips.
- Media settle: `scale(1.12 → 1)` 1.8 s expo (images); `scale(1.05 → 1)` + fade 1.8 s (video).
- Proven timelines (start delays):
  - Cinematic glass hero: badge .4 → headline words (stagger .1) → sub .8 → CTAs 1.1 → stat cards 1.3 → partner strip 1.4.
  - Minimal centred: headline 0 → sub .2 → CTA .4 (0.8 s, y 24).
  - Bold left-aligned: tagline 0 → heading .2 → sub .4 → CTA row .6 → stats .8 (y 30).
  - Editorial light page: nav down (0.8 s) · video settle 1.8 s · badge/eyebrow .2–.6 → heading .4–.8 → paragraph .7 → buttons .9–1.0.
  - Tight technical: brand/nav/CTA 0 → headline .06 → sub .14 → CTAs .22 → logo strip .34 (fade only, 1.1 s); y 14.
  - Nav-first: logo 0 · links .10/.15/.20/.25/.30 · nav actions .35/.40 · title .4 · description .5 · primary .6 · secondary .7.
  - Two-line headline: line 1 .25, line 2 .42, bottom-left copy .70, bottom-right copy .85.
  - Split hero: header fade-down −20 px · left copy rise 40 px 1 s · right visual `scale(.85 → 1)` 1.2 s at .3 · logo strip .6.
- Rules of thumb: 80–200 ms between siblings, everything lands by ~1.5 s, the headline gets the longest duration, logos and fine print only fade.

**Implementation**
```css
@keyframes blurRise{from{opacity:0;transform:translateY(var(--rise,28px));filter:blur(var(--blur,12px))}to{opacity:1;transform:none;filter:blur(0)}}
@keyframes fadeRise{from{opacity:0;transform:translateY(var(--rise,20px))}to{opacity:1;transform:none}}
@keyframes fadeDown{from{opacity:0;transform:translateY(-16px)}to{opacity:1;transform:none}}
@keyframes settleZoom{from{transform:scale(var(--zoom-from,1.12))}to{transform:scale(1)}}
.in-blur{animation:blurRise var(--dur,1.1s) var(--ease-out-expo) var(--d,0ms) both}
.in-fade{animation:fadeRise var(--dur,1s) var(--ease-out-expo) var(--d,0ms) both}
.in-down{animation:fadeDown .8s var(--ease-out-expo) var(--d,0ms) both}
.in-zoom{animation:settleZoom 1.8s var(--ease-out-expo) both}
@media (prefers-reduced-motion:reduce){.in-blur,.in-fade,.in-down,.in-zoom{animation:none}}
```
```html
<header class="in-down">…</header>
<div class="hero__bg in-zoom" style="background-image:url(hero.jpg)"></div>
<h1>
  <span class="in-blur" style="display:block;--d:250ms">First line</span>
  <span class="in-blur" style="display:block;--d:420ms">second line</span>
</h1>
<p class="in-fade" style="--d:700ms">Supporting copy…</p>
<a class="btn in-fade" style="--d:850ms" href="#">Primary action</a>
```
`both` keeps elements hidden only during their delay; if animations never run, everything stays visible. Gate the sequence on fonts to avoid a re-layout mid-animation:
```css
.in-blur,.in-fade{animation-play-state:paused}
.fonts-ready .in-blur,.fonts-ready .in-fade{animation-play-state:running}
```
```js
document.fonts.ready.then(() => document.documentElement.classList.add('fonts-ready'));
setTimeout(() => document.documentElement.classList.add('fonts-ready'), 1500);   // never wait forever
```

**Framer Motion variant**
```tsx
const rise = (delay = 0) => ({
  initial: { opacity: 0, y: 28, filter: 'blur(12px)' },
  animate: { opacity: 1, y: 0, filter: 'blur(0px)' },
  transition: { duration: 1.1, delay, ease: [0.16, 1, 0.3, 1] },
});
<motion.h1 {...rise(0.25)}>…</motion.h1>
// lists: variants with custom index -> delay: i * 0.12
```
**GSAP variant:** `gsap.timeline({defaults:{ease:'power3.out'}}).from('.name',{opacity:0,y:50,duration:1.2,delay:.1}).from('.blur-in',{opacity:0,y:20,filter:'blur(10px)',duration:1,stagger:.1},.3)`.

---

## 2. Fail-safe entrance system with a motion vocabulary

**What / when:** A production-grade version of technique 1. Each element picks a *verb* (scale, soft-rise, mask, pop, button, side-slide, stat) and a delay. The page can never be stuck blank, and once an animation ends its `transform` is released so hover effects work. Use it on single-file pages that want rich choreography with zero framework.

**Premium parameters**
- Resting state visible (`opacity:1`); hiding comes only from `animation-fill-mode: both`.
- Duration 1.05 s, `cubic-bezier(.16,1,.3,1)`, delay from `--d` (default .08 s). The lede gets 1.25 s.
- Vocabulary: `in-scale` `opacity 0, scale(.84)` (logo, alternating nav items) · `in-soft` `translateY(14px)` · `in-mask` `translateY(40%)` inside an overflow-hidden line · `in-pop` `scale(.9) → 1.03 @70 % → 1` (badges) · `in-btn` `translateY(18px) scale(.94)` · `in-side` `translateX(22px)` (secondary CTAs) · `in-stat` `translateY(20px)` · `in-star` `scale(.2) rotate(-50deg) → scale(1.2) rotate(8deg) @65 % → rest`, 0.9 s (sparkle icon) · `in-em` `opacity .35, blur(4px)` → sharp, 1.2 s @ .72 s (italic accent words).
- Example timeline: logo .08; nav items .16/.28/.40/.52 (alternating scale/soft); header CTA .34; badge .22; H1 line 1 .42, line 2 .62; lede .82; primary CTA .96; ghost CTA 1.10; stats 1.12/1.28/1.44.
- After `animationend` the element gets `.is-in` (`animation:none` + final values); otherwise the held `transform` from fill-mode overrides `:hover{transform}`.
- JS fallback: after two rAFs, if no animation is running or finished, force `.is-in` on everything.

**Implementation**
```css
.appear{animation-duration:1.05s;animation-fill-mode:both;animation-timing-function:cubic-bezier(.16,1,.3,1);animation-delay:var(--d,.08s)}
.appear--scale{animation-name:in-scale}
.appear--soft {animation-name:in-soft}
.appear--mask {animation-name:in-mask}
.appear--pop  {animation-name:in-pop}
.appear--btn  {animation-name:in-btn}
.appear--side {animation-name:in-side}
.appear--stat {animation-name:in-stat}
.appear.is-in{animation:none;opacity:1;transform:none;clip-path:none;filter:none}
@keyframes in-scale{from{opacity:0;transform:scale(.84)}}
@keyframes in-soft {from{opacity:0;transform:translateY(14px)}}
@keyframes in-mask {from{opacity:0;transform:translateY(40%)}}
@keyframes in-pop  {0%{opacity:0;transform:scale(.9)}70%{opacity:1;transform:scale(1.03)}100%{opacity:1;transform:scale(1)}}
@keyframes in-btn  {from{opacity:0;transform:translateY(18px) scale(.94)}}
@keyframes in-side {from{opacity:0;transform:translateX(22px)}}
@keyframes in-stat {from{opacity:0;transform:translateY(20px)}}
@keyframes in-star {0%{transform:scale(.2) rotate(-50deg)}65%{transform:scale(1.2) rotate(8deg)}100%{transform:none}}
@keyframes in-em   {from{opacity:.35;filter:blur(4px)}}
.headline-line{display:block;overflow:hidden;padding:.06em .15em .14em}  /* room for descenders/italics */
.badge-star{animation:in-star .9s cubic-bezier(.16,1,.3,1) .28s both}
h1 em{animation:in-em 1.2s cubic-bezier(.16,1,.3,1) .72s both}
@media (prefers-reduced-motion:reduce){
  .appear,.badge-star,h1 em{animation:none!important;opacity:1;transform:none;clip-path:none;filter:none}
}
```
```html
<a class="logo appear appear--scale" style="--d:.08s">…</a>
<span class="badge appear appear--pop" style="--d:.22s"><svg class="badge-star">…</svg>Label</span>
<h1>
  <span class="headline-line appear appear--mask" style="--d:.42s">First line with <em>accent</em></span>
  <span class="headline-line appear appear--mask" style="--d:.62s">second line.</span>
</h1>
<p class="lede appear appear--soft" style="--d:.82s;animation-duration:1.25s">…</p>
<a class="btn appear appear--btn" style="--d:.96s">Primary</a>
<a class="btn appear appear--side" style="--d:1.10s">Secondary</a>
```
```js
const appearEls = document.querySelectorAll('.appear');
appearEls.forEach((el) => el.addEventListener('animationend', (e) => {
  if (e.target === el) el.classList.add('is-in');     // ignore bubbling from children (e.g. <em>)
}));
requestAnimationFrame(() => requestAnimationFrame(() => {
  const running = [...appearEls].some((el) =>
    (el.getAnimations ? el.getAnimations() : []).some((a) => a.playState === 'running' || a.playState === 'finished'));
  if (!running) appearEls.forEach((el) => el.classList.add('is-in'));
}));
```

---

## 3. Word-by-word blur-in headline

**What / when:** Headline words arrive one after another, each rising from below, overshooting slightly upward and coming into focus. It feels like an exhale. Best with large italic serif display type over video. Trigger on load for heroes and on scroll-into-view for section headings.

**Premium parameters**
- Per word: `blur(10px), opacity 0, y 50px` → at 50 %: `blur(5px), opacity .5, y -5px` → `blur(0), opacity 1, y 0`. 0.7 s per word, ease-out, stagger 100 ms.
- Words are `inline-block` with `margin-right: .28em` (non-breaking spaces get eaten by tight negative tracking).
- Container `display:flex; flex-wrap:wrap; justify-content:center; row-gap:.1em`. IntersectionObserver threshold 0.1, once.
- Pairs with italic serif display ~`clamp(56px,7vw,88px)`, `line-height:.8`, `letter-spacing:-.045em`.

**Implementation**
```html
<h1 class="blur-text">Words that arrive one breath at a time</h1>
```
```css
.blur-text{display:flex;flex-wrap:wrap;justify-content:center;row-gap:.1em;
  font:italic 400 clamp(56px,7vw,88px)/.8 'Instrument Serif',serif;letter-spacing:-.045em;color:#fff}
.bt-word{display:inline-block;margin-right:.28em;opacity:0;filter:blur(10px);transform:translateY(50px);will-change:transform,filter,opacity}
.bt-word:last-child{margin-right:0}
.blur-text.is-in .bt-word{animation:bt-in .7s ease-out both;animation-delay:calc(var(--i) * var(--stagger,100ms) + var(--base,0ms))}
@keyframes bt-in{
  0%  {filter:blur(10px);opacity:0;transform:translateY(50px)}
  50% {filter:blur(5px); opacity:.5;transform:translateY(-5px)}
  100%{filter:blur(0);   opacity:1;transform:translateY(0)}
}
@media (prefers-reduced-motion:reduce){.bt-word{opacity:1;filter:none;transform:none}.blur-text.is-in .bt-word{animation:none}}
```
```js
function blurText(el, { stagger = 100, base = 0, threshold = 0.1 } = {}) {
  const words = el.textContent.trim().split(/\s+/);
  el.textContent = '';
  words.forEach((w, i) => {
    const s = document.createElement('span');
    s.className = 'bt-word'; s.textContent = w; s.style.setProperty('--i', i);
    el.append(s);
    if (i < words.length - 1) el.append(' ');   // real spaces keep copy/paste and screen readers right
  });
  el.style.setProperty('--stagger', `${stagger}ms`);
  el.style.setProperty('--base', `${base}ms`);
  const io = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) { el.classList.add('is-in'); io.disconnect(); }
  }, { threshold });
  io.observe(el);
}
document.querySelectorAll('.blur-text').forEach((el) => blurText(el));
```
The word spans are created by the script, so without JS the headline simply shows as plain text. For headlines with an `<em>` word, wrap the words by hand in `.bt-word` spans with `--i` inline and call only the observer part.

**Framer Motion variant**
```tsx
{words.map((w, i) => (
  <motion.span key={i} style={{ display: 'inline-block', marginRight: '0.28em' }}
    initial={{ filter: 'blur(10px)', opacity: 0, y: 50 }}
    animate={inView ? { filter: ['blur(10px)', 'blur(5px)', 'blur(0px)'], opacity: [0, 0.5, 1], y: [50, -5, 0] } : undefined}
    transition={{ duration: 0.7, times: [0, 0.5, 1], ease: 'easeOut', delay: i * 0.1 }}>{w}</motion.span>
))}
```

---

## 4. Split-text headline entrances (masked line/word pull-up · soft word rise · per-character cascade)

**What / when:** Headlines that assemble line by line, word by word or letter by letter. The masked pull-up (type rising out of a slot) is the classic editorial move for giant display words and stacked uppercase statements; the per-character lateral cascade feels like a sentence being written across the screen. `splitText()` below is also the splitter used by technique 10.

**Premium parameters**
- Masked lines (hand-written): `translateY(110%) → 0` inside `overflow:hidden`, 0.7 s `cubic-bezier(.22,1,.36,1)`, delays `0.4 + i × 0.14 s`. Stacked display words at line-height .88–.92, e.g. right-aligned uppercase 600 at `clamp(2rem, 9vw, 9rem)`.
- Masked words: inner word `translateY(110%) → 0`, **1.2 s** `--ease-out-expo`, stagger **60 ms** (letter blocks) to **80 ms** (words); optional parent `scale(1.03 → 1)` over the same time.
- Soft rise (no mask): `y 20px + opacity`, stagger 80 ms, ~0.8 s.
- Character cascade: `translateX(-18px) + opacity 0` → rest, 500 ms per char, **30 ms** step, starts at 200 ms; subhead at 800 ms, CTAs 1200 ms.
- The mask needs breathing room: pad the clip box `.06em .15em .14em` with an equal negative margin, or descenders and italic overhangs get cut.
- Words stay unbreakable (`white-space:nowrap` on the word wrapper); italic serif words inside `<em>` keep their styling after splitting.

**Implementation (hand-written masked lines, CSS only)**
```html
<h1 class="mask-lines">
  <span class="ml"><span style="--i:0">Make</span></span>
  <span class="ml"><span style="--i:1">Things</span></span>
  <span class="ml"><span style="--i:2">Last</span></span>
</h1>
```
```css
.mask-lines{margin:0;font:600 clamp(2rem,9vw,9rem)/.88 Inter,sans-serif;text-transform:uppercase;text-align:right;letter-spacing:-.02em}
.ml{display:block;overflow:hidden;padding:.06em .15em .14em;margin:-.06em -.15em -.14em}
.ml>span{display:block;animation:ml-up .7s cubic-bezier(.22,1,.36,1) both;animation-delay:calc(.4s + var(--i) * .14s)}
@keyframes ml-up{from{transform:translateY(110%)}}
@media (prefers-reduced-motion:reduce){.ml>span{animation:none}}
```

**Implementation (automatic splitter)**
```js
// modes: 'words' (masked pull-up) | 'chars' (lateral cascade) | 'plain' (bare word spans) | 'plain-chars'
function splitText(root, mode = 'words') {
  if (root.dataset.splitDone) return;
  root.dataset.splitDone = '1';
  // Word spans read fine in screen readers. Letter spans can be spelled out, so in char modes
  // the split copy is aria-hidden and one clean visually-hidden copy is added.
  const charMode = mode === 'chars' || mode === 'plain-chars';
  const plain = (root.innerText || root.textContent).replace(/\s+/g, ' ').trim();
  let i = 0;
  const span = (cls, text) => { const s = document.createElement('span'); s.className = cls; if (text != null) s.textContent = text; return s; };
  const walk = (node) => [...node.childNodes].forEach((n) => {
    if (n.nodeType === Node.ELEMENT_NODE) return walk(n);       // keeps <em>, <strong>, <br>
    if (n.nodeType !== Node.TEXT_NODE) return;
    const frag = document.createDocumentFragment();
    n.textContent.split(/(\s+)/).forEach((part) => {
      if (!part) return;
      if (/^\s+$/.test(part)) { frag.append(' '); return; }
      if (charMode) {
        const w = span(mode === 'chars' ? 'sc-w' : 'sp-w');
        w.setAttribute('aria-hidden', 'true');
        for (const ch of part) { const c = span(mode === 'chars' ? 'sc-c' : 'sp', ch); c.style.setProperty('--i', i++); w.append(c); }
        frag.append(w);
      } else if (mode === 'plain') {
        const w = span('sp', part); w.style.setProperty('--i', i++); frag.append(w);
      } else {
        const o = span('sw-o'), inner = span('sw-i', part);
        inner.style.setProperty('--i', i++); o.append(inner); frag.append(o);
      }
    });
    n.replaceWith(frag);
  });
  walk(root);
  if (charMode) root.prepend(span('sr-only', plain));
  return i;   // number of pieces
}
// Hero (on load): split, then add .is-in after the first paint.
document.querySelectorAll('[data-split-text]').forEach((el) => {
  splitText(el, el.dataset.splitText);
  requestAnimationFrame(() => requestAnimationFrame(() => el.classList.add('is-in')));
});
// Below the fold: add .is-in from an IntersectionObserver instead (scroll.md, technique 1).
```
```css
/* masked word pull-up */
.sw-o{display:inline-block;overflow:hidden;vertical-align:top;padding:0 .06em .14em;margin:0 -.06em -.14em}
.sw-i{display:inline-block;transform:translateY(110%);transition:transform var(--dur,1.2s) var(--ease-out-expo);
  transition-delay:calc(var(--start,0ms) + var(--i) * var(--step,60ms))}
.is-in .sw-i{transform:none}
/* soft word rise (no mask) */
.split-soft .sw-o{overflow:visible}
.split-soft .sw-i{transform:translateY(20px);opacity:0;transition-property:transform,opacity;--dur:.8s;--step:80ms}
.split-soft.is-in .sw-i{transform:none;opacity:1}
/* per-character lateral cascade */
.sc-w{display:inline-block;white-space:nowrap}
.sc-c{display:inline-block;opacity:0;transform:translateX(-18px);transition:opacity .5s ease-out,transform .5s ease-out;
  transition-delay:calc(var(--start,200ms) + var(--i) * 30ms)}
.is-in .sc-c{opacity:1;transform:none}
.sp-w{display:inline-block;white-space:nowrap}
@media (prefers-reduced-motion:reduce){.sw-i,.sc-c{transition:none!important;transform:none!important;opacity:1!important}}
```
```html
<h1 data-split-text="words" style="font-size:clamp(4rem,20vw,18rem);line-height:.85;letter-spacing:-.07em">Wordmark</h1>
<h2 data-split-text="words" class="split-soft">I make <em>quiet, cinematic</em> work.</h2>
<h1 data-split-text="chars">Shaping tomorrow<br>with vision and action.</h1>
```

**Framer Motion variant:** `<span className="block overflow-hidden"><motion.span className="block" initial={{ y: '110%' }} animate={{ y: 0 }} transition={{ delay: 0.4 + i * 0.14, duration: 0.7, ease: [0.22, 1, 0.36, 1] }} /></span>`; for soft words use `initial={{y:20,opacity:0}}` with `useInView(ref,{once:true})` and `delay: i*0.08`.

---

## 5. Serif-italic accent words inside a headline

**What / when:** One to three words of a headline switch to an italic display serif, a touch larger and in a muted tone. The headline gains a spoken emphasis and an editorial voice. One of the most reliable premium signals; use it whenever a headline has a natural key phrase.

**Premium parameters**
- Sans base: Inter 500, `letter-spacing:-.045em`, `line-height:1.12`. Accent: Instrument Serif italic 400 at `1.08em` (serif x-height is smaller), `letter-spacing:-.03em`.
- Accent colour is **muted, not brighter**: `#9a9a9a` on black, `#6F6F6F` on white, or `rgba(255,255,255,.6–.8)`. A contrasting hue also works (deep green `#336443` with sage `#85AB8B`).
- Inverse version: an all-serif headline (`line-height:.95`, `letter-spacing ≈ -.025em`) with the italic words greyed out.
- Tone-only variant: no italics, just `<em class="not-italic">` in the muted foreground.
- Optional sharpen-in: the accent starts at `opacity .35, blur(4px)` and focuses over 1.2 s after its line lands (.72 s).
- Pairings: Inter + Instrument Serif; Poppins + Source Serif 4 italic; Barlow body with an all-italic Instrument Serif display; Playfair Display italic as the accent.

**Implementation**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<h1 class="mixed">Ship <em>calmer software</em><br>in half the time.</h1>
```
```css
.mixed{font:500 clamp(36px,4.4vw,76px)/1.12 Inter,system-ui,sans-serif;letter-spacing:-.045em;color:#fff;text-align:center}
.mixed em{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;font-size:1.08em;
  letter-spacing:-.03em;color:#9a9a9a;animation:em-sharpen 1.2s cubic-bezier(.16,1,.3,1) .72s both}
@keyframes em-sharpen{from{opacity:.35;filter:blur(4px)}}
@media (prefers-reduced-motion:reduce){.mixed em{animation:none}}
```

---

## 6. Gradient-clipped text: static metallic and animated shine sweep

**What / when:** **Metallic:** a vertical two-stop gradient clipped to giant type, reading as brushed steel lit from below; use it for name-as-hero portfolios and section titles. **Shine sweep:** a multi-stop gradient whose highlight travels endlessly through one key word; use it for the single "magic" word of a SaaS headline. Gradient text is rare by design: one element per page.

**Premium parameters**
- Metallic: `linear-gradient(180deg, #646973 0%, #BBCCD7 100%)` (dark top → cool light bottom) on weight 900, uppercase, `line-height:1`, tight tracking.
- Sweep stops `dark 0 % → brand-dark 12.5 % → highlight 32.5 % → brand 50 % → brand-dark 67.5 % → dark 87.5–100 %`. First and last stops must match so the tile repeats seamlessly. `background-size:200% auto`, position `-200% → 200%`, 6 s linear infinite.
- Choose base stops for contrast with what's behind: on black use mid-greys or blues, not near-black.
- Optional grain inside the glyphs (surfaces-and-buttons.md, technique 8) makes the gradient feel printed; drop it ≤1024 px.

**Implementation**
```css
.text-metal{background:linear-gradient(180deg,#646973 0%,#BBCCD7 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.text-shine{background-image:linear-gradient(to right,#091020 0%,#0B2551 12.5%,#A4F4FD 32.5%,#00d2ff 50%,#0B2551 67.5%,#091020 87.5%,#091020 100%);
  background-size:200% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent;
  animation:shine 6s linear infinite}
@keyframes shine{from{background-position:-200% center}to{background-position:200% center}}
@media (prefers-reduced-motion:reduce){.text-shine{animation:none;background-position:30% center}}
```
```html
<h1 style="font:600 clamp(40px,7vw,72px)/.9 Inter,sans-serif;letter-spacing:-.025em">Your workflow.<br><span class="text-shine">Reimagined</span></h1>
```
Keep `color:transparent` together with `-webkit-text-fill-color` (engines differ). Theme `::selection` so selected gradient text stays readable.

---

## 7. Scramble / decode text (entrance + hover)

**What / when:** Characters resolve from random glyphs left to right, like a terminal decoding: on entrance for headline lines, on hover for nav links and buttons. Made for AI, tech and sci-fi brands, especially in a monospace.

**Premium parameters**
- Glyph set `A–Z a–z 0–9 !@#$%^&*()_+~|}{[]:;?><`.
- Entrance: tick **25 ms**, reveal cursor advances **0.5 chars/tick**; up to **3** random glyphs run ahead of it and nothing beyond (the text "grows"). Spaces stay spaces. Line delays e.g. 200 / 500 / 700 / 1000 ms for four corner lines.
- Hover: everything scrambles, then resolves at **4 ticks per char**; unhover snaps back instantly.
- Use a **monospace** face: constant glyph widths mean zero jitter.
- Pair with a body paragraph that simply fades up (y 25 → 0, 0.9 s, `--ease-out-cubic`, 0.2 s delay).

**Implementation**
```js
const GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~|}{[]:;?><';
const randGlyph = () => GLYPHS[(Math.random() * GLYPHS.length) | 0];

function scrambleIn(el, { delay = 0, speed = 0.5, lookahead = 3, tick = 25 } = {}) {
  const text = el.textContent;
  const sr = document.createElement('span'); sr.className = 'sr-only'; sr.textContent = text;
  el.after(sr); el.setAttribute('aria-hidden', 'true');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  el.textContent = ' ';
  setTimeout(() => {
    let pos = 0;
    const id = setInterval(() => {
      pos += speed;
      const shown = Math.floor(pos);
      let out = '';
      for (let i = 0; i < text.length; i++) {
        if (i >= shown + lookahead) break;
        out += text[i] === ' ' ? ' ' : i < shown ? text[i] : randGlyph();
      }
      el.textContent = out || ' ';
      if (shown >= text.length) { clearInterval(id); el.textContent = text; }
    }, tick);
  }, delay);
}
function scrambleOnHover(el, { framesPerChar = 4, tick = 25 } = {}) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const text = el.textContent; let id = 0;
  el.addEventListener('mouseenter', () => {
    let frame = 0; clearInterval(id);
    id = setInterval(() => {
      const revealed = Math.floor(frame / framesPerChar);
      el.textContent = [...text].map((c, i) => (c === ' ' ? ' ' : i < revealed ? c : randGlyph())).join('');
      if (revealed >= text.length) { clearInterval(id); el.textContent = text; }
      frame++;
    }, tick);
  });
  el.addEventListener('mouseleave', () => { clearInterval(id); el.textContent = text; });
}
document.querySelectorAll('[data-scramble]').forEach((el) => scrambleIn(el, { delay: +(el.dataset.delay || 0) }));
document.querySelectorAll('[data-scramble-hover]').forEach((el) => scrambleOnHover(el));
```
```html
<h1 class="mono"><span data-scramble data-delay="200">Line one</span><br><span data-scramble data-delay="500">Line two</span></h1>
<a href="#about"><span data-scramble-hover>About</span></a>
```
**Layout:** reserve each line's width (`display:inline-block; min-width: Nch` in a mono face) so the growing entrance never reflows neighbours.

---

## 8. Typewriter with zero-reflow caret, two-tone text and a depth-of-field lead-in

**What / when:** An "assistant is speaking" hero or a typed headline: a soft, out-of-focus intro line sits above a sharp line that types itself out with a blinking caret, optionally switching colour mid-sentence, followed by quick-reply pills or a CTA. For AI products, agencies with a persona, and contact pages.

**Premium parameters**
- **35–38 ms/char**, start delay **400–600 ms**. The caret disappears when typing ends.
- Caret: `2px × 1.1em`, `currentColor` or the accent, `blink 1s step-end infinite`; `margin-right:-2px` cancels its own width so it never pushes a word to the next line.
- **Zero reflow:** the untyped remainder is rendered `color: transparent`, so the block holds its final size and line breaks from frame one (no `min-height` hacks). `white-space: pre-wrap` supports `\n`.
- Two-tone: split at a character index (e.g. first ~60 % dark, the rest light), great over a split-tone background.
- **Depth-of-field lead-in:** the line above is the same size (`clamp(18px,4vw,26px)`, lh 1.33) with `filter: blur(4px)`, non-selectable: the eye racks focus onto the sharp line.
- Follow-ups: a CTA at typing end + ~200 ms; or quick-reply pills independently at 400 ms (`opacity + translateY(8px)`, 0.4 s). Pills: white, black text, `1px solid rgba(0,0,0,.1)`, 13–15 px, `padding:.3em 1.25em`; hover inverts over 200 ms; an outline pill copies an email to the clipboard.
- Large contact-headline variant: 48 → 76 px, `line-height 1.08`, tight tracking.

**Implementation**
```html
<div class="persona">
  <p class="voice" aria-hidden="true">Hi, I'm the studio's assistant,<br>here to point you the right way</p>
  <p class="tw" data-text="Good to see you. What are we making today?" data-split="17"></p>
  <div class="replies">
    <button class="reply">Start a project</button>
    <button class="reply">See open roles</button>
    <button class="reply reply--outline" data-copy="hello@example.com">Reach us: <u>hello@example.com</u></button>
  </div>
</div>
```
```css
.persona{max-width:36rem;color:#fff}
.voice,.tw{font-size:clamp(18px,4vw,26px);line-height:1.33;font-weight:400;margin:0 0 24px}
.voice{filter:blur(4px);user-select:none;pointer-events:none}
.tw{white-space:pre-wrap}
.tw__a{color:inherit}
.tw__b{color:var(--tw-b,rgb(255 255 255/.55))}     /* second tone */
.tw__rest{color:transparent}
.tw__caret{display:inline-block;width:2px;height:1.1em;margin-right:-2px;vertical-align:-.15em;
  background:var(--accent,currentColor);animation:tw-blink 1s step-end infinite}
.tw.is-done .tw__caret{display:none}
@keyframes tw-blink{0%,100%{opacity:1}50%{opacity:0}}
.replies{display:flex;flex-wrap:wrap;row-gap:4px;opacity:0;transform:translateY(8px);transition:opacity .4s ease,transform .4s ease}
.replies.is-in{opacity:1;transform:none}
.reply{display:inline-flex;align-items:center;gap:10px;white-space:nowrap;border-radius:999px;cursor:pointer;
  background:#fff;color:#000;border:1px solid rgba(0,0,0,.1);font-size:clamp(13px,1.2vw,15px);
  padding:.3em 1.25em;margin:0 .2em .4em;transition:background-color .2s,color .2s}
.reply:hover{background:#000;color:#fff}
.reply--outline{background:transparent;color:#fff;border-color:#fff}
.reply--outline:hover{background:#fff;color:#000}
@media (prefers-reduced-motion:reduce){.tw__caret{animation:none}}
```
```js
function typewriter(el, { speed = 36, startDelay = 500, onDone } = {}) {
  const text = el.dataset.text.replace(/\\n/g, '\n');
  const split = el.dataset.split ? +el.dataset.split : text.length;   // chars before split use tone A
  const sr = document.createElement('span'); sr.className = 'sr-only'; sr.textContent = text;
  const vis = document.createElement('span'); vis.setAttribute('aria-hidden', 'true');
  vis.innerHTML = '<span class="tw__a"></span><span class="tw__b"></span><span class="tw__caret"></span><span class="tw__rest"></span>';
  el.replaceChildren(sr, vis);
  const [a, b, , rest] = vis.children;
  const paint = (n) => {
    const k = Math.min(n, split);
    a.textContent = text.slice(0, k);
    b.textContent = text.slice(k, n);
    rest.textContent = text.slice(n);
  };
  const finish = () => { el.classList.add('is-done'); onDone && onDone(); };
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { paint(text.length); return finish(); }
  paint(0);
  setTimeout(() => {
    let n = 0;
    const id = setInterval(() => { paint(++n); if (n >= text.length) { clearInterval(id); finish(); } }, speed);
  }, startDelay);
}
typewriter(document.querySelector('.tw'));
setTimeout(() => document.querySelector('.replies').classList.add('is-in'), 400);
// or: typewriter(el, { onDone: () => setTimeout(() => cta.classList.add('is-in'), 200) });
document.querySelectorAll('[data-copy]').forEach((b) => b.addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(b.dataset.copy); b.dataset.state = 'copied'; } catch {}   // https or localhost only
}));
```

**React variant:** a `useTypewriter(text, speed = 36, startDelay = 500)` hook returning `{ count, done }` (a `setTimeout` that starts a `setInterval`, both cleared on unmount), rendered with the same three spans: `text.slice(0,count)`, caret, and `text.slice(count)` in transparent.

---

## 9. Rotating word slot (zero-reflow)

**What / when:** One word inside a sentence cycles through alternatives ("A ___ based in …"), set in an italic serif accent. Also used for the cycling word in a preloader. Adds personality without extra copy.

**Premium parameters:** interval **2 s** (sentence) / **900 ms** (preloader); enter `opacity 0, translateY(8px)` → rest in **0.4 s ease-out**, exit upward (preloader travels ±20 px). All words are stacked in one grid cell, so the slot is as wide as the longest word and the sentence never reflows.

**Implementation**
```html
<p class="role-line">A <span class="rotator" data-interval="2000" aria-hidden="true">
  <span class="is-active">designer</span><span>developer</span><span>founder</span><span>writer</span>
</span><span class="sr-only">designer, developer, founder and writer</span> based somewhere nice.</p>
```
```css
.rotator{display:inline-grid;vertical-align:bottom;font-family:'Instrument Serif',serif;font-style:italic}
.rotator>span{grid-area:1/1;justify-self:center;opacity:0;transform:translateY(8px);transition:opacity .4s ease-out,transform .4s ease-out}
.rotator>span.is-active{opacity:1;transform:none}
.rotator>span.is-leaving{opacity:0;transform:translateY(-8px)}
```
```js
document.querySelectorAll('.rotator').forEach((r) => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const items = [...r.children];
  let i = Math.max(0, items.findIndex((s) => s.classList.contains('is-active')));
  setInterval(() => {
    const prev = items[i];
    prev.classList.replace('is-active', 'is-leaving');
    setTimeout(() => prev.classList.remove('is-leaving'), 400);
    i = (i + 1) % items.length;
    items[i].classList.add('is-active');
  }, +r.dataset.interval || 2000);
});
```
Single-element variant (used by the preloader in technique 13): `swapWord()` animates the old text out with WAAPI and the new one in.

---

## 10. Scroll-linked word-by-word (or char-by-char) opacity reveal

**What / when:** A manifesto or About paragraph in large type starts at 15–20 % opacity and "lights up" piece by piece as the reader scrolls through it, so reading pace is tied to the scrollbar. Highlight 2–3 key words in full foreground while the rest end on a softer tone. One or two per page.

**Premium parameters**
- Start opacity **0.15** (words) / **0.2** (chars); end 1.
- Progress window `['start 0.8', 'end 0.2']`: 0 when the block's top hits 80 % of the viewport, 1 when its bottom reaches 20 %.
- Per-piece window `[i/N − 0.1, i/N + 0.05]` (soft overlap), or strict `[i/N, (i+1)/N]` for a crisper sweep (`before:0, after:1/N`).
- Type: words `clamp(1.5rem, 4vw, 3rem)`, 500, `letter-spacing:-1px`, lh 1.2; chars version centred, `max-width:560px`, `clamp(1rem,2vw,1.35rem)`, lh 1.625, a cool light tone (e.g. `#D7E2EA`) on near-black.
- Opacity-only, so no layout shift; pieces are inline spans, so line breaking stays natural.

**Implementation** (needs `splitText()` from technique 4: `'plain'` for words, `'plain-chars'` for characters)
```html
<p class="scroll-reveal">We're building a place where <span class="hl">depth</span> meets
<span class="hl">clarity</span>, and every word arrives as you get to it.</p>
```
```css
.scroll-reveal{font-size:clamp(1.5rem,4vw,3rem);font-weight:500;letter-spacing:-1px;line-height:1.2;color:hsl(210 17% 82%)}
.scroll-reveal .hl{color:#fff}
.scroll-reveal .sp{opacity:.15}
```
```js
function scrollReveal(el, { mode = 'plain', from = 0.15, start = 0.8, end = 0.2, before = 0.1, after = 0.05 } = {}) {
  splitText(el, mode);
  const pieces = [...el.querySelectorAll('.sp')], N = pieces.length;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let last = -1, ticking = false;
  const update = () => {
    ticking = false;
    const r = el.getBoundingClientRect(), vh = innerHeight;
    const p = reduce ? 1 : Math.min(1, Math.max(0, (start * vh - r.top) / ((start - end) * vh + r.height)));
    if (Math.abs(p - last) < 0.0005) return;
    last = p;
    pieces.forEach((s, i) => {
      const a = i / N - before, b = i / N + after;
      const t = Math.min(1, Math.max(0, (p - a) / (b - a)));
      s.style.opacity = (from + (1 - from) * t).toFixed(3);
    });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('resize', update);
  update();
}
document.querySelectorAll('.scroll-reveal').forEach((el) => scrollReveal(el));
// characters: scrollReveal(el, { mode: 'plain-chars', from: 0.2, before: 0, after: 1 / el.textContent.length })
```

**Framer Motion variant:** `const {scrollYProgress} = useScroll({target: ref, offset: ['start 0.8','end 0.2']})`; per piece `const o = useTransform(scrollYProgress, [i/N - 0.1, i/N + 0.05], [0.15, 1])` on a `motion.span`.

---

## 11. Giant display type as image (ghost word behind subject · edge-to-edge wordmark · watermark · scattered words)

**What / when:** Type set so large it becomes architecture. Patterns:
- **Ghost word behind a cut-out subject:** a viewport-wide word sits *between* the background and a transparent product/character/portrait, so the subject stands in front of the letters. Instant depth and a poster composition.
- **Edge-to-edge name / wordmark:** anchored at the bottom or top of the hero, almost touching both edges, often metallic (technique 6), with a tiny superscript mark.
- **Echo / ghost watermark:** the hero line repeated as an enormous low-opacity backdrop title for a later section (pricing, CTA), with cards sitting over it.
- **Scattered words:** a 3-word headline broken across the viewport (left / right / indented), with tiny stats tucked into the gaps.

**Premium parameters**
- Ghost word: condensed heavy face (Anton-style), uppercase, `clamp(90px, 28vw, 380px)`, lh 1, `letter-spacing:-.02em`, nowrap, solid white on a saturated background, `top:18%`. The subject PNG is anchored at the bottom (`object-fit:contain; object-position:bottom center`) and scaled up (×1.68 desktop, ×1.25 mobile) so it covers the lower half of the letters. Z-order: background → word (2) → subject (3) → grain (50) → UI (60).
- Photographic variant: serif title `clamp(4.5rem,14vw,14rem)` / lh .78, width `min(94vw,1780px)`, `top: clamp(122px,19vh,205px)`, cream `#fdf1e1` over a landscape, with the subject cut-out at `bottom:5vh`.
- Wordmark: `19–26vw` (stepping 26 → 24 → 22 → 20 → 19vw by breakpoint), lh .85, `letter-spacing:-.07em`, weight 500; superscript mark `position:absolute; top:.65em; right:-.3em; font-size:.31em`. Name-as-hero: `14vw → 17.5vw`, weight 900, uppercase, with a portrait (280 → 520 px) centred at the bottom overlapping the name.
- Ghost watermark: `clamp(120px, 30vw, 521px)`, uppercase condensed, `letter-spacing:-4px`, `opacity .10`, fill `radial-gradient(circle, rgba(c,0) 0%, c 70%)` via `background-clip:text`, centred +50 px below middle. Echo title alternative: ~9rem / 800 / `-.05em` / lh .9, dropping to 3.5rem solid colour ≤1024 px.
- Scattered: words `14vw` (mobile) / `13vw`, lh .95, `-.04em`, all lowercase; at `top 18 % left` · `top 38 % right` · `top 58 % left 18–28 %`; a note `max-width 240px; 15px` at `top 46 %`; stats 36–48 px with rotated hairlines (`96×1 px`, `rgba(255,255,255,.4)`, `rotate(±20deg)`) and 12–14 px labels at 70 %; a bottom gradient to black.
- For an **exact** full-width fit, measure and scale after `document.fonts.ready` (vw sizes drift with font metrics). Pair the wordmark with a 12-column bottom grid (8 for the word, 4 for a short paragraph + CTA) and animate it with the masked pull-up (technique 4).

**Implementation**
```html
<!-- Ghost word behind a cut-out -->
<section class="ghost-stage">
  <div class="ghost-word" aria-hidden="true">FORM</div>
  <img class="ghost-subject" src="subject.png" alt="Product figure">
  <div class="ghost-ui"><!-- labels, arrows, CTA --></div>
</section>
<!-- Edge-to-edge wordmark -->
<div class="mega-wrap"><h1 class="mega" data-fit>Wordmark<sup class="mega__mark">*</sup></h1></div>
<!-- Ghost gradient watermark (inside a position:relative section) -->
<div class="ghost-mark" aria-hidden="true">Studio</div>
```
```css
.ghost-stage{position:relative;height:100vh;height:100dvh;overflow:hidden;background:var(--stage-bg,#F4845F)}
.ghost-word{position:absolute;left:0;right:0;top:18%;z-index:2;display:flex;justify-content:center;
  font:400 clamp(90px,28vw,380px)/1 Anton,Impact,'Arial Narrow',sans-serif;letter-spacing:-.02em;
  text-transform:uppercase;white-space:nowrap;color:#fff;pointer-events:none;user-select:none}
.ghost-subject{position:absolute;left:50%;bottom:0;height:92%;z-index:3;
  transform:translateX(-50%) scale(1.68);transform-origin:bottom center;object-fit:contain;object-position:bottom center}
.ghost-ui{position:relative;z-index:60}
@media (max-width:639px){.ghost-subject{height:60%;bottom:22%;transform:translateX(-50%) scale(1.25)}}

.mega-wrap{width:100%;overflow:hidden}
.mega{position:relative;display:inline-block;margin:0;white-space:nowrap;font-size:19vw;font-weight:500;line-height:.85;letter-spacing:-.07em;color:#E1E0CC}
.mega__mark{position:absolute;top:.65em;right:-.3em;font-size:.31em;line-height:1}

.ghost-mark{position:absolute;left:50%;top:calc(50% + 50px);translate:-50% -50%;z-index:0;margin:0;pointer-events:none;user-select:none;
  white-space:nowrap;text-transform:uppercase;letter-spacing:-4px;opacity:.1;
  font:400 clamp(120px,30vw,521px)/1 'Anton',Impact,sans-serif;
  background:radial-gradient(circle,rgba(142,127,148,0) 0%,#8E7F94 70%);
  -webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
```
```js
// Exact fit-to-width: the element must be display:inline-block; white-space:nowrap
function fitToWidth(el) {
  let lastW = 0;
  const fit = () => {
    const w = el.parentElement.clientWidth;
    if (!w || w === lastW) return;
    lastW = w;
    el.style.fontSize = '100px';
    el.style.fontSize = (100 * w / el.getBoundingClientRect().width).toFixed(2) + 'px';
  };
  new ResizeObserver(fit).observe(el.parentElement);
  if (document.fonts) document.fonts.ready.then(() => { lastW = 0; fit(); });
}
document.querySelectorAll('[data-fit]').forEach(fitToWidth);
```
Scattered words:
```html
<section class="scatter">
  <video class="scatter__bg" src="VIDEO_URL.mp4" autoplay muted loop playsinline aria-hidden="true"></video>
  <h1><span class="scatter__w scatter__w--1">first</span> <span class="scatter__w scatter__w--2">second</span> <span class="scatter__w scatter__w--3">third</span></h1>
  <p class="scatter__note">A two-line supporting sentence tucked into the gap.</p>
  <div class="scatter__stat" style="right:96px;top:14%;text-align:right">
    <div class="scatter__stat-row" style="justify-content:flex-end"><span class="scatter__rule" style="rotate:20deg"></span><span class="scatter__stat-num">+65k</span></div>
    <div class="scatter__label">customers</div>
  </div>
</section>
```
```css
.scatter{position:relative;height:100vh;height:100dvh;overflow:hidden;background:#000;color:#fff}
.scatter__bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.scatter h1{margin:0;font:inherit}
.scatter__w{position:absolute;margin:0;font-size:14vw;font-weight:500;line-height:.95;letter-spacing:-.04em}
.scatter__w--1{left:16px;top:18%}.scatter__w--2{right:16px;top:38%}.scatter__w--3{left:18%;top:58%}
.scatter__note{position:absolute;left:24px;top:46%;max-width:240px;font-size:15px;line-height:1.375;color:rgba(255,255,255,.9)}
.scatter__stat{position:absolute}
.scatter__stat-row{display:flex;align-items:center;gap:12px}
.scatter__stat-num{font-size:clamp(36px,4vw,48px);font-weight:500;letter-spacing:-.025em}
.scatter__rule{display:none;width:96px;height:1px;background:rgba(255,255,255,.4)}
.scatter__label{margin-top:4px;font-size:14px;color:rgba(255,255,255,.7)}
@media (min-width:768px){.scatter__w{font-size:13vw}.scatter__w--1{left:40px}.scatter__w--2{right:40px}.scatter__w--3{left:28%}.scatter__rule{display:block}}
```

**Mobile:** retest the subject/word overlap at 375 px; clip the root with `overflow-x:clip` so vw type never causes horizontal scroll.

---

## 12. Geometric SVG wordmark assembly

**What / when:** A full-width wordmark drawn from flat polygons (verticals, diagonals, crossbars). On load each polygon slides up from below the SVG's edge in a quick cascade while the whole mark settles from a 3 % zoom, like type being set in metal. Ideal for museum, institution or studio headers.

**Premium parameters:** each block `translateY(120 user units) → 0` + fade, **1.2 s** `--ease-out-expo`, stagger **60 ms** after 100 ms; parent `scale(1.03 → 1)` 1.4 s; stroke weight 14 units on a 100-unit cap height; letter gap ~66 units; fill `#111` on `#fcfcfc`.

**Implementation**
```html
<h1 class="wm" aria-label="NH"><!-- set aria-label to the real word -->
  <svg viewBox="0 0 494 100" aria-hidden="true" focusable="false">
    <g>                                     <!-- N -->
      <polygon style="--i:0" points="0,0 14,0 14,100 0,100"/>
      <polygon style="--i:1" points="200,0 214,0 214,100 200,100"/>
      <polygon style="--i:2" points="0,0 33,0 214,100 181,100"/>
    </g>
    <g transform="translate(280,0)">        <!-- H -->
      <polygon style="--i:3" points="0,0 14,0 14,100 0,100"/>
      <polygon style="--i:4" points="200,0 214,0 214,100 200,100"/>
      <polygon style="--i:5" points="14,43 200,43 200,57 14,57"/>
    </g>
  </svg>
</h1>
```
```css
.wm{margin:0}
.wm svg{display:block;width:100%;height:auto;fill:#111;overflow:hidden;animation:wm-settle 1.4s var(--ease-out-expo) both}
.wm polygon{animation:wm-block 1.2s var(--ease-out-expo) both;animation-delay:calc(100ms + var(--i) * 60ms)}
@keyframes wm-block{from{transform:translateY(120px);opacity:0}}
@keyframes wm-settle{from{transform:scale(1.03)}to{transform:scale(1)}}
@media (prefers-reduced-motion:reduce){.wm svg,.wm polygon{animation:none}}
```
CSS `px` on SVG children equals user units, so 120 px is more than the 100-unit cap height and each block starts fully below the viewBox (the SVG clips it). Letter recipes: **M** = two verticals + two diagonals meeting at the bottom centre; **A/V** = two diagonals + optional bar.

---

## 13. Count-up statistics & counter preloader

**What / when:** Stat values roll up from zero when the row becomes visible, each slightly later and longer than the previous one (hero footers, proof bars, orbit centres). And a full-screen intro loader: a 000 → 100 counter in huge display numerals, a cycling word in italic serif and a hairline gradient progress bar, after which the hero entrance plays.

**Premium parameters**
- easeOutCubic `1 − (1 − t)³`. In a row: duration `1500 + i × 80` ms, delay `480 + i × 90` ms, so counting starts as the row's entrance lands. Single big metric: 2 s.
- IntersectionObserver threshold 0.25, once. `font-variant-numeric: tabular-nums`; fixed decimals (`99.99`); prefix/suffix (`+`, `k+`, `%`, `ms`, `/7`, `M`) outside the animated digits.
- The **final value is in the HTML**, so no-JS users, crawlers and reduced-motion users see real numbers; JS resets to 0 just before animating.
- Compact proof bar: icon glyph → value `clamp(18px, 2.2vw, 26px)` `-.025em` → muted label `clamp(11px, 1.2vw, 12.5px)` `#8e8e8e`; 4 columns → 2×2 at ≤720 px.
- Big metric: `clamp(48px, 10vw, 96px)`, weight 300, `-.04em`, lh 1; label 13–15 px at 40 % white, `margin-top:16px`; columns stagger 0.15 s.
- Loader: **2.7 s** rAF counter, `padStart(3,'0')`; numerals 60 → 128 px display serif bottom-right; words cycle every **900 ms** (y 20 → 0 → −20); eyebrow 12 px uppercase `.3em` top-left; bar **3 px**, gradient `scaleX(p)`, glow `0 0 8px rgba(accent,.35)`; hold **400 ms** at 100, fade out 0.6 s, then start the hero timeline. Skip it on repeat visits in the same session.

**Implementation**
```html
<div class="stats-grid" data-count-group>
  <div class="stat"><span class="stat-val" data-count="120" data-suffix="ms">120ms</span><span class="stat-label">Response time</span></div>
  <div class="stat"><span class="stat-val" data-count="99.99" data-decimals="2" data-suffix="%">99.99%</span><span class="stat-label">Uptime</span></div>
  <div class="stat"><span class="stat-val" data-count="2.4" data-decimals="1" data-suffix="M">2.4M</span><span class="stat-label">Active users</span></div>
</div>
```
```css
.stats-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:920px;margin:0 auto;text-align:center}
.stat{display:flex;flex-direction:column;align-items:center;gap:6px}
.stat-val{font-size:clamp(18px,2.2vw,26px);letter-spacing:-.025em;color:#fff;font-variant-numeric:tabular-nums}
.stat-label{font-size:clamp(11px,1.2vw,12.5px);color:#8e8e8e}
.stat-big{font-size:clamp(48px,10vw,96px);font-weight:300;letter-spacing:-.04em;line-height:1;font-variant-numeric:tabular-nums}
@media (max-width:720px){.stats-grid{grid-template-columns:repeat(2,1fr)}}
```
```js
function countUp(el, { duration = 2000, delay = 0 } = {}) {
  const to = parseFloat(el.dataset.count), dec = +(el.dataset.decimals || 0);
  const nf = new Intl.NumberFormat('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec });
  const fmt = (v) => (el.dataset.prefix || '') + nf.format(v) + (el.dataset.suffix || '');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = fmt(to); return; }
  el.textContent = fmt(0);
  setTimeout(() => {
    const t0 = performance.now();
    requestAnimationFrame(function f(now) {
      const t = Math.min(1, (now - t0) / duration);
      el.textContent = fmt(to * (1 - Math.pow(1 - t, 3)));
      if (t < 1) requestAnimationFrame(f);
    });
  }, delay);
}
const countIO = new IntersectionObserver((entries) => entries.forEach((e) => {
  if (!e.isIntersecting) return;
  countIO.unobserve(e.target);
  if (e.target.hasAttribute('data-count-group')) {
    e.target.querySelectorAll('[data-count]').forEach((el, i) => countUp(el, { duration: 1500 + i * 80, delay: 480 + i * 90 }));
  } else countUp(e.target);
}), { threshold: 0.25 });
document.querySelectorAll('[data-count-group], [data-count]:not([data-count-group] [data-count])').forEach((el) => countIO.observe(el));
```
Counter preloader:
```html
<div class="loader" role="status" aria-label="Loading">
  <span class="loader__eyebrow">Portfolio</span>
  <span class="loader__word">Design</span>
  <span class="loader__count">000</span>
  <div class="loader__bar"><i></i></div>
</div>
```
```css
.loader{position:fixed;inset:0;z-index:9999;background:#0a0a0a;color:#f5f5f5;transition:opacity .6s ease,visibility .6s}
.loader.is-done{opacity:0;visibility:hidden}
.loader__eyebrow{position:absolute;top:32px;left:32px;font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:#888}
.loader__word{position:absolute;inset:0;display:grid;place-items:center;opacity:.8;font:italic 400 clamp(2.25rem,6vw,4.5rem)/1 'Instrument Serif',serif}
.loader__count{position:absolute;right:32px;bottom:40px;font:400 clamp(3.75rem,10vw,8rem)/1 'Instrument Serif',serif;font-variant-numeric:tabular-nums}
.loader__bar{position:absolute;left:0;right:0;bottom:0;height:3px;background:rgba(31,31,31,.5)}
.loader__bar i{display:block;height:100%;transform-origin:left;transform:scaleX(0);
  background:linear-gradient(90deg,#89AACC,#4E85BF);box-shadow:0 0 8px rgba(137,170,204,.35)}
```
```js
function swapWord(el, text) {                         // exit up, enter from below
  const out = el.animate([{ opacity: 1, transform: 'translateY(0)' }, { opacity: 0, transform: 'translateY(-20px)' }],
    { duration: 250, easing: 'ease-in', fill: 'forwards' });
  out.onfinish = () => {
    el.textContent = text; out.cancel();
    el.animate([{ opacity: 0, transform: 'translateY(20px)' }, { opacity: 1, transform: 'translateY(0)' }],
      { duration: 350, easing: 'cubic-bezier(.16,1,.3,1)' });
  };
}
function runLoader(onDone, { duration = 2700, words = ['Design', 'Create', 'Inspire'], every = 900 } = {}) {
  const el = document.querySelector('.loader');
  const count = el.querySelector('.loader__count'), bar = el.querySelector('.loader__bar i'), word = el.querySelector('.loader__word');
  const finish = () => { el.classList.add('is-done'); onDone && onDone(); setTimeout(() => el.remove(), 700); };
  let seen = false;
  try { seen = sessionStorage.getItem('intro-seen') === '1'; sessionStorage.setItem('intro-seen', '1'); } catch {}
  if (seen || matchMedia('(prefers-reduced-motion: reduce)').matches) return finish();
  let w = 0;
  const wid = setInterval(() => { w = (w + 1) % words.length; swapWord(word, words[w]); }, every);
  const t0 = performance.now();
  requestAnimationFrame(function f(now) {
    const p = Math.min(1, (now - t0) / duration);
    count.textContent = String(Math.round(p * 100)).padStart(3, '0');
    bar.style.transform = `scaleX(${p})`;
    if (p < 1) requestAnimationFrame(f);
    else { clearInterval(wid); setTimeout(finish, 400); }
  });
}
runLoader(() => document.documentElement.classList.add('hero-go'));   // start the hero entrance from here
```
Gate hero entrances on `.hero-go` (e.g. `.hero-go .in-blur{animation-play-state:running}`) so they play after the loader, not behind it.
