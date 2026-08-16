---
name: conventional-commit
description: Enforce Conventional Commits 1.0.0 and produce compliant Git and pull-request metadata. An agent MUST use this skill whenever it creates, amends, squashes, rebases, rewords, or recommends a commit; creates or edits a pull request; prepares a merge or squash message; writes a release entry or changelog from commits; or chooses commit types, scopes, breaking-change markers, footers, and semantic-version effects.
---

# Conventional Commit

Apply Conventional Commits 1.0.0 to every commit-facing workflow. Read
[`references/specification.md`](references/specification.md) before drafting or validating a
commit message or pull-request title.

## Workflow

1. Inspect the complete change set and repository conventions before choosing a message.
2. Separate unrelated changes into distinct commits when practical. Do not hide multiple
   independent intents behind one type.
3. Select `feat` for a new capability and `fix` for a bug correction. Select another repository-
   accepted type only when neither applies.
4. Add a short noun scope only when it helps identify the affected area.
5. Mark every incompatible change with `!`, a `BREAKING CHANGE:` footer, or both. Explain the
   incompatibility and any migration requirement.
6. Write the summary as a concise description of the change. Add a body for context, rationale,
   or consequences, and add valid footers for references or acknowledgements.
7. Validate the result against every applicable rule in the specification reference.
8. Before executing a commit, show or otherwise verify the exact message against the staged diff.
   Do not stage unrelated user changes.

Use this shape:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

## Pull Requests and Merges

- Format a pull-request title as a Conventional Commit because it commonly becomes the squash or
  merge commit subject.
- Keep the pull-request body readable prose; it need not use commit-message grammar. State
  breaking changes explicitly and ensure the eventual merge message carries the required marker.
- When one pull request contains several change categories, choose the title that represents the
  release-relevant primary outcome. Prefer splitting the pull request when the changes are truly
  independent.
- Revalidate the final squash or merge message; a compliant branch history does not guarantee a
  compliant merge commit.

## Output

When asked only to propose a message, return the exact message in a code block followed by a brief
explanation only if the type, scope, or release impact is not self-evident. When asked to commit or
create a pull request, use the validated message directly and report it after the action succeeds.
