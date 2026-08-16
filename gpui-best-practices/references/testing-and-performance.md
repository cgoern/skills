# GPUI testing and performance

Use for tests, flaky async behavior, redraw analysis, list scaling, and measured optimization. Resolve test features and helper names from the host pin.

## Contents

- [Choose the smallest test surface](#choose-the-smallest-test-surface)
- [Drive execution deterministically](#drive-execution-deterministically)
- [Test rendered and lifecycle behavior](#test-rendered-and-lifecycle-behavior)
- [Optimize from evidence](#optimize-from-evidence)
- [Review checklist](#review-checklist)
- [Search recipes](#search-recipes)

## Choose the smallest test surface

| Contract                               | Prefer                 | Escalate when                      |
| -------------------------------------- | ---------------------- | ---------------------------------- |
| Entity transition, notify, typed event | State/test app context | Rendering participates             |
| Focus, actions, layout, input          | Visual test context    | Native translation is the contract |
| Timers and task ordering               | GPUI test executor     | External work cannot be mocked     |
| Multi-app ordering                     | Multiple test contexts | Backend integration is required    |
| Portable window behavior               | Test/headless platform | OS behavior itself is under test   |

Inspect `crates/gpui/Cargo.toml`, `src/test.rs`, `app/test_context.rs`, and `gpui_macros` before choosing features, attributes, options, or accessor names. Use the revision-matched `examples/testing.rs` for callback shape, not a different-version snippet.

- Test state through the smallest context API; test dispatch through the rendered focus/input path.
- Retain subscriptions and tasks required by the behavior.
- Assert queued observer/event effects only after the update/effect boundary.
- Use property tests for shrinkable invariants and seeded iterations for scheduling/state-machine sequences when supported.

## Drive execution deterministically

| Need                            | Typical operation—verify target name |
| ------------------------------- | ------------------------------------ |
| Await one result                | Await its task                       |
| Drain runnable work             | Run until parked/quiescent           |
| Trigger timers                  | Advance the executor clock           |
| Explore ordering                | Inject randomized delay/yields       |
| Reproduce scheduling            | Reuse the reported seed              |
| Await unavoidable external work | Scope parking permission narrowly    |

Use the GPUI executor's clock/timer in testable application code. Avoid real sleeps and wall-clock polling. Mock network, filesystem, process, and clock boundaries where practical. Treat unexpected parking as a deadlock or unmodeled dependency signal.

Await, store, or intentionally detach every task; exercise cancellation separately from completion. Observe fallible detached work instead of merely asserting that it was spawned.

## Test rendered and lifecycle behavior

- Create the test window, render the production focus/key-context path, then dispatch actions or input.
- Simulate keyboard, text/IME, pointer, modifiers, resize, and accessibility operations through target-supported helpers.
- Use stable IDs for debug selectors and assert semantics before incidental geometry.
- Cover composition, UTF-8/UTF-16 mapping, selection, clipboard, caret, and hit testing for custom inputs.
- Obey native backend thread requirements; prefer portable test/headless paths otherwise.

For release/leak checks: enable the target leak facility; retain a weak handle/snapshot; exercise behavior; close/drop strong owners; drain effects/tasks; then assert release. Audit detached tasks, subscriptions, globals, and strong entity captures first. Enable allocation backtraces only when the target supports them.

## Optimize from evidence

1. Reproduce a representative workload.
2. Measure frame/input latency, task polls, allocation, redraw causes, and collection scale.
3. Use the resolved profiler/inspector features when available.
4. Remove blocking render/handler/foreground work.
5. Replace broad refresh with owner-scoped invalidation.
6. Batch coherent mutation and notify once.
7. Virtualize offscreen collection work.
8. Fix unstable identity/state churn before caching.
9. Add specialized cache/allocation changes only with explicit invalidation and measured benefit.
10. Re-measure under production-like inspector/profiler settings.

| Area                  | Prefer                                   | Avoid / verify                              |
| --------------------- | ---------------------------------------- | ------------------------------------------- |
| Invalidation          | Notify changed owner                     | Refreshing every window for local state     |
| Stateless composition | `RenderOnce`-style value component       | Entity solely for a visual recipe           |
| Uniform rows          | Uniform virtual list                     | Using it for variable heights               |
| Variable rows         | Variable list + measurement invalidation | Stale offscreen measurements                |
| Initial list metrics  | Height estimate                          | Measuring every huge item eagerly           |
| View cache            | Definite size + complete invalidation    | Ambient unobserved dependencies             |
| Render asset          | Helper that redraws on completion        | Assuming a cache getter redraws             |
| Text shaping          | API matching line structure              | Sending multiline text to a single-line API |
| Animation             | Frame-rate/reduced-motion limits         | Unbounded rerendering                       |

Treat executor priorities as hints unless the target promises ordering. Keep foreground polls within the interaction/frame budget.

## Review checklist

- Smallest context and production registration path tested?
- Dispatch/focus/input driven through rendered semantics?
- Tasks/subscriptions retained and cancellation covered?
- Executor time used instead of sleeps?
- Effects drained before release assertions?
- Late entity/window disappearance handled?
- Optimization measured before and after?
- List/cache/asset behavior verified in resolved source?
- Stable IDs preserved under insertion/reorder?

## Search recipes

```sh
rg -n '#\[gpui::(test|property_test)' . --glob '*.rs'
rg -n 'thread::sleep|tokio::time::sleep|Instant::now' . --glob '*.rs'
rg -n 'advance_clock|run_until_parked|simulate_random_delay|allow_parking' . --glob '*.rs'
rg -n '\.(spawn|background_spawn|detach|detach_and_log_err)\b|Subscription' . --glob '*.rs'
rg -n 'notify\(|refresh_windows|uniform_list|ListState|\.cached\(' . --glob '*.rs'
```

Verify in the resolved checkout: `crates/gpui/src/{test,executor,profiler,view}.rs`, `app/test_context.rs`, list/animation/asset/text elements, `crates/scheduler/src/executor.rs`, and revision-matched tests/examples.
