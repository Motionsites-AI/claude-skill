<!-- Solar Fog · Interactive · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_041507_8e9c2d22-8be2-4652-8bbe-1f4556ea463a.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=lumen-roof-hero -->

# Lumen Roof — Morning / Night Fog Hero (exact recreation prompt)

Give me a single-file, full-viewport solar company hero called **Lumen Roof**. A charcoal farmhouse with solar panels fills the screen under a big centred headline. A glass Morning / Night toggle sits at the bottom. Clicking it sinks the whole house about a quarter of the screen into rising fog, swaps the time of day while it is hidden, and floats the house back up in the new light, while the sky, fog colour, nav, headline and button change with it.

Plain HTML, CSS and one vanilla script with raw WebGL2 in one file, with no libraries. The only external resources are the Google Font and the six image URLs below. Reproduce every value, string and timing exactly, and use the complete code at the end as the source of truth.

Six rules define it:
1. **Three layers, one moving.** A blurred sky stays still. The house and its garden sit in one layer that moves on the Y axis only. Fog is a live shader canvas above both, and all text sits above the fog.
2. **Two images make the moving layer.** The full photo is masked so only its lower part shows (the ground and shrubs). The transparent house cutout sits on top of it, so the house's outline stays clean against the blurred sky.
3. **The swap happens at the deepest point.** Fog fully covers the roof at that moment, so the change of house is never seen.
4. **Everything is driven by one clock.** There are no CSS transitions on the scene. One `requestAnimationFrame` function computes sink, fog surge and colours from the time since the click and writes them to CSS variables and shader uniforms.
5. **Colours are mixed, not swapped.** Every text colour is a `color-mix()` on `--k`, where 0 is morning and 1 is night.
6. **No video.** The fog is a generated shader, so it moves forever and never loops.

---

## 1. Page basics

- Title: `Lumen Roof`
- Meta description: `Forget the energy market, weather conditions and seasons. Our Smart Controller guarantees you get no electricity bill for seven years.`
- Font: `https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap`, with preconnects to fonts.googleapis.com and fonts.gstatic.com (crossorigin). The supplied standalone file embeds the latin woff2 as base64 instead.
- `html`, `body` and `.hero` background `#0b1426`. `.hero` is `100svh` tall with `min-height:520px`, `overflow:hidden` and `isolation:isolate`. Body has `overflow:hidden`.
- The unit for all desktop sizes is `--u:min(calc(100vw/1600),calc(100vh/900))`. It becomes `1px` at 820px wide and below.
- The page starts on **Night**: `--k:1`, the night set visible and the Night button pressed.

## 2. Images (use these exact URLs)

All are served through images.higgs.ai as webp and are `object-fit:cover; object-position:50% 62%`.

1. Morning sky, blurred, no house (w=1600, q=80): `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040343_a73684b4-3f71-4613-a843-c8be80fb1211.png&w=1600&q=80`
2. Night sky, blurred, no house (w=1600, q=80): `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040308_f31964ab-ed8e-4ea4-90eb-3226c0859936.png&w=1600&q=80`
3. Morning full photo, used for ground (w=2560, q=85): `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040259_1be34093-835e-4de4-b3a8-f875e6a74591.png&w=2560&q=85`
4. Morning house cutout, transparent (w=2560, q=85): `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040416_e3b05fa4-cc80-4a43-afde-8a0a053933e9.png&w=2560&q=85`
5. Night full photo, used for ground (w=2560, q=85): `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040211_c8fd4865-285e-4c1f-8a37-4bfe0771357b.png&w=2560&q=85`
6. Night house cutout, transparent (w=2560, q=85): `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040415_2ab95096-8c39-449f-b36c-17c2813815a4.png&w=2560&q=85`

## 3. Layer stack, bottom to top

1. `.sky`: morning image with the night image on top. Both have `filter:blur(calc(7*var(--u)))` and `transform:scale(1.05)`. The night image has `opacity:var(--k)`, so the sky blends in step with the text.
2. `.home`: full-screen layer with `transform:translate3d(0,var(--sink,0px),0)` and `will-change:transform`. It holds `#setM` and `#setN`, of which only `.is-on` is visible (`visibility`). Each set is a `.ground` layer with the full photo under `mask-image:linear-gradient(transparent 54%,#000 64%)`, then the cutout at full size.
3. `.tilt`: `backdrop-filter:blur(calc(9*var(--u)))` masked with `linear-gradient(transparent 70%,#000 92%)`, which softens the foreground like a tilt-shift lens.
4. `#fog`: the WebGL2 canvas, `pointer-events:none`.
5. `.ui`: all text and buttons, `z-index:2`.

