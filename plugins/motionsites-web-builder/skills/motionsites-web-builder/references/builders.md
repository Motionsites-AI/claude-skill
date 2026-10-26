# Prompts for other builders

When the user wants a prompt to paste into another AI builder, the spec **is** the deliverable. Write it in the same style as the examples: imperative, exact, ordered. Then adapt it for the tool:

| Tool | Stack line to open with | Notes |
|---|---|---|
| **Lovable** | "React + Vite + TypeScript + Tailwind CSS + shadcn/ui, framer-motion for animation, lucide-react for icons." | Put tokens as HSL CSS variables in `index.css` (Lovable's convention). Ask for the full hero in one go; for long pages, "build the hero and next two sections now". |
| **Bolt** | "Vite + React + TypeScript + Tailwind CSS + Framer Motion, single page, no backend." | Bolt follows numbered structure closely: keep sections numbered and the tokens in one block. Ask for one component per file. |
| **v0** | "Next.js App Router + Tailwind + shadcn/ui; framer-motion for animation." | v0 is conservative with motion unless asked; spell out every animation. |
| **Cursor / Claude Code** | The user's existing stack, or "a single index.html, no build step". | Can follow very long specs; include the file structure. |
| **Manus / Kimi / Google AI Studio** | "Build a single standalone index.html (inline CSS and JS, no build step)." | Agentic builders do best with one self-contained file and every asset URL spelled out. |

**Rules for any builder:**
1. **Exact media URLs.** Paste every URL in full, with what it's for and how it's positioned. Builders invent media if you're vague.
2. **Exact copy.** Spell out every headline, nav label and CTA. Left alone, builders write bland copy.
3. **Numbers, not adjectives:** sizes per breakpoint, tracking, durations, easing, opacities.
4. **Constraints last:** finish with "Do not add…" lines, e.g. "No extra sections, no decorative blobs, no placeholder images, no emoji." Builders respect what comes last.
5. **Length:** 3–15k characters is normal for a gallery-grade hero. Don't trim precision to save space.
6. **If the result drifts:** send one focused fix per message ("make the H1 clamp(56px,8vw,120px) with -0.04em tracking"), not a long list.
