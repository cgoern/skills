# GPUI foundations and version discipline

Read this for every GPUI task. It defines source precedence, the mental model, and the execution workflow.

## Resolve the target API first

GPUI is pre-1.0 and changes frequently. The target project's locked source beats this skill's snapshot, Zed `main`, published rustdoc, gpui.rs, blog posts, and remembered examples.

Use this evidence order:

1. Host instructions, architecture, wrappers, and validation commands.
2. `Cargo.toml`, `Cargo.lock`, workspace dependencies, patches, and path/git dependencies.
3. Exact source selected by `cargo metadata --locked`.
4. Rustdoc and examples from that same revision.
5. This skill's [research source map](source-map.md) for historical evidence and examples.
6. gpui.rs and official posts for explanation; verify signatures locally.

```sh
rg -n 'gpui|gpui_platform|gpui_tokio' --glob 'Cargo.toml' --glob 'Cargo.lock'
cargo tree -i gpui
cargo metadata --format-version 1 --locked
```

Adapt commands to the host. Do not upgrade/add dependencies to make an example compile unless requested. Report the resolved version/revision when drift matters.

## Keep the model straight

| Concept      | Contract                                                                         |
| ------------ | -------------------------------------------------------------------------------- |
| `App`        | Owns entities, windows, globals, executors, and application services             |
| `Entity<T>`  | Typed reference-counted handle into app-owned `T`; access only through a context |
| View         | An entity whose value implements `Render`                                        |
| Element tree | Frame-local output rebuilt, laid out, prepainted, painted, then dropped          |
| `Context<T>` | `App` plus current entity identity, effects, listeners, spawn, focus helpers     |
| `Window`     | Window-local input/focus/layout/paint services; not an app context               |
| `RenderOnce` | Consumed stateless component recipe                                              |
| `Element`    | Low-level layout/prepaint/paint contract                                         |
| Effect       | Queued notification/event/release work flushed after updates                     |

Persist state in entities, globals, owner fields, or stable keyed element state—not ordinary element values. Use the highest-level primitive that meets the need: composition → `RenderOnce` → entity/view → canvas → custom `Element`.

## Preserve these invariants

- Access entity/global state only through a compatible GPUI context; never re-lease the same value recursively.
- Call `notify` for observable state change; use typed `emit` for occurrences. Neither implies the other.
- Store/await/intentionally detach every `Task`; dropping cancels it.
- Store/join/intentionally detach every `Subscription`; dropping unsubscribes.
- Prefer weak entity capture for callbacks/tasks that should end with the owner.
- Never carry synchronous contexts, windows, or borrowed entity values across `.await`.
- Treat entity/window access after awaiting as fallible lifecycle state.
- Give repeated, stateful, interactive, focusable, and accessible nodes stable unique IDs.
- Pair pointer behavior with keyboard, focus-visible, and accessibility semantics.
- Keep render synchronous, pure, and fast; move blocking/CPU work off the foreground thread.
- Treat optional platform APIs as capabilities, not guaranteed behavior.
- Use deterministic GPUI executor time and input/action simulation in tests.

## Execute the task

### Create

Discover pin and local wrappers → name state/window/task owners → choose the simplest primitive → implement complete error/focus/a11y/lifecycle behavior → add focused tests → format/check/lint with host commands.

### Refactor

Establish baseline → trace entities/tasks/subscriptions/focus/IDs/windows → preserve cancellation, notification, event order, identity, and focus restoration → change in compiling slices → add regression coverage.

### Fix

Reproduce minimal sequence → classify with [diagnostics.md](diagnostics.md) → inspect exact implementation plus same-revision example/test → repair the invariant → add deterministic regression test.

### Review

Trace input/async completion → mutation → `notify`/`emit` → render/dispatch/a11y → cancellation/cleanup. Separate framework facts from host-project preferences and Zed conventions.

## Terminology and portability

Use neutral current names (`App`, `Context<T>`, `Entity<T>`, `WeakEntity<T>`, `Window`, `Render`, `RenderOnce`, `Element`, async contexts). Follow older names when the target revision requires them; do not migrate unless asked.

Zed is production evidence, not a required module layout, theme, global-state model, or service architecture. Follow each host project's instructions and abstractions.

Use [source-map.md](source-map.md) only when local resolved source cannot answer the question or a production example is useful. Its commit-pinned links document one research snapshot, not the host project's API.
