# Async work, cancellation, and errors

Use for loading, timers, background work, Tokio integration, cancellation, shutdown, or async UI failures. Signatures and fallibility move quickly; inspect the target's resolved source.

## Contents

- [Choose the executor](#choose-the-executor)
- [Make task lifetime explicit](#make-task-lifetime-explicit)
- [Cross await boundaries safely](#cross-await-boundaries-safely)
- [Handle errors by ownership](#handle-errors-by-ownership)
- [Respect replacement and shutdown](#respect-replacement-and-shutdown)
- [Review checklist](#review-checklist)

## Choose the executor

| Work                                  | Prefer                                         | Constraint                                      |
| ------------------------------------- | ---------------------------------------------- | ----------------------------------------------- |
| UI-affecting workflow                 | `cx.spawn`, `window.spawn`, or `spawn_in`      | Foreground/main thread; keep every poll short   |
| `Send + 'static` CPU/I/O future       | `background_spawn` / background executor       | Move owned plain data; no GPUI borrows          |
| Blocking or stack-heavy isolated call | `spawn_dedicated` where available              | Dedicated OS thread; use deliberately           |
| Native Tokio API                      | Initialize `gpui_tokio`, then bridge spawn API | GPUI task cancellation aborts linked Tokio work |
| Opportunistic maintenance             | `spawn_when_idle`                              | Obey the idle-time budget and yield             |

Foreground futures do not make synchronous work non-blocking. A long computation before the next `.await` freezes input and paint. Treat executor priorities as hints unless the resolved scheduler explicitly guarantees ordering; never use priority for correctness.

Use the GPUI executor's `now()` and `timer()` for workflows that need deterministic tests. Avoid `thread::sleep`, blocking waits, and unrelated wall clocks.

## Make task lifetime explicit

`Task<T>` is `#[must_use]`; dropping it cancels the work. For every task choose exactly one:

- **Await** it for structured work and a result.
- **Store** it on the owning entity/service so replacement or teardown cancels it.
- **Detach** it only for intentional process/application-lifetime work.

For detached `Task<Result<...>>`, handle inside the future or use the target's `detach_and_log_err`/equivalent. Never use `.detach()` or `.ok()` merely to silence a warning.

Common owner pattern: keep `Option<Task<_>>`; replace it to cancel obsolete work; capture the owner weakly using the resolved spawn form; await background work; merge through a short fallible foreground update; notify once. Inspect exact result nesting before using `?`.

## Cross await boundaries safely

Never retain these across `.await`:

- `&App` / `&mut App`;
- `&mut Context<T>`;
- `&mut Window`;
- a borrowed entity/global value;
- frame-local element/layout/paint state.

Move owned `Send` input to background work. Return owned output, then re-enter the foreground with `AsyncApp`, `AsyncWindowContext`, `WeakEntity`, or explicit window handles in a short update closure.

Treat fallibility precisely:

- `WeakEntity` read/update fails after entity release.
- window-handle and `AsyncWindowContext` updates fail after window closure/unavailability.
- Do not assume `AsyncApp` methods share one failure model; inspect each resolved method.
- Do not use `AppContext::as_mut` as a universal async/test escape hatch.
- nested update results may require two `?` operators; inspect the exact return type rather than discarding an inner error.

Use variable shadowing to keep clones and strong handles scoped to the async block that needs them.

## Handle errors by ownership

| Failure                               | Handling                                                         |
| ------------------------------------- | ---------------------------------------------------------------- |
| Caller owns recovery                  | Return/propagate `Result`                                        |
| Background failure affects current UI | Re-enter owner, store error state, notify, expose retry/feedback |
| Expected entity/window closure        | Match and stop quietly unless diagnostics are useful             |
| Detached infrastructure failure       | Log with context/backtrace policy                                |
| Startup window failure                | Handle inside the platform run callback and quit or recover      |

Do not `unwrap` window creation, asset loads, or async updates in production unless the invariant and panic boundary are explicit. Add operation and target context to errors without erasing their source.

## Respect replacement and shutdown

- Store cancellable task handles when newer work supersedes older work.
- Add a generation/request ID when cancellation alone cannot prevent stale results.
- Clear loading state on success, failure, and cancellation paths that remain observable.
- Do not let a detached task retain a view or large graph indefinitely; capture weak handles.
- Inspect the target quit boundary and timeout; register shutdown work before quit and do not start foreground work after the API forbids it.
- Treat timers, subscriptions, platform callbacks, and external runtimes as resources requiring teardown.

## Review checklist

- Is every `Task` awaited, stored, or intentionally detached?
- Are detached fallible tasks logged or surfaced?
- Does any foreground future perform blocking/CPU-heavy work?
- Does any synchronous reference or borrow cross `.await`?
- Are weak entity/window failures handled as lifecycle outcomes?
- Could stale results overwrite newer state?
- Does teardown cancel tasks, subscriptions, timers, and external-runtime work?
- Are executor time and fake clocks used in tests?
- Does shutdown avoid spawning new foreground work too late?

Verify in the resolved checkout: `crates/gpui/src/{executor,app/async_context,app/context,app}.rs`, `crates/scheduler/src/executor.rs`, and `crates/gpui_tokio` when used.
