---
name: gpui-best-practices
description: Create, refactor, debug, review, test, or optimize project-agnostic GPUI Rust code. Use for GPUI dependency/version drift, App and Context handling, Entity/WeakEntity ownership, views and elements, render/layout/paint, element identity, events and actions, keyboard/focus/input/accessibility, async tasks and cancellation, globals, windows/platforms, assets/text/images, lists, testing, performance, and Zed-source pattern research.
---

# GPUI best practices

Build correct GPUI code from the target project's locked source and local conventions. Treat the bundled research map as historical evidence, never as the host API.

## Start here

Read [references/foundations.md](references/foundations.md) for every task. Then load only the smallest matching reference set:

| Task                                                                                | Read                                                                            |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| State placement, entities, contexts, notify/events, subscriptions, globals, windows | [state-and-context.md](references/state-and-context.md)                         |
| Components, views, IDs, layout/style, custom paint, lists, caching                  | [rendering-and-layout.md](references/rendering-and-layout.md)                   |
| Actions, keys, input, focus, drag/drop, accessibility, editable text                | [interaction-and-accessibility.md](references/interaction-and-accessibility.md) |
| Tasks, executors, background work, cancellation, errors, shutdown                   | [async-and-errors.md](references/async-and-errors.md)                           |
| Startup, features, windows, backends, assets, images, SVG, text                     | [platform-assets-and-text.md](references/platform-assets-and-text.md)           |
| Tests, fake time, leaks, profiling, redraws, scaling                                | [testing-and-performance.md](references/testing-and-performance.md)             |
| Symptom-led bug diagnosis                                                           | [diagnostics.md](references/diagnostics.md) plus one topic file                 |
| Historical source snapshot, examples, Zed case studies, further reading             | [source-map.md](references/source-map.md) on demand                             |

Do not load every reference by default. Resolve exact APIs locally; open the snapshot map only for relevant evidence or examples.

## Resolve the actual GPUI API

Before proposing API code:

1. Read the host repository's instructions and existing UI abstractions.
2. Inspect `Cargo.toml`, `Cargo.lock`, workspace dependencies, patches, and path/git sources.
3. Use `cargo metadata --locked` or equivalent to locate the resolved GPUI source.
4. Search local wrappers and same-revision call sites before importing raw GPUI APIs.
5. Verify exact signatures, macro forms, features, and platform support in that source.

If the dependency cannot be resolved, state the assumed version/revision. Never silently change GPUI to fit an example. Current source, gpui.rs, docs.rs, blogs, and Zed call sites may legitimately differ because GPUI is pre-1.0.

## Design before editing

Write down only what affects the change:

- owners of entities, globals, window handles, tasks, subscriptions, focus, and list state;
- strong versus weak edges and cancellation/replacement behavior;
- input/action → mutation → `notify`/`emit` → render path;
- stable IDs for repeated/stateful/focusable/accessible nodes;
- loading, empty, failure, cancellation, stale-result, and shutdown states;
- keyboard, pointer, focus-visible, disabled, and accessibility parity;
- platform/feature assumptions and test surface.

Prefer standard element composition and `RenderOnce`; introduce an entity for retained/shared behavior and custom `Element` only for justified layout/hit-testing/paint control.

## Implement with GPUI invariants

- Keep context/entity/global leases short, synchronous, and non-reentrant.
- Call `notify` for observable state change and typed `emit` for occurrences; neither substitutes for the other.
- Await, store, or intentionally detach every `Task`; dropping cancels it.
- Store, join, or intentionally detach every `Subscription`; dropping unsubscribes.
- Capture entities weakly in stored callbacks/tasks unless retention is intentional.
- Move owned `Send` data to background work; merge briefly and fallibly on the foreground context.
- Keep render pure and fast; preserve stable element identity across frames and reordering.
- Route mouse, key, menu, tests, and accessibility through the same semantic action/method.
- Treat custom input, custom elements, windows, assets, and platform capabilities as full lifecycle contracts.
- Surface user-impacting failures through the host application's UI/error conventions.

Use Zed only as production evidence. Adapt its patterns; do not prescribe `crates/ui`, workspaces, themes, services, directory layout, or feature graph to another project.

## Validate proportionally

1. Format with the host command.
2. Run the narrowest compile/check and focused tests first.
3. Run host lints and broader relevant tests.
4. Exercise keyboard/focus/accessibility and cancellation/error paths for interactive or async changes.
5. Use GPUI executor time, input/action simulation, and effect draining instead of sleeps.
6. Test all claimed platform/feature combinations or state the unverified matrix.

For reviews, report evidence-backed correctness issues first. Distinguish GPUI contracts, revision-specific facts, host conventions, and optional Zed-derived improvements.
