<!-- Runway Lookbook · Interactive · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_044911_1ad79156-a8dc-475a-8891-8408a9b61320.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=vell-lookbook -->

# Maison Vell — Runway Depth Lookbook (exact recreation prompt)

Give me a single-file, full-viewport fashion page called **Maison Vell**. Six models stand in one line that recedes from the right of the screen into a blurred distance on the left. Dragging, scrolling or pressing the arrow keys walks the whole line forward: the front model grows and slides out behind the product column, everyone else takes the next place, and a new model arrives out of the haze at the back. The product column on the right scrolls in sync, and a big look number rolls over at bottom left. It loops forever.

Plain HTML, CSS and one vanilla script in one file, with no libraries. The only external resources are the Google Fonts and the two image sheets below. Reproduce every value, string and timing exactly, and use the complete code at the end as the source of truth.

Six rules define it:
1. **One number drives everything.** `p` is the current look position as a float. Each model's depth is `d = wrap(i - p, 6)`, moved into the range -1 to 5. Model, product column and look number are all computed from `p` alone.
2. **Depth is a table, not a formula.** Each model's position, size, blur and opacity are read from seven stops, one per depth from -1 to 5, and interpolated linearly.
3. **Two sprite sheets, cropped with SVG.** All six models come from one transparent image and all twelve products from another. Each is shown through an inline `<svg viewBox>` holding a nested `<svg>` so nothing outside the box can ever show.
4. **Layers scale, they do not resize.** Models are laid out once at 1.2 × stage height and only `transform` changes, so they stay sharp. Blur is divided by the scale so it looks the same on screen at any depth.
5. **Drag is direct, release snaps.** During a drag `target` follows the pointer. On release, or 150 ms after the wheel stops, it rounds to a whole look. `p` always chases `target` with an exponential ease.
6. **The product column wraps.** Twelve cards sit on one looping track, so scrolling never ends.

---

## 1. Page basics

- Title: `Maison Vell`
- Meta description: `A runway lookbook where six looks stand in a line into the distance and every drag brings the next one to the front.`
- Fonts: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Michroma&display=swap`, with preconnects to fonts.googleapis.com and fonts.gstatic.com (crossorigin). The supplied standalone file embeds the latin woff2 files as base64 instead.
- Michroma, uppercase, wide-tracked, for the logo, tabs, nav, headings, labels and look number. Inter for the paragraph and prices.
- Colours: ink `#16191f`, mid `#737b86`, dim `#a4adb8`, white page, rail `#f3f6fa`.
- Unit: `--u:min(calc(100vw/1600),calc(100vh/900))`, which becomes `1px` at 820px wide and below.
- `.page` is `100svh` tall, `min-height:520px`, a grid of header then main. Body has `overflow:hidden`.
- A fixed `.wait` cover in `#f1f5fa` fades over .5s once both sheets have decoded and fonts are ready.

## 2. Images (use these exact URLs)

1. Models sheet, transparent, 3840 × 2160: `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_042056_1a704ff7-b0e5-4a9f-bbda-62392b819fb6.png&w=3840&q=85`
2. Products sheet, transparent, 2400 wide: `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_042057_080e85b0-b4aa-4072-8eb9-2304c7baf42b.png&w=2400&q=85`

Models are measured on a 960 × 540 sheet, all with `y` from 48 to 496. Their `x` ranges in order: 12–176 (blush feather jacket and satin trousers), 178–330 (sage pleated gown), 331–470 (champagne satin trench), 476–633 (blush billow blouse and trousers), 634–767 (powder-blue coat), 767–956 (ivory ruffle gown).

Products are measured on a 960 × 720 sheet (x0, x1, y0, y1, name, price):

