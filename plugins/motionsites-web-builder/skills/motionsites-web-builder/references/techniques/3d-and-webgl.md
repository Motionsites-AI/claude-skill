# 3D & WebGL

Real-time 3D models and shader backdrops. Both are **heavy**: use one per page, as the signature, and always ship a static fallback.

**Conventions.** Single-file, no build step. Pin library versions (`three@0.170.0`). Clamp the device pixel ratio, pause rendering off-screen, and render a still frame for `prefers-reduced-motion`. Opening the page over `file://` blocks model fetches, so serve it (`npx serve .` or `python3 -m http.server`) when testing; the fallback image appears otherwise.

---

## 1. Real 3D model hero (Three.js + GLB)

**What / when:** A real product, character or object model that the visitor can grab and turn, framed exactly inside a chosen area of the layout (usually the right half), with the copy beside it. It settles in with a short turn, sways gently when left alone, and drops to a PNG render if anything fails. Use it when you have (or can generate) a GLB and the object itself is the story: hardware, collectibles, sneakers, packaging, characters.

**Premium parameters**
- Lens **fov 30°** (product-shot look, little distortion). The model is re-centred on its bounding sphere and scaled to **unit radius**, so any GLB frames the same way; the camera distance is solved so the sphere fills **90 %** of the stage's shorter side.
- **Framing with `camera.setViewOffset`:** the camera still looks straight at the model (no perspective skew), but the projection is shifted so the model's centre lands on the centre of a stage element (`[data-stage]`). Layout decides where the model sits; resize keeps it there.
- Rig `pivot > spin > holder > model`: **holder** = centring + unit scale + authored-orientation fix; **spin** = user rotation + inertia; **pivot** = intro turn + idle sway. Each concern owns one group, so they never fight.
- Drag: **0.006 rad/px**, vertical at 0.6× of horizontal; rotations are **premultiplied** onto the spin quaternion around the screen axes, so dragging right always turns the visible face right whatever the current orientation (no gimbal lock). Release keeps the smoothed velocity and decays it (`friction 3.5/s`, max 12 rad/s); a pause of >90 ms before lifting kills the throw.
- Zoom: wheel / trackpad pinch / two-finger pinch, clamped **1 → 1.8**, smoothed (lerp ~10/s). The start zoom *is* the minimum, so a downward wheel over the hero scrolls the page instead of being trapped; trackpad pinch (`ctrlKey`) is always captured.
- Idle: after **1.8 s** without input the sway fades in (yaw ±0.22 rad, pitch ±0.06, lift 0.03 units, ~11 s period) and the model levels itself back upright, keeping its yaw.
- Intro: canvas fades in over 0.9 s while the pivot turns from −0.9 rad and scales 0.9 → 1 over 1.6 s (expo out). Shaders are compiled before the reveal so the first frame doesn't hitch.
- Light: `RoomEnvironment` baked through PMREM (sigma 0.04) as the environment + one key `DirectionalLight` (1.5) for definition; `NeutralToneMapping` keeps product colours honest (use `ACESFilmicToneMapping` for a filmic look).
- Loader: a 140 × 2 px bar driven by real download progress (indeterminate shimmer when the size is unknown). Fallback: a PNG render of the model at its default angle, loaded only when needed (GLB error, no WebGL, context loss, Save-Data).
- Performance: DPR clamped to **2**, rendering paused off-screen (IntersectionObserver), `ResizeObserver` on canvas and stage. Model budget ≤ 3–5 MB, textures 1–2K: `npx gltf-transform optimize in.glb model.glb --compress draco --texture-compress webp --texture-size 2048`.

