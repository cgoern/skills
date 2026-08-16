# Structure and Boundary Rules

Use these rules to design or audit a technology-agnostic Vertical Slice Architecture.

## Contents

- [Core objective](#core-objective)
- [Architectural roles](#architectural-roles)
- [Dependency rules](#dependency-rules)
- [Feature anatomy](#feature-anatomy)
- [Cross-slice coordination](#cross-slice-coordination)
- [State and service ownership](#state-and-service-ownership-in-stateful-systems)
- [Shared-kernel decision](#shared-kernel-decision)
- [Shared capability decision](#shared-capability-decision)
- [Shared presentation](#shared-presentation)
- [Naming](#naming)
- [Architecture audit questions](#architecture-audit-questions)

## Core objective

Optimize for change locality: a capability change should touch its slice and, only when necessary, the composition layer or a genuinely shared contract. Organize around why the system changes rather than the framework mechanism used to implement it.

## Architectural roles

| Role                                | Owns                                                                                   | Must not become                                     |
| ----------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Entry point                         | Process startup and delegation                                                         | A second composition root                           |
| Application/composition             | Bootstrap, lifecycle, shell, routing, global coordination, cross-slice intent handling | A home for feature rules or data access details     |
| Feature slice                       | One cohesive capability from input to outcome                                          | A technical layer or grab bag of screens            |
| Shared kernel                       | Stable vocabulary, contracts, and neutral primitives used with identical meaning       | A generic dumping ground                            |
| Shared capability/internal platform | Cohesive cross-slice workflows and adapters behind a narrow façade                     | A hidden composition layer or speculative framework |
| Infrastructure                      | Replaceable technical mechanisms and platform adapters                                 | The owner of product workflows                      |

Allow folder names to differ. Preserve the roles and dependency rules even when the host ecosystem uses packages, modules, namespaces, components, services, or assemblies.

## Dependency rules

Prefer this direction:

```text
entry -> application/composition
application/composition -> feature façades + shared + infrastructure
feature internals -> own slice + shared + narrow application-context contracts + approved technical ports/adapters
shared kernel -> shared kernel or infrastructure-neutral contracts
shared capability -> shared kernel + approved technical ports/adapters
infrastructure adapters -> owning port contracts + infrastructure + external technology
```

Enforce these invariants:

- Do not import one feature's internals from another feature.
- Let the composition layer translate cross-slice intent into navigation, orchestration, or state changes.
- Prefer slice-owned state or narrow, feature-neutral application-context contracts. Treat feature access to composition implementations as a reverse dependency requiring redesign or an explicit exception.
- Let infrastructure implement inward-owned port contracts when useful, but keep it ignorant of feature and application policy.
- Keep shared code ignorant of feature internals.
- Prefer a shared contract or port over a direct adapter dependency when adapter replacement or testability warrants the indirection. Do not add a port mechanically.
- Permit a deliberate exception only when its owner, reason, and dependency direction remain clear.

## Feature anatomy

Include only the subset required to deliver a slice's capability:

```text
features/
  capability-name/
    facade
    model
    use-cases-or-workflow
    presentation-or-delivery
    data-mapping
    persistence
    remote-integration
```

Do not create empty ceremonial layers. Start with a small façade and a few cohesive modules; split only when responsibilities become independently understandable.

Expose the capability, not its implementation. A façade should normally reveal use-case entry points, intent or result types, and presentation entry points required by composition. Keep storage rows, response payloads, helper functions, and control state private unless another approved owner truly needs them.

## Cross-slice coordination

Express what happened or what is requested without naming another feature's implementation.

```text
Feature A -> OpenItem(item_id) intent -> application coordinator
application coordinator -> navigation/state/use case -> Feature B façade
```

Use the host technology's natural mechanism: events, messages, commands, callbacks, reducers, queues, or application services. The mechanism is secondary to three constraints:

1. The emitting slice does not control the receiving slice.
2. The composition layer owns the multi-slice decision.
3. Payloads use stable identifiers or contracts rather than another slice's private state.

## State and service ownership in stateful systems

Use the following as ownership examples for interactive or long-lived stateful systems, not as mandatory VSA roles:

| State kind                                                                                            | Preferred owner                                             |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Process lifecycle, current route, authenticated session, globally surfaced errors                     | Application state                                           |
| Initialized database handles, transport clients, credentials configuration, clocks, platform gateways | Application services or composition-owned runtime container |
| Capability workflow state and feature data                                                            | The feature slice, unless genuinely global                  |
| Focus, selection, expansion, draft input, scroll position                                             | The owning presentation component or view                   |
| Canonical identity or stable domain data shared with identical meaning                                | A deliberately governed shared kernel                       |

Separate mutable product state from initialized runtime capabilities when their ownership or lifecycle would otherwise be ambiguous. They may remain together in small or short-lived systems where the distinction adds no clarity.

## Shared-kernel decision

Move a concept into shared ownership only when all answers are yes:

- Do multiple existing slices consume it now?
- Does it mean exactly the same thing to each consumer?
- Do its invariants and lifecycle align across consumers?
- Can it evolve without learning feature-specific policy?
- Would fixing or changing it correctly require coordinated changes for all consumers?

Similar syntax is insufficient. Duplicate a small amount of code when the business meaning differs.

## Shared capability decision

Use a shared capability or internal platform when multiple slices depend on the same cohesive subsystem rather than only the same vocabulary. Require all of these conditions:

- Give the subsystem one stable purpose and one clear owner.
- Expose it through a narrow façade rather than its internal storage, transport, or workflow modules.
- Keep slice-specific membership, permissions, navigation, and user journeys out of it.
- Let it own persistence, remote integration, indexing, or other adapters only when those mechanisms serve the shared purpose consistently.
- Confirm that extracting it reduces competing sources of truth or duplicated invariants rather than merely reducing file count.

Do not let a shared capability coordinate otherwise independent slices. Return multi-slice product decisions to the application/composition layer.

### Shared entity, distinct workflows

Two capabilities may operate on the same canonical entity without becoming one slice. For example, `owned-items` and `saved-items` may consume a shared `item-catalog` capability that owns canonical identity, metadata, persistence, remote synchronization, search projection, and ordering behind a narrow façade. Keep membership rules, commands, empty states, errors, permissions, and user journeys inside their respective slices. Share a neutral list renderer separately when its presentation semantics match. Let a separate `item-detail` capability serve both through an `OpenItem` intent.

This pattern preserves one source of truth without coupling distinct reasons to change.

## Shared presentation

Share presentation code when it accepts values and callbacks or intents and has no knowledge of feature state, feature persistence, navigation, or remote APIs. Keep feature-specific labels, permissions, loading rules, empty states, and commands in the slice.

If a reusable control starts reading global feature state or dispatching feature-specific operations, return that behavior to the owning slice.

## Naming

Use names that reveal capability and role:

- Name slices after user or business capabilities, preferably nouns or goal phrases.
- Name orchestration types after application roles such as root, shell, router, coordinator, state, or services.
- Name messages after intent or completed facts.
- Name use cases with verbs and outcomes.
- Name shared kernels after the stable concept they govern.
- Rename obsolete `controller`, `domain`, `screen`, or `service` terms when they no longer describe the new responsibility; retain them when they remain accurate in the host ecosystem.

Avoid names that merely repeat a framework primitive or hide ownership.

## Architecture audit questions

1. Can a reviewer explain each slice's capability in one sentence?
2. Does a normal feature change remain mostly inside one slice?
3. Can any feature reach another feature's private implementation?
4. Does composition coordinate without implementing feature policy?
5. Are infrastructure adapters free of product workflow decisions?
6. Does every shared kernel item or capability have multiple current consumers with aligned semantics?
7. Is control state owned close to its interaction?
8. In stateful systems, is the relationship between global state and runtime services deliberate?
9. Do façades expose only what external owners need?
10. Are old layer names, compatibility wrappers, and empty directories gone?