| Look | Piece | Box | Name | Price |
|---|---|---|---|---|
| 15 | 1 | 26, 224, 28, 214 | Feather Jacket | $2,900 |
| 15 | 2 | 304, 412, 22, 236 | Satin Wide Leg Trousers | $1,450 |
| 16 | 1 | 530, 666, 12, 242 | Pleated Dress | $2,200 |
| 16 | 2 | 752, 922, 100, 146 | Gold Waist Belt | $420 |
| 17 | 1 | 70, 176, 246, 466 | Satin Trench Dress | $2,350 |
| 17 | 2 | 294, 422, 294, 432 | Top Handle Bag | $980 |
| 18 | 1 | 508, 688, 240, 452 | Billow Sleeve Blouse | $860 |
| 18 | 2 | 780, 890, 252, 466 | Tie Waist Trousers | $740 |
| 19 | 1 | 64, 178, 484, 698 | Powder Long Coat | $1,980 |
| 19 | 2 | 316, 396, 482, 698 | Ivory Straight Trousers | $690 |
| 20 | 1 | 530, 672, 508, 682 | Sculpted Ruffle Top | $1,120 |
| 20 | 2 | 754, 916, 484, 700 | Pleated Maxi Skirt | $1,340 |

## 3. Header

- White, padding 20u top, 46u sides, 15u bottom. First row is a `1fr auto 1fr` grid.
- Logo `Maison Vell`, 15.5u, tracking .2em.
- Tabs, 14.5u, tracking .14em, gap 48u, dim colour: `Runway` (active, ink), `The Maison`, `Lookbook`, `Shop`.
- Right, 9.5u, tracking .12em, gap 22u: `Login`, search icon, heart icon, bag icon, `Cart (0)`. The icons are 17u outline SVGs.
- Second row, 17u below, centred, 9.5u, tracking .14em, gap 60u: `Collections`, `Clothing`, `Lookbook`, `Beauty`, `Accessories`, `Our World`.

## 4. Stage

- `main` is a grid of the stage plus a `372u` rail.
- Stage background: `linear-gradient(transparent 60%,rgba(255,255,255,.72) 100%)` over `linear-gradient(90deg,#f1f5fa 0%,#e7eff6 38%,#eef4f9 62%,#f6f9fc 100%)`. It has `cursor:none`, `touch-action:pan-y` and no text selection.
- Top left at 46u, 36u: `Spring Summer 2027`, 22u, tracking .16em. Then the paragraph 16u below, 14u Inter, line height 1.62, mid colour, 390u wide: `A study in softness and strength. The new season collection from Maison Vell blends delicate textures and modern silhouettes, crafted for a more beautiful tomorrow.`
- Bottom left at 46u, 44u: `Look` and the rolling number, 29u on a 38u line, tracking .14em. Then the underlined link `Shop the look`, 9.5u, 13u below.
- Rolling number: a 38u tall window with overflow hidden holding 15, 16, 17, 18, 19, 20, 15 stacked. It moves by `-wrap(p,6) × line height`, so the numbers slide past each other.
- Each model has a soft elliptical floor shadow: `radial-gradient(closest-side,rgba(70,85,105,.24),transparent)`, 84% wide, 3.6% tall, just below the feet.

## 5. Depth table

All are fractions of stage size. Depth runs -1, 0, 1, 2, 3, 4, 5. At depth -1 the model leaves past the rail, and at depth 5 it arrives from nothing.

| Value | -1 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|
| Centre X (`KX`) | 1.2 | .744 | .496 | .346 | .235 | .15 | .085 |
| Feet Y (`KF`) | 1.14 | .89 | .777 | .704 | .651 | .616 | .59 |
| Height (`KH`) | 1.18 | .832 | .574 | .436 | .334 | .258 | .19 |
| Blur px (`KB`) | 0 | 0 | 1.5 | 4 | 8 | 12 | 17 |
| Opacity (`KO`) | 1 | 1 | 1 | 1 | .86 | .5 | 0 |

`z-index` is `100 - round(d*10)`. Filter and opacity are written only when they change, and the page only repaints while `p` is moving.

## 6. Interaction