**Implementation**
```html
<!-- in <head>, before any module script -->
<script type="importmap">
{ "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/"
} }
</script>

<section class="hero3d" data-model="model.glb">
  <canvas class="hero3d__canvas" aria-hidden="true"></canvas>
  <div class="hero3d__copy">
    <h1>Built to be held.</h1>
    <p>Drag it, turn it, look underneath. Every edge is exactly where you'd want it.</p>
    <a class="btn" href="#buy">Pre-order</a>
  </div>
  <div class="hero3d__stage" data-stage tabindex="0" role="group" aria-label="3D view of the product. Drag or use the arrow keys to rotate.">
    <div class="hero3d__loader is-indeterminate" role="status"><span class="hero3d__bar"><i></i></span><span>Loading model</span></div>
    <img class="hero3d__fallback" data-src="model-fallback.png" alt="The product, front three-quarter view" hidden>
  </div>
</section>
```
```css
.hero3d{position:relative;isolation:isolate;min-height:100vh;min-height:100dvh;display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);align-items:center;gap:clamp(24px,4vw,64px);
  padding:clamp(96px,12vh,140px) clamp(20px,5vw,72px) clamp(40px,6vh,80px);overflow:hidden;background:#0b0b0c;color:#f4f4f2}
.hero3d__canvas{position:absolute;inset:0;width:100%;height:100%;display:block;z-index:0;pointer-events:none;
  opacity:0;transition:opacity .9s cubic-bezier(.22,1,.36,1)}
.hero3d.is-ready .hero3d__canvas{opacity:1}
.hero3d.is-fallback .hero3d__canvas{display:none}
.hero3d__copy{position:relative;z-index:2;max-width:34rem}
.hero3d__copy h1{margin:0 0 20px;font:500 clamp(40px,5.2vw,76px)/.98 Inter,system-ui,sans-serif;letter-spacing:-.035em}
.hero3d__copy p{margin:0 0 32px;max-width:28rem;font-size:17px;line-height:1.55;color:rgb(244 244 242/.6)}
/* The stage is an empty box in the layout: the model is framed on its centre and it receives the drag */
.hero3d__stage{position:relative;z-index:1;align-self:stretch;min-height:clamp(320px,62vh,760px);display:grid;place-items:center;
  cursor:grab;touch-action:pan-y;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent;border-radius:24px;outline:none}
.hero3d__stage:active{cursor:grabbing}
.hero3d__stage:focus-visible{box-shadow:inset 0 0 0 1px rgb(255 255 255/.3)}
.hero3d__stage>*{grid-area:1/1}
.hero3d__loader{display:grid;justify-items:center;gap:12px;font:500 11px/1 ui-monospace,monospace;letter-spacing:.2em;
  text-transform:uppercase;color:rgb(255 255 255/.5);transition:opacity .4s}
.hero3d__bar{width:140px;height:2px;border-radius:2px;background:rgb(255 255 255/.12);overflow:hidden}
.hero3d__bar i{display:block;width:100%;height:100%;background:#fff;transform-origin:left;transform:scaleX(var(--p,0));transition:transform .2s linear}
.hero3d__loader.is-indeterminate .hero3d__bar i{width:40%;transform:none;animation:hero3d-bar 1.1s ease-in-out infinite}
@keyframes hero3d-bar{from{translate:-100% 0}to{translate:250% 0}}
.hero3d.is-ready .hero3d__loader,.hero3d.is-fallback .hero3d__loader{opacity:0;pointer-events:none}
.hero3d__fallback{width:min(88%,560px);height:auto;object-fit:contain}
.hero3d.is-fallback .hero3d__stage{cursor:default}
@media (max-width:860px){
  .hero3d{grid-template-columns:1fr;align-content:start}
  .hero3d__stage{min-height:56vh;min-height:56svh}
}
@media (prefers-reduced-motion:reduce){
  .hero3d__canvas{transition:none}
  .hero3d__loader.is-indeterminate .hero3d__bar i{animation:none;width:100%;opacity:.4}
}
```
```html
<script type="module">
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const DRACO_PATH = 'https://www.gstatic.com/draco/versioned/decoders/1.5.7/';
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const easeOutExpo = (t) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t));

function modelHero(root, opts = {}) {
  const o = {
    src: root.dataset.model,
    fov: 30,                    // narrow lens: product-shot look
    fill: 0.9,                  // share of the stage's shorter side the bounding sphere fills
    zoomMin: 1, zoomMax: 1.8,   // start = min, so a downward wheel scrolls the page
    dragSpeed: 0.006,           // rad per px
    friction: 3.5,              // inertia decay per second
    idleAfter: 1800,            // ms without input before the idle sway
    sway: { yaw: 0.22, pitch: 0.06, lift: 0.03, speed: 0.55 },
    rightOnIdle: true,          // level the model again when idle (keeps its yaw)
    baseRotation: [0, 0, 0],    // fix the model's authored orientation (radians)
    exposure: 1,
    ...opts,
  };
  const canvas = root.querySelector('.hero3d__canvas');
  const stage = root.querySelector('[data-stage]');
  const loaderEl = root.querySelector('.hero3d__loader');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let renderer, raf = 0, ready = false, visible = true, dead = false;

  const dropLoader = () => setTimeout(() => loaderEl?.remove(), 500);
  const showFallback = () => {
    if (dead) return;
    dead = true; ready = false; cancelAnimationFrame(raf); raf = 0;
    root.classList.remove('is-ready'); root.classList.add('is-fallback');
    const img = root.querySelector('.hero3d__fallback');
    if (img) { if (!img.getAttribute('src')) img.src = img.dataset.src; img.hidden = false; }
    dropLoader();
  };
  if (!o.src || navigator.connection?.saveData) { showFallback(); return () => {}; }
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' });
  } catch (e) { showFallback(); return () => {}; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NeutralToneMapping;
  renderer.toneMappingExposure = o.exposure;
  canvas.addEventListener('webglcontextlost', (e) => { e.preventDefault(); showFallback(); });

  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  const room = new RoomEnvironment();
  scene.environment = pmrem.fromScene(room, 0.04).texture;
  room.dispose?.(); pmrem.dispose();
  const key = new THREE.DirectionalLight(0xffffff, 1.5);
  key.position.set(2.5, 3.5, 4);
  scene.add(key);
  const camera = new THREE.PerspectiveCamera(o.fov, 1, 0.05, 200);

  // Rig: pivot (intro + idle sway) > spin (user rotation + inertia) > holder (centre + unit scale) > model
  const pivot = new THREE.Group(), spin = new THREE.Group(), holder = new THREE.Group();
  holder.rotation.set(...o.baseRotation);
  spin.add(holder); pivot.add(spin); scene.add(pivot);

  // State
  let baseDist = 10, zoomT = clamp(1, o.zoomMin, o.zoomMax), zoom = zoomT;
  let vx = 0, vy = 0, dragging = false, swayW = 0, last = 0, introStart = 0, lastInput = performance.now();
  const AX_X = new THREE.Vector3(1, 0, 0), AX_Y = new THREE.Vector3(0, 1, 0);
  const dq = new THREE.Quaternion(), upright = new THREE.Quaternion(), eul = new THREE.Euler(0, 0, 0, 'YXZ');
  const rotateBy = (ax, ay) => {                       // premultiply = rotate about screen axes
    spin.quaternion.premultiply(dq.setFromAxisAngle(AX_Y, ax));
    spin.quaternion.premultiply(dq.setFromAxisAngle(AX_X, ay));
  };

  // Framing: project the model's centre onto the stage element's centre
  function layout() {
    const W = canvas.clientWidth, H = canvas.clientHeight;
    if (!W || !H) return;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setSize(W, H, false);
    const c = canvas.getBoundingClientRect();
    let s = stage.getBoundingClientRect();
    if (!s.width || !s.height) s = c;
    const sx = s.left - c.left + s.width / 2, sy = s.top - c.top + s.height / 2;
    camera.aspect = W / H;
    camera.setViewOffset(W, H, W / 2 - sx, H / 2 - sy, W, H);
    const fitPx = o.fill * Math.min(s.width, s.height);                 // on-screen diameter of the unit sphere
    baseDist = H / (fitPx * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)));
    camera.updateProjectionMatrix();
    wake();
  }

  function tick(now) {
    raf = 0;
    const dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now;
    const rm = reduce.matches;
    let busy = false;
    if (!dragging && (vx || vy)) {                                      // inertia
      if (rm) { vx = vy = 0; }
      else {
        rotateBy(vx * dt, vy * dt);
        const k = Math.exp(-o.friction * dt); vx *= k; vy *= k;
        if (Math.hypot(vx, vy) < 0.02) vx = vy = 0; else busy = true;
      }
    }
    zoom = rm ? zoomT : zoom + (zoomT - zoom) * (1 - Math.exp(-dt * 10));
    if (Math.abs(zoomT - zoom) > 1e-4) busy = true; else zoom = zoomT;
    camera.position.set(0, 0, Math.max(1.6, baseDist / zoom));

    const intro = rm ? 1 : easeOutExpo(Math.min(1, (now - introStart) / 1600));
    if (intro < 1) busy = true;

    const idle = !rm && !dragging && !vx && !vy && now - lastInput > o.idleAfter;
    swayW += ((idle ? 1 : 0) - swayW) * (1 - Math.exp(-dt * (idle ? 1.2 : 6)));
    if (o.rightOnIdle && swayW > 0.001) {                               // level out, keep the yaw
      eul.setFromQuaternion(spin.quaternion); eul.x = 0; eul.z = 0;
      spin.quaternion.slerp(upright.setFromEuler(eul), (1 - Math.exp(-dt * 1.5)) * swayW);
    }
    const t = (now / 1000) * o.sway.speed;
    pivot.rotation.set(swayW * o.sway.pitch * Math.sin(t * 1.3 + 1), (1 - intro) * -0.9 + swayW * o.sway.yaw * Math.sin(t), 0);
    pivot.position.y = swayW * o.sway.lift * Math.sin(t * 1.7);
    pivot.scale.setScalar(0.9 + 0.1 * intro);

    renderer.render(scene, camera);
    if (visible && !dead && (busy || dragging || !rm)) raf = requestAnimationFrame(tick);   // reduced motion: render on demand
  }
  function wake() { if (!raf && visible && ready) { last = performance.now(); raf = requestAnimationFrame(tick); } }
  const poke = () => { lastInput = performance.now(); wake(); };

  // Drag to rotate (one pointer) and pinch to zoom (two pointers)
  const pointers = new Map();
  let lastX = 0, lastY = 0, lastT = 0, pinch = 0;
  stage.addEventListener('pointerdown', (e) => {
    if (!ready || (e.pointerType === 'mouse' && e.button !== 0)) return;
    stage.setPointerCapture(e.pointerId);
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size === 1) { dragging = true; vx = vy = 0; lastX = e.clientX; lastY = e.clientY; lastT = e.timeStamp; }
    else if (pointers.size === 2) { const [a, b] = [...pointers.values()]; pinch = Math.hypot(a.x - b.x, a.y - b.y); }
    poke();
  });
  stage.addEventListener('pointermove', (e) => {
    if (!pointers.has(e.pointerId)) return;
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size >= 2) {
      const [a, b] = [...pointers.values()];
      const d = Math.hypot(a.x - b.x, a.y - b.y);
      if (pinch > 0) zoomT = clamp(zoomT * (d / pinch), o.zoomMin, o.zoomMax);
      pinch = d;
    } else {
      const dx = e.clientX - lastX, dy = e.clientY - lastY, dms = Math.max(1, e.timeStamp - lastT);
      lastX = e.clientX; lastY = e.clientY; lastT = e.timeStamp;
      const ax = dx * o.dragSpeed;
      const ay = e.pointerType === 'touch' ? 0 : dy * o.dragSpeed * 0.6;   // touch: vertical swipes scroll the page
      rotateBy(ax, ay);
      vx = 0.75 * vx + 0.25 * (ax / dms) * 1000;                          // rad/s, smoothed
      vy = 0.75 * vy + 0.25 * (ay / dms) * 1000;
    }
    poke();
  });
  const release = (e) => {
    if (!pointers.delete(e.pointerId)) return;
    if (pointers.size === 1) {                                            // pinch -> drag: re-seed
      const [p] = [...pointers.values()];
      lastX = p.x; lastY = p.y; lastT = e.timeStamp; pinch = 0; vx = vy = 0;
    } else if (pointers.size === 0) {
      dragging = false;
      if (e.type === 'pointercancel' || e.timeStamp - lastT > 90 || reduce.matches) vx = vy = 0;
      vx = clamp(vx, -12, 12); vy = clamp(vy, -12, 12);
    }
    poke();
  };
  stage.addEventListener('pointerup', release);
  stage.addEventListener('pointercancel', release);

  // Wheel / trackpad pinch zoom; at the limits the page scrolls normally
  stage.addEventListener('wheel', (e) => {
    if (!ready) return;
    const dy = e.deltaY * (e.deltaMode === 1 ? 16 : 1);
    const atLimit = dy > 0 ? zoomT <= o.zoomMin + 1e-3 : zoomT >= o.zoomMax - 1e-3;
    if (atLimit && !e.ctrlKey) return;
    e.preventDefault();
    zoomT = clamp(zoomT * Math.exp(-dy * (e.ctrlKey ? 0.01 : 0.0015)), o.zoomMin, o.zoomMax);
    poke();
  }, { passive: false });

  // Keyboard: arrows rotate 15°, +/- zoom
  stage.addEventListener('keydown', (e) => {
    if (!ready) return;
    const step = 0.26;
    const turns = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, -step], ArrowDown: [0, step] };
    if (turns[e.key]) rotateBy(...turns[e.key]);
    else if (e.key === '+' || e.key === '=') zoomT = clamp(zoomT * 1.15, o.zoomMin, o.zoomMax);
    else if (e.key === '-') zoomT = clamp(zoomT / 1.15, o.zoomMin, o.zoomMax);
    else return;
    e.preventDefault();
    poke();
  });

  // Load: re-centre on the bounding sphere, scale to unit radius, compile, reveal
  const draco = new DRACOLoader().setDecoderPath(DRACO_PATH);
  const loader = new GLTFLoader().setDRACOLoader(draco);
  loader.load(o.src, (gltf) => {
    draco.dispose();
    if (dead) return;
    const model = gltf.scene;
    model.updateMatrixWorld(true);
    const sphere = new THREE.Box3().setFromObject(model).getBoundingSphere(new THREE.Sphere());
    if (!(sphere.radius > 0) || !Number.isFinite(sphere.radius)) { showFallback(); return; }
    model.position.sub(sphere.center);
    holder.scale.setScalar(1 / sphere.radius);
    holder.add(model);
    layout();
    const reveal = () => {
      if (dead) return;
      ready = true;
      introStart = lastInput = performance.now();
      root.classList.add('is-ready');
      dropLoader();
      wake();
    };
    renderer.compileAsync(scene, camera).then(reveal, reveal);           // no shader hitch on the first frame
  }, (e) => {
    if (!loaderEl || !e.lengthComputable || !e.total) return;
    loaderEl.classList.remove('is-indeterminate');
    loaderEl.style.setProperty('--p', Math.min(1, e.loaded / e.total).toFixed(3));
  }, () => { draco.dispose(); showFallback(); });

  const ro = new ResizeObserver(() => layout());
  ro.observe(canvas); ro.observe(stage);
  const io = new IntersectionObserver(([en]) => { visible = en.isIntersecting; if (visible) wake(); });
  io.observe(root);
  reduce.addEventListener('change', wake);
  document.fonts?.ready.then(() => layout());

  return () => { dead = true; cancelAnimationFrame(raf); ro.disconnect(); io.disconnect(); renderer.dispose(); };
}

modelHero(document.querySelector('.hero3d'));
// Options: modelHero(el, { baseRotation: [0, Math.PI / 4, 0], fill: 0.8, zoomMax: 2.2, rightOnIdle: false });
</script>
```

