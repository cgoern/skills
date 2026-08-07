---
name: vertical-slice-architecture
description: Design, refactor, and review software systems using technology-agnostic Vertical Slice Architecture. Use when organizing a codebase around end-to-end capabilities, migrating from horizontal technical layers, defining feature and composition boundaries, deciding what belongs in shared code, coordinating cross-feature workflows, aligning state ownership and internal naming during a capability-centered refactor, or auditing a proposed VSA structure for coupling and scope drift.
---

# Vertical Slice Architecture

Organize software around cohesive capabilities so one product change stays primarily inside one slice. Treat directory structure as evidence of ownership and dependency direction, not as the architecture itself.

## Load the guidance

- Read [references/structure.md](references/structure.md) before designing, implementing, or reviewing a VSA structure.
- Also read [references/refactoring.md](references/refactoring.md) when changing an existing codebase.

## Establish the task contract

Determine whether the user wants analysis, design, implementation, review, or a full refactor. Preserve behavior unless behavior changes are explicit. Record scope exclusions such as tests, API changes, visual changes, persistence migrations, or deployment work.

Do not turn an architecture request into an unrelated rewrite. Prefer moves, narrow façades, dependency changes, and role-accurate renames over speculative abstractions.

## Discover before designing

1. Read repository instructions and use its native build and validation commands.
2. Map entry points, product capabilities, user-visible workflows, state owners, runtime services, persistence, external integrations, and shared concepts.
3. Trace dependencies and cross-capability calls. Distinguish orchestration from feature behavior.
4. Identify names and folders that describe technical layers instead of ownership.
5. Establish a passing baseline or report pre-existing failures before editing.

Use evidence from code and dependency searches. Do not infer boundaries solely from filenames.

## Produce a boundary map

Classify each responsibility into one of these roles:

- **Entry point:** start the system and hand control to the application layer.
- **Application/composition:** bootstrap, navigation or delivery shell, global coordination, lifecycle, and cross-slice intent handling.
- **Feature slice:** one end-to-end capability, including the behavior and adapters specific to that capability.
- **Shared kernel:** stable concepts or reusable presentation primitives with identical semantics across multiple slices.
- **Shared capability/internal platform:** a cohesive cross-slice subsystem with stable semantics, its own façade, and proven consumers.
- **Infrastructure:** technical mechanisms such as transport, persistence engines, telemetry, filesystem access, and platform integration.

Define the allowed dependency direction before moving files. Give every mutable state value, runtime capability, workflow, and shared abstraction one clear owner.

## Refactor by capability

Move one coherent slice at a time. Keep its internal model, use cases, presentation or delivery code, data mapping, and slice-specific persistence close together. Expose only the smallest surface required by the composition layer or other approved consumers.

Replace direct feature-to-feature calls with explicit intents, messages, events, commands, or application-level orchestration. Keep the mechanism native to the host technology; preserve the architectural direction.

Rename internals as part of the refactor when old names encode obsolete layers or responsibilities. Prefer capability and role names. Avoid vague containers such as `manager`, `helper`, `common`, or `utils` unless they name a precise, established concept.

## Govern shared code

Require evidence before moving code into shared ownership:

1. At least two current slices need it.
2. They use the same semantics and invariants, not merely similar shapes.
3. The abstraction can remain feature-neutral.
4. Its likely changes belong to all consumers together.

Keep distinct workflows as distinct slices even when they display the same entity or list. Share the canonical identity, stable domain vocabulary, query or ordering semantics, and stateless presentation only when those pass the tests above.

Do not use `shared` as a waiting room for code whose owner is unclear.

## Validate architecture and behavior

After implementation:

1. Search for forbidden feature-to-feature dependencies and legacy layer names.
2. Confirm entry points are thin and the composition layer contains coordination rather than feature policy.
3. Confirm every feature exposes a narrow façade and keeps its internals private where the technology permits.
4. Classify feature dependencies on application context as narrow contracts, host-native context access, or deliberate exceptions; reject access to composition implementation details.
5. Recheck shared items against the shared-kernel or shared-capability criteria.
6. Remove empty legacy directories and stale module declarations.
7. Run repository-native formatting, build or type checks, linting, and existing tests that are in scope.
8. Inspect the final diff for accidental behavior, dependency, configuration, or generated-file changes.

Report the resulting boundary map, important naming changes, validation evidence, and any deliberate exceptions.

## Apply judgment

Do not assume VSA requires a universal folder tree, one file per use case, CQRS, domain-driven design, dependency injection, or microservices. Introduce these only when the system benefits from them independently.

Prefer a modest shared kernel and slightly duplicated slice code over a premature abstraction that couples unrelated capabilities. Extract shared code after semantic identity is demonstrated.
