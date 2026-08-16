# Actions, input, focus, and accessibility

Use for commands, keybindings, pointer/input handlers, focus navigation, editable text, drag/drop, or accessibility. Check exact APIs in the target GPUI revision.

## Contents

- [Use actions for semantic commands](#use-actions-for-semantic-commands)
- [Handle propagation deliberately](#handle-propagation-deliberately)
- [Make focus durable and visible](#make-focus-durable-and-visible)
- [Pair interaction with accessibility](#pair-interaction-with-accessibility)
- [Treat text input as a platform protocol](#treat-text-input-as-a-platform-protocol)
- [Review checklist](#review-checklist)

## Use actions for semantic commands

Define semantic commands as actions so keymaps can rebind them and dispatch follows the focused tree. Resolve unit/payload declaration forms from `action.rs` and `gpui_macros`; common forms are `actions!` and `#[derive(Action)]`, but never copy a macro absent from the target exports.

- Derive the traits required by the target action registry/keymap format; opt out of serialization only deliberately.
- Namespace public action names, keep them stable, and use aliases for migrations where supported. Duplicate registered names panic at app construction.
- Bind defaults during app initialization with the target revision's `KeyBinding` API.
- Render `.key_context(...)`, `.track_focus(...)`, and `.on_action(...)` on the same focused dispatch path.
- Use raw key handlers only for physical-key behavior or an actual text-input protocol.
- Route pointer activation, keybindings, menus, command palettes, tests, and accessibility to the same action/method; do not duplicate mutations.

Deeper focused key contexts take precedence over ancestors. Verify multi-stroke encoding and context syntax in the resolved keymap implementation. Follow host conventions for platform bindings and user keymaps.

## Handle propagation deliberately

Capture dispatch travels toward the target; bubble dispatch travels outward. Prefer bubble handlers near the behavior owner.

| Handler               | Verify in target        | Deliberate override                                     |
| --------------------- | ----------------------- | ------------------------------------------------------- |
| Low-level input event | Default propagation     | Stop only when ancestors must not observe it            |
| Action handler        | Default bubble behavior | Propagate when an ancestor/global handler must also run |

`prevent_default` and propagation are independent. Suppressing a default click/scroll behavior does not necessarily justify hiding the event from ancestors.

- Stop propagation only when another handler must not observe the event.
- Use capture for exceptional cross-cutting behavior; careless capture handling breaks non-local controls.
- Prefer `cx.listener(Self::handler)` for view methods; it weakly targets the entity and no-ops after release.
- Keep pointer hitboxes, visual bounds, cursor, drag state, and accessible behavior aligned.
- Model drag/drop with typed payloads and explicit enter/move/leave/drop states.

## Make focus durable and visible

Focus requires retained state and a rendered association:

1. Create and store a `FocusHandle`, normally during entity construction.
2. Implement `Focusable` when the view exposes its handle.
3. Render `.track_focus(&focus_handle)` on the correct node.
4. Put actions/key context on that focus path.
5. Render a visible focus state appropriate to input modality.

Use `.tab_index(...)` inside a deliberate tab group. Use `.tab_stop(false)` for a focusable container skipped during normal keyboard traversal. Preserve focused identity across rerenders; when conditional UI removes it, choose and restore a sensible successor or ancestor.

For modals/popovers, record prior focus, focus after installing the overlay, and restore only if focus still belongs to that overlay; never steal focus the user moved elsewhere.

Do not use hover as keyboard focus. Check focus-visible behavior with mouse and keyboard. Honor the target's reduced-motion state and verify animation-helper behavior.

## Pair interaction with accessibility

Every interactive control should expose one coherent contract:

- stable unique element ID;
- appropriate role;
- accessible name/label and current value/state;
- keyboard action path;
- pointer behavior;
- focusability and visible focus;
- accessible actions for non-click operations;
- disabled/selected/expanded/checked state where applicable.

Gate disabled behavior across every activation path. Give icon-only controls an accessible name and, when useful, a tooltip; a clickable visual alone is not a complete control.

A node needs stable identity and semantics. Supply a unique ID, role, label, and state according to the resolved accessibility builder. Duplicate/changing IDs can drop nodes or appear as removal plus insertion.

Critical repeated-text rule: default `text!` identity comes from the macro call site. Supply a stable explicit ID or identified ancestor inside loops. Use inaccessible text only when a parent already exposes that text as its label and duplicate narration would be wrong.

GPUI command `Action` and AccessKit `AccessibleAction` are unrelated. Wire accessible operations to the same method as pointer/keyboard activation. Verify whether the target's built-in click handler installs accessible-click behavior.

Custom `Element` implementations own accessibility hooks and any synthetic children. Prepare accessibility data only after layout/prepaint information exists.

## Treat text input as a platform protocol

Do not implement an editable field as a few `on_key_down` callbacks. A custom text editor must integrate:

- `EntityInputHandler`/`InputHandler` for the target revision;
- focus and platform input-handler registration;
- selection, composition/IME, replacement ranges, caret bounds, and hit testing;
- UTF-8 byte boundaries in Rust and platform UTF-16 ranges;
- clipboard, commands/actions, and accessibility;
- multiline shaping/wrapping when applicable.

Use standard/native project controls when available. If custom input is required, start from the revision-matched `crates/gpui/examples/input.rs`, then add deterministic composition, selection, clipboard, keyboard, pointer, and accessibility tests.

## Review checklist

- Are rebindable commands actions rather than raw keys?
- Are action names unique, namespaced, and supported by the resolved macro API?
- Does the focus handle persist and appear via `track_focus`?
- Are dispatch context, actions, and focus on one path?
- Is propagation behavior intentional for input versus actions?
- Does every interactive node have stable ID, role, label/state, keyboard, pointer, focus, and a11y behavior?
- Are repeated text/control IDs unique?
- Do dynamic removals restore focus sensibly?
- Does editable text implement the full platform protocol?
- Are reduced motion and keyboard focus visibility respected?

Verify in the resolved checkout: `crates/gpui/src/{action,key_dispatch,interactive,_accessibility}.rs`, `elements/div.rs`, `crates/gpui_macros`, and `crates/gpui/examples/input.rs`.
