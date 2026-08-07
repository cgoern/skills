# Quick reference

Source section: [The Neubrutalism Cheat Sheet](https://neubrutalism.com/#cheatsheet)

Use this as an initial calibration and review aid. Read the detailed references before making production decisions.

## Core primitives

| Primitive | Source design parameter |
|---|---|
| Border | `3` units, solid, black `#000000` |
| Hard shadow | Horizontal `+5`, vertical `+5`, blur `0`, spread `0`, black `#000000` |
| Corner radius | `0` |
| Shadow blur | Always `0` |

Scale source units coherently for the target medium and density.

## Interaction states

| State | Position change | Shadow behavior |
|---|---|---|
| Hover or equivalent preview | Move `2` units left and `2` units up | Grow the shadow; this section does not specify the amount |
| Active or pressed | Move `3` units right and `3` units down | Remove the shadow |

Provide host-native equivalents where hover or translation does not exist. Honor reduced-motion preferences.

## Typography roles

| Role | Source family | Weight |
|---|---|---:|
| Display | Syne | 800 |
| Heading | Space Grotesk | Not specified in this section |
| Body | Inter | 400 |
| Monospace | Space Mono | Not specified in this section |

Treat families as curated examples. Preserve role contrast when substituting for brand, language, licensing, or platform needs.

## Color and contrast

- Base pairing: black `#000000` on off-white `#FFFDF5`.
- Stated base-pair contrast: `18.5:1`.
- Minimum contrast for ordinary text: `4.5:1` under WCAG 2.2 AA.

Verify all actual pairs and states. One passing base pair does not establish accessibility.

## The one rule

Begin with a conventional UX foundation, then apply neubrutalist visual parameters. Preserve familiar navigation, predictable information architecture, and clear system-status feedback before adding visual aggression. Treat neubrutalism as a theme over standard interaction patterns, not permission to discard interaction standards.

## Source

- [Neubrutalism.com — Quick Reference](https://neubrutalism.com/#cheatsheet)
