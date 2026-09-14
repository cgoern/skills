---
name: vertical-slice-architecture
description: Design, refactor, and review software systems using technology-agnostic Vertical Slice Architecture. Use when organizing a codebase around end-to-end capabilities, migrating from horizontal technical layers, or defining feature and composition boundaries. Also use when deciding what belongs in shared code or coordinating cross-feature workflows. Also use when aligning state ownership and internal naming during a capability-centered refactor. Also use when auditing a proposed VSA structure for coupling and scope drift. This skill works at the level of a capability boundary. Do not use it to decide where one helper file goes, or to rename folders with no boundary change.
---

# Vertical Slice Architecture

Divide the software into cohesive capabilities so that one product change stays primarily inside one slice. Use the directory structure as evidence of ownership and dependency direction, not as the architecture itself.

## Load the guidance

This file carries the role list, the shared-code tests, and the validation steps. Do not load a
reference file that the task does not need.

Read [references/structure.md](references/structure.md) only in these conditions:

- You must apply the dependency rules between two roles, or record a deliberate exception.
- You must select between a shared kernel and a shared capability.
- Two capabilities use the same entity, and you must decide whether they are one slice.
- You audit a structure and you need the ten audit questions.

Read [references/refactoring.md](references/refactoring.md) only when you move existing code. It
gives the increment sequence, the naming pass, and the scope safeguards.

## Make the task contract

Find the type of task that the user wants: analysis, design, implementation, review, or a full refactor. Keep the behavior unless the user explicitly asks for a behavior change.

Record each scope exclusion, for example:

- Tests
- API changes
- Visual changes
- Persistence migrations
- Deployment work

Do not change an architecture request into an unrelated rewrite. Prefer moves, narrow facades, dependency changes, and role-accurate renames over speculative abstractions.

## Discover before the design

1. Read the instructions of the host project and use its native build and validation commands.
2. Map entry points, product capabilities, user-visible workflows, state owners, runtime services, persistence, external integrations, and shared concepts.
3. Trace dependencies and cross-capability calls. Identify the difference between orchestration and feature behavior.
4. Identify names and folders that describe technical layers instead of ownership.
5. Before you edit the code, make a passing baseline or tell the user about the failures that already exist.

Use evidence from the code and from dependency searches. Do not decide a boundary from a filename only.

## Produce a boundary map

Classify each responsibility into one of these roles:

- **Entry point** - start the system and give control to the application layer.
- **Application/composition** - bootstrap, navigation or delivery shell, global coordination, lifecycle, and cross-slice intent handling.
- **Feature slice** - one end-to-end capability, with the behavior and the adapters that are specific to that capability.
- **Shared kernel** - stable concepts or reusable presentation primitives with identical semantics across multiple slices.
- **Shared capability/internal platform** - a cohesive cross-slice subsystem with stable semantics, its own facade, and proven consumers.
- **Infrastructure** - technical mechanisms, for example transport, persistence engines, telemetry, filesystem access, and platform integration.

Define the allowed dependency direction before you move files. Give every mutable state value, runtime capability, workflow, and shared abstraction one clear owner.

## Refactor by capability

Move one coherent slice at a time. Keep these parts of the slice close together:

- The internal model
- The use cases
- The presentation code or the delivery code
- The data mapping
- The slice-specific persistence

Expose only the smallest surface that is necessary for the composition layer or other approved consumers.

Replace each direct feature-to-feature call with one of these mechanisms:

- An explicit intent
- A message
- An event
- A command
- Application-level orchestration

Keep the mechanism native to the host technology. Keep the architectural direction.

Rename internals as part of the refactor when a name encodes an obsolete layer or responsibility. Prefer capability and role names. It is better not to use vague containers, for example `manager`, `helper`, `common`, or `utils`. Use one of these names only when the name gives a precise and established concept.

## Govern shared code

Move code into shared ownership only when you have evidence of all of these conditions:

1. The code is necessary for two current slices or more.
2. The slices use the same semantics and invariants, not only similar shapes.
3. The abstraction can stay feature-neutral.
4. The likely changes to the abstraction belong to all the consumers together.

Keep distinct workflows as distinct slices, even when the workflows display the same entity or list. Share only these items, and only when each item obeys the four tests above:

- The canonical identity
- The stable domain vocabulary
- The query semantics or the ordering semantics
- The stateless presentation

Do not use `shared` as a temporary location for code with an unclear owner.

## Validate architecture and behavior

After the implementation:

1. Find forbidden feature-to-feature dependencies and legacy layer names.
2. Make sure that the entry points are thin and that the composition layer contains coordination, not feature policy.
3. Make sure that every feature exposes a narrow facade. If the technology can keep the internals private, make sure that the internals stay private.
4. Classify feature dependencies on application context as narrow contracts, host-native context access, or deliberate exceptions. Reject access to composition implementation details.
5. Do a check of each shared item again, against the shared-kernel criteria or the shared-capability criteria.
6. Remove the empty legacy directories and the stale module declarations.
7. Run the native formatting, build or type checks, linting, and existing tests of the host project that are in scope.
8. Examine the final diff for accidental changes to behavior, dependencies, configuration, or generated files.

Tell the user about the new boundary map, the important naming changes, the validation evidence, and the deliberate exceptions.

## Apply judgment

Do not assume that VSA makes these necessary:

- A universal folder tree
- One file per use case
- CQRS
- Domain-driven design
- Dependency injection
- Microservices

Add one of these patterns only when the system gets a benefit from it independently.

Prefer a modest shared kernel and slightly duplicated slice code over a premature abstraction that couples unrelated capabilities. Extract the shared code after the evidence shows semantic identity.
