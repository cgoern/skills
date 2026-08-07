# Refactoring Workflow

Use this workflow when migrating an existing system to Vertical Slice Architecture.

## Contents

- [Establish a baseline](#1-establish-a-baseline)
- [Inventory behavior and ownership](#2-inventory-behavior-and-ownership)
- [Design the target map](#3-design-the-target-map)
- [Migrate in stable increments](#4-migrate-in-stable-increments)
- [Perform the naming pass](#5-perform-the-naming-pass)
- [Audit boundaries](#6-audit-boundaries)
- [Run quality gates](#7-run-quality-gates)
- [Report the result](#8-report-the-result)
- [Scope safeguards](#scope-safeguards)

## 1. Establish a baseline

- Read repository instructions and architecture documentation.
- Record the current branch and working-tree state; preserve unrelated changes.
- Run the fastest authoritative build or type check and relevant linting.
- Record pre-existing failures instead of attributing them to the refactor.
- Identify explicit scope exclusions before editing.

## 2. Inventory behavior and ownership

Map:

- executable or delivery entry points;
- user and business capabilities;
- workflows crossing multiple capabilities;
- domain entities and persistence ownership;
- remote and platform integrations;
- global, feature, and control-specific state;
- existing shared modules and their consumers;
- dependency edges between current layers.

Build the map from call sites and imports, not directory names alone.

## 3. Design the target map

For every in-scope, architecture-owned runtime module, assign one primary destination: entry, composition, feature slice, shared kernel, shared capability, or infrastructure. Resolve ambiguous ownership before moving code. Leave tests, generated code, migrations, vendored packages, build tooling, documentation, and explicitly excluded areas in their native organization unless the task includes them.

Define:

- slice names and one-sentence responsibilities;
- each slice's narrow façade;
- allowed dependency directions;
- cross-slice intents and their coordinator;
- state and runtime-service owners;
- shared-kernel entries with current consumers and semantic justification.
- shared capabilities with a stable purpose, narrow façade, and proven consumers.

Do not design empty modules merely to make every slice look identical.

## 4. Migrate in stable increments

Prefer this sequence unless repository constraints suggest a safer migration:

1. Create the target top-level boundaries.
2. Select a representative pilot capability and migrate it end to end, including its model, workflow, presentation, and slice-specific data access.
3. Move or introduce only the infrastructure adapters and shared concepts whose ownership the pilot proves.
4. Add or tighten the pilot slice's façade.
5. Replace its direct cross-feature calls with intents handled by composition.
6. Repeat for remaining capabilities, growing infrastructure and shared ownership from demonstrated use.
7. Slim the entry point and composition layer after feature ownership is established.
8. Perform a systematic naming pass.
9. Delete obsolete wrappers, declarations, and empty legacy directories.

For a small, well-understood system, moving stable infrastructure or already-proven shared concepts first may reduce churn. Treat that as a deliberate migration strategy, not a prerequisite for the first slice.

Keep the system buildable between increments when practical. Favor version-control-recognizable moves and focused edits over simultaneous rewrites.

## 5. Perform the naming pass

Rename symbols and files that still encode the old architecture. Check:

- root and shell roles;
- feature and use-case names;
- view, handler, endpoint, or delivery names;
- intent and event names;
- application state versus runtime services;
- shared concepts versus feature-specific models;
- infrastructure adapters versus product services.

Do not rename established framework terms or clear domain vocabulary merely for uniformity.

## 6. Audit boundaries

Search the final tree and dependency graph for:

- feature-to-feature imports;
- feature imports of application composition internals or unrestricted global state;
- shared modules importing feature internals;
- infrastructure importing application or feature policy;
- feature behavior left in the composition layer;
- old layer paths and compatibility re-exports;
- public internals that bypass slice façades;
- singleton or global state with no clear owner;
- shared code with only one consumer;
- duplicate canonical identities or competing sources of truth;
- empty directories and stale generated metadata.

Treat a boundary exception as a design decision. Document why it is cheaper and clearer than the preferred direction.

## 7. Run quality gates

Use repository-native commands. At minimum, run the applicable formatter check, build or type check, linter, existing in-scope tests, and a whitespace or patch-integrity check. Run architecture-specific dependency checks when the ecosystem provides them.

Do not create tests when the user excludes them. Do not claim behavior preservation from compilation alone; state exactly what was and was not exercised.

Inspect the final diff for unrelated behavior, schema, public API, dependency, lockfile, generated artifact, and documentation changes.

## 8. Report the result

Summarize:

- the final boundary map;
- migrated capabilities and removed legacy layers;
- important internal renames;
- shared-kernel decisions and their consumers;
- shared-capability decisions and their façades;
- cross-slice coordination mechanism;
- validation commands and results;
- deliberate exceptions, remaining risks, and excluded work.

## Scope safeguards

- Preserve behavior unless the request authorizes behavior changes.
- Preserve unrelated working-tree changes.
- Avoid dependency upgrades during an architecture-only refactor.
- Avoid new frameworks, code generators, or architectural libraries unless required.
- Avoid extracting abstractions solely to remove visual duplication.
- Avoid moving feature policy into global state for convenience.
- Avoid retaining parallel old and new structures after migration unless a staged rollout requires it.