## 4. Content

- Logo: 12-ray sun, each ray `M18.3 3.5h3.4l.9 8.4h-5.2Z` rotated in 30° steps about (20,20) in a 40 viewBox, 38u wide, filled with `color-mix(in srgb,#6d8f2a calc((1 - var(--k))*100%),#d8ee8e)`. Wordmark `Lumen Roof`, 25u, weight 500, letter spacing -.025em, gap 9u.
- Nav, centred: `How It Works`, `Our Cases`, `About Us`, `Careers`, `Resources`, 16.5u, weight 500, gap 42u.
- Right side: `Customers`, then the pill button `Get an Instant Quote`, 46u tall, 26u side padding, radius 99px. Black `#0d1117` with white text in the morning, white with `#0d1117` text at night, mixed on `--k`. It lifts 1px on hover.
- Bar padding: 22u top, 38u sides. Logo and right side are `flex:1 1 0` so the links stay truly centred.
- Headline, 58u below the bar, 64u, line height 1.09, weight 500, letter spacing -.022em: `$0 Electricity Bills` / `for the next 7 Years`.
- Headline colour `--ink` mixes `#14202f` to `#fff`. `for the next` uses `--k2` and a muted `#7c8794` tone in the morning, so it is two-tone by day and all white by night, exactly like the reference's split headline.
- Toggle, 524u × 86u, radius 16u, 2u padding, `rgba(120,132,140,.34)` with a `rgba(255,255,255,.2)` border and `backdrop-filter:blur(14u)`. Two equal buttons: `Morning` and `Night`, each 23u weight 500 with `$0 for Electricity` under it at 15u, 72% opacity.
- The active button shows a `:before` with `linear-gradient(160deg,#f7f8dc,#e2ee9f 90%)` and `box-shadow:inset 0 0 18u rgba(255,255,255,.65)`. Its opacity is `--on`, which is `1 - k` on Morning and `k` on Night, so the two buttons crossfade rather than slide. Label colour mixes `#1c2316` and `#fff` on `--on`.
- Caption, 22u below the toggle, 16.4u, line height 1.3, colour `--soft`: `Forget the energy market, weather conditions and seasons. Our Smart` line break `Controller guarantees you get no electricity bill for seven years.` Dock has 40u bottom padding.

## 5. The switch

Constants: `SINK=240`, `RISE=820`, `DEPTH=.27`. With `d` as milliseconds since the click:

- **Sink:** for `d<SINK`, `y = x*x*(3-2*x)*DEPTH` with `x=d/SINK`.
- **Swap:** the first frame with `d>=SINK` swaps the visible house set.
- **Rise:** `y = Math.pow(1-x,3.4)*DEPTH` with `x=(d-SINK)/RISE`.
- `--sink` is `y*innerHeight` in px.
- **Fog surge:** `s = smooth(0,SINK*.92,d) * (1-smooth(SINK+70,SINK+RISE*.92,d))`.
- **UI dip:** `dip = smooth(30,190,d) * (1-smooth(330,720,d))`. Nav links, `Customers` and the headline's first line and `7 Years` fade by 80–82%, and the button by 62%. `for the next` stays solid, as it does in the reference.
- **Colours:** `k` moves from its start to the target on `smooth(120,520,d)`. `k2` does the same on `smooth(340,760,d)`.
- At `d>=SINK+RISE` the animation ends. A click during the animation is queued and runs next, unless it matches the current target.
- With `prefers-reduced-motion` the state changes instantly.
- Buttons are real `<button>` elements with `aria-pressed`, inside `role="group" aria-label="Time of day"`, with a 2px white focus ring.

## 6. Fog shader

A fragment shader on one fullscreen triangle, rendered at no more than 960px wide (upscaled by CSS), with `premultipliedAlpha:true`. Uniforms: `R` size, `T` seconds, `S` surge, `K` night amount.

