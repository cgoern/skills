# State, contexts, entities, and events

Use for state placement, context choice, observation/events, globals, ownership, or stale-state bugs. Verify signatures against the target's resolved GPUI source.

## Contents

- [Place state deliberately](#place-state-deliberately)
- [Choose the narrowest context](#choose-the-narrowest-context)
- [Update entities without cycles](#update-entities-without-cycles)
- [Separate notifications and events](#separate-notifications-and-events)
- [Own subscriptions](#own-subscriptions)
- [Constrain globals and windows](#constrain-globals-and-windows)
- [Review checklist](#review-checklist)

## Place state deliberately

| State                                         | Default owner                            |
| --------------------------------------------- | ---------------------------------------- |
| One render's immutable input                  | Plain `RenderOnce` field                 |
| Small local interaction at one tree location  | `Window::use_state`                      |
| Repeated local interaction                    | `use_keyed_state(stable_domain_id, ...)` |
| Shared/durable feature or view state          | `Entity<T>`                              |
| Truly application-wide typed service/settings | Private `Global` + narrow façade         |

The element tree is disposable. Keep durable entities, focus/list/scroll state, tasks, and subscriptions on the owner whose lifetime they follow. Follow the host project's composition and state model; Zed's hierarchy is not mandatory.

## Choose the narrowest context

| Context                                | Use                                                             | Constraint                                  |
| -------------------------------------- | --------------------------------------------------------------- | ------------------------------------------- |
| `&App`                                 | Read entities/globals/services                                  | Read-only; no entity/window identity        |
| `&mut App`                             | Create/update entities, globals, windows; register app behavior | Main application scope                      |
| `&mut Context<T>`                      | Update `T`; notify/emit/observe/subscribe/listen/spawn          | Short synchronous lease; derefs to `App`    |
| `&mut Window`                          | Focus, input, layout, paint, element state, window services     | Pair with app/entity context                |
| `AsyncApp`                             | Re-enter app state after awaiting                               | Owned; exact methods have mixed fallibility |
| `AsyncWindowContext`                   | Re-enter a particular window                                    | Handle closure/unavailability               |
| `TestAppContext` / `VisualTestContext` | Deterministic state or rendered interaction tests               | Accessor set differs from `App`             |

Use generic `AppContext`/`VisualContext` only at proven reusable boundaries. Never retain synchronous contexts, windows, or borrowed values across `.await`. Do not treat `AppContext::as_mut` as a universal escape hatch; inspect each context implementation.

## Update entities without cycles

`Entity<T>` is an opaque typed handle into app-owned state. Read/update it only through a compatible context.

- Use `cx.new` normally; reserve/insert only when construction needs the future entity ID.
- Keep read/update closures short and synchronous.
- Batch coherent mutation, then notify once when rendered/observed state changed. Do not assume an update/replacement helper notifies; verify its target-source contract.
- Do not read/update the same entity re-entrantly while leased; this can panic. Finish, defer/emit, pass plain data, or split ownership.
- Use weak handles for upward references, registries, long-lived callbacks, and async work that should end with the entity.
- Verify listener/processor capture semantics in the target; prefer weak capture unless retention is intentional.
- Do not store a task/subscription that strongly captures its owning entity; this forms a leak cycle.
- Use release observers for cleanup that must precede value drop.

Strong ownership should usually flow downward; upward and asynchronous references should usually be weak. Treat failed weak access as normal liveness unless user work was lost.

## Separate notifications and events

| Channel                        | Meaning                             |
| ------------------------------ | ----------------------------------- |
| `cx.notify()` → `observe`      | Observable state changed; reread it |
| `cx.emit(event)` → `subscribe` | Typed occurrence/intent happened    |

Implement `EventEmitter<E>` before emitting. Neither channel implies the other; call both when both semantics apply. Effects flush after the update boundary, not re-entrantly inside the mutation.

Prefer windowless observe/subscribe. Use `_in` variants only when the callback truly needs a window; window unavailability can skip/fail window-aware work.

Choose boundaries deliberately:

- parent commands child: direct typed update;
- child announces intent/result: typed event;
- several views share state: shared entity + observation;
- focus-hierarchy command: typed action;
- cross-feature workflow: composition-root subscription/callback/registry.

Do not use globals or events as an unstructured message bus.

## Own subscriptions

`Subscription` is a cancellation handle:

- dropping unsubscribes;
- store it when owner teardown/replacement should cancel;
- join handles with one logical lifetime;
- detach only when endpoint release is the intended lifetime.

Never detach just to silence `#[must_use]`. Make setup idempotent or replace old handles to avoid duplicate listeners.

## Constrain globals and windows

For globals:

- initialize before infallible access; use `try_global` when absence is valid;
- update through the target API so observers run;
- expose a private global through narrow public operations;
- never recursively update the same leased global;
- prefer explicit entity/service handles unless discovery is truly app-wide.

For lifecycle/windows:

- final strong-handle drop queues release; drain effects before leak assertions;
- an entity may render in multiple windows;
- do not assume `App::with_window` identifies the semantic target in multi-window code; inspect its association rule;
- carry a typed/erased `WindowHandle` when semantics require a specific window;
- re-enter windows fallibly and never store borrowed `Window` values.

## Review checklist

- One deliberate owner per mutable value?
- Correct narrow context and short leases?
- Notify and/or emit for the intended semantics?
- Every subscription stored, joined, or intentionally detached?
- Weak edges break parent/self/task cycles?
- No same-entity/global re-entrant lease?
- Explicit window for multi-window work?
- Effect queue drained before release assertion?