- Each frame, `p += (target-p) * (1-exp(-dt*.0072))`, with `dt` capped at 50 ms. It snaps to `target` under .0004.
- **Drag:** `target = start + dx / max(150, stageWidth*.2)`. Dragging right moves the line forward. Release rounds `target`.
- **Click:** a press that moves under 6px on a model in the line jumps to that look.
- **Wheel:** adds `clamp(deltaY+deltaX,-120,120)/420`, then rounds 150 ms after the last event.
- **Keys:** Right and Down go forward one look, Left and Up go back one. The stage is focusable.
- **Reduced motion:** `p` jumps straight to `target`.
- **Ring cursor:** 46u circle, 2.5u `#16191f` border, following the pointer at 32% per frame. While dragging it becomes an 84u × 34u pill over .22s with `cubic-bezier(.2,.8,.2,1)`. It shows only for a mouse.

## 7. Product rail

- Background `#f3f6fa`, overflow hidden. Exactly three cards fit, each `rail height / 3`. Odd cards are white.
- Card position: `y = wrap(i*card - p*2*card, 12*card)`, moved up by a full track if past the last slot, so each look's first piece lands at the top.
- Card padding 18u top and bottom, 24u sides. Heart button top left at 22u, 18u. Product image fills the remaining space, contained. Name 9.5u Michroma, tracking .14em. Price 12.5u Inter. Plus button 26u at bottom right, drawn with two 1.5px bars, rotating 90° on hover.
- Heart toggles `aria-pressed` and fills `#d8a7a0`. Plus adds one to the cart count.

## 8. Phones (820px and below)

`--u:1px`. Tabs, second nav row and all account items except the cart are hidden. Header padding 14px 16px 12px. `main` becomes a `1fr 190px` grid with the rail along the bottom as a horizontal track of 160px cards using `translate3d(x,0,0)`. The heading is 17px, the paragraph is hidden, the look number is 22px on a 30px line, and the ring is removed.

---

## Complete code