**Notes**
- **Placing the model:** move or resize `[data-stage]` with ordinary CSS (a grid column, an absolutely positioned box, a card) and the model follows; nothing in the script knows about the layout. The canvas stays full-bleed so the model can overhang the stage edges slightly without clipping.
- **Orientation:** most GLBs face +Z. If yours faces sideways or lies down, fix it once with `baseRotation` rather than rotating in the rig.
- **Look:** a dark page with the model lit by the room environment reads as a studio shot. For a light page set the section background light and `exposure` ~0.9. Add a soft CSS ground shadow under the stage (`radial-gradient(closest-side, rgb(0 0 0/.35), transparent)` in a squashed ellipse) if the object needs to sit on something.
- **Hosting:** the GLB and fallback PNG must come from the same origin or a host that sends CORS headers. The Draco decoder is fetched from gstatic only when the file is Draco-compressed.
- **Reduced motion:** no intro turn, no sway or self-levelling, no inertia, zoom snaps, and frames render only on input. Drag still works because it is user-driven.
- **Mobile:** on touch, horizontal drags rotate and vertical swipes scroll the page (`touch-action: pan-y`); two-finger pinch zooms. The layout stacks the stage under the copy at ≤860 px.
- **React:** call `modelHero(ref.current)` inside `useEffect` and return its cleanup function; keep the markup identical. (React Three Fiber with drei's `useGLTF`/`Bounds` is the idiomatic alternative when the project already uses it.)

---

## 2. Animated shader backdrop (swirl + pointer chroma blob + fluted glass + grain)

**What / when:** A light, almost-white hero whose background is alive: a slow marble swirl between two near-whites, a saturated accent blob that lazily follows the cursor, all seen through vertical **fluted (reeded) glass** with slight chromatic aberration and ridge highlights, plus film grain. For agency and studio heroes on light themes; dark text sits on top with no scrim.

**Premium parameters**
- Swirl `colorA #ffffff`, `colorB #f0f0f0`, twist ("detail") **1.7**.
- Chroma blob in one accent (e.g. `#ff5f03`), heavy momentum (follow lerp **0.04** per frame), soft radius.
- Fluted glass: **8** flutes, angle **31°**, refraction ~0.04 of the frame, aberration ~0.004, ridge highlight **.12**, rounded flute shading.
- Film grain strength **.05**. Page background `#EFEFEF` behind it (the CSS fallback when WebGL is unavailable).
- Full-screen fragment shaders are fill-rate bound: cap DPR at **1.5**, stop the loop off-screen, render one still frame for reduced motion.

**Implementation**
```html
<section class="shader-hero">
  <canvas class="shader-hero__canvas" aria-hidden="true"></canvas>
  <div class="shader-hero__content">…</div>
</section>
```
```css
.shader-hero{position:relative;min-height:100vh;min-height:100svh;background:#EFEFEF;overflow:hidden}
.shader-hero__canvas{position:absolute;inset:0;width:100%;height:100%;display:block;z-index:0;pointer-events:none}
.shader-hero__content{position:relative;z-index:1}
```
```js
const SHADER_VERT = `
attribute vec2 aPos;
void main(){ gl_Position = vec4(aPos, 0.0, 1.0); }`;

const SHADER_FRAG = `
#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
uniform vec2  uRes;
uniform float uTime;
uniform vec2  uPointer;
uniform vec3  uColA, uColB, uAccent;
uniform float uFlutes, uAngle, uRefract, uAberr, uHighlight, uGrain;

float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float noise(vec2 p){
  vec2 i = floor(p), f = fract(p);
  vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), u.x),
             mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);
}
float fbm(vec2 p){
  float v = 0.0, a = 0.5;
  for (int i = 0; i < 4; i++){ v += a * noise(p); p *= 2.0; a *= 0.5; }
  return v;
}
vec3 scene(vec2 uv){
  float aspect = uRes.x / uRes.y;
  vec2 p = vec2(uv.x * aspect, uv.y);
  float t = uTime * 0.06;
  vec2 c = p - vec2(0.5 * aspect, 0.5);
  float r = length(c);
  float ang = atan(c.y, c.x) + r * 1.7 - t;                 // swirl twist ("detail")
  vec2 q = vec2(cos(ang), sin(ang)) * r;
  float s = fbm(q * 2.5 + vec2(t, -t));
  vec3 col = mix(uColA, uColB, smoothstep(0.3, 0.7, s));
  vec2 m = vec2(uPointer.x * aspect, uPointer.y);
  float d = length(p - m) + 0.12 * (fbm(p * 3.0 + t * 3.0) - 0.5);
  float blob = 1.0 - smoothstep(0.0, 0.45, d);              // chroma blob
  return mix(col, uAccent, blob);
}
void main(){
  vec2 uv = gl_FragCoord.xy / uRes;
  float aspect = uRes.x / uRes.y;
  vec2 p = vec2((uv.x - 0.5) * aspect, uv.y - 0.5);
  float ca = cos(uAngle), sa = sin(uAngle);
  float across = ca * p.x - sa * p.y;                       // coordinate across the flutes
  float bend = fract(across * uFlutes) * 2.0 - 1.0;         // -1..1 inside one flute
  vec2 dir = vec2(ca, -sa);
  vec2 off = dir * bend * uRefract; off.x /= aspect;        // refraction
  vec2 ab  = dir * uAberr;          ab.x  /= aspect;        // chromatic aberration
  vec3 col;
  col.r = scene(uv + off + ab).r;
  col.g = scene(uv + off).g;
  col.b = scene(uv + off - ab).b;
  col *= 1.0 - 0.06 * bend * bend;                          // rounded flute shading
  col += uHighlight * pow(max(0.0, 1.0 - abs(bend)), 6.0);  // ridge highlight
  col += (hash(gl_FragCoord.xy + fract(uTime) * 61.0) - 0.5) * uGrain;   // film grain
  gl_FragColor = vec4(col, 1.0);
}`;

function shaderBackdrop(canvas, opts = {}) {
  const o = Object.assign({ colA: '#ffffff', colB: '#f0f0f0', accent: '#ff5f03', flutes: 8, angle: 31,
    refract: 0.04, aberr: 0.004, highlight: 0.12, grain: 0.05, momentum: 0.04, speed: 1 }, opts);
  const gl = canvas.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'low-power' });
  if (!gl) return false;                                      // the CSS background is the fallback
  const compile = (type, src) => {
    const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
    return s;
  };
  const prog = gl.createProgram();
  gl.attachShader(prog, compile(gl.VERTEX_SHADER, SHADER_VERT));
  gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, SHADER_FRAG));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog));
  gl.useProgram(prog);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);  // one covering triangle
  const aPos = gl.getAttribLocation(prog, 'aPos');
  gl.enableVertexAttribArray(aPos);
  gl.vertexAttribPointer(aPos, 2, gl.FLOAT, false, 0, 0);
  const U = (n) => gl.getUniformLocation(prog, n);
  const rgb = (h) => { const n = parseInt(h.slice(1), 16); return [(n >> 16 & 255) / 255, (n >> 8 & 255) / 255, (n & 255) / 255]; };
  gl.uniform3fv(U('uColA'), rgb(o.colA)); gl.uniform3fv(U('uColB'), rgb(o.colB)); gl.uniform3fv(U('uAccent'), rgb(o.accent));
  gl.uniform1f(U('uFlutes'), o.flutes); gl.uniform1f(U('uAngle'), o.angle * Math.PI / 180);
  gl.uniform1f(U('uRefract'), o.refract); gl.uniform1f(U('uAberr'), o.aberr);
  gl.uniform1f(U('uHighlight'), o.highlight); gl.uniform1f(U('uGrain'), o.grain);
  const uRes = U('uRes'), uTime = U('uTime'), uPointer = U('uPointer');

  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let px = 0.72, py = 0.35, tx = px, ty = py, visible = true, raf = 0;
  const resize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 1.5);   // full-screen fragment shader: cap DPR
    canvas.width = Math.round(canvas.clientWidth * dpr);
    canvas.height = Math.round(canvas.clientHeight * dpr);
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.uniform2f(uRes, canvas.width, canvas.height);
  };
  const draw = (t) => {
    px += (tx - px) * o.momentum; py += (ty - py) * o.momentum;  // heavy "momentum" follow
    gl.uniform1f(uTime, (t / 1000) * o.speed);
    gl.uniform2f(uPointer, px, py);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  };
  const loop = (t) => { draw(t); raf = visible && !reduce ? requestAnimationFrame(loop) : 0; };
  resize();
  addEventListener('resize', () => { resize(); if (!raf) draw(performance.now()); });
  addEventListener('pointermove', (e) => {
    const r = canvas.getBoundingClientRect();
    tx = (e.clientX - r.left) / r.width; ty = 1 - (e.clientY - r.top) / r.height;   // GL y points up
  }, { passive: true });
  new IntersectionObserver(([e]) => {
    visible = e.isIntersecting;
    if (visible && !raf && !reduce) raf = requestAnimationFrame(loop);
  }).observe(canvas);
  if (reduce) draw(12000); else raf = requestAnimationFrame(loop);
  return true;
}
shaderBackdrop(document.querySelector('.shader-hero__canvas'));
```

**Mobile:** with no pointer the blob rests at its start position (72 % / 35 %); for touch you can drift it slowly with a `sin`/`cos` target instead. On low-end phones consider `flutes` 6 and DPR 1.
