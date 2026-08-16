# Rendering, identity, layout, and painting

Use for components, views, element state, custom layout/paint, lists, or rendering-performance bugs. Verify method signatures against the target GPUI revision.

## Contents

- [Pick the cheapest abstraction](#pick-the-cheapest-abstraction)
- [Keep rendering frame-local](#keep-rendering-frame-local)
- [Make identity stable](#make-identity-stable)
- [Compose layout and style](#compose-layout-and-style)
- [Implement custom elements by phase](#implement-custom-elements-by-phase)
- [Virtualize and cache deliberately](#virtualize-and-cache-deliberately)
- [Review checklist](#review-checklist)

## Pick the cheapest abstraction

| Need                                     | Use                                            | Avoid                                           |
| ---------------------------------------- | ---------------------------------------------- | ----------------------------------------------- |
| Stateful, independently invalidated UI   | `Entity<T>` + `impl Render for T`              | Rebuilding an entity per frame                  |
| Stateless reusable component             | Value + `RenderOnce` + `IntoElement`           | Entity solely for composition                   |
| Normal layout/input                      | `div`, text, image, SVG, lists, canvas, layers | Custom `Element`                                |
| Small custom drawing                     | `canvas(prepaint, paint)`                      | Full element lifecycle                          |
| Custom layout/hitboxes/high-volume paint | `Element`                                      | Forcing standard elements beyond their contract |

`Render` borrows retained view state; `RenderOnce` consumes a frame-local component. Verify derive availability in the resolved macros crate. Implement real render logic explicitly; do not assume a `Render` derive synthesizes UI.

Return concrete `impl IntoElement`/`AnyElement` according to the host code's abstraction and compiler needs. Prefer the project's existing component wrappers and public `gpui::*` façade over private module paths.

## Keep rendering frame-local

Treat `render` as a pure, fast projection of state:

- Do not perform blocking I/O, long CPU work, unrelated mutation, or task creation on every render.
- Put durable state in an entity/global/view field or keyed element state.
- Register element callbacks as frame-local wiring; use weak listener helpers when they target the view.
- Invalidate with `cx.notify()` at the mutation site, not by forcing all windows to refresh.
- Keep list/scroll/focus/task/subscription handles on the owner whose lifecycle they follow.
- Use conditional builder helpers already present in the target revision instead of duplicating large branches.

Rendering the same entity-backed view twice as siblings can collide because view identity contributes to element state. Wrap instances in distinct identified ancestors or use distinct entities.

## Make identity stable

GPUI derives a global element identity from an element's ID plus identified ancestors. Identity drives retained element state, focus dispatch, scroll state, inspection, caching, and accessibility.

- Assign stable unique IDs to stateful, interactive, repeated, focusable, and accessible nodes.
- Key dynamic items by stable domain ID, not index, when reorder/insert/delete should preserve state.
- `window.use_state` is call-site keyed; call it once per namespace/call site.
- In loops or reusable call sites, use `use_keyed_state(stable_key, ...)` or a stable identified wrapper.
- Repeated `text!` from one macro call site needs an explicit unique ID for accessibility.
- Never reuse sibling IDs in the same identified namespace.
- Preserve identity through refactors; changing an ID intentionally resets associated state.

When a bug follows the wrong row, resets focus/scroll, duplicates accessibility nodes, or appears only after reordering, audit identity before mutation logic.

## Compose layout and style

GPUI layout uses Taffy and familiar flex/grid constraints. Diagnose constraints before adding measurements:

- Give scroll containers a definite size on the scrolling axis.
- Let overflowing text shrink: check parent width, flex basis, `min_w_0`, wrapping, and overflow.
- Use `truncate()` only when nowrap + hidden overflow + ellipsis is the intended behavior.
- Prefer typed geometry (`Pixels`, `DevicePixels`, `Point`, `Size`, `Bounds`, `Edges`) to untyped `f32` at API boundaries.
- Keep logical/device-pixel and scale-factor conversions explicit.
- Use semantic colors from the host application's theme when it has one; GPUI itself does not prescribe a theme architecture.
- Use anchored/deferred layers for overlays when stacking, clipping, and event ordering require them.
- Remember paint transforms such as SVG transformations do not automatically change layout or hitboxes.

Do not infer intrinsic size from a cached subtree or a virtualized collection. Measure only when composition cannot express the constraint.

## Implement custom elements by phase

Use the strict lifecycle:

| Phase            | Do                                                                                    | Do not                             |
| ---------------- | ------------------------------------------------------------------------------------- | ---------------------------------- |
| `request_layout` | Refine style; request layout; return layout state                                     | Paint, hit-test, retain frame refs |
| `prepaint`       | Read bounds; insert hitboxes; establish masks; compute paint data; prepare a11y/input | Append final scene primitives      |
| `paint`          | Append quads, paths, text, images, SVG/surfaces; install paint-time listeners         | Change layout or discover hitboxes |

Pass owned state from each phase to the next. Respect ancestor content masks, opacity, text style, element offset, and scale factor. `with_content_mask` intersects ancestor clipping; it does not replace it.

Before writing `Element`, inspect `canvas` and the closest built-in element. A custom element owns hit testing, input/focus integration, and accessibility—not only drawing.

## Virtualize and cache deliberately

### Lists

| Data                    | Primitive            | Contract                                                |
| ----------------------- | -------------------- | ------------------------------------------------------- |
| Truly equal row heights | `uniform_list`       | Measures one row; renders visible ranges                |
| Variable row heights    | `list` + `ListState` | Call `splice`/`reset` when offscreen heights may change |
| Small collection        | Normal children      | Virtualization overhead may not help                    |

Avoid `measure_all` on huge lists unless exact initial scrollbar geometry justifies first-frame cost. A uniform-height estimate can converge as rows render. Tune overdraw only from observed scroll behavior.

### View caching

Use `entity.cached(style)` only when all are true:

- the composer supplies definite bounds;
- the subtree has no intrinsic-size responsibility;
- every dependency invalidates through the entity's `notify` path;
- profiling shows a benefit.

Do not add redundant caches around text, layout, or assets without evidence; GPUI already caches these internally. Cached subtree behavior may be disabled during inspector picking.

## Review checklist

- Is persistent state outside disposable element values?
- Could a `RenderOnce` component replace an entity, or standard composition replace a custom element?
- Are repeated/stateful/a11y IDs stable and unique?
- Does every custom element honor layout → prepaint → paint?
- Do transforms, masks, hitboxes, and visual bounds agree?
- Is the chosen list primitive consistent with row-height behavior?
- Are list mutations reflected in `ListState`?
- Does caching have definite size, complete invalidation, and measured value?
- Is render free of blocking work and accidental per-frame setup?

Verify in the resolved checkout: `crates/gpui/src/{element,view,window,styled}.rs`, `elements/canvas.rs`, `elements/uniform_list.rs`, and `elements/list.rs`.