- Five-octave value-noise `fbm`, rotated first by `mat2(.8,.6,-.6,.8)` and offset by 5.3 so no grid shows, then by `mat2(1.6,1.2,-1.2,1.6)` for each octave.
- Time is `T*.05`. Domain warp `w`, then density `d`, then a slower `e`.
- Resting fog is three parts added together: `low` along the bottom (`smoothstep(.70,1.04,y+(d-.5)*.34)`), `side` on the left and right edges at 20% strength, and `wisps` in mid-air at 18%.
- Surge: fog front at `1.02-S*.68`, with `rise = smoothstep(front-.02,front+.26,y+(d-.5)*.5)`, plus overall `haze = S*(.3+.46*d)`.
- Alpha is the largest of resting fog, `rise*.97` and `haze`.
- Colour is mixed by density: morning `(.79,.78,.71)` to `(.97,.93,.84)`, night `(.15,.19,.29)` to `(.40,.45,.57)`, blended by `K`.
- At night a warm amber `(.86,.55,.27)` glow spot at (.72,.74) tints the fog by the porch, at 42%, and it disappears during a surge.

## 7. Phones (820px and below)

`--u:1px`, nav links and `Customers` hidden, bar padding 16px, logo 21px, button 40px tall. Headline `clamp(34px,10.4vw,56px)`. Images shift to `object-position:72% 62%` so the panels and porch stay in frame. Toggle is full width up to 440px and 74px tall, labels 19px and 13px. Caption is 14px with its line break removed.

---

## Complete code

