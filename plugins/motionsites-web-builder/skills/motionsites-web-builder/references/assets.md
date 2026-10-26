# Media: sourcing, generating, preparing

Great pages are carried by their media. Choose it before you design the layout around it.

## Order of preference
1. **The user's assets.** Ask once if the brief clearly needs them (a product photo, footage, a logo). Otherwise don't block on it.
2. **Generate them** if you have an image or video generation tool. Use the formulas below.
3. **The media shelf** (`media/MEDIA.md` + `media/sheet-*.jpg`):
   - Open the contact sheets, look at them, and pick by eye. Match:
     - the **edge colour** to your intended page background;
     - the **subject position** to the side opposite your text;
     - the **palette** to the brand;
     - the **motion type** (ambient loop vs. something you'll scrub).
   - Use the URL exactly as listed.
   - Skip anything showing recognisable characters, celebrities, logos or brands.
   - "Site preview" entries are screenshots of finished designs. Use them only as project thumbnails in a portfolio grid, never as a hero background.
   - Tell the user which shelf items you used and that they're stand-ins they may want to replace.
4. **No media.** Build a type-led hero, for example:
   - mega word at 14–28vw with mono labels;
   - monochrome + grain + one soft directional light falloff (≤8% alpha, static);
   - a dot grid at 5%;
   - a large inline-SVG mark.

   Never use grey placeholder boxes, random stock photos or lorem-picsum.

**Before you rely on any URL,** check it's alive (a quick ranged GET, or the QA report from `scripts/shoot.py`). Never invent URLs or file paths you don't have.

## What makes hero media work
- **One subject, one continuous shot, no cuts.** Slow motion: gentle orbit, drift, float, turn in place, a slow push-in. Nothing enters or leaves the frame.
- **Loopable:** the end matches the start, or the loop is masked with a fade, boomerang or crossfade.
- **Edges fall off to one flat colour** that becomes the page background, so no seams and no overlay are needed.
- **A defined empty zone** (left half, top 35–40%, or bottom band) where the copy sits for the entire loop.
- **A restrained palette:** 2–3 hues, plus one luminous highlight (rim light, glow, sunset band) against a dark or neutral field.
- **A cinematic grade:** 24fps, soft volumetric light, shallow depth of field. Often a CGI render or illustration rather than stock photography.
- **No text, logos, UI or watermark** inside the footage.
- **Paired stills** (spotlight reveal, parallax layers) must be pixel-aligned: the same composition in two materials or separated layers.

**Archetypes that work:**
- an isolated object in a seamless void (glass, chrome, silk, a floating island);
- a stylised 3D character on a saturated flat backdrop;
- a painterly landscape with a low horizon and a tiny figure;
- a surreal minimal scene (a silhouette walking toward a glowing portal);
- a studio product or fashion shot on white seamless;
- photoreal nature b-roll as switchable moods;
- abstract terrain with a single rim glow.

## Placing media
- **Background video:** `position:absolute; inset:0; width:100%; height:100%; object-fit:cover` with `autoplay muted loop playsinline preload="auto"`. Give it a `poster` when you have one.
- **Focal control:** use `object-position` (e.g. `70% center`), oversize to 110–120% (top-aligned), or translate offsets, so the subject lands away from the text.
- **Mobile:** re-aim `object-position`, or move the media below the text in a square or 4:5 frame.
- **Cut-outs:** `object-fit: contain; object-position: bottom`, sized by viewport height. Use `draggable="false"` and `pointer-events: none`, and preload with `new Image()`.
- **Tiles:** a rounded container with `overflow: hidden` and a fixed aspect ratio. On hover, scale 1.05 over 700ms. Use a bottom gradient only where text sits on the tile.
- **HLS (`.m3u8`):** use native playback where `video.canPlayType('application/vnd.apple.mpegurl')` succeeds, otherwise hls.js.
- **Decorative media** gets `alt=""` / `aria-hidden="true"`. Meaningful images get real alt text.

## Generating media (when you have a generation tool)
**Workflow:**
1. Generate a still keyframe (16:9, 2K+).
2. Animate it image-to-video for 5–10s.
3. Make it loop.
4. Export H.264 MP4 at 1920×1080, 24fps, no audio, ≤8MB, and pull a first-frame poster.

**Still (keyframe) formula:**
```
[shot type] of [ONE subject], [material/finish], [pose/state],
placed in the [right third | lower half | center-bottom], occupying ~30% of frame,
[seamless backdrop | environment] that falls off to pure [#000000 | #FFFFFF | brand hex] at all edges,
[lighting: soft rim light / volumetric haze / single warm key],
palette limited to [2–3 colours], [one luminous highlight],
[style: photoreal CGI render | cinematic 35mm still, shallow DOF | hand-painted anime-film background | high-key studio],
large empty negative space on the [left half | top 40%] reserved for a headline,
no text, no logos, no UI, no watermark, 16:9, ultra-detailed.
```

**Motion (image-to-video) formula:**
```
Single continuous shot, no cuts. Camera: [locked | very slow push-in ~5% | slow 15° orbit].
Subject: [rotates slowly in place | floats gently | grass sways | fabric ripples | light pulses softly].
Nothing enters or leaves frame; background stays flat [colour]; lighting constant.
Slow and calm, ~half real-time. 24 fps, 8–10 seconds, seamless loop: last frame matches first.
```

**Cut-out sets:** generate "full body [subject] isolated on flat [chroma colour], even studio light, 3:4, consistent style across the set", then remove the background, then export WebP with alpha at ≤500KB.

**Checks before using generated media:**
- Look at frames from 0%, 50% and 100%: the text zone must be empty in all three.
- The edges must equal the page background.
- No stray text or artefacts.
- The loop seam must be invisible.

If a check fails, fix it with `object-position` or oversizing, or regenerate. Don't paper over it with a dark overlay.

## Preparing video for the web (ffmpeg)
```bash
# Web MP4: H.264, 1080p, 24fps, no audio, fast start
ffmpeg -i in.mp4 -an -vf "scale=1920:-2,fps=24" -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -movflags +faststart hero.mp4
# Mobile version
ffmpeg -i in.mp4 -an -vf "scale=960:-2,fps=24" -c:v libx264 -preset slow -crf 28 -pix_fmt yuv420p -movflags +faststart hero-mobile.mp4
# Poster (first frame, WebP)
ffmpeg -i hero.mp4 -frames:v 1 -vf "scale=1920:-2" -q:v 80 poster.webp
# Seamless loop: crossfade the last second into the first (for an 8s clip)
ffmpeg -i in.mp4 -filter_complex "[0]split[a][b];[a]trim=1:8,setpts=PTS-STARTPTS[main];[b]trim=0:1,setpts=PTS-STARTPTS[head];[main][head]xfade=transition=fade:duration=1:offset=6[v]" -map "[v]" -an loop.mp4
```
