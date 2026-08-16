# Conventional Commits 1.0.0 Reference

This is a faithful, operational restatement of the
[Conventional Commits 1.0.0 specification](https://www.conventionalcommits.org/en/v1.0.0/#specification).
Normative terms such as MUST, MUST NOT, REQUIRED, SHOULD, RECOMMENDED, MAY, and OPTIONAL carry the
meanings defined by [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119). The source specification is
licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).

## Contents

- [Grammar and semantics](#grammar-and-semantics)
- [Normative rules](#normative-rules)
- [Examples](#examples)
- [Operational guidance](#operational-guidance)

## Grammar and semantics

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

- `fix` represents a bug correction and normally maps to a SemVer PATCH release.
- `feat` represents a new feature and normally maps to a SemVer MINOR release.
- A breaking API change may occur under any type. Mark it with `!` immediately before the colon,
  with a `BREAKING CHANGE:` footer, or with both; it normally maps to a SemVer MAJOR release.
- Other types are permitted. Common conventions include `build`, `chore`, `ci`, `docs`, `style`,
  `refactor`, `perf`, and `test`, but the specification assigns them no inherent SemVer effect
  unless they carry a breaking change.
- An optional parenthesized scope supplies codebase context, such as `feat(parser):`.
- Footers other than breaking-change declarations are permitted and resemble Git trailers.

## Normative rules

1. Begin every commit with a noun-like type. It MUST be followed, in order, by an optional scope,
   an optional `!`, and the required `: ` delimiter.
2. Use `feat` when the change adds a feature to an application or library.
3. Use `fix` when the change corrects a bug in an application.
4. A scope MAY follow the type. When present, it MUST be a noun naming a codebase area and MUST be
   enclosed in parentheses, as in `fix(parser):`.
5. Put the short description immediately after the colon and space. It MUST briefly summarize the
   code changes.
6. A longer body MAY add context. When present, it MUST start after one blank line following the
   description.
7. The body is free-form and MAY contain any number of newline-separated paragraphs.
8. One or more footers MAY follow the body, separated from it by one blank line. Each footer MUST
   contain a word token, then either `: ` or ` #`, then a string value.
9. Replace whitespace inside ordinary footer tokens with `-`, as in `Acked-by`. The literal token
   `BREAKING CHANGE` is the allowed space-containing exception.
10. A footer value MAY contain spaces and newlines. A parser MUST continue that value until it
    encounters the next valid footer token plus separator.
11. Every breaking change MUST be identified either in the type/scope prefix or in a footer.
12. A footer-based breaking declaration MUST use uppercase `BREAKING CHANGE`, then `: `, then a
    description of the break.
13. A prefix-based breaking declaration MUST place `!` directly before `:`. With `!`, the breaking
    footer MAY be omitted and the short description serves as the explanation of the break.
14. Types other than `feat` and `fix` MAY be used.
15. Implementations MUST treat Conventional Commit information units as case-insensitive except
    for `BREAKING CHANGE`, which MUST be uppercase.
16. In a footer token, `BREAKING-CHANGE` MUST be treated as equivalent to `BREAKING CHANGE`.

## Examples

Description only:

```text
docs: correct changelog spelling
```

Scoped feature:

```text
feat(locale): add Polish translations
```

Breaking change marked in the footer:

```text
feat: allow configuration inheritance

BREAKING CHANGE: the extends key now resolves and merges external configuration files
```

Breaking change marked in the prefix:

```text
feat(api)!: replace the legacy shipment notification endpoint
```

Multi-paragraph body and multiple footers:

```text
fix(requests): ignore stale responses

Track the latest request identifier and discard responses from older requests.

Remove the timeout workaround because request identity now resolves the race.

Reviewed-by: A. Reviewer
Refs: #123
```

## Operational guidance

- Apply the convention even before an initial public release; downstream users still need clear
  feature, fix, and compatibility signals.
- Type casing is not normative, but keep it consistent within a project; lowercase is conventional.
- If a change fits multiple independent types, split it into multiple commits when possible.
- Teams may define and evolve extra types without violating the specification.
- Before merge or release, correct a valid-but-wrong type by rewriting the commit when safe. After
  release, follow the project's remediation process.
- An unknown or misspelled type may be ignored by release tooling even though Git accepts it.
- With squash merging, maintainers may normalize the final message, so every contributor need not
  author compliant intermediate commits.
- Revert behavior is intentionally left to tooling. A common pattern is `revert` plus a `Refs:`
  footer containing the reverted commit identifiers.
- The convention supports automated changelogs, semantic-version calculation, clearer history,
  build and publish triggers, and easier contribution review.