This is the finished page. Build exactly this.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maison Vell</title>
<meta name="description" content="A runway lookbook where six looks stand in a line into the distance and every drag brings the next one to the front.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Michroma&display=swap" rel="stylesheet">
<style>
:root{--u:min(calc(100vw/1600),calc(100vh/900));--ink:#16191f;--mid:#737b86;--dim:#a4adb8;--line:#e6ebf0;--ice:#e9f0f7}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#fff}
body{font-family:Inter,system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;overflow:hidden}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
ul{list-style:none}
.wide{font-family:Michroma,sans-serif;text-transform:uppercase}
.page{height:100svh;min-height:520px;display:grid;grid-template-rows:auto 1fr;background:#fff}
header{position:relative;z-index:5;background:#fff;padding:calc(20*var(--u)) calc(46*var(--u)) calc(15*var(--u))}
.r1{display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.brand{font-size:calc(15.5*var(--u));letter-spacing:.2em}
.tabs{display:flex;gap:calc(48*var(--u));font-size:calc(14.5*var(--u));letter-spacing:.14em;color:var(--dim)}
.tabs a{transition:color .25s}
.tabs a:hover,.tabs .on{color:var(--ink)}
.acct{justify-self:end;display:flex;align-items:center;gap:calc(22*var(--u));font-size:calc(9.5*var(--u));letter-spacing:.12em}
.acct svg{width:calc(17*var(--u));height:calc(17*var(--u));fill:none;stroke:currentColor;stroke-width:1.5}
.r2{display:flex;justify-content:center;gap:calc(60*var(--u));margin-top:calc(17*var(--u));font-size:calc(9.5*var(--u));letter-spacing:.14em}
.r2 a{transition:color .2s}.r2 a:hover{color:var(--mid)}
main{position:relative;display:grid;grid-template-columns:1fr calc(372*var(--u));min-height:0}
.stage{position:relative;overflow:hidden;min-width:0;touch-action:pan-y;user-select:none;-webkit-user-select:none;cursor:none;
  background:linear-gradient(transparent 60%,rgba(255,255,255,.72) 100%),linear-gradient(90deg,#f1f5fa 0%,#e7eff6 38%,#eef4f9 62%,#f6f9fc 100%)}
.line{position:absolute;inset:0}
.m{position:absolute;left:0;top:0;transform-origin:0 0;will-change:transform,filter;cursor:none}
.m svg{display:block;position:relative;width:100%;height:100%}
.m:before{content:"";position:absolute;left:8%;right:8%;bottom:-1.6%;height:3.6%;border-radius:50%;background:radial-gradient(closest-side,rgba(70,85,105,.24),transparent)}
.intro{position:absolute;z-index:2;left:calc(46*var(--u));top:calc(36*var(--u));width:calc(390*var(--u));pointer-events:none}
.intro h2{font-weight:400;font-size:calc(22*var(--u));line-height:1.2;letter-spacing:.16em;white-space:nowrap}
.intro p{margin-top:calc(16*var(--u));font-size:calc(14*var(--u));line-height:1.62;letter-spacing:.012em;color:var(--mid)}
.tag{position:absolute;z-index:2;left:calc(46*var(--u));bottom:calc(44*var(--u))}
.look{display:flex;font-size:calc(29*var(--u));line-height:calc(38*var(--u));letter-spacing:.14em;gap:.5em;pointer-events:none}
.win{height:calc(38*var(--u));overflow:hidden}
.roll{display:block;will-change:transform}
.roll b{display:block;font-weight:400;height:calc(38*var(--u))}
.shop{display:inline-block;margin-top:calc(13*var(--u));font-size:calc(9.5*var(--u));letter-spacing:.14em;padding-bottom:calc(4*var(--u));border-bottom:1px solid currentColor}
.ring{position:absolute;z-index:4;left:0;top:0;width:calc(46*var(--u));height:calc(46*var(--u));margin:calc(-23*var(--u)) 0 0 calc(-23*var(--u));border:calc(2.5*var(--u)) solid #16191f;border-radius:99px;pointer-events:none;opacity:0;transition:width .22s cubic-bezier(.2,.8,.2,1),height .22s cubic-bezier(.2,.8,.2,1),margin .22s cubic-bezier(.2,.8,.2,1),opacity .2s}
.ring.show{opacity:1}
.ring.drag{width:calc(84*var(--u));height:calc(34*var(--u));margin:calc(-17*var(--u)) 0 0 calc(-42*var(--u))}
.rail{position:relative;overflow:hidden;background:#f3f6fa;min-height:0}
.card{position:absolute;left:0;top:0;width:100%;display:flex;flex-direction:column;padding:calc(18*var(--u)) calc(24*var(--u)) calc(18*var(--u));will-change:transform;background:#f3f6fa}
.card.alt{background:#fff}
.fav{position:absolute;left:calc(22*var(--u));top:calc(18*var(--u));width:calc(22*var(--u));height:calc(22*var(--u));z-index:1;color:var(--ink)}
.fav svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.4;transition:fill .2s}
.fav[aria-pressed=true] svg{fill:#d8a7a0;stroke:#b98179}
.shot{flex:1;min-height:0;display:block}
.shot svg{display:block;width:100%;height:100%}
.meta{display:grid;grid-template-columns:1fr auto;align-items:end;margin-top:calc(8*var(--u))}
.meta h3{font-weight:400;font-size:calc(9.5*var(--u));letter-spacing:.14em}
.meta span{display:block;grid-column:1;margin-top:calc(6*var(--u));font-size:calc(12.5*var(--u));color:var(--mid);letter-spacing:.03em}
.add{grid-column:2;grid-row:1/3;width:calc(26*var(--u));height:calc(26*var(--u));position:relative;transition:transform .2s}
.add:before,.add:after{content:"";position:absolute;left:50%;top:50%;width:calc(15*var(--u));height:1.5px;margin:-.75px 0 0 calc(-7.5*var(--u));background:var(--ink)}
.add:after{transform:rotate(90deg)}
.add:hover{transform:rotate(90deg)}
.wait{position:fixed;inset:0;z-index:9;background:#f1f5fa;transition:opacity .5s;pointer-events:none}
.wait.gone{opacity:0}
button:focus-visible,a:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
@media (max-width:820px){
  :root{--u:1px}
  header{padding:14px 16px 12px}
  .r1{grid-template-columns:1fr auto}
  .tabs,.r2,.acct>a:not(:last-child){display:none}
  .brand{font-size:14px}
  main{grid-template-columns:1fr;grid-template-rows:1fr 190px}
  .stage{cursor:auto}.m{cursor:auto}.ring{display:none}
  .intro{left:16px;top:18px;width:calc(100% - 32px)}
  .intro h2{font-size:17px}
  .intro p{display:none}
  .tag{left:16px;bottom:18px}
  .look{font-size:22px;line-height:30px}.win,.roll b{height:30px}
  .card{width:160px;height:100%;padding:12px}
  .fav{left:10px;top:10px}
}
</style>
</head>
<body>
<div class="page">
  <header>
    <div class="r1">
      <a class="brand wide" href="#" aria-label="Maison Vell">Maison Vell</a>
      <nav class="tabs wide" aria-label="Sections"><a class="on" href="#" aria-current="page">Runway</a><a href="#">The Maison</a><a href="#">Lookbook</a><a href="#">Shop</a></nav>
      <div class="acct wide">
        <a href="#">Login</a>
        <a href="#" aria-label="Search"><svg viewBox="0 0 24 24"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/></svg></a>
        <a href="#" aria-label="Saved"><svg viewBox="0 0 24 24"><path d="M12 20S3.5 15 3.5 9A4.6 4.6 0 0 1 12 6.6 4.6 4.6 0 0 1 20.500 9C20.500 15 12 20 12 20Z"/></svg></a>
        <a href="#" aria-label="Bag"><svg viewBox="0 0 24 24"><path d="M5 8h14l1 13H4Z"/><path d="M9 10V6a3 3 0 0 1 6 0v4"/></svg></a>
        <a href="#">Cart (<span id="cart">0</span>)</a>
      </div>
    </div>
    <nav class="r2 wide" aria-label="Departments"><a href="#">Collections</a><a href="#">Clothing</a><a href="#">Lookbook</a><a href="#">Beauty</a><a href="#">Accessories</a><a href="#">Our World</a></nav>
  </header>
  <main>
    <section class="stage" id="stage" aria-label="Runway looks. Drag, scroll or use the arrow keys to change look." tabindex="0">
      <div class="line" id="line"></div>
      <div class="intro">
        <h2 class="wide">Spring Summer 2027</h2>
        <p>A study in softness and strength. The new season collection from Maison Vell blends delicate textures and modern silhouettes, crafted for a more beautiful tomorrow.</p>
      </div>
      <div class="tag">
        <div class="look wide" aria-live="polite"><span>Look</span><span class="win"><span class="roll" id="roll"></span></span></div>
        <a class="shop wide" href="#">Shop the look</a>
      </div>
      <div class="ring" id="ring"></div>
    </section>
    <aside class="rail" id="rail" aria-label="Pieces in this look"></aside>
  </main>
</div>
<div class="wait" id="wait"></div>
<script>
const MODELS='https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_042056_1a704ff7-b0e5-4a9f-bbda-62392b819fb6.png&w=3840&q=85';
const PIECES='https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261102_042057_080e85b0-b4aa-4072-8eb9-2304c7baf42b.png&w=2400&q=85';
// each model's box on the 960 x 540 sheet: x0, x1
const LOOKS=[[12,176],[178,330],[331,470],[476,633],[634,767],[767,956]],Y0=48,Y1=496,FIRST=15;
// each piece's box on the 960 x 720 sheet: x0, x1, y0, y1, name, price
const ITEMS=[
  [26,224,28,214,'Feather Jacket','$2,900'],[304,412,22,236,'Satin Wide Leg Trousers','$1,450'],
  [530,666,12,242,'Pleated Dress','$2,200'],[752,922,100,146,'Gold Waist Belt','$420'],
  [70,176,246,466,'Satin Trench Dress','$2,350'],[294,422,294,432,'Top Handle Bag','$980'],
  [508,688,240,452,'Billow Sleeve Blouse','$860'],[780,890,252,466,'Tie Waist Trousers','$740'],
  [64,178,484,698,'Powder Long Coat','$1,980'],[316,396,482,698,'Ivory Straight Trousers','$690'],
  [530,672,508,682,'Sculpted Ruffle Top','$1,120'],[754,916,484,700,'Pleated Maxi Skirt','$1,340']];
// depth stops from d = -1 (leaving past the rail) to d = 5 (arriving out of the haze)
const KX=[1.2,.744,.496,.346,.235,.15,.085],KF=[1.14,.89,.777,.704,.651,.616,.59],KH=[1.18,.832,.574,.436,.334,.258,.19],
      KB=[0,0,1.5,4,8,12,17],KO=[1,1,1,1,.86,.5,0];
const N=LOOKS.length,$=id=>document.getElementById(id),calm=matchMedia('(prefers-reduced-motion:reduce)').matches;
const stage=$('stage'),rail=$('rail'),ring=$('ring'),roll=$('roll'),line=$('line');
const NS='http://www.w3.org/2000/svg',wrap=(x,n)=>((x%n)+n)%n;
function crop(href,x0,y0,w,h,sheetW,sheetH){
  const s=document.createElementNS(NS,'svg');s.setAttribute('viewBox',`${x0} ${y0} ${w} ${h}`);s.setAttribute('aria-hidden','true');
  const f=document.createElementNS(NS,'svg');[['x',x0],['y',y0],['width',w],['height',h],['viewBox',`${x0} ${y0} ${w} ${h}`]].forEach(([k,v])=>f.setAttribute(k,v));
  const i=document.createElementNS(NS,'image');i.setAttribute('href',href);i.setAttribute('width',sheetW);i.setAttribute('height',sheetH);f.append(i);s.append(f);return s;
}
const people=LOOKS.map(([a,b],i)=>{
  const e=document.createElement('div');e.className='m';e.dataset.i=i;e.append(crop(MODELS,a,Y0,b-a,Y1-Y0,960,540));line.append(e);
  return{e,r:(b-a)/(Y1-Y0),f:'',o:''};
});
const cards=ITEMS.map(([a,b,c,d,name,price],i)=>{
  const e=document.createElement('article');e.className='card'+(i%2?' alt':'');
  e.innerHTML=`<button class="fav" aria-pressed="false" aria-label="Save ${name}"><svg viewBox="0 0 24 24"><path d="M12 20S3.5 15 3.5 9A4.6 4.6 0 0 1 12 6.6 4.600 4.600 0 0 1 20.500 9C20.500 15 12 20 12 20Z"/></svg></button><span class="shot"></span><div class="meta"><h3 class="wide">${name}</h3><span>${price}</span><button class="add" aria-label="Add ${name} to cart"></button></div>`;
  e.querySelector('.shot').append(crop(PIECES,a,c,b-a,d-c,960,720));rail.append(e);return e;
});
for(let i=0;i<=N;i++){const b=document.createElement('b');b.textContent=FIRST+i%N;roll.append(b)}
let cart=0;
rail.addEventListener('click',e=>{
  const f=e.target.closest('.fav');if(f)f.setAttribute('aria-pressed',f.getAttribute('aria-pressed')!=='true');
  if(e.target.closest('.add'))$('cart').textContent=++cart;
});

let W=0,H=0,base=0,cardS=0,side=false,dirty=true,p=0,target=0,last=0;
function size(){
  W=stage.clientWidth;H=stage.clientHeight;base=H*1.2;side=innerWidth<=820;
  people.forEach(m=>{m.e.style.width=base*m.r+'px';m.e.style.height=base+'px'});
  cardS=side?160:rail.clientHeight/3;
  cards.forEach(c=>c.style.height=side?'100%':cardS+'px');
  roll.style.setProperty('--h',roll.firstChild.getBoundingClientRect().height);
  dirty=true;
}
addEventListener('resize',size);

function paint(){
  people.forEach((m,i)=>{
    let d=wrap(i-p,N);if(d>N-1)d-=N;
    const k=clamp(d+1,0,6),a=Math.floor(k),b=Math.min(6,a+1),t=k-a,mix=A=>A[a]+(A[b]-A[a])*t;
    const h=mix(KH)*H,s=h/base,w=h*m.r,x=mix(KX)*W-w/2,y=mix(KF)*H-h;
    m.e.style.transform=`translate3d(${x.toFixed(1)}px,${y.toFixed(1)}px,0) scale(${s.toFixed(4)})`;
    const f=mix(KB)/s,fs=f<.2?'none':`blur(${f.toFixed(1)}px)`,o=mix(KO).toFixed(3);
    if(fs!==m.f){m.f=fs;m.e.style.filter=fs}
    if(o!==m.o){m.o=o;m.e.style.opacity=o}
    m.e.style.zIndex=100-Math.round(d*10);
  });
  const all=cardS*ITEMS.length;
  cards.forEach((c,i)=>{
    let y=wrap(i*cardS-p*2*cardS,all);if(y>all-cardS)y-=all;
    c.style.transform=side?`translate3d(${y.toFixed(1)}px,0,0)`:`translate3d(0,${y.toFixed(1)}px,0)`;
  });
  roll.style.transform=`translate3d(0,${(-wrap(p,N)*roll.firstChild.offsetHeight).toFixed(1)}px,0)`;
}
const clamp=(x,a,b)=>Math.min(b,Math.max(a,x));

function frame(now){
  const dt=Math.min(50,now-last)||16;last=now;
  const was=p;
  if(calm)p=target;else p+=(target-p)*(1-Math.exp(-dt*.0072));
  if(Math.abs(target-p)<.0004)p=target;
  if(p!==was||dirty){dirty=false;paint()}
  cx+=(mx-cx)*.32;cy+=(my-cy)*.32;
  ring.style.transform=`translate3d(${cx.toFixed(1)}px,${cy.toFixed(1)}px,0)`;
}

let mx=0,my=0,cx=0,cy=0,down=false,sx=0,st=0,moved=0,wheelT=0;
const PULL=()=>Math.max(150,W*.2);
stage.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')ring.classList.add('show')});
stage.addEventListener('pointerleave',()=>ring.classList.remove('show'));
stage.addEventListener('pointermove',e=>{
  const r=stage.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top;
  if(!down)return;
  const dx=e.clientX-sx;moved=Math.max(moved,Math.abs(dx));target=st+dx/PULL();
});
stage.addEventListener('pointerdown',e=>{
  if(e.target.closest('a'))return;
  down=true;sx=e.clientX;st=target;moved=0;stage.setPointerCapture(e.pointerId);ring.classList.add('drag');
});
function release(e){
  if(!down)return;down=false;ring.classList.remove('drag');
  if(moved<6){
    const hit=document.elementsFromPoint(e.clientX,e.clientY).find(x=>x.classList&&x.classList.contains('m'));
    if(hit){let d=wrap(+hit.dataset.i-target,N);d=Math.round(d);if(d>0&&d<N)target=Math.round(target)+d}
  }else target=Math.round(target);
}
stage.addEventListener('pointerup',release);stage.addEventListener('pointercancel',release);
stage.addEventListener('wheel',e=>{
  e.preventDefault();target+=clamp(e.deltaY+e.deltaX,-120,120)/420;
  clearTimeout(wheelT);wheelT=setTimeout(()=>{target=Math.round(target)},150);
},{passive:false});
addEventListener('keydown',e=>{
  if(['ArrowRight','ArrowDown'].includes(e.key)){e.preventDefault();target=Math.round(target)+1}
  if(['ArrowLeft','ArrowUp'].includes(e.key)){e.preventDefault();target=Math.round(target)-1}
});

function loop(t){frame(t);requestAnimationFrame(loop)}
Promise.all([MODELS,PIECES].map(u=>{const i=new Image;i.src=u;return i.decode().catch(()=>{})})).then(()=>document.fonts.ready).then(()=>{
  size();paint();$('wait').classList.add('gone');
});
size();requestAnimationFrame(loop);
</script>
</body>
</html>
```
