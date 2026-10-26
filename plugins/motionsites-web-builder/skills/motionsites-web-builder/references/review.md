# Look-and-fix review

You cannot judge a page you have not seen. After every build, run:

```bash
python scripts/shoot.py index.html shots/
```

Open `shots/desktop.png`, `shots/mobile.png` and `shots/desktop-early.png` and look at them properly, as images. Read the QA report too. Then score the page against the rubric below, honestly, as a jury member who has seen a thousand landing pages this year.

If the screenshot tool is unavailable, use whatever browser or preview tool you have. If you truly have none, say so, review the code line by line against this rubric, and tell the user the page was not visually checked.

## Fix immediately (blocking)
Any of these makes the page fail, whatever else is good:
- Console errors, failed requests, broken images, or a video that should play but doesn't (the QA report lists them).
- Horizontal overflow on mobile (`horizontalOverflow: true`).
- A white or blank flash in `desktop-early.png` on a dark design (set the background colour on `html` and `body` in the first CSS rule).
- Text you can't read: over a busy part of an image/video, under ~4.5:1 contrast for body text, or clipped.
- Fonts not loaded (`fontsLoaded` missing the display font) or the H1 falling back to a system font.
- Layout broken at either size: overlapping elements that shouldn't overlap, a nav wrapping onto two lines, a hero taller than the viewport hiding the CTA on desktop.
- Placeholder or filler copy ("Lorem", "Your tagline here", "Feature 1").

## Score 1–10 on each
1. **First glance (the 3-second test).** One clear focal point. You know what it is and where to look. It feels intentional, like a studio made it, not a template.
2. **Signature.** Is there one memorable thing (the media, an interaction, a type moment) that someone would screenshot and share? Average pages have none.
3. **Typography.** Display type is big, confident and tightly tracked; body is calm and readable; at most 2 families; consistent scale; nothing default-looking.
4. **Composition and space.** Generous, deliberate negative space; aligned edges; the eye travels hero → message → CTA. No clutter, no orphaned elements, no equal-weight everything.
5. **Colour and light.** A small palette with one accent used with intent; text protected over media (gradients/scrims); depth from light, blur or grain rather than random decoration.
6. **Media integration.** The image/video/3D feels like part of the design (cropped, positioned and layered on purpose), not a rectangle dropped in.
7. **Motion (judge from code + early/late frames).** Entrance is choreographed (staggered, 0.6–1.2s total, ease-out), interactions feel physical, nothing loops distractingly, reduced motion respected.
8. **Mobile.** Not just "stacked": type rescaled, media re-cropped, tap targets ≥ 44px, still has the signature.
9. **Copy.** Specific, short, believable for this brand; a headline with a point of view; CTA with a verb.
10. **Polish.** Hover/focus states, consistent radii and borders, favicon/title, no stray scrollbars, no layout shift as fonts/media load.

**The bar is an average of 8 or more with no score under 7.** Most first drafts land at 6–7. That's normal; the fixes are what make it great.

## Fix loop
1. Write down the three weakest scores and, for each, the specific change (values, not adjectives): "H1 from 64px to clamp(56px, 8vw, 128px), tracking -0.04em", "add a 40% black-to-transparent gradient over the bottom of the video", "move the stats row into one line with 1px dividers".
2. Make those changes, then shoot again and look again.
3. Repeat up to 3 rounds, or until you clear the bar. If something can't be fixed (e.g. no suitable media), tell the user plainly what would lift it.

Common high-impact fixes:
- **It looks generic.** Make the type bigger, cut words, strengthen the signature, remove a section or element.
- **It looks busy.** Remove decorative elements, unify radii, increase spacing by one step, reduce the colours to bg/ink/muted/accent.
- **It looks flat.** Add depth with a media layer, gradient scrim, subtle grain, glass surfaces, or light falloff.
- **The text fights the video.** Reposition the text over the calm area, add a scrim, or choose a calmer clip.
- **Mobile looks broken.** Re-crop media with `object-position`, scale display type with `clamp()`, hide secondary nav behind a menu.
