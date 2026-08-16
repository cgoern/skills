# GPUI diagnostic index

Use this symptom-first index, then open the linked topic reference and the target revision's source.

| Symptom                                    | First checks                                                                                 | Reference                                                              |
| ------------------------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| State changed but UI stayed stale          | Missing `cx.notify()`; mutated wrong owner; cached view dependency                           | [State](state-and-context.md), [rendering](rendering-and-layout.md)    |
| Observer ran but event payload is missing  | `notify`/`observe` used instead of `emit`/`subscribe`                                        | [State](state-and-context.md)                                          |
| Callback never runs                        | Dropped `Subscription`; setup replaced; window-aware callback has no window                  | [State](state-and-context.md)                                          |
| Async work never completes                 | Dropped `Task`; owner/replacement cancelled it; app/window/entity closed                     | [Async](async-and-errors.md)                                           |
| Error vanished                             | Detached fallible task; ignored nested `Result`; blank asset fallback                        | [Async](async-and-errors.md), [assets](platform-assets-and-text.md)    |
| UI freezes                                 | Blocking render/handler; CPU work on foreground future; real sleep                           | [Async](async-and-errors.md), [rendering](rendering-and-layout.md)     |
| Entity access panics                       | Same entity leased recursively; strong cycle; invalid async/test `as_mut`                    | [State](state-and-context.md)                                          |
| Wrong window updates                       | Implicit/default window association in multi-window flow                                     | [State](state-and-context.md), [platform](platform-assets-and-text.md) |
| Focus/keybinding does nothing              | Handle not retained/tracked; key context/action off focus path; wrong action name            | [Interaction](interaction-and-accessibility.md)                        |
| Parent action never runs                   | Verify action propagation default and child override                                         | [Interaction](interaction-and-accessibility.md)                        |
| Pointer event unexpectedly reaches parent  | Verify input propagation; distinguish default prevention from stopping                       | [Interaction](interaction-and-accessibility.md)                        |
| Row state follows wrong item               | Index/call-site key; duplicate sibling ID; repeated same entity view                         | [Rendering](rendering-and-layout.md)                                   |
| Accessibility node disappears/duplicates   | Missing role/ID; duplicate ID; repeated `text!` call-site identity                           | [Interaction](interaction-and-accessibility.md)                        |
| Transformed control clicks at old position | Paint transform changed visuals, not layout/hitbox                                           | [Rendering](rendering-and-layout.md)                                   |
| Cached view is empty/wrong size            | Cache used for intrinsic size or without definite bounds                                     | [Rendering](rendering-and-layout.md)                                   |
| Variable list jumps/stales                 | Offscreen height changed without `ListState::splice`/`reset`                                 | [Rendering](rendering-and-layout.md)                                   |
| Image loads but never appears              | Cache-only fetch used while expecting redraw; missing invalidation/fallback                  | [Assets](platform-assets-and-text.md)                                  |
| Text shaping panics                        | Multiline content passed to a target-documented single-line shaper                           | [Assets/text](platform-assets-and-text.md)                             |
| Platform feature silently does nothing     | Optional `PlatformWindow` default/no-op; missing backend feature                             | [Platform](platform-assets-and-text.md)                                |
| Test hangs or is flaky                     | Real clock/sleep; task not awaited/drained; parking misuse                                   | [Testing](testing-and-performance.md)                                  |
| Leak assertion fails unexpectedly          | Strong task/subscription/entity cycle; effect queue not drained                              | [Testing](testing-and-performance.md), [state](state-and-context.md)   |
| Copied action macro fails                  | Macro copied from another revision; inspect target exports                                   | [Interaction](interaction-and-accessibility.md)                        |
| Derived view renders nothing               | Derive behavior assumed from another revision; inspect macro and implement render explicitly | [Rendering](rendering-and-layout.md)                                   |

For API-not-found/type errors:

1. Inspect `Cargo.lock`, workspace dependencies, patches, and `cargo metadata --locked`.
2. Find the exact definition/re-export in the resolved GPUI source.
3. Search target code and same-revision examples for callback shape.
4. Fix to the target pin; do not silently upgrade GPUI.

Useful searches:

```sh
rg -n 'cx\.(notify|emit)\(|\.(observe|subscribe)(_in)?\(' --glob '*.rs'
rg -n '\.(spawn|background_spawn|detach|detach_and_log_err)\b' --glob '*.rs'
rg -n 'focus_handle|track_focus|key_context|on_action|bind_keys' --glob '*.rs'
rg -n '\.(id|with_id)\(|text!|use_(keyed_)?state' --glob '*.rs'
rg -n 'thread::sleep|tokio::time::sleep|advance_clock|run_until_parked' --glob '*.rs'
```
