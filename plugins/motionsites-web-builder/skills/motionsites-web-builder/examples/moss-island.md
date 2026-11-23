<!-- Moss Island · SaaS · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261106_032528_99eb9a00-a553-40b6-8b97-017e918971c6.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=moss-island -->

# Mossline: Floating Moss Island Scroll Fly-In (exact recreation prompt)

Build a single-file landing page for **Mossline**, a fictional environmental-data company that measures ecosystems with field sensors. The page is one long pinned scroll story followed by a white solutions section.

The story has five beats:

1. **Hero:** a misty pale-grey sky with a huge floating rock island covered in moss and ferns, and the one-line headline "Measure the Living Planet". The island's ferns grow in front of the bottom of the headline letters.
2. **Fly-in:** scrolling scrubs a cinematic video in which the camera pushes into the island, glides over its mossy top and lands at eye level in a moss landscape facing a slim sensor mast. Two small floating rocks fly past the camera, and the vision statement resolves out of blur mid-flight.
3. **Landscape:** an accounting paragraph writes in word by word and four lime hotspots pop up on the moss. A fog bank rolls in from the left to keep the sky behind the text clean.
4. **Station:** a heading, a glass "Accumulated carbon balance" card with a count-up and a drawing sparkline, and a five-row feature list.
5. **Solutions:** a white rounded panel slides up with a heading, three tilting image cards and four count-up stats.

Use plain HTML, CSS and vanilla JS in one file, with no libraries. Every value below is exact. Reproduce every string, number, timing and URL as written.

---

## 1. Page basics

- `<html lang="en">`, title `Mossline — Measure the Living Planet`, viewport `width=device-width,initial-scale=1`, charset utf-8.
- **Fonts (Google Fonts):** `https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap`, with preconnects to `https://fonts.googleapis.com` and `https://fonts.gstatic.com` (crossorigin). The standalone version embeds the five latin woff2 faces (Inter Tight 400/500/600, JetBrains Mono 400/500) as base64 `@font-face` rules instead of the link.
- **CSS variables on `:root`:**
  - `--ink:#10291a`, `--ink2:#2c4434`
  - `--mist:#e7ebe8`, `--paper:#f6f7f4`
  - `--lime:#c6f35c`, `--lime2:#a9dd3a`
  - `--glass:rgba(244,247,243,.16)`, `--line:rgba(255,255,255,.28)`
  - `--sans:"Inter Tight","Helvetica Neue",Arial,sans-serif`
  - `--mono:"JetBrains Mono",ui-monospace,Menlo,monospace`
- **Global reset and base:**
  - Universal `box-sizing:border-box;margin:0;padding:0`.
  - `html` and `body` background `var(--mist)`; body font `var(--sans)`, colour `var(--ink)`, `-webkit-font-smoothing:antialiased`, `overflow-x:hidden`.
  - Links inherit colour with no underline.
- **`.mono` utility:** mono font, uppercase, letter-spacing .14em, 11px.
- **`.chip`** (the lime tag used everywhere): inline-flex, centred, height 22px, padding 0 9px, background `--lime`, colour `--ink`, radius 3px, mono 10.5px, letter-spacing .16em, uppercase.

## 2. Assets (all URLs exact)

All images are Higgsfield results served through the images.higgs.ai proxy. The video is a direct CloudFront mp4.

1. **Fly-in video (Kling 4.0, 5.04 s, 24 fps, 121 frames, 1912×1080, no audio):**
   `https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20261106_025717_906b686d-9a9a-4dea-bab4-ae2454f8390e.mp4`
   Content: the camera starts on the floating moss island in the misty sky, pushes forward and descends over its mossy top through fog, and lands at eye level in a moss-and-fern landscape facing a slim grey sensor mast (white louvered sensor housings, small solar panel). Distant floating rocks hang in the haze behind.
2. **High-res hero still (GPT Image 2.5 recreation of video frame 0, 2688×1520):**
   `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261106_031618_8ce6dca1-972d-429d-8d13-bf0691c37848.png&w=2400&q=88`
