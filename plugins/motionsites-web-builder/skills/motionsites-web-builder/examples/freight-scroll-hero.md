<!-- Freight Scroll Hero · Logistics · free MotionSites prompt -->
<!-- Preview: https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20261023_072356_6829b75c-8dc0-44bf-9593-73f508f599d7.png&w=1280&q=85 · Source: https://motionsites.ai/?prompt=freight-scroll-hero -->

# Prompt: freight scroll hero ("Logistics that works as hard as you do.")

Build a single-file **scroll-driven logistics hero** in plain HTML, CSS and vanilla JS, with no framework and no build step. A sticky, full-viewport top-down aerial video sits behind the content. Scrolling scrubs a continuous camera climb: it starts close over a red-and-white container freight train crossing black coal terrain, rises higher and higher as mist drifts across, and ends inside soft white cloud. Over it the content scrolls up normally: first only the scene, then a big 4-line headline rising up the train's axis, then a mirrored features block, and then the clouds take over and fade into a plain text testimonial section.

## Media

- **Pull-up clip:** one clip, 1920×1080, 24 fps, 5.04 s, no audio. Encoded with a keyframe every 4 frames so it seeks instantly.
  - **1080p:** https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/e02bb27f-80d8-445f-a03e-1b609dac4261.mp4
  - **720p** (for screens ≤ 900px or Save-Data): https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/e8eb434f-d097-4b1b-b9e6-c8b46fa43040.mp4
- **Poster:** the clip's first frame, https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/5e018553-cb8a-420a-819f-fcdfa08e5df0.jpg
- **Clip content:**
  - 0–2.3 s: the camera climbs over the train, which stays on the vertical centre line, with wisps of mist.
  - From about 2.3 s: white clouds slide in from the edges.
  - Last frame: almost all white/grey cloud.
- **Rule:** the video is never played, looped or faded. It is only scrubbed (`currentTime`). Nothing in the scene is drawn or animated in code.

## Type and colour

- **Headline:** Exo 2 ExtraBold 800, uppercase.
- **UI text:** Public Sans 700 for titles and the eyebrow, 400 for body.
- **Colours:**
  - cream `#F7F5EF` (headline, eyebrow)
  - white `#F9F9F9` (titles, icons)
  - body text white at 88%
  - page and track `#0a0b0c`
  - body background after the track `#e2dedd` (cloud grey)
- **Shadows:** soft text shadows on all type, for example a headline shadow of 0 12u 32u black at 50%.

## Scale and structure

- **Unit:** the design is drawn on a 1280×800 frame. `u = min(100vh/800, 100vw/716)`. 800 design px equals one viewport height, so vertical positions are written as `N/8 vh`.
- **Track:** `.track` (relative, height set by JS). Inside it:
  - `.scene`: `position:sticky; top:0; height:100vh` (100lvh). It holds the `<video>` (object-fit cover), and a very light top/bottom tint (black at 2–12%).
  - `.content`: an absolute layer the full height of the track, holding the scrolling blocks.

## Scrolling blocks (desktop, positions from the top of the track)

- **Intro, top 940/8 vh** (enters after 140 design px of scroll). Centred, 1280u wide:
  - eyebrow "WHY US": 7.4u, tracking .304em
  - headline "LOGISTICS / THAT WORKS / AS HARD AS / YOU DO.": 56u on a 62u line, one span per line, nowrap
- **Features:** each block is 300u wide. Each has:
  - a 34u white icon, 30u above the title, sitting on the inner side near the axis
  - an uppercase title, 19.6u on a 20u line, two lines
  - a body of 12.3u on a 15.4u line, three lines
- **Rows:**

  | Row | Top | Left column | Right column |
  |---|---|---|---|
  | 1 | 1500/8 vh | right-aligned, right edge 78u left of the axis | left-aligned, 78u right of it |
  | 2 | 1759/8 vh | right-aligned, 88u left of the axis | left-aligned, 88u right of it |
  | 3 | 2063/8 vh | the fifth block, centred | |

  1. **One point of contact** (dotted ring around a white globe): "No more chasing multiple vendors. One / team manages your entire end-to-end flow, / origin to destination."
  2. **Full supply chain visibility** (three stepped container blocks): "Track your freight in real time and get / proactive updates before issues become / delays."
  3. **Compliance you can trust** (dotted ring around a white disc with a dark check): "Licensed customs brokers keep your / shipments moving within every regulatory / requirement, border to border."
  4. **Competitive, transparent pricing** (bold "$" stroke): "No hidden fees. Clear, competitive pricing / backed by responsive sales support / throughout the shipment."
  5. **Fast issue resolution** (double chevron): "When something unexpected happens, we / do not point fingers, we solve it. Our team / acts at once to protect your timeline."

