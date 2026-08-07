---
name: neobrutalism-design
description: Design, implement, adapt, or audit technology-agnostic neobrutalist interfaces and design systems. Use when creating a frontend visual direction, component language, design tokens, interaction states, typography system, layout specification, accessibility plan, critique, migration, or acceptance criteria in neobrutalism, neo-brutalism, neobrutalism, soft neobrutalism, or a related hard-border and offset-shadow style across web, desktop, mobile, or other graphical applications.
---

# Neobrutalism Design

Create deliberate neobrutalist interfaces as a usable visual system, not a collection of loud effects. Preserve the host product's interaction model and express the style through portable design decisions that fit its technology, platform conventions, audience, and risk.

## Load the guidance

Read the references needed for the task before proposing or changing a design:

- Read [references/01-definition.md](references/01-definition.md) to distinguish neobrutalism from architectural brutalism, web brutalism, and accidental roughness.
- Read [references/02-visual-dna.md](references/02-visual-dna.md) for color, geometry, borders, depth, typography, and layout grammar.
- Read [references/03-typography.md](references/03-typography.md) when selecting or auditing type roles, families, weights, or pairings.
- Read [references/04-history.md](references/04-history.md) when explaining provenance, influences, contested origins, or historical claims.
- Read [references/05-implementation.md](references/05-implementation.md) when defining tokens, components, state behavior, or portable implementation specifications.
- Always read [references/06-usage-and-accessibility.md](references/06-usage-and-accessibility.md) before recommending the style for a product or implementing interactive surfaces.
- Read [references/07-ecosystem.md](references/07-ecosystem.md) when evaluating examples, adoption patterns, tools, or market context.
- Read [references/08-future-and-subtypes.md](references/08-future-and-subtypes.md) when choosing intensity, hybrid direction, or subtype.
- Read [references/09-quick-reference.md](references/09-quick-reference.md) for a compact design review or initial token baseline; do not treat it as a substitute for the detailed references.
- Read [references/10-sources.md](references/10-sources.md) when citing claims, verifying provenance, or refreshing time-sensitive facts.

## Establish the design contract

1. Determine whether the user wants a concept, specification, implementation, refactor, audit, or critique.
2. Identify the host medium, interaction conventions, existing design system, brand constraints, supported input methods, content density, accessibility target, and regulated or high-stakes context.
3. Preserve existing information architecture, task flow, semantics, platform behavior, and system-status feedback unless the user explicitly requests changes.
4. Choose an intensity level: accent-only, moderated or soft, standard, or editorial/poster. Use stronger intensity on expressive surfaces and lower intensity on operational surfaces.
5. State assumptions and exclusions that materially affect the result.

Do not assume a particular framework, styling language, rendering engine, component library, unit system, or file format. Inspect the project and translate the portable specification into its native primitives only after the design decisions are settled.

## Start from conventional usability

Build or retain a dependable UX skeleton before applying the visual grammar:

- Keep navigation, reading order, grouping, labels, forms, errors, and recovery predictable.
- Keep core controls recognizable and make every state perceivable without relying on color alone.
- Use local visual disruption around stable interaction patterns; do not make the interaction itself deliberately confusing.
- Protect dense, transactional, trust-sensitive, or high-stakes flows from unnecessary visual noise.

Treat neobrutalism as a presentation and brand layer over a conventional interaction model, not permission to abandon platform standards.

## Define a portable system

Specify semantic parameters rather than framework syntax. At minimum define:

- structural dark and base-light colors plus a limited accent palette;
- text, surface, border, focus, selected, success, warning, and error color pairings;
- one default stroke weight plus intentional thin and thick hierarchy variants;
- square or near-square corner policy;
- small, medium, large, and optional extra-large hard-shadow tiers with zero blur;
- spacing and density rules that keep outlined objects from crowding one another;
- display, heading, body, and optional monospace type roles;
- state transitions for default, hover or equivalent preview, focus, pressed, selected, disabled, loading, success, warning, and error;
- reduced-motion and non-pointer equivalents for any movement-based feedback;
- rules for macro asymmetry and micro alignment.

Name tokens by semantic purpose. Numerical examples in the references are starting points, not universal physical units; scale them coherently for the host medium and density.

## Apply the visual grammar

Use a coordinated set of moves:

- Make object boundaries explicit with strong, consistent outlines.
- Use flat categorical fills; avoid atmospheric gradients as a default stylistic device.
- Create depth with opaque offset shadows, not diffuse simulated lighting.
- Pair forceful display typography with calm, readable operational text.
- Disrupt the macro composition selectively while preserving a grid, scan path, grouping logic, and stable micro alignment.
- Reserve the harshest border, shadow, scale, and color treatments for a small number of priorities.
- Make borders and shadows communicate hierarchy or state; remove decoration that carries no role.

Do not infer that every object needs a border, shadow, saturated fill, rotation, or oversized label. If everything shouts, hierarchy disappears.

## Specify component behavior

For each component, document:

1. Semantic role and importance.
2. Surface, outline, depth tier, corner policy, spacing, and type role.
3. Complete interaction and system states.
4. Actual operable region rather than apparent size created by decoration.
5. Focus treatment that remains distinct from the normal outline and shadow.
6. Keyboard, pointer, touch, assistive-technology, reduced-motion, and high-contrast behavior as applicable to the host platform.
7. Content limits, responsive or constrained-space behavior, localization stress, and failure behavior.

Use physical feedback consistently: an available control may appear raised; preview or hover may lift it slightly; activation may move it toward the shadow and reduce or remove depth. Provide equivalent state feedback where hover and motion do not exist.

## Validate before handoff

1. Confirm the style fits the audience, sector, trust requirement, and task risk.
2. Verify hierarchy remains clear without color and without decorative shadows.
3. Test every foreground/background and state pairing against the applicable accessibility standard; use WCAG 2.2 as the baseline for web content unless a stricter project or legal standard applies.
4. Confirm visible focus, non-color state cues, operable target size, reading order, semantics, error communication, reduced motion, zoom or scaling, and reflow where applicable.
5. Check that borders do not obscure focus or state and that shadows do not imply false hit areas.
6. Test representative content extremes, dense screens, narrow or small surfaces, localization, and all input modes supported by the product.
7. Compare every component with the shared token system and remove one-off values without a documented hierarchy reason.
8. Inspect the result at normal use distance. Reduce saturation, shadow depth, stroke weight, or disruption if expression overwhelms comprehension.

Report the chosen intensity, portable tokens, component/state rules, accessibility evidence, deliberate deviations, and unresolved risks.

## Keep evidence current

Treat historical origin claims, brand examples, library popularity, platform counts, and future forecasts as time-sensitive. Verify them before presenting them as current. Prefer the original neubrutalism.com section, W3C standards, primary historical sources, and first-party project or brand sources. Distinguish the source site's synthesis from independent verification and label contested or inferred claims.