3. **Transparent cut-out of that still (big island plus two small side rocks on transparency):**
   `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261106_031657_baaa3380-5ece-482a-a623-a1838fd7653c.png&w=2400&q=90`
4. **Floating rock sprite sheet (three mossy rocks in a row on transparency, treated as a 1200×678 coordinate frame):**
   `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261106_025635_82593f6a-1cf7-41c1-94ac-96fb89ebfd1a.png&w=2400&q=85`
5. **Sensor-mast landscape still (used for two solution cards):**
   `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261106_025630_9a37a1e0-2547-4973-8160-c75205993914.png&w=1400&q=82`
6. **Floating island in clouds still (used for the middle solution card):**
   `https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261106_025545_b003e5cc-e68f-4fee-b686-c217a5d81eea.png&w=1400&q=82`

## 3. Navigation (fixed)

- **Bar:** fixed to the top, z-index 50, a three-column grid (`1fr auto 1fr`), items centred, padding 22px 34px.
- **Logo (left):**
  - Flex with 9px gap; Inter Tight 600, 21px, letter-spacing -.02em; text "Mossline".
  - Icon: a 26×26 inline SVG on a 32×32 viewBox.
    - A hexagon filled with currentColor: path `M16 2l12 7v14l-12 7-12-7V9z`.
    - A lime `#c6f35c` leaf on top: path `M16 8c-4 4-5 9-1 16 1-5 4-9 8-11-3 0-5 1-7 3 0-3 0-5 0-8z`.
- **Menu (centre):**
  - Four links with a 30px gap: "Solutions", "Our tech", "Company", "Resources".
  - Each is mono 11.5px, letter-spacing .14em, uppercase, with a 7px gap before a chevron.
  - Chevron: a 6×6 box with 1.3px right and bottom borders in currentColor, `translateY(-2px) rotate(45deg)`.
  - Hover colour `--lime2`.
- **Right:**
  - "LET'S TALK" in mono 11.5px, letter-spacing .16em, with a 12px gap before a 20×20 lime square (radius 3px) holding "›" in ink.
  - On hover the square shifts 3px right (.3s transition).

## 4. Scroll story structure

- **`#story`:** position relative, height **640vh**.
- **Stage:** sticky at top 0, height 100vh, overflow hidden, background `#dfe3e0`. Inside it, in stacking order:
  1. **Camera box `.cam`:** absolute with inset `-9% -3% -3%` (it overhangs the top by 9% and the other sides by 3%), `will-change:transform`. It contains:
     - A `<canvas id="cv">`.
     - The high-res still (asset 2) as `<img class="plate">`, absolutely filling the box with `object-fit:cover`, stacked above the canvas.
     - A `.mist` div at inset -10% with two radial gradients: `40% 30% at 20% 80%` white .55 → transparent 70%, and `35% 25% at 85% 30%` white .4 → transparent 70%. It runs a "drift" animation (18 s ease-in-out infinite alternate) to `translate3d(4%,-2%,0)`.
  2. **Hidden `<video id="push">`:** asset 1, `muted playsinline preload="auto" crossorigin="anonymous"`, 2×2px, opacity 0, pointer-events none.
  3. **Fog bank `.fog`** (section 8).
  4. **Layer L0:** the hero headline block.
  5. **Front cut-out `.cam.camF`:** a second camera box with the same inset. It holds asset 3 as an `<img>` filling the box with `object-fit:cover`. A horizontal mask keeps only the big island: `linear-gradient(90deg, transparent 25%, #000 27.5%, #000 71.5%, transparent 74%)`, with a `-webkit-` prefix too. It starts `visibility:hidden` and has no pointer events.
  6. **Two floating rock sprites** (section 6).
  7. **Layers L1** (hero HUD, caption, scroll hint), **L2** (vision), **L3** (accounting and hotspots) and **L4** (station).
  8. **Progress bar `.prog`:** absolute, centred at bottom 22px, 120×2px, background `rgba(16,41,26,.18)`, radius 2px. Its inner bar is `--lime2` with left origin and `scaleX(progress)`.