## Scroll → clip mapping (JS)

- **Track length:** `end = lastBlock.bottom + 0.75 × viewport`, and track height = `end + viewport`.
- **Progress:** `p = clamp((scrollY − track.top) / end)`.
- **Two-part mapping:** `knee = lastBlock.bottom / end`.
  - While `p < knee`, clip progress = `p / knee × 0.46`, so the camera only climbs over the train while text is on screen.
  - After that, it runs from 0.46 to 1, so the clouds take over once the last block has left.
- **Time:** target time = progress × (duration − 1/48).
- **Smoothing:** each frame, `cur += (target − cur) × 0.22`. Set `currentTime` only when the video isn't already seeking and the difference is more than 1/60 s, and re-seek on `seeked`.
- **Recorder mode (`?rec=1`):** a 6.5 s Web Animation drives the progress: hold to 3%, one even ease (cubic-bezier .45,.05,.55,.95) to 94%, then hold. It runs past the end of the track by 0.9 viewport so the testimonial section scrolls in. `window.__recTime(video, t)` scrolls the page to that progress and returns the matching clip time, so a frame-by-frame recorder is deterministic.

## After the clouds: testimonial section (text only)

- **Placement:** a `<section class="trust">` right after the track, pulled up 34vh over the end of the sticky scene. It starts with a 34vh gradient from transparent to `#e2dedd`, so the white clouds run straight into the page. Ink `#141516`.
- **Container:** max 1120px wide, centred, 64px side gutters, 140px bottom padding.
- **Header:** a two-column grid (1fr and 300px).
  - Left: "TRUSTED / BY BUSINESSES / ACROSS THE REGION" in Display 800 at clamp(34px, 4.4vw, 60px), line-height 1. The last line is grey `#8f8b8a`.
  - Right: a 13px note at 70% ink: "From first-time importers to high-volume shippers, our customers stay because every consignment is treated like it matters."
  - A 1px rule (ink at 16%) under the header.
- **Quotes:** three rows, each a grid of 260px and 1fr, 44px vertical padding, with a 1px rule under each. No photos.
  - Left: the name in 13px bold uppercase, the role in 12px at 60% ink.
  - Right: the quote in UI 400 at clamp(17px, 1.6vw, 21px), line-height 1.42, max 680px.
  - Thomas Reid, Director, Harbour Fit Group: "My business would not function without this team. They treat every consignment on its own merits, and our account managers know our business well enough to answer before we ask. We have never had that from a bigger carrier."
  - Ana Park, Supply Chain Lead, Northline Projects: "As a first-time shipper on a major infrastructure job, we were in unfamiliar territory. They planned the whole route with us, flagged every risk early, and our first delivery reached site on the day they promised."
  - Liam Carter, Operations Manager, Coastline Foods: "One contact, one dashboard, no surprises. When a vessel slipped two days, we heard about it before our customers did, and the new plan was already in place."
- **Portrait:** the header and each quote stack to one column (18px and 14px gaps), 22px side gutters.

## Portrait (≤ 609px wide, or any portrait aspect)

- **Unit:** `u = min(100vw/390, 1.6px)`.
- **Content:** one centred column with 112vh top padding:
  - headline at clamp(34px, 46u, 72px)
  - each feature centred with its icon above, the first 24vh below the headline, then 16vh apart
  - title lines and body lines flow inline
- **Overflow:** no sideways scroll.

## Acceptance check (1440×960)

- **On load:** only the train close-up.
- **Headline:** rises up the train's axis and exits the top.
- **Features:** the 2×2 block and the centred fifth block scroll through, mirrored across the train, while the camera climbs.
- **End:** once the last block has gone, clouds roll in, the frame ends in white cloud, and the testimonial section rises out of it.
- **Scrubbing:** scrolling back reverses everything smoothly.
- **Content:** no real brands or logos.
