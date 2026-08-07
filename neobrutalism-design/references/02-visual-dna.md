# Visual DNA

Source section: [02 — Visual DNA: The Anatomy of Neubrutalism](https://neubrutalism.com/#anatomy)

Neubrutalism is a repeatable visual grammar rather than a single fixed appearance. Its identity comes from a compact set of color, geometry, depth, typography, and layout parameters.

## Color theory

Use color categorically rather than atmospherically: each fill defines an obvious, discrete surface. Flat, memorable blocks should make the composition feel assembled from separate physical pieces. Start with a black-and-white structural foundation and one to three saturated accents. Avoid gradients as the default grammar.

### Canonical palette

| Portable token | Value | Intended role |
|---|---:|---|
| `color.structure-dark` | `#000000` | Outlines, text, structural contrast |
| `color.base-light` | `#FFFDF5` | Warm neutral background |
| `color.accent-yellow` | `#FFD23F` | Bold yellow accent |
| `color.accent-coral` | `#FF6B6B` | Coral-pink accent |
| `color.accent-blue` | `#74B9FF` | Sky-blue accent |
| `color.accent-green` | `#88D498` | Soft-green accent |
| `color.accent-orange` | `#FFA552` | Orange accent |
| `color.accent-lavender` | `#B8A9FA` | Lavender accent |

Treat these values as a source palette, not a mandatory brand palette. Preserve the relationship of neutral base, structural dark, and limited accents when adapting it.

### Do

- Keep the palette structurally simple even when its colors are forceful.
- Combine one neutral base, one dark outline color, and a limited accent set.
- Maintain at least `4.5:1` contrast for ordinary body text under WCAG 2.2 AA.
- Use fills to distinguish surfaces as immediately recognizable objects.

### Do not

- Introduce gradients as a routine atmospheric effect.
- Give every component maximum saturation and equal visual intensity.
- Assume a loud combination is accessible; yellow against white is a source example of a likely contrast failure.
- Use color as the only carrier of state or meaning.

## Geometry and borders

Use heavy outlines as the primary geometric signature. Cards, controls, fields, and illustrations should feel stamped, boxed, or screen-printed. Borders serve brand identity and structural clarity.

| Corner parameter | Typical reading |
|---|---|
| `12` relative units | Conventional soft surface |
| Fully rounded | Pill surface |
| `0` | Canonical neubrutalist surface |

Prefer square or near-square corners. Define one canonical stroke-width token for most components, with the source baseline at `2–3` relative units. Deviate only to communicate hierarchy. The outline must clarify an object without overpowering its content.

## Shadows and depth

Create intentionally anti-naturalistic depth. Use opaque offset shapes with zero or near-zero blur so surfaces appear stacked, shifted, or slightly misregistered like print layers rather than realistically lit objects.

Represent depth portably as `(horizontal offset, vertical offset, blur, spread, color)`.

| Treatment | Portable parameters | Effect |
|---|---|---|
| None | No shadow | Flat surface |
| Conventional soft depth | `(0, 4, 12, 0, dark at 15% opacity)` | Diffuse, naturalistic elevation; comparison only |
| Hard offset | `(5, 5, 0, 0, #000000)` | Canonical neubrutalist depth |
| Large hard offset | `(10, 10, 0, 0, #000000)` | Exaggerated separation |

### Three-tier system

| Token | Portable parameters | Intended hierarchy |
|---|---|---|
| `shadow.small` | `(3, 3, 0, 0, #000000)` | Badges, chips, inline actions |
| `shadow.medium` | `(5, 5, 0, 0, #000000)` | Cards, buttons, panels |
| `shadow.large` | `(8, 8, 0, 0, #000000)` | Overlays, heroes, major focus |

Scale shadow size with prominence and depth. Applying the same aggressive shadow to every object erases hierarchy.

## Typography

Create assertive contrast with oversized sans-serif display text, abrupt scale changes, and occasional tension. Pair expressive display typography with restrained operational text.

| Role | Source specimen | Portable principle |
|---|---|---|
| Display | Syne 800 | Oversized, declarative, attention-dominating |
| Heading | Space Grotesk 700 | Strong structural voice below display intensity |
| Body | Inter 400 | Calm, readable, predictable |
| Monospace | Space Mono 400 | Mechanical or structural annotation |

The named families are examples of roles, not requirements. Use a high-weight grotesque or display sans for major statements, a bold legible sans for headings, a neutral utility sans for sustained reading, and an optional monospace family for metadata or engineered accents.

### Do

- Use an impactful grotesque or display sans for headlines, with high weight and tight tracking.
- Use a highly legible utility sans for body text, with generous line height.
- Reserve extreme treatment for headlines, heroes, and calls to action.
- Build contrast through size and weight rather than novelty letterforms.

### Do not

- Make every role shout at the same intensity.
- Depend on ornate or decorative faces.
- Reduce body readability to make all roles aesthetically uniform.
- Neglect line height or spacing in pursuit of impact.

## Layout

Start with an underlying grid, then disrupt it selectively through offsets, asymmetric spacing, overlaps, rotation, and oversized modules. The governing principle is **broken, but not random**.

### Structured disruption

Keep navigation and primary reading flows predictable. Create energy through local breaks such as offset cards, overlapping panels, and rotated elements. Expressive composition is usually more tolerable than expressive interaction, so frame the core experience without making controls harder to understand.

### Macro versus micro

Apply asymmetry to heroes, card stacks, illustrations, and other macro compositions. Keep labels, fields, buttons, error states, and other micro mechanics aligned. Disruption becomes sabotage once it interferes with comprehension.

### Layout rules

- Preserve an underlying grid even when selected modules break from it.
- Keep scan paths, grouping logic, and reading order intact.
- Concentrate asymmetry in large compositional gestures.
- Keep detailed interface mechanics consistently aligned.
- Make the composition feel slightly misbehaved while remaining fully legible and navigable.

## Source

- [Neubrutalism.com — Visual DNA](https://neubrutalism.com/#anatomy)