- **Every `.layer`:** absolute inset 0, pointer-events none, with children re-enabled (`pointer-events:auto`).

## 5. Video frame cache and canvas scrubbing

The clip has only a couple of keyframes, so it is never seeked live. It plays once on load while every frame is cached as a JPEG blob, and the canvas then draws cached frames by scroll position.

- **Constants and state:** `FPS=24`. When the video reaches `loadeddata` (or immediately if `readyState>=2`):
  - `NF=max(2, round(duration*24))`, which is 121 here; `frames=new Array(NF)`.
  - An offscreen grab canvas of 1600×900.
- **Frame 0 first:** draw the video into the grab canvas immediately and `toBlob` it as `image/jpeg` quality .9 into `frames[0]`, then call drawWant. Playback callbacks can skip frame 0, and the hero hand-off depends on it.
- **With `requestVideoFrameCallback`:**
  - On each callback compute `i=min(NF-1, round(mediaTime*24))`.
  - If `i>0` and that frame isn't cached, draw the video into the grab canvas and store a JPEG blob at quality .86. If `i` is the wanted frame, call drawWant.
  - Re-register until the video ends. Start with `play()`.
- **Fallback (no rVFC):** step `currentTime=min(i/24, duration-.01)` for i=0…NF-1. On each `seeked`, grab the frame the same way and advance.
- **Canvas size:** the backing store is `canvas.clientWidth × canvas.clientHeight × min(devicePixelRatio, 1.5)`, recomputed on resize. This matches the canvas's CSS box exactly so the frame isn't stretched.
- **drawWant():**
  - If not busy, find the nearest cached frame to `want`, searching outward ±k.
  - If it differs from the one shown, `createImageBitmap(blob)` and draw it cover-fitted and centred into the canvas, using `max(cw/bw, ch/bh)` as the scale.
  - Record `shown`, close the bitmap, and repeat if the target has changed.
- **Expose** `window.__hero = { ready: () => cached >= NF-2, settled: () => !busy && nearest(want)===shown }` (used only by the recording script; omit it from the standalone).

## 6. Floating rock sprites

Each rock is cropped from the sprite sheet (asset 4) using a crop rectangle in the sheet's 1200×678 frame.

- **Markup:** `.rock` is `position:absolute; overflow:hidden`, with an inner `.bob` (absolute inset 0) holding an `<img>`.
- **Crop maths:** for a crop `x,y,w,h`, the img is absolute with `max-width:none`, width `1200/w*100%`, left `-x/w*100%` and top `-y/h*100%`.
- **Rock 1 `.rk1`:** left 4%, top 13%, width 7.5vw, aspect-ratio 260/295; crop `30,200,260,295`; data x -.3, y -.6, depth 1.3.
- **Rock 3 `.rk3`:** left 80%, top 58%, width 14vw, aspect-ratio 265/270; crop `895,240,265,270`; data x 1, y .55, depth 1.8.
- **Bob animation:** `.bob` runs "bob" 7 s ease-in-out infinite alternate, from `translateY(-1.2%) rotate(-1.2deg)` to `translateY(1.6%) rotate(1.4deg)`. Rock 1 uses 6 s; rock 3 uses 8.5 s with a -3 s delay.
- **Fly past (per frame):**
  - `fp=seg(sp, .02, .2)`, `fe=fp²`.
  - Transform: `translate3d(x*fp*70 + sx*-24*d vw, y*fp*60 + sy*-16*d vh, 0) scale(1+fe*1.6*d)`.
  - Filter: `blur(fe*5*d px)`.
  - Hidden once fp reaches 1.

## 7. Hero (L0 and L1)

- **Headline block `.hero-copy`** (in L0): absolute, left and right 0, centred text.
  - A chip "Planet intelligence".
  - An `h1` holding one masked line "Measure the Living Planet".
    - h1 style: Inter Tight 500, line-height .92, letter-spacing -.045em, margin-top 18px, colour ink.
    - The line wrapper is `display:block; overflow:hidden; padding-bottom:.06em; white-space:nowrap`.
    - The inner span starts at `translateY(105%)` and animates "rise" to none over 1.1 s with `cubic-bezier(.2,.8,.2,1)`.
