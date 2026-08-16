# Application, windows, platforms, assets, and text

Use for setup, features, windows, platform behavior, assets/images/SVG, text, or low-level graphics. Resolve the target dependency first; these APIs move frequently.

## Contents

- [Resolve setup and features](#resolve-setup-and-features)
- [Handle application and windows](#handle-application-and-windows)
- [Isolate platform behavior](#isolate-platform-behavior)
- [Load assets visibly](#load-assets-visibly)
- [Choose text and graphics APIs](#choose-text-and-graphics-apis)
- [Review checklist](#review-checklist)

## Resolve setup and features

Startup has moved between constructors and platform façade crates. Read the resolved `crates/gpui/README.md`, both `Cargo.toml` files, and the revision-matched `examples/hello_world.rs`; do not copy remembered startup code.

| Target/capability | Verify in the resolved source                            |
| ----------------- | -------------------------------------------------------- |
| macOS             | Renderer and font-rasterization features                 |
| Linux/FreeBSD     | Enabled window-system backends and runtime fallback      |
| Windows           | Native backend requirements and manifest features        |
| Web/Wasm          | Initialization order and threading mode                  |
| Tests/headless    | Test-support features versus pixel-renderer availability |
| Diagnostics       | Profiler, leak, inspector, and capture gates             |

Keep feature code on public `gpui`/platform façades. Isolate direct backend dependencies behind a platform adapter.

## Handle application and windows

- Create the application on the required thread and use the target platform constructor.
- Handle window creation and updates as fallible unless the resolved contract proves otherwise.
- Store typed/erased window handles, never borrowed `Window` values.
- Carry the semantic target handle in multi-window workflows; do not infer it from an entity association.
- Choose close/quit behavior explicitly and register bounded cleanup.
- Treat window options and optional services as best effort across backends.
- Handle startup failures inside the boundary that owns recovery, logging, and quit behavior.

## Isolate platform behavior

The portable platform traits may expose displays, dialogs, clipboard, credentials, menus, notifications, keyboard mapping, capture, lifecycle, and headless services. Trait presence does not guarantee backend support.

- Call `App`/`Window` façades from feature code.
- Put OS calls and `cfg` gates in one narrow adapter.
- Check capability/`Option`/`Result` and provide a fallback.
- Keep screen coordinates, logical/device pixels, and scale factor explicit.
- Test every claimed backend or state the unverified matrix.

## Load assets visibly

- Configure the target's asset source and preserve load-error versus not-found semantics.
- Confirm cache key, deduplication, invalidation, and redraw behavior in `assets.rs`, `asset_cache.rs`, and `window.rs`.
- Never assume a cache getter schedules redraw; choose the render-facing helper whose resolved contract does.
- Render loading, failure/fallback, and loaded states; make retry reachable.
- Reserve sensible image layout and choose fit deliberately so late dimensions do not jump.
- Prefer standard image/SVG elements; retain parsed/raster data only after measuring reuse.

## Choose text and graphics APIs

- Use immutable shared strings without depending on their backing representation.
- Prefer ordinary text elements/styles for labels and paragraphs.
- Choose single-line versus multiline shaping from the resolved text-system contract.
- Use hash-based shaping only when collision/identity assumptions are explicit and measured.
- Follow [interaction-and-accessibility.md](interaction-and-accessibility.md) for editable text.
- Use `canvas` for bounded custom drawing and `Element` only for justified layout/hit testing.
- Paint only in the paint phase; respect ancestor clipping, typed units, opacity, offsets, and scale.
- Keep visual transform, layout, hitbox, and accessibility bounds synchronized.

## Review checklist

- Setup and features match the resolved GPUI/platform crates?
- Startup/window operations and semantic window selection are lifecycle-safe?
- Optional platform behavior has a fallback?
- Asset loading invalidates correctly and exposes all states?
- Text API matches line structure and input requirements?
- Graphics respect phase, clipping, units, and hitboxes?

Verify in the resolved checkout: `crates/gpui/{README.md,Cargo.toml}`, `crates/gpui_platform`, `crates/gpui/src/{app,platform,window,assets,asset_cache,text_system,svg_renderer}.rs`, `elements/img.rs`, and revision-matched examples.
