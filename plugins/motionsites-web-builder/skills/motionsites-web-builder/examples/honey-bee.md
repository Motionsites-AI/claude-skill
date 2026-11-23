<!-- Honey Bee · Creative · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261017_154537_1384fa6d-282d-46e2-8748-a70be1cf681a.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=honey-bee -->

Build a single, standalone index.html landing page called "Melli — Master 3D Artistry". Everything (HTML, CSS, JS) lives in ONE file. No build step, no frameworks. Use three.js 0.160.0 via an import map. Reproduce EXACTLY the structure, copy, assets, CSS values, animations and the scroll-driven 3D honeybee described below.

=====================================================================
1. HEAD
=====================================================================
<meta charset="utf-8">, <meta name="viewport" content="width=device-width, initial-scale=1">
<title>Melli — Master 3D Artistry</title>
Fonts: preconnect to https://fonts.googleapis.com and https://fonts.gstatic.com (crossorigin), then load:
https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap
Whole site uses font-family: "Poppins", system-ui, sans-serif.

=====================================================================
2. ASSETS (use these exact CloudFront URLs)
=====================================================================
HERO_BG (soft lavender bokeh, CSS background):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261016_130303_301c35dd-e2d1-4b40-a396-2b53f884d787.png
COSMOS (transparent PNG, purple dewy cosmos, hero bottom-left):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132919_c994332b-7f9d-43b5-933d-1e94faa91dd4.png
HANGING COSMOS (transparent PNG, upside-down flower, section 01 top-left):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132924_764b726d-d37a-44cc-8eba-662d823d9a4c.png
S2_BG (deep violet macro bokeh, CSS background):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132814_c3d2b090-c27d-49d1-8107-66d0cfa216c2.png
IRIS PETAL (transparent PNG, section 02 bottom-right):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132926_a7892ae5-8052-4e4b-96a8-ccbdcaaaa5ad.png
PASSION FLOWER (transparent PNG, section 03 left):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132921_d71538ea-5066-4372-963a-2f2d6468374f.png
BEE_GLB (3D bumblebee body, NO wings, head points along the model's +Z axis):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132918_e8364d8f-7df2-4788-a725-dec28ec19af8.glb
WING_TEX (single veined iridescent bee wing photographed on pure BLACK, 16:9, wing root at left edge, pointing right):
https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261017_132814_3a56ac14-47d8-4e49-a163-94234dea5639.png
All flower <img> tags use alt="".

=====================================================================
3. CSS (exact values)
=====================================================================
:root {
  --ink: #0d0b1a; --muted: #4a4568; --lilac: #e7e3fb; --num: #cfc6f6;
  --num-dark: rgba(214,203,255,.55); --violet: #5b3bd1; --pad: clamp(18px, 3.2vw, 46px);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: auto; }
body { font-family: Poppins; color: var(--ink); background: var(--lilac); overflow-x: hidden; -webkit-font-smoothing: antialiased; }
a { color: inherit; text-decoration: none; }

NAV (fixed):
.nav { position: fixed; z-index: 30; top:0; left:0; right:0; display:flex; align-items:center; padding: 18px var(--pad) 0; pointer-events:none; }  .nav > * { pointer-events:auto; }
.logo { 40x40, display:grid; place-items:center; margin-right: clamp(28px,5vw,66px); }  .logo svg { 38x38; transition: transform .6s cubic-bezier(.2,.8,.2,1); }  .logo:hover svg { rotate(90deg) }
.nav__links { display:flex; gap: clamp(22px,4.5vw,58px); font-size:15.5px; font-weight:400; }
.nav__links a { position:relative } with ::after underline: left:0; right:0; bottom:-3px; height:1.5px; background currentColor; transform scaleX(0) origin left; transition transform .35s ease; on hover scaleX(1).
.nav__cta { margin-left:auto; font-weight:600; font-size:16px; padding-right: clamp(0px,4vw,70px); }
.nav, .badge { transition: color .5s ease; }   body.on-dark .nav, body.on-dark .badge { color:#fff; }

BADGE (fixed bottom-right): position fixed; z-index 30; right var(--pad); bottom 22px; flex; align-items center; gap 8px; font-size 12.5px; font-weight 500; color #2b2550.  .badge b { font-weight:700; color: var(--violet) }  body.on-dark .badge b { color:#d9ccff }  .badge svg { 20x20 }

BEE CANVAS: #bee { position:fixed; inset:0; z-index:20; width:100%; height:100%; pointer-events:none; opacity:0; transition: opacity 1.2s ease; }  #bee.ready { opacity:1 }

SECTIONS: section { position:relative; min-height:100vh; height:100vh; overflow:hidden; }
.flower { position:absolute; pointer-events:none; user-select:none; will-change:transform; }

HERO:
.hero { background: #e4e0fa url(HERO_BG) center/cover no-repeat; overflow: visible; z-index: 3; }
.hero h1 { position:absolute; left:0; right:0; top:15.5vh; text-align:center; font-weight:800; font-size: clamp(42px, 6.25vw, 112px); line-height:1.04; letter-spacing:-.035em; color:var(--ink); text-shadow: 0 0 40px rgba(255,255,255,.35); will-change:transform; z-index:2; }
.hero h1 .line { display:block; overflow:hidden; padding-bottom:.06em; }
.hero h1 .line span { display:inline-block; transform: translateY(110%); }
.loaded .hero h1 .line span { animation: rise 1.1s cubic-bezier(.2,.8,.15,1) forwards; }
.hero h1 .line:nth-child(2) span { animation-delay: .12s; }
@keyframes rise { to { transform: translateY(0); } }
.hero__side { position:absolute; right: clamp(24px,6.5vw,120px); top:59vh; width: min(260px,80vw); z-index:2; opacity:0; }
.loaded .hero__side { animation: fade 1s .7s ease forwards; }
.hero__side p { font-size: clamp(15px,1.45vw,20px); line-height:1.32; color:var(--muted); font-weight:400; }
@keyframes fade { from { opacity:0; transform:translateY(16px) } to { opacity:1; transform:none } }
.join { display:inline-flex; align-items:center; gap:14px; margin-top:40px; font-weight:600; font-size: clamp(15px,1.4vw,19px); }
.join i { width:25px; height:32px; border:1.8px solid currentColor; border-radius:10px; display:grid; place-items:center; transition: transform .35s ease, background .35s; }  .join i svg { 9x9 }  .join:hover i { transform: translateX(4px) }
.hero .flower--cosmos { width: clamp(420px,64vw,1100px); left:-14vw; bottom:-24vw; transform-origin:60% 40%; filter: drop-shadow(0 30px 40px rgba(80,50,160,.18)); z-index:1; }

SHARED TYPE:
.num { font-weight:600; line-height:.8; letter-spacing:-.06em; font-size: clamp(110px,15vw,250px); color: var(--num); }
.title { font-weight:700; font-size: clamp(30px,3.4vw,56px); line-height:1.12; letter-spacing:-.02em; }
.copy { margin-top:22px; font-size: clamp(13.5px,1.05vw,16px); line-height:1.6; color:var(--muted); max-width:420px; }
.reveal { opacity:0; transform:translateY(40px); transition: opacity 1s ease, transform 1.1s cubic-bezier(.2,.8,.15,1); }
.in .reveal { opacity:1; transform:none; }  .in .reveal.d1 { transition-delay:.1s }  .in .reveal.d2 { transition-delay:.22s }  .in .reveal.d3 { transition-delay:.34s }

SECTION 01:
.s1 { background: linear-gradient(180deg, #e4e0fa 0%, #ece9fc 100%); z-index:2; }
.s1 .flower--hang { width: clamp(380px,46vw,820px); left:-9vw; top:-14vw; transform-origin:50% 0%; }
.s1 .num { position:absolute; left:6vw; top:50vh; }
.s1 .text { position:absolute; left:50vw; top:41vh; width: min(520px,44vw); }

SECTION 02 (dark):
.s2 { background: #3a1f8c url(S2_BG) center/cover no-repeat; color:#fff; z-index:3; }
.s2::before { content:""; position:absolute; inset:0; background: linear-gradient(90deg, rgba(25,10,70,.45) 0%, rgba(25,10,70,0) 55%); }
.s2 .num { color: var(--num-dark); position:relative; }
.s2 .text { position:absolute; left:6vw; top:22vh; width: min(500px,46vw); }
.s2 .title { margin-top:22px; }  .s2 .copy { color: rgba(240,234,255,.82); }
.s2 .flower--iris { width: clamp(380px,46vw,820px); right:-8vw; bottom:-20vw; transform-origin:30% 30%; filter: drop-shadow(0 40px 60px rgba(20,0,60,.45)); z-index:2; }

SECTION 03:
.s3 { background: linear-gradient(180deg, #ece9fc 0%, #e7e3fb 100%); z-index:1; }
.s3 .flower--passion { width: clamp(360px,42vw,760px); left:-10vw; top:6vh; transform-origin:40% 50%; }
.s3 .text { position:absolute; left:54vw; top:26vh; width: min(500px,40vw); }  .s3 .title { margin-top:24px; }

FOOTER:
.foot { background:#e7e3fb; height:100vh; z-index:1; }
.foot .brand { position:absolute; left:var(--pad); bottom:80px; }  .foot .brand strong { display:block; font-size: clamp(30px,3vw,46px); font-weight:700; letter-spacing:-.02em; }  .foot .brand span { font-size:14px; color:var(--muted); }
.foot .cols { position:absolute; right: calc(var(--pad) + 120px); bottom:80px; display:flex; gap:64px; font-size:14.5px; font-weight:500; }  .foot .cols a { display:block; line-height:1.9; }  .foot .cols a:hover { color: var(--violet); }
.foot .cta { position:absolute; left:50%; top:18vh; transform:translateX(-50%); text-align:center; }  .foot .cta .title { font-size: clamp(30px,3.6vw,60px); }

LOADER:
.loader { position:fixed; inset:0; z-index:50; background:var(--lilac); display:grid; place-items:center; transition: opacity .8s ease, visibility .8s; }  .loader.done { opacity:0; visibility:hidden; }
.loader svg { 46x46; animation: spin 1.6s linear infinite; }  @keyframes spin { to { transform: rotate(360deg) } }

MOBILE (@media (max-width: 760px)):
.nav__links { display:none }
.hero h1 { top:14vh }
.hero__side { top:auto; bottom:14vh; right:18px; width:62vw }
.hero .flower--cosmos { width:110vw; left:-38vw; bottom:-55vw }
.s1 .num { top:16vh; left:auto; right:6vw }
.s1 .text, .s3 .text { left:18px; right:18px; width:auto; top:auto; bottom:10vh }
.s2 .text { left:18px; right:18px; width:auto; top:14vh }
.s3 .flower--passion { width:90vw }
.foot .cols { right:18px; bottom:150px; gap:30px }
.foot .brand { bottom:150px }

=====================================================================
4. HTML BODY (exact order and copy)
=====================================================================
4-point star SVG path (used for logo and loader), viewBox "0 0 40 40":
M20 0c1.2 11.5 8.5 18.8 20 20-11.5 1.2-18.8 8.5-20 20-1.2-11.5-8.5-18.8-20-20C11.5 18.8 18.8 11.5 20 0z
Chevron SVG for .join buttons: viewBox "0 0 10 10", fill none, stroke currentColor, stroke-width 1.6, path "M3 1l4 4-4 4".

<div class="loader" id="loader"> star SVG with fill #0d0b1a </div>

<nav class="nav">
  <a class="logo" href="#top" aria-label="Home"> star SVG fill currentColor </a>
  <div class="nav__links"><a href="#about">Inside the class</a><a href="#contact">Ping us</a></div>
  <a class="nav__cta" href="#access">Buzz in!</a>
</nav>

<canvas id="bee"></canvas>

<main>
 <section class="hero" id="top" data-theme="light">
   <h1 data-speed="0.55"><span class="line"><span>Imagine your next site</span></span><span class="line"><span>built just like this</span></span></h1>
   <img class="flower flower--cosmos" data-speed="-0.25" data-rot="8" src="COSMOS">
   <div class="hero__side">
     <p>Master 3D animation in just three days with our newest program</p>
     <a class="join" href="#access"><i>chevron</i>Buzz in!</a>
   </div>
 </section>

 <section class="s1" id="about" data-theme="light">
   <img class="flower flower--hang" data-speed="0.35" data-rot="-6" src="HANGING COSMOS">
   <div class="num reveal">01</div>
   <div class="text">
     <h2 class="title reveal d1">Explore this<br>Universe of<br>3D Motion</h2>
     <p class="copy reveal d2">Every lesson is crafted by studio veterans to equip you with the newest methods and software in 3D animation. Whether you're just starting or already a pro, our program will sharpen your skills fast.</p>
   </div>
 </section>

 <section class="s2" id="access" data-theme="dark">
   <div class="text">
     <div class="num reveal">02</div>
     <h2 class="title reveal d1">Claim Early<br>Invite</h2>
     <p class="copy reveal d2">Get early entry to our all-new 3D animation lessons! Add your name to the waitlist and you'll be first to enroll with VIP pricing.</p>
   </div>
   <img class="flower flower--iris" data-speed="-0.3" data-rot="10" src="IRIS PETAL">
 </section>

 <section class="s3" data-theme="light">
   <img class="flower flower--passion" data-speed="-0.2" data-rot="-10" src="PASSION FLOWER">
   <div class="text">
     <div class="num reveal">03</div>
     <h2 class="title reveal d1">Study and<br>Build with Us!</h2>
     <p class="copy reveal d2">Become part of a lively hive of artists. Ship real work, get notes from expert mentors and see your concepts come alive in vivid 3D depth.</p>
   </div>
 </section>

 <section class="foot" id="contact" data-theme="light">
   <div class="cta"><h2 class="title reveal">Prepared to fly high?</h2><a class="join reveal d1" href="#access"><i>chevron</i>Buzz in!</a></div>
   <div class="brand reveal"><strong>Melli_Motion</strong><span>A 3D motion academy</span></div>
   <div class="cols reveal d1">
     <div><a href="#">YouTube</a><a href="#">LinkedIn</a><a href="#">Instagram</a></div>
     <div><a href="#">Facebook</a><a href="#">Dribbble</a></div>
   </div>
 </section>
</main>

<div class="badge">
  <svg viewBox="0 0 20 20" fill="currentColor"> four circles r=4.2 at (6,6), (14,6, opacity .75), (6,14, opacity .75), (14,14) </svg>
  Made by <b>Melli</b>
</div>

=====================================================================
5. JAVASCRIPT
=====================================================================
Import map:
{ "imports": { "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
               "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/" } }
<script type="module"> imports THREE, GLTFLoader (three/addons/loaders/GLTFLoader.js), RoomEnvironment (three/addons/environments/RoomEnvironment.js).

5a. DOM scroll effects
- IntersectionObserver (threshold .3) on every main > section: add class "in" when it intersects (never removed). This triggers the .reveal fade-ups.
- On scroll (passive) and once at start, for every [data-speed] element: sec = closest section; p = -sec.getBoundingClientRect().top / innerHeight;
  el.style.transform = `translate3d(0, p*speed*innerHeightpx,0)rotate({p * rot}deg)` (rot = data-rot or 0). This gives the flowers/headline parallax and slow rotation.
- Nav theme: find the section whose rect spans y = innerHeight*0.06; toggle body.on-dark if its data-theme is "dark" (makes nav + badge white over section 02).

5b. Loader
- setTimeout 2500ms: add "done" to #loader and "loaded" to body (fallback so the page shows while the 19MB GLB streams).
- On GLB load success or error: same (add "done" + "loaded"); on success also add "ready" to canvas.

5c. three.js scene
- WebGLRenderer({ canvas:#bee, antialias:true, alpha:true }); pixelRatio min(devicePixelRatio,2); outputColorSpace SRGB; toneMapping ACESFilmic; exposure 1.15.
- scene.environment = PMREMGenerator.fromScene(new RoomEnvironment(), .04).texture.
- PerspectiveCamera(fov 30, near .1, far 100) at (0,0,10). Resize: renderer.setSize(innerWidth, innerHeight, false), update aspect.
- Lights: HemisphereLight(0xf2eeff, 0x7a62c9, 1.3); DirectionalLight(0xfff1d6, 2.6) at (3,5,6); DirectionalLight(0xc8b8ff, 2.2) at (-5,2,-4).
- Hierarchy: scene > flight (Group: world position, scale, yaw) > beeRoot (Group: roll/pitch) > holder (model) + wing groups. beeRoot frame: +X = head, +Y = up, +Z = bee's right side.

5d. Model load and normalisation
- Load BEE_GLB. For each mesh: frustumCulled=false, material.envMapIntensity=.7.
- holder = new Group; holder.add(model); model.rotation.set(0, Math.PI/2, 0) (turns head from +Z to +X).
- Box3 of holder → scale model by 1/max(size.x,size.y,size.z); recompute box; model.position.sub(box center); recompute box.
- Wing hinge anchor: x = box.min.x + (box.max.x-box.min.x)*0.66, y = box.max.y*0.86, z = (box.max.z-box.min.z)*0.05. Build the right side at that anchor, then the left side at the same anchor with scale.z = -1 (mirror).

5e. Procedural wings (the GLB has no wings)
- Wing texture: load WING_TEX into an Image (crossOrigin "anonymous"), draw into a 1024x576 canvas. For every pixel: l = (r*.3 + g*.59 + b*.11)/255; alpha = clamp((l - .035)*4.2, 0, 1)*255; then brighten r = min(255, r*1.5+30), g = min(255, g*1.5+30), b = min(255, b*1.5+40). putImageData; use it as a THREE.CanvasTexture (SRGB, set needsUpdate after processing).
- Material: MeshBasicMaterial({ map, transparent:true, opacity, side:DoubleSide, depthWrite:false, color:0xffffff, NormalBlending }).
- Geometry(span): PlaneGeometry(span, span*9/16); translate(span/2 - span*.03, 0, 0) (hinge at the root); rotateX(-PI/2) (flat); rotateY(-PI/2) (span points along +Z).
- Per side, two wings: forewing { span .72, sweep -.42, phase 0, lift .02 }, hindwing { span .52, sweep -.95, phase -.5, lift -.01 }.
  For each: sweep Group (rotation.y = sweep, position.y = lift). Inside it, three flap Groups, each with one mesh: [phase offset 0, opacity .95], [+.55, .28], [-.55, .28]. The two faint copies fake motion blur. Store each flap group with phase = wing phase + offset.

5f. Scroll-driven flight path
Keyframes, one per section (x/y in viewport units -1..1, s = size multiplier, yaw degrees where 0 = facing right, 180 = facing left, 90 = facing camera):
DESKTOP:
 hero   { x:-.03, y:-.12, s:1.00, yaw:150, pitch:6,  roll:-4 }
 01     { x:-.30, y:-.04, s:1.00, yaw:125, pitch:10, roll:6 }
 02     { x: .22, y:-.30, s:1.00, yaw:40,  pitch:-6, roll:-8 }
 03     { x:-.22, y: .02, s:0.96, yaw:160, pitch:8,  roll:4 }
 footer { x: .02, y:-.08, s:0.92, yaw:105, pitch:4,  roll:0 }
MOBILE (innerWidth < 760):
 { x:.05, y:-.02, s:.75, yaw:150, pitch:6, roll:-4 }
 { x:.10, y:.12,  s:.8,  yaw:125, pitch:10, roll:6 }
 { x:.15, y:-.20, s:.75, yaw:40,  pitch:-6, roll:-8 }
 { x:.25, y:.20,  s:.72, yaw:160, pitch:8, roll:4 }
 { x:0,   y:.1,   s:.7,  yaw:105, pitch:4, roll:0 }
ease(t) = t<.5 ? 4t³ : 1 - (-2t+2)³/2.  lerpAngle(a,b,t): d = ((b-a+540)%360)-180; return a + d*t.
targetAt(p) where p = scrollY/innerHeight (if not finite, p = 0); clamp p to [0, K.length-1]; i = min(K.length-2, floor(p)); f = p - i;
 t = ease(clamp((f - .12)/.76, 0, 1))   (holds still at each section, flies in between)
 dive = sin(t*PI) * -.22   (the bee drops down mid-transition, then glides back up)
 returns x = lerp, y = lerp + dive, s = lerp * (1 + sin(t*PI)*.12), yaw = lerpAngle, pitch/roll = lerp, moving = sin(t*PI).

5g. Animation loop (requestAnimationFrame)
- dt = min(clock.getDelta(), .05); t = elapsed time.
- Smooth follow: k = 1 - exp(-dt*3.2) for x, y, s, pitch, roll; yaw uses lerpAngle with 1 - exp(-dt*2.6). So the bee lags behind the scroll and flies to its spot.
- Velocity: vx, vy = change in cur.x / cur.y divided by dt.
- Mouse: track pointer in NDC (-1..1, y up); smoothed with 1 - exp(-dt*2).
- halfH = tan(fov/2)*camera.z; halfW = halfH*aspect; hover = sin(t*2.1)*.045 + sin(t*3.7)*.015.
- flight.position = ( cur.x*halfW + sin(t*1.3)*.04 + mouse.sx*.12,  cur.y*halfH + hover*halfH*.5 + mouse.sy*.08,  sin(t*.9)*.15 ).
- flight.scale = halfH*2*.30*cur.s (bee ≈ 30% of viewport height).
- flight.rotation.set(0, -(cur.yaw + mouse.sx*12) in radians, 0).
- pitch = cur.pitch - clamp(vy*22, -28, 28) + sin(t*2.1+1)*3 + mouse.sy*6;  roll = cur.roll + clamp(vx*18, -30, 30) + sin(t*1.7)*4;
  beeRoot.rotation.set(roll rad, 0, pitch rad, "YZX")  (nose down when diving, banks into turns).
- Wing beat: freq = 2π*(17 + moving*5); for each flap group: a = sin(t*freq + phase); rotation.x = -.25 + a*.95; rotation.y = a*.18.
- Render only once the GLB has loaded.

=====================================================================
6. RESULT
=====================================================================
A lavender, full-viewport scroll story: a hero with a giant black Poppins 800 headline that rises in, a dewy purple cosmos in the bottom-left corner, and a small paragraph + "Buzz in!" button on the right. A photoreal 3D bumblebee with flapping glassy wings hovers mid-screen and, as you scroll, dives and flies to a new spot in each section: beside "01 Explore this Universe of 3D Motion" (hanging cosmos top-left), down to the iris petal in the deep-violet "02 Claim Early Invite" section (nav turns white), over to the passion flower in "03 Study and Build with Us!", then front-and-centre in the footer ("Prepared to fly high?", Melli_Motion, social links). Flowers move at different scroll speeds and rotate slightly, section text fades up, the bee leans slightly toward the cursor, and on screens under 760px wide the layout and flight path switch to the mobile values above.