- **Placement (JS layoutHero; runs on load, on resize and after `document.fonts.ready`).** The island's fern tips must sit on the lower half of the letters at any viewport shape:
  1. `bw=W*1.06`, `bh=H*1.12`, `k=max(bw/1600, bh/900)`.
  2. `fernTop = -.09H + (bh - 900k)/2 + 245k + .06H` (fern tips are at y=245 in the 1600×900 frame, and the resting camera sits .06H lower).
  3. Font size `fs=min(104, 72k)` px. If the line is wider than 86% of the viewport, scale fs down to fit.
  4. Block top = `fernTop + .5*fs - blockHeight`.
  - Below 821px wide, clear these inline values, allow the line to wrap, and fall back to the CSS (top 12.5vh, size `clamp(44px,6vw,96px)`).
- **HUD** (in L1): absolute at left 53.5%, top 62%, sitting on the island.
  - A white 22px crosshair (two 1px lines) 44px to its left, at top 4px.
  - A chip "Biodiversity".
  - A `pre` in mono 11px, letter-spacing .12em, line-height 1.65, white with `text-shadow 0 1px 6px rgba(0,0,0,.35)`, margin-top 12px, reading `LAT  34.0922° N` / `LON 116.2432° W` / `ELEV 842 M`.
  - A thin corner-bracket frame around it: a 1px `rgba(255,255,255,.55)` border, offset -8px left and top, -14px right and -10px bottom, clip-pathed so only 14px corner ticks show.
- **Caption** (bottom-left, left and bottom 34px): 16px left padding with a 2px lime left border; mono 11.5px, line-height 1.75, letter-spacing .13em, uppercase, colour ink2. Text: "Real-time ecosystem insights. / Powered by science, blockchain, / and transparent data."
- **Scroll hint** (right 34px, bottom 36px): mono 11px, letter-spacing .16em, ink2, "SCROLL TO EXPLORE". It follows a 20px circle (1.3px border) holding a small chevron that nudges 2px down and back every 1.6 s.

## 8. Fog bank

This keeps the sky behind the left-hand copy clean by covering the distant left island.

- **Box:** absolute at left -8vw, top -6vh, 56vw × 60vh; hidden until needed.
- **Mask:** `radial-gradient(ellipse 52% 48% at 46% 46%, #000 44%, rgba(0,0,0,.7) 64%, transparent 100%)` (with a `-webkit-` prefix).
- **Three stacked layers:**
  - **f0:** `radial-gradient(60% 55% at 40% 45%, #d9dddd, #cfd4d4 60%, #c9cfcf)` with blur 10px. These are the sky's own sampled greys.
  - **f1:** inset -20%. An SVG data-URI fractal-noise texture (700×460, feTurbulence fractalNoise, baseFrequency `0.006 0.014`, 3 octaves, seed 4). A colour matrix maps it to grey `.74/.78/.79`, with alpha `1.4·R - .7`. Opacity .55, blur 14px. Animated "fogA" 26 s alternate to `translate3d(6%,3%,0) scale(1.08)`.
  - **f2:** inset -20%. The same kind of noise (baseFrequency `0.004 0.009`, 4 octaves, seed 11), mapped to light grey `.9/.92/.92` with alpha `1.6·R - .55`. Opacity .9, blur 8px. Animated "fogB" 19 s alternate to `translate3d(-7%,-2%,0) scale(1.12)`.
- **Per frame:**
  - `fg=ease(seg(sp, .38, .47))`, used for visibility and opacity.
  - Transform: `translate3d((fg-1)*18 + sx*-10 vw, sy*-6 px, 0)`, so it rolls in from the left.

## 9. Vision (L2)

