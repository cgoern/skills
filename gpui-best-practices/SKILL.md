---
name: gpui-best-practices
description: Create, refactor, debug, review, test, or optimize project-agnostic GPUI Rust code. Use for GPUI dependency or version drift, App and Context handling, Entity/WeakEntity ownership, views and elements. Use for render, layout, paint, element identity, events and actions, keyboard, focus, input, and accessibility. Use for async tasks and cancellation, globals, windows, platforms, assets, text, images, lists, testing, performance, and Zed-source pattern research. This skill is for a project that depends on GPUI. Do not use this skill for generic Rust code or generic UI work with no GPUI dependency.
---

# GPUI best practices

Build correct GPUI code from the locked source and the local conventions of the host project. Use the bundled research map as historical evidence, and never as the host API.

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

Do not load every reference by default. Resolve the exact APIs locally. Open the snapshot map only for relevant evidence or examples.

## Resolve the actual GPUI API

Do not propose API code before these steps are complete:

1. Read the host instructions and the existing UI abstractions.
2. Examine `Cargo.toml`, `Cargo.lock`, the workspace dependencies, the patches, and the path sources and git sources.
3. Use `cargo metadata --locked` or an equivalent command to find the resolved GPUI source.
4. Find the local wrappers and the same-revision call sites before the import of a raw GPUI API.
5. Read that source. Make sure that the exact signatures, the macro forms, the features, and the platform support are correct.

If an agent cannot resolve the dependency, state the assumed version or revision. Never silently change GPUI to match an example. The current source, gpui.rs, docs.rs, blogs, and the Zed call sites can differ legitimately, because GPUI is pre-1.0.

## Design before editing

Record only the items that affect the change:

- Record the owner of each entity, global, window handle, task, subscription, focus, and list state.
- Record the strong edges, the weak edges, and the behavior for cancellation and replacement.
- Record the path from an input or an action, through a mutation and `notify` or `emit`, to `render`.
- Record the stable ID for each repeated, stateful, focusable, or accessible node.
- Record these states: loading, empty, failure, cancellation, stale-result, and shutdown.
- Record the parity between the keyboard, the pointer, the focus-visible state, the disabled state, and accessibility.
- Record the assumptions about the platform and the features, and the test surface.

Prefer standard element composition and `RenderOnce`. Introduce an entity when the behavior is retained or shared. Introduce a custom `Element` only for justified control of layout, hit-testing, or paint.

## Implement with GPUI invariants

Obey these rules for the leases and the notifications:

- Keep each context lease, entity lease, and global lease short, synchronous, and non-reentrant.
- Call `notify` for an observable state change.
- Call a typed `emit` for an occurrence. `notify` and `emit` are not substitutes for each other.

Obey these rules for the tasks and the subscriptions:

- Await, store, or intentionally detach every `Task`, because GPUI cancels a dropped `Task`.
- Store, join, or intentionally detach every `Subscription`, because GPUI unsubscribes a dropped `Subscription`.
- Capture an entity weakly in a stored callback or a stored task, unless the retention is intentional.

Obey these rules for the background work and for `render`:

- Move owned `Send` data to the background work. Merge the result briefly and fallibly on the foreground context.
- Keep `render` pure and fast. Keep the element identity stable across frames and across a reorder.

Obey these rules for the input, the lifecycle, and the failures:

- Send the mouse, key, menu, test, and accessibility paths through the same semantic action or method.
- Obey the full lifecycle contracts of custom input, custom elements, windows, assets, and platform capabilities.
- Show a failure that affects a user through the UI conventions and the error conventions of the host application.

Use Zed only as production evidence. Adapt the patterns of Zed. Do not prescribe `crates/ui`, workspaces, themes, services, a directory layout, or a feature graph to another project.

## Validate proportionally

1. Format the code with the host command.
2. Run the narrowest compile or check command and the focused tests first.
3. Run the host lints and the broader relevant tests.
4. For an interactive change or an async change, test the keyboard, focus, accessibility, cancellation, and error paths.
5. Use the GPUI executor time, the input and action simulation, and the effect draining instead of sleeps.
6. Test all claimed combinations of platform and feature, or state the unverified matrix.

For a review, tell the user the evidence-backed correctness issues first. Distinguish the GPUI contracts, the revision-specific facts, the host conventions, and the optional Zed-derived improvements.
