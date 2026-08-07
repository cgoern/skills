# Usage and accessibility

Source section: [06 — Usage Guide: When to Use Neubrutalism](https://neubrutalism.com/#usage)

## Decision principle

Neubrutalism is strongest as a layer for attention, brand acquisition, and differentiation. It is a weaker default where institutional trust, anxiety reduction, dense work, or consequential tasks dominate. Its distinctiveness breaks visual expectations; usability still depends on stable hierarchy, recognizable affordances, and coherent reading order.

Concentrate expressive treatment in heroes, campaigns, mastheads, and other introductory surfaces. Reduce intensity in forms, accounts, dashboards, and transactions.

## Sector fit

| Fit | Context | Appropriate use and boundary |
|---|---|---|
| Best | Creator and portfolio experiences | Audiences value personality, novelty, and identity; strongest in short top-of-funnel journeys |
| Best | SaaS marketing | Differentiates acquisition surfaces from visually interchangeable startup marketing; does not automatically fit the product interior |
| Best | Web3 and crypto | Aligns with anti-establishment and attention-driven positioning; this is a brand-fit observation, not evidence of inherent usability or trust |
| Caution | E-commerce | Use on campaigns and brand surfaces; moderate in carts, checkout, returns, and accounts |
| Caution | Editorial and media | Strong for mastheads and heroes; calm long-form and dense reading views |
| Caution | Product dashboards | Use as an accent or shell; keep tables, filters, settings, and dense panels conventional and state-clear |
| Avoid or heavily moderate | Banking and insurance | Calm, conventional competence and trust usually outweigh expressive aggression |
| Avoid or heavily moderate | Healthcare | Visual friction may increase anxiety; clarity, error prevention, and accessibility are high-stakes |
| Avoid or heavily moderate | Government services | Universal usability and statutory accessibility outweigh novelty |

Treat this matrix as guidance, not a substitute for user research, brand context, product risk analysis, or applicable law.

## Accessibility strengths and failure modes

### Potential strengths

- Large headings and defined edges can support scanning.
- Clear control boundaries can improve discoverability compared with extremely flat interfaces.
- A deliberately high-contrast palette can exceed thresholds.
- Hard depth cues can make interactive elements appear actionable.

These are possibilities, not automatic properties. Boldness and saturation do not establish accessibility.

### Common failure modes

- **Insufficient contrast:** vivid mid-tone combinations may still be unreadable.
- **Color-only meaning:** selected, success, warning, error, or action state depends only on hue.
- **Misleading target size:** a thick border or shadow looks large while the operable region remains small.
- **Lost focus:** a focus indicator blends into the normal border, shadow, or decoration.
- **Excess motion:** lift, press, scale, and toast animations ignore reduced-motion preferences.
- **Hierarchy collapse:** every object receives equally strong outline, depth, saturation, and type.

## WCAG 2.2 requirements emphasized by the source

Verify against the current [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/); the table is not a complete conformance checklist.

| Criterion | Level | Requirement | Neubrutalist implication |
|---|---:|---|---|
| 1.4.3 Contrast (Minimum) | AA | Text requires `4.5:1`; large-scale text requires `3:1`; defined exceptions apply | Test every foreground/background pair and state, not palette swatches in isolation |
| 1.4.11 Non-text Contrast | AA | Visual information needed to identify active controls, states, and essential graphics requires `3:1` against adjacent colors, with defined exceptions | Separate semantic boundaries and state cues from decorative borders |
| 2.4.7 Focus Visible | AA | Every keyboard-operable interface has a mode with visible focus | Make focus independently perceivable from the normal outline and hard shadow |
| 2.5.8 Target Size (Minimum) | AA | Pointer targets are at least `24 × 24` CSS pixels unless a specified exception applies | Measure the operable region; border and shadow bulk do not count automatically |
| 1.4.1 Use of Color | A | Color is not the only visual means of conveying information, action, response, or distinction | Pair color with text, a meaningful icon, pattern, shape, label, or structural cue |

WCAG's “large-scale” definition and exceptions are technical; do not classify text as large merely because it feels visually prominent. Conformance requires every applicable success criterion across complete pages and user processes.

## Current-standard caveat

WCAG 2.2 remains the current stable W3C Recommendation, and W3C advises using the latest WCAG 2 version. WCAG 3.0 remains an incomplete Working Draft whose details will change. W3C states that WCAG 3 will not simply replace WCAG 2 and that WCAG 2 will remain required in jurisdictions for a long time. Build and evaluate against WCAG 2.2 today while tracking the formal standard and law applicable to the product. Treat the source site's approximate WCAG 3 timeline as a forecast, not a commitment.

## Contrast verification

- Evaluate rendered pairs, not individual swatches; saturation and loudness do not predict luminance contrast.
- Test default, hover or preview, focus, pressed, selected, disabled, success, warning, and error states.
- Apply `4.5:1` to ordinary text and `3:1` only when text meets the formal large-scale definition.
- Evaluate required control boundaries, state indicators, and meaningful graphics against every adjacent color at `3:1` where 1.4.11 applies.
- Check overlapping panels, accent fills, and decorative shadows; a token may pass on one surface and fail on another.
- Treat a contrast checker as one early constraint, not proof of whole-interface accessibility.

## Implementation best practices

### Separate expression from interaction

Apply the strongest treatment to heroes, marketing blocks, campaigns, and editorial modules. Reduce intensity in dashboards, forms, settings, checkout, account management, and other transactional flows. Keep interaction behavior familiar.

### Systematize the aesthetic

Define a small shared set of border, depth, corner, spacing, color, and type parameters. Adjust intensity consistently rather than redesigning every component.

### Make loudness serve hierarchy

Keep body text systematic and readable. Assign the strongest treatment to limited priorities. When every element demands maximum attention, the interface stops communicating importance.

### Prove accessibility early

Evaluate contrast, focus, target size, non-color cues, semantics, reading order, motion, scaling, reflow, and input modes during design rather than after launch.

### Treat borders as signals

A border should communicate container, interaction, focus, selection, error, or another defined role. Remove outlines that carry no useful distinction because decorative borders can dilute semantic ones.

### Reserve the harshest gestures

Use one coherent border system, one predictable hard-shadow behavior, and one dominant display scale. Do not make every component behave like a poster.

### Test with users

Retain recognizable controls, readable typography, sufficient space, visible interaction states, and meaningful hierarchy. Test the resulting product with representative users; visual distinctiveness is not evidence of usability.

## Sources

- [Neubrutalism.com — Usage Guide](https://neubrutalism.com/#usage)
- [Nielsen Norman Group — Neobrutalism: Definition and Best Practices](https://www.nngroup.com/articles/neobrutalism/)
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C — WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [W3C — WCAG 3 introduction](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/)
- [W3C — WCAG 3 Working Draft](https://www.w3.org/TR/wcag-3.0/)