- **Block:** centred at 50%/50% (translate -50%,-50%), width `min(820px,90vw)`, white, centred text.
- **Contents:**
  - A chip "Our vision".
  - An h2 with each word in its own inline-block span: "From Data Chaos to" / "Science-Backed," / "Actionable Insights" (line breaks after "to" and after "Science-Backed,").
    - h2 style: Inter Tight 500, `clamp(34px,4.6vw,70px)`, line-height 1, letter-spacing -.04em, margin 18px 0 20px.
    - Shadows: `0 2px 40px rgba(10,30,15,.55)` and `0 1px 3px rgba(10,30,15,.3)`.
  - A 16px paragraph (line-height 1.45, shadow `0 1px 14px rgba(10,30,15,.7)`): "A breakthrough in environmental measurement, / built for commercial use."
- **Per frame:**
  - `vIn=seg(sp,.16,.27)`, `vOut=seg(sp,.34,.42)`.
  - Each word i gets `k=clamp(vIn*1.6 - i*.08)`:
    - transform `translate3d(0, (1-k)*30 - vOut*60 px, 0)`
    - blur `(1-k)*12 + vOut*14 px`
    - opacity `k*(1-vOut)`
  - The chip and paragraph get opacity `clamp(vIn*2-.6)*(1-vOut)` and lift `-vOut*50px`.

## 10. Accounting and hotspots (L3)

- **Paragraph `.acct`:**
  - Position: left 34px, top 14vh, width `min(560px,86vw)`.
  - Type: ink, `clamp(20px,1.9vw,29px)`, line-height 1.16, letter-spacing -.02em, with a soft white halo `text-shadow:0 0 24px rgba(255,255,255,.8)`.
  - Text, split into word spans: "Our ecosystem-level accounting translates complex field science into verifiable, compliance-ready metrics — so you can drive measurable results, not just reports."
- **Four hotspots** (positions are relative to the stage):
  - left 12%, top 58%: "Soil carbon", value "+3.8 t/ha"
  - left 33%, top 41%: "Canopy moisture", value "71 % RH"
  - left 70%, top 66%: "Species index", value "214 taxa"
  - left 83%, top 47%: "Microclimate", value "14.2 °C"
- **Hotspot anatomy:**
  - **Dot:** 22px lime circle with a centred ink plus (two 10×1.4px bars). It pings with a box-shadow every 2.4 s: 0 → 14px transparent at 70%.
  - **Label:** a glass pill in mono 10.5px, letter-spacing .14em, uppercase, ink; padding 6px 9px, radius 4px, background `rgba(246,248,245,.72)`, backdrop blur 8px.
  - **Value:** sits in a hidden `em` (colour `#4f8a12`, max-height 0). It expands to 20px on hover or when the hotspot has the `.on` class (.45s).
  - **Interaction:** clicking toggles `.on` (one at a time). On hover the dot scales 1.15.
- **Per frame:**
  - `aIn=seg(sp,.45,.55)`, `aOut=seg(sp,.63,.68)`.
  - Word i of the paragraph gets `k=clamp(aIn*2.2 - i/count*1.2)`: opacity `(.15+.85k)*(1-aOut)`, blur `(1-k)*6 + aOut*10 px`.
  - Hotspot i gets `k=seg(sp, .49+i*.02, .53+i*.02)`: transform `translate3d(sx*-30px, sy*-20px, 0) scale(k*(1-aOut))`.

## 11. Station (L4)

- **Heading `.cred`:**
  - Position: left 34px, top 13vh, max-width 380px.
  - Type: ink, `clamp(22px,2vw,30px)`, line-height 1.08, letter-spacing -.025em, white halo shadow.
  - Above it, a lime mono label on its own line (`display:flex; width:max-content`, 10.5px, padding 4px 8px, radius 3px): "✕ Field station 07".
  - Heading text: "Scientific credibility for corporate climate action".
