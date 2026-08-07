# Portable implementation specification

Source section: [05 — Implementation: Building with Neubrutalism](https://neubrutalism.com/#implementation)

Neubrutalism is straightforward to systematize because its grammar uses discrete primitives: strong strokes, square corners, hard offset shadows, flat fills, and explicit states. Express these as host-native design parameters. The source values below are calibration points; scale them coherently for the target medium and density rather than assuming a universal physical unit.

## Core token system

| Portable token | Source value | Meaning |
|---|---:|---|
| `border.default` | `3` solid units, `#000000` | Primary object boundary |
| `border.thin` | `2` solid units, `#000000` | Secondary boundaries and dividers |
| `border.thick` | `4` solid units, `#000000` | Section dividers and heroes |
| `shadow.small` | offset `(3,3)`, blur `0`, spread `0`, `#000000` | Badges, chips, small controls |
| `shadow.default` | offset `(5,5)`, blur `0`, spread `0`, `#000000` | Cards, buttons, panels |
| `shadow.large` | offset `(8,8)`, blur `0`, spread `0`, `#000000` | Major hover/preview states and overlays |
| `shadow.extra-large` | offset `(12,12)`, blur `0`, spread `0`, `#000000` | Heroes and dialogs |
| `corner.default` | `0` | Square corners |
| `color.base` | `#FFFDF5` | Off-white background |
| `color.accent.yellow` | `#FFD23F` | Primary loud fill |
| `color.accent.coral` | `#FF6B6B` | Accent or error candidate |
| `color.accent.blue` | `#74B9FF` | Information or focus candidate |

Use zero blur for the defining hard-shadow system. Treat the border as the primary structural signifier and color and depth as hierarchy devices. Assign semantic roles only after verifying contrast and non-color state cues; a source swatch is not automatically suitable for success, warning, or error semantics.

## Action control

### Base model

| Parameter | Source baseline |
|---|---:|
| Border | `3` solid units, `#000000` |
| Corner radius | `0` |
| Fill | `#FFD23F` |
| Text | `#000000` |
| Shadow | offset `(5,5)`, zero blur, `#000000` |
| Text weight | `700` |
| Internal space | `12` vertical, `24` horizontal |
| State transition | `100 ms`, eased |

### State model

| State | Position | Shadow | Required cue |
|---|---|---|---|
| Rest | `(0,0)` | `(5,5)` | Flat fill and hard outline |
| Hover or preview | `(-2,-2)` | `(7,7)` | Object lifts away from shadow |
| Active or pressed | `(+3,+3)` | None | Object presses into shadow |
| Keyboard or directional focus | Unchanged | Unchanged | Distinct `3`-unit focus outline offset by `3` units |
| Disabled | No lift or press | Reduced or none | Perceivable unavailable state without relying on opacity or color alone |

Preserve the physical model across input methods: approach or preview lifts; activation compresses. Where hover does not exist, do not invent it; use focus, pressed, or selection behavior native to the platform. Honor reduced-motion preferences by changing non-motion cues instead of translating the object.

### Variants

| Variant | Rest | Hover/preview | Pressed |
|---|---|---|---|
| Default | White surface, black outline and `(5,5)` shadow | Lift `(-2,-2)` and grow shadow to `(7,7)` | Move `(+3,+3)` and remove shadow |
| Primary | Yellow surface, black outline and `(5,5)` shadow | Same lift model | Same press model |
| Inverted | Black surface, light text, coral `(5,5)` shadow | Lift and grow coral shadow | Press and remove shadow |
| Ghost | Transparent surface, black outline, no shadow | Add yellow fill, lift `(-2,-2)`, add `(5,5)` shadow | Define explicitly for the host system; the source demo omits a distinct pressed rule |

## Cards and panels

| Parameter | Source baseline |
|---|---:|
| Fill | `#FFFFFF` |
| Border | `3` solid units, `#000000` |
| Shadow | offset `(5,5)`, zero blur, `#000000` |
| Internal space | `24` units |
| Transition | `150 ms` |
| Interactive hover/preview | position `(-2,-2)`, shadow `(7,7)` |

| Variant | Specification | Intended role |
|---|---|---|
| Standard | White surface, black border, black default shadow | General-purpose workhorse |
| Colored shadow | White surface, colored border and matching shadow | Personality with intact structure |
| Filled | Loud accent fill, black border, large `(8,8)` shadow | Call to action or highlight |

Do not give noninteractive cards hover lift. Make interaction semantics explicit; visual elevation alone must not imply that a container is actionable.

## Form controls

Retain host-native control semantics while applying the visual grammar. Labels, descriptions, errors, required state, selected state, focus, and hit regions remain functional requirements.

### Text, email, selection, and multiline fields

| Parameter | Rest | Focus |
|---|---|---|
| Internal space | `12` vertical, `16` horizontal | Unchanged |
| Fill | `#FFFFFF` | `#FFFFFF` |
| Border | `3` solid units, black | Same |
| Radius | `0` | `0` |
| Shadow | `(3,3)`, zero blur | `(5,5)`, zero blur |
| Position | `(0,0)` | `(-1,-1)` if motion is acceptable |
| Focus indicator | None | Distinct `3`-unit blue outline offset by `2` units |
| Transition | `150 ms` | `150 ms` |

Use a visible label, readable placeholder if present, and persistent error or help text outside the placeholder. Allow multiline input to grow or scroll according to platform convention. Selection controls may map the source's small `(3,3)`, medium `(5,5)`, large `(8,8)`, and extra-large `(12,12)` depth choices into a demonstration or theme control, but normal product fields should use a consistent tier.

### Checkbox

Use a square `24 × 24` source-unit target with a `3`-unit black border, zero radius, and a selected accent fill plus a centered visible checkmark. Use a `3`-unit offset focus outline. Make the full associated label operable where platform convention permits.

### Radio group

Use a mutually exclusive native group. The source uses a square `24 × 24` outer control with a `3`-unit border and a centered `10 × 10` internal mark plus selected fill. A round platform-native indicator is also acceptable if replacing it would reduce recognition. Preserve group naming, arrow-key or directional behavior, and a visible selected mark independent of color.

### Toggle

The source track is `52 × 28` with a `3`-unit border; the thumb is `18 × 18` with a `2`-unit border and moves `24` units. Off uses a neutral fill; on uses a green accent. Animate for `200 ms` only when motion is allowed. Retain native switch semantics and expose on/off state programmatically and visually.

## Notifications

Use a high-contrast fill, `3`-unit border, `(5,5)` hard shadow, bold label, and a maximum readable width. Pair every severity color with text and a distinct icon or other non-color cue.

| Type | Source fill | Source symbol | Example message role |
|---|---|---|---|
| Success | `#88D498` | Check | Confirmation |
| Error | `#FF6B6B` | Cross | Failure and recovery |
| Information | `#74B9FF` | Information mark | Noncritical update |
| Warning | `#FFD23F` | Warning mark | Actionable caution |

The source demo enters over `300 ms`, moves from `+20` to `0`, scales from `0.95` to `1`, and fades in; it auto-dismisses after `4,000 ms`; exit lasts `250 ms`, moves to `-10`, scales to `0.95`, and fades out. Do not copy auto-dismiss mechanically. Give users enough time, pause or persist messages that require action, expose an operable dismiss action with an accessible name, announce messages with the platform's appropriate status or alert semantic, and remove nonessential movement under reduced-motion settings.

## Parameter playground model

The source demonstrates that the style is a continuum rather than a binary preset.

| Parameter | Minimum | Maximum | Initial | Increment |
|---|---:|---:|---:|---:|
| Border width | `0` | `8` | `3` | `1` |
| Shadow offset | `0` | `20` | `5` | `1` |
| Corner radius | `0` | `32` | `0` | `1` |

Derive a nested control border as approximately two-thirds of its container border with a minimum of `1`; derive its shadow as approximately three-fifths of the container shadow; inherit the container's radius. Provide immediate value readouts and expose selection state programmatically. The source offers white, yellow, coral, blue, and green preview surfaces.

## Compact-width calibration

The source reduces depth at constrained widths. At its first compact threshold (`768` source pixels), default/large/extra-large shadows reduce from `5/8/12` to `4/6/8`; multi-column regions become one column. At its narrow threshold (`320` source pixels), those tiers reduce to `3/5/6`, controls tighten, and preview padding decreases.

Translate the principle, not the breakpoint: reduce shadow offsets, stroke crowding, padding, and compositional overlap as available space shrinks. Preserve operable target sizes and readable spacing even when the visual system becomes denser.

## Completeness checklist

- Define rest, hover or preview, focus, pressed, selected, disabled, loading, success, warning, and error states.
- Keep focus distinct from the normal border and hard shadow.
- Make actual hit areas meet the platform and accessibility target-size requirement; decoration does not enlarge the operable region.
- Keep selection and severity perceivable without color.
- Preserve native semantics for controls and notifications.
- Apply reduced-motion behavior to every nonessential translation, scaling, and entrance or exit animation, not only primary buttons.
- Verify responsive or constrained-space behavior through content and input-method testing.
- Use host-native primitives; no particular styling language or framework is required.

## Sources

- [Neubrutalism.com — Implementation](https://neubrutalism.com/#implementation)
- [Neubrutalism.com open-source repository](https://github.com/neubrutalism/neubrutalism.com)