This is the finished page. Build exactly this.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lumen Roof</title>
<meta name="description" content="Forget the energy market, weather conditions and seasons. Our Smart Controller guarantees you get no electricity bill for seven years.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --u:min(calc(100vw/1600),calc(100vh/900));
  --k:1;--k2:1;--dip:0;
  --ink:color-mix(in srgb,#14202f calc((1 - var(--k))*100%),#fff);
  --nav:color-mix(in srgb,#1b2736 calc((1 - var(--k))*100%),#eef1f6);
  --soft:color-mix(in srgb,#1b2736 calc((1 - var(--k))*100%),#dfe5ee);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#0b1426}
body{font-family:"Instrument Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow:hidden}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
.hero{position:relative;height:100svh;min-height:520px;overflow:hidden;isolation:isolate;background:#0b1426}
.layer,.layer img{position:absolute;inset:0;width:100%;height:100%}
.layer img{display:block;object-fit:cover;object-position:50% 62%}
.sky img{filter:blur(calc(7*var(--u)));transform:scale(1.05)}
#skyN{opacity:var(--k)}
.home{will-change:transform;transform:translate3d(0,var(--sink,0px),0)}
.home .set{position:absolute;inset:0;visibility:hidden}
.home .set.is-on{visibility:visible}
.ground{-webkit-mask-image:linear-gradient(transparent 54%,#000 64%);mask-image:linear-gradient(transparent 54%,#000 64%)}
.tilt{position:absolute;inset:0;pointer-events:none;-webkit-backdrop-filter:blur(calc(9*var(--u)));backdrop-filter:blur(calc(9*var(--u)));-webkit-mask-image:linear-gradient(transparent 70%,#000 92%);mask-image:linear-gradient(transparent 70%,#000 92%)}
#fog{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.ui{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;align-items:center;pointer-events:none}
.ui a,.ui button{pointer-events:auto}
.bar{width:100%;display:flex;align-items:center;padding:calc(22*var(--u)) calc(38*var(--u)) 0;color:var(--nav)}
.logo{display:flex;align-items:center;gap:calc(9*var(--u));font-size:calc(25*var(--u));font-weight:500;letter-spacing:-.025em;color:var(--ink);flex:1 1 0}
.logo svg{width:calc(38*var(--u));height:calc(38*var(--u));flex:none}
.links{display:flex;gap:calc(42*var(--u));list-style:none;font-size:calc(16.5*var(--u));font-weight:500;opacity:calc(1 - var(--dip)*.82)}
.side{flex:1 1 0;display:flex;align-items:center;justify-content:flex-end;gap:calc(40*var(--u));font-size:calc(16.5*var(--u));font-weight:500}
.side>a:first-child{opacity:calc(1 - var(--dip)*.82)}
.cta{display:inline-flex;align-items:center;height:calc(46*var(--u));padding:0 calc(26*var(--u));border-radius:99px;
  background:color-mix(in srgb,#0d1117 calc((1 - var(--k))*100%),#fff);color:color-mix(in srgb,#fff calc((1 - var(--k))*100%),#0d1117);opacity:calc(1 - var(--dip)*.62);transition:transform .25s}
.cta:hover{transform:translateY(-1px)}
h1{margin-top:calc(58*var(--u));text-align:center;font-size:calc(64*var(--u));line-height:1.09;font-weight:500;letter-spacing:-.022em;color:var(--ink)}
h1 span{display:block}
h1 .l1,h1 .y{opacity:calc(1 - var(--dip)*.8)}
h1 i{font-style:normal;color:color-mix(in srgb,#14202f calc((1 - var(--k2))*42%),color-mix(in srgb,#fff calc(var(--k2)*100%),#7c8794))}
h1 .y{display:inline}
.dock{margin-top:auto;padding-bottom:calc(40*var(--u));display:flex;flex-direction:column;align-items:center}
.toggle{position:relative;display:grid;grid-template-columns:1fr 1fr;width:calc(524*var(--u));height:calc(86*var(--u));padding:calc(2*var(--u));border-radius:calc(16*var(--u));overflow:hidden;
  background:rgba(120,132,140,.34);border:1px solid rgba(255,255,255,.2);-webkit-backdrop-filter:blur(calc(14*var(--u)));backdrop-filter:blur(calc(14*var(--u)))}
.toggle button{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(3*var(--u));border-radius:calc(13*var(--u));color:#fff;overflow:hidden}
.toggle button:before{content:"";position:absolute;inset:0;border-radius:inherit;background:linear-gradient(160deg,#f7f8dc,#e2ee9f 90%);box-shadow:inset 0 0 calc(18*var(--u)) rgba(255,255,255,.65);opacity:var(--on)}
.toggle b,.toggle small{position:relative;color:color-mix(in srgb,#1c2316 calc(var(--on)*100%),#fff)}
.toggle b{font-size:calc(23*var(--u));font-weight:500;letter-spacing:-.012em}
.toggle small{font-size:calc(15*var(--u));opacity:.72}
.toggle button:focus-visible{outline:2px solid #fff;outline-offset:-4px}
#bm{--on:calc(1 - var(--k))}#bn{--on:var(--k)}
.cap{margin-top:calc(22*var(--u));text-align:center;font-size:calc(16.4*var(--u));line-height:1.3;color:var(--soft)}
@media (max-width:820px){
  :root{--u:1px}
  .bar{padding:16px 16px 0}
  .logo{font-size:21px}.logo svg{width:32px;height:32px}
  .links,.side>a:first-child{display:none}
  .cta{height:40px;padding:0 16px;font-size:14px}
  h1{margin-top:34px;padding:0 16px;font-size:clamp(34px,10.4vw,56px)}
  .layer img,.home .cut{object-position:72% 62%!important}
  .dock{width:100%;padding:0 16px 24px}
  .toggle{width:100%;max-width:440px;height:74px}
  .toggle b{font-size:19px}.toggle small{font-size:13px}
  .cap{font-size:14px;max-width:360px}
  .cap br{display:none}
}
</style>
</head>
<body>
<main class="hero">
  <div class="layer sky">
    <img id="skyM" alt="" src="https://images.higgs.ai/?default=1&amp;output=webp&amp;url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040343_a73684b4-3f71-4613-a843-c8be80fb1211.png&amp;w=1600&amp;q=80">
    <img id="skyN" alt="" src="https://images.higgs.ai/?default=1&amp;output=webp&amp;url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040308_f31964ab-ed8e-4ea4-90eb-3226c0859936.png&amp;w=1600&amp;q=80">
  </div>
  <div class="layer home">
    <div class="set" id="setM">
      <div class="layer ground"><img alt="" src="https://images.higgs.ai/?default=1&amp;output=webp&amp;url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040259_1be34093-835e-4de4-b3a8-f875e6a74591.png&amp;w=2560&amp;q=85"></div>
      <img class="cut" alt="A charcoal farmhouse with solar panels in soft morning light" src="https://images.higgs.ai/?default=1&amp;output=webp&amp;url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040416_e3b05fa4-cc80-4a43-afde-8a0a053933e9.png&amp;w=2560&amp;q=85" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 62%">
    </div>
    <div class="set is-on" id="setN">
      <div class="layer ground"><img alt="" src="https://images.higgs.ai/?default=1&amp;output=webp&amp;url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040211_c8fd4865-285e-4c1f-8a37-4bfe0771357b.png&amp;w=2560&amp;q=85"></div>
      <img class="cut" alt="The same farmhouse at dusk with warm amber windows" src="https://images.higgs.ai/?default=1&amp;output=webp&amp;url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_040415_2ab95096-8c39-449f-b36c-17c2813815a4.png&amp;w=2560&amp;q=85" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 62%">
    </div>
  </div>
  <div class="tilt"></div>
  <canvas id="fog" aria-hidden="true"></canvas>
  <div class="ui">
    <header class="bar">
      <a class="logo" href="#" aria-label="Lumen Roof">
        <svg viewBox="0 0 40 40" aria-hidden="true"><g fill="color-mix(in srgb,#6d8f2a calc((1 - var(--k))*100%),#d8ee8e)"><circle cx="20" cy="20" r="0"/><path id="ray" d="M18.3 3.5h3.4l.9 8.4h-5.2Z"/><use href="#ray" transform="rotate(30 20 20)"/><use href="#ray" transform="rotate(60 20 20)"/><use href="#ray" transform="rotate(90 20 20)"/><use href="#ray" transform="rotate(120 20 20)"/><use href="#ray" transform="rotate(150 20 20)"/><use href="#ray" transform="rotate(180 20 20)"/><use href="#ray" transform="rotate(210 20 20)"/><use href="#ray" transform="rotate(240 20 20)"/><use href="#ray" transform="rotate(270 20 20)"/><use href="#ray" transform="rotate(300 20 20)"/><use href="#ray" transform="rotate(330 20 20)"/></g></svg>
        Lumen Roof
      </a>
      <ul class="links">
        <li><a href="#">How It Works</a></li><li><a href="#">Our Cases</a></li><li><a href="#">About Us</a></li><li><a href="#">Careers</a></li><li><a href="#">Resources</a></li>
      </ul>
      <div class="side"><a href="#">Customers</a><a class="cta" href="#">Get an Instant Quote</a></div>
    </header>
    <h1><span class="l1">$0 Electricity Bills</span><span><i>for the next</i> <span class="y">7 Years</span></span></h1>
    <div class="dock">
      <div class="toggle" role="group" aria-label="Time of day">
        <button id="bm" aria-pressed="false"><b>Morning</b><small>$0 for Electricity</small></button>
        <button id="bn" aria-pressed="true"><b>Night</b><small>$0 for Electricity</small></button>
      </div>
      <p class="cap">Forget the energy market, weather conditions and seasons. Our Smart<br>Controller guarantees you get no electricity bill for seven years.</p>
    </div>
  </div>
</main>
<script>
const root=document.documentElement.style,$=id=>document.getElementById(id);
const calm=matchMedia('(prefers-reduced-motion:reduce)').matches;
const SINK=240,RISE=820,DEPTH=.27;
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const smooth=(a,b,x)=>{x=clamp((x-a)/(b-a));return x*x*(3-2*x)};
let night=1,target=1,from=1,start=-1e9,queued=null,swapped=true,k=1,surge=0;

const cv=$('fog'),gl=cv.getContext('webgl2',{alpha:true,premultipliedAlpha:true,antialias:false});
let U={};
if(gl){
  const vs=`#version 300 es
  void main(){vec2 p=vec2((gl_VertexID<<1)&2,gl_VertexID&2);gl_Position=vec4(p*2.-1.,0,1);}`;
  const fs=`#version 300 es
  precision highp float;
  uniform vec2 R;uniform float T,S,K;out vec4 O;
  float h(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}
  float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);
    return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
  float fbm(vec2 p){float a=.5,s=0.;mat2 m=mat2(1.6,1.2,-1.2,1.6);p=mat2(.8,.6,-.6,.8)*p+5.3;for(int i=0;i<5;i++){s+=a*n(p);p=m*p;a*=.5;}return s;}
  void main(){
    vec2 uv=gl_FragCoord.xy/R;uv.y=1.-uv.y;
    float asp=R.x/R.y;vec2 p=vec2(uv.x*asp,uv.y);
    float t=T*.05;
    vec2 w=vec2(fbm(p*1.3+vec2(t,-t*.6)),fbm(p*1.3+vec2(-t*.8,t)+7.));
    float d=fbm(p*1.9+w*1.7+vec2(t*1.6,-t*1.1+S*.5));
    float e=fbm(p*.9-w+vec2(-t,t*.5)+3.);
    float low=smooth2(.70,1.04,uv.y+(d-.5)*.34);
    float side=smooth2(.2,.0,uv.x+(e-.5)*.28)+smooth2(.8,1.,uv.x+(e-.5)*.28);
    side*=smooth2(.25,.6,uv.y)*.2;
    float wisps=smooth2(.5,.78,d)*smooth2(.22,.5,uv.y)*smooth2(.86,.6,uv.y)*.18;
    float rest=clamp(low+side+wisps,0.,1.);
    float front=1.02-S*.68;
    float rise=smooth2(front-.02,front+.26,uv.y+(d-.5)*.5);
    float haze=S*(.3+.46*d);
    float a=clamp(max(rest,max(rise*.97,haze)),0.,1.);
    vec3 dayA=vec3(.97,.93,.84),dayB=vec3(.79,.78,.71);
    vec3 nitA=vec3(.40,.45,.57),nitB=vec3(.15,.19,.29);
    vec3 c=mix(mix(dayB,dayA,d*1.15),mix(nitB,nitA,d*1.1),K);
    float porch=exp(-dot((uv-vec2(.72,.74))*vec2(1.7,2.6),(uv-vec2(.72,.74))*vec2(1.7,2.6))*3.2);
    c=mix(c,vec3(.86,.55,.27),K*porch*.42*(1.-S));
    O=vec4(c*a,a);
  }`.replace(/smooth2/g,'smoothstep');
  const sh=(t,s)=>{const o=gl.createShader(t);gl.shaderSource(o,s);gl.compileShader(o);
    if(!gl.getShaderParameter(o,gl.COMPILE_STATUS))console.error(gl.getShaderInfoLog(o));return o};
  const pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,vs));gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,fs));
  gl.linkProgram(pr);gl.useProgram(pr);
  for(const u of['R','T','S','K'])U[u]=gl.getUniformLocation(pr,u);
}
function size(){
  if(!gl)return;
  const w=Math.round(Math.min(innerWidth,960)),h=Math.round(w*innerHeight/innerWidth);
  if(cv.width!==w||cv.height!==h){cv.width=w;cv.height=h;gl.viewport(0,0,w,h)}
}
addEventListener('resize',size);size();

function show(n){
  $('setM').classList.toggle('is-on',!n);$('setN').classList.toggle('is-on',!!n);
}
function pick(n){
  if(n===target&&queued===null)return;
  $('bm').setAttribute('aria-pressed',!n);$('bn').setAttribute('aria-pressed',!!n);
  if(calm){target=night=n;k=n;show(n);return}
  if(animating)queued=n;else begin(n,clock);
}
let animating=false,clock=0;
function begin(n,now){target=n;from=k;start=now;swapped=false;animating=true}
$('bm').onclick=()=>pick(0);$('bn').onclick=()=>pick(1);

function frame(now){
  clock=now;
  const d=now-start;let y=0,s=0,dip=0,k2=k;
  if(animating){
    if(d<SINK){const x=d/SINK;y=x*x*(3-2*x)*DEPTH}
    else{
      if(!swapped){swapped=true;night=target;show(target)}
      const x=clamp((d-SINK)/RISE);y=Math.pow(1-x,3.4)*DEPTH;
    }
    s=smooth(0,SINK*.92,d)*(1-smooth(SINK+70,SINK+RISE*.92,d));
    dip=smooth(30,190,d)*(1-smooth(330,720,d));
    k=from+(target-from)*smooth(120,520,d);
    k2=from+(target-from)*smooth(340,760,d);
    if(d>=SINK+RISE){animating=false;k=k2=target;y=s=dip=0;if(queued!==null&&queued!==target){const q=queued;queued=null;begin(q,now)}else queued=null}
  }
  root.setProperty('--sink',(y*innerHeight).toFixed(1)+'px');
  root.setProperty('--k',k.toFixed(3));root.setProperty('--k2',k2.toFixed(3));root.setProperty('--dip',dip.toFixed(3));
  if(gl){gl.uniform2f(U.R,cv.width,cv.height);gl.uniform1f(U.T,now/1000);gl.uniform1f(U.S,s);gl.uniform1f(U.K,k);gl.drawArrays(gl.TRIANGLES,0,3)}
}
function loop(t){frame(t);requestAnimationFrame(loop)}
requestAnimationFrame(loop);
</script>
</body>
</html>
```