- **Carbon card:**
  - Box: left 38%, top 38vh, 250px wide, padding 18px, radius 10px, background `rgba(40,58,44,.32)`, border `1px rgba(255,255,255,.22)`, `backdrop-filter: blur(16px) saturate(1.2)`, white text.
  - Contents, top to bottom:
    - h4 "Accumulated carbon / balance" (15px, 500).
    - Mono 9.5px note at opacity .7: "Plot 07 · 12 months".
    - Big number (46px, 500, -.04em) counting 0 → 24, followed by a mono 10px "tCO₂e".
    - A lime tag "+2.6 tCO₂e" absolutely placed at right 16px, top 96px.
    - A 220×70 SVG sparkline: a lime 1.6px polyline `0,60 30,55 60,57 90,44 120,46 150,30 180,24 214,10`, white 2.4px dots at (90,44) and (150,30), and a lime 3.4px dot at (214,10).
    - A mono footer "Q1 · Q2 · Q3 · Q4".
- **Feature list `.feats`:**
  - Box: right 34px, top 30vh, width `min(400px,36vw)`, padding 6px 16px, radius 10px, background `rgba(246,248,245,.62)`, backdrop blur 14px.
  - Each row is a grid of `30px 1fr 16px` with an 8px gap: index (opacity .6), label, "→".
  - Row type: padding 11px 0, a 1px bottom rule `rgba(16,41,26,.14)` (none on the last row), mono 11px, letter-spacing .12em, uppercase.
  - Rows:
    - 01 Gold-standard observation system
    - 02 World-class atmospheric monitoring (AMRV)
    - 03 Integrated algorithmic processing
    - 04 Blockchain-secured traceability
    - 05 Built for scale and complexity
  - Hover (or `.on` after a click; one at a time): colour `#4f8a12`, 6px extra left padding, and the arrow moves 4px right (.3s).
- **Per frame:**
  - `sIn=seg(sp,.72,.82)`: the heading's opacity, rise of `(1-sIn)*30px` and blur of `(1-sIn)*8px`.
  - `cIn=ease(seg(sp,.74,.86))`: card opacity, and transform `translate3d(sx*-14px, (1-cIn)*60 + sy*-10 px, 0) rotateY(sx*8deg) rotateX(-sy*8deg)`.
  - Number = `round(24*seg(sp,.76,.9))`.
  - The sparkline's dashoffset goes from its full length to 0 over `seg(sp,.77,.92)`.
  - Row i: `k=ease(seg(sp,.76+i*.025,.82+i*.025))`, giving opacity k and transform `translateX((1-k)*40px)`.

## 12. Per-frame scroll controller

One rAF loop drives everything.

- **Helpers:** `seg(p,a,b)=clamp((p-a)/(b-a))`; `ease` is cubic in-out (`t<.5 ? 4t³ : 1-(-2t+2)³/2`).
- **Progress:**
  - Raw `p = clamp(-storyRect.top / (story.offsetHeight - innerHeight))`.
  - Smoothed `sp += (p-sp)*(1-.86^(dt/16.7))`, with dt capped at 64ms. Snap to p when within .0002.
- **Pointer:** `mx,my` = pointer position / viewport - .5. Smoothed `sx,sy` follow at 6% per frame.
- **Video:** `vp=ease(seg(sp,.05,.70))`, `want=round(vp*(NF-1))`, then drawWant.
- **Camera:** both `.cam` and `.camF` get `translate3d(-sx*18px, -sy*12 + (1-vp)*innerHeight*.06 px, 0) scale(1+.02*(1-vp))`.
- **Hand-off (no visible jump):**
  - `ho = shown<0 ? 0 : (shown===0 ? seg(sp,.06,.105) : 1)`.
  - The plate (high-res still) and the front cut-out both get opacity `1-ho` and become hidden at 0.
  - Because the eased scrub keeps the video parked on frame 0 until about sp .115, both high-res layers dissolve into the identical frame 0 while the headline is blurring out. The scrub only starts moving after that.
- **Hero copy:**
  - `h=seg(sp,.02,.1)`.
  - Headline block: transform `translate3d(-sx*10px, -h*80 - sy*6 px, 0) scale(1+h*.12)`, blur `h*14px`, opacity `1-h`.
  - HUD: `translate3d(sx*26px, sy*18 - h*40 px, 0)`, opacity `1-seg(sp,.02,.08)`.
  - Caption and hint: opacity `1-seg(sp,.01,.05)`.
  - L0 and L1 hide when h reaches 1.
- **Other layers:** set `visibility` hidden whenever their computed amount is 0.
- **Progress bar:** `scaleX(sp)`.

## 13. Solutions section

- **Panel `#sol`:**
  - position relative, z-index 5, margin-top **-30vh** (it slides up over the end of the pinned stage).
  - White background, radius 22px 22px 0 0, padding 70px 34px 90px, shadow `0 -30px 60px rgba(16,41,26,.12)`.
- **Head:** a flex row (space-between, aligned to the bottom, 40px gap, wraps).
  - Left: a chip "Our solutions" and an h2 "Validating what the ecosystem does naturally" (Inter Tight 500, `clamp(34px,3.9vw,58px)`, line-height 1, -.04em, max-width 640px, margin-top 20px).
  - Right: a 15px paragraph (max-width 360px, colour `#4a5a4f`): "Field sensors, atmospheric flux towers and satellite data fused into one auditable record — so every tonne you report can be traced back to the ground it came from."
- **Cards:** a three-column grid (14px gap, margin-top 54px), each card 440px tall, radius 12px, overflow hidden, base `#1b3122`, white text.
  - **Background:** an image div with `background-size:cover` that scales 1.07 on hover (1.2 s, `cubic-bezier(.2,.8,.2,1)`).
  - **Overlay:** `linear-gradient(180deg, rgba(10,25,15,.45), transparent 35%, transparent 55%, rgba(10,25,15,.75))`.
  - **Top row** (18px insets): a mono bracket label, and a 28px lime circle with "→" that rotates -45deg on hover.
  - **Bottom:** an h3 (25px, 500, -.03em, line-height 1.05) and a 13.5px paragraph hidden at max-height 0 that opens to 80px on hover (.6s).
  - **Tilt:** on pointermove each card gets `perspective(1000px) rotateY(x*6deg) rotateX(-y*6deg)`, where x and y are the pointer position in the card minus .5. Reset on leave.
  - **Card 1:** asset 5 at `background-position:22% 70%; background-size:260%`. Label "[Nature-based solutions]". Title "Forest & peatland / carbon projects". Body: "Continuous flux measurement replaces sampled estimates, so credits reflect what the land actually absorbs."
  - **Card 2:** asset 6 at `50% 50%`, size 190%. Label "[Supply chain solutions]". Title "Scope 3 sourcing / verification". Body: "Trace commodities to the plots that grew them, with deforestation-free evidence attached to every shipment."
  - **Card 3:** asset 5 at `62% 30%`, size 230%. Label "[Biodiversity credits]". Title "Living species / baselines". Body: "Acoustic and eDNA monitoring builds a measurable biodiversity baseline you can report against year over year."
- **Stats:** a four-column grid, margin-top 60px, top rule `1px #e0e5e0`, each cell padded 22px on top.
  - Numbers: 44px, 500, -.04em. Labels: mono 10.5px, .14em, uppercase, `#6a7a6f`.
  - Values: 1240 "Sensors deployed" (shown with a thousands comma), 38 "Countries monitored", 2.1 "Mt CO₂e verified" (1 decimal), 99.4 "% Data uptime" (1 decimal).
  - The first time the panel's top passes 60% of the viewport height, all four count up from 0 over 1.6 s with the cubic in-out ease.

## 14. Responsive (≤820px)

- Nav padding becomes 16px 18px; the menu is hidden.
- Rock widths: rk1 16vw; rk3 30vw at top 70%.
- The headline wraps.
- HUD moves to 50%/66%. Caption sits at left and right 18px, bottom 70px. Hint at right 18px, bottom 24px.
- Station:
  - Heading at left 18px, top 11vh, max-width 80vw.
  - Card at left 18px, bottom 6vh, 210px wide.
  - Feature list at right 18px, bottom 6vh, 45vw wide, 9.5px text, arrows hidden.
- Solutions: padding 50px 18px 70px, one-column cards 340px tall, two-column stats.
