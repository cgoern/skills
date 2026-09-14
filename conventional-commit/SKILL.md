---
name: conventional-commit
description: Enforce Conventional Commits 1.0.0 and produce compliant Git and pull-request metadata. An agent MUST use this skill in these contexts. The agent creates, amends, squashes, rebases, rewords, or recommends a commit. The agent creates or edits a pull request. The agent prepares a merge message or a squash message. The agent writes a release entry or a changelog from commits. The agent chooses commit types, scopes, breaking-change markers, footers, or semantic-version effects. This skill writes commit text and pull-request text. This skill does not review the code change itself.
---

# Conventional Commit

Apply Conventional Commits 1.0.0 to every commit-facing workflow.

This file carries the common case. A message of the form `type(scope): description`, with an
optional body, needs no reference file. Read
[`references/specification.md`](references/specification.md) only in these conditions:

- The change is incompatible, and you must select between the `!` marker and the footer.
- The message has more than one footer, or a footer value continues on more than one line.
- You must select a type that is not `feat`, `fix`, `docs`, `chore`, `refactor`, or `test`.
- You write a squash message, a merge message, a release entry, or a changelog from many commits.
- A tool rejected a message, and you must find the rule that the message does not obey.

## Workflow

1. Examine the complete change set and the repository conventions first. Then select a message.

2. Divide unrelated changes into distinct commits when practical. Do not hide multiple independent
   intents behind one type.

3. Select `feat` for a new capability. Select `fix` for a bug correction. Select another type that
   the repository accepts only when neither is applicable.

4. Add a short noun scope only when the scope helps to identify the affected area.

5. Identify every incompatible change with `!`, with a `BREAKING CHANGE:` footer, or with the two
   markers together. Explain the incompatibility and each migration requirement.

6. Write the summary as a concise description of the change. Add a body for context, rationale, or
   consequences. Add correct footers for references or acknowledgments.

7. Validate the result against every applicable rule in the specification reference.

8. Before the commit occurs, make sure that the exact message agrees with the staged diff. Show the
   message, or use a different method for this check. Do not stage unrelated user changes.

Use this shape:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

## Pull Requests and Merges

- Format a pull-request title as a Conventional Commit, because the title commonly becomes the
  squash or merge commit subject.

- Keep the pull-request body in readable prose. The body does not need commit-message grammar.
  State each breaking change explicitly. Make sure that the eventual merge message carries the
  necessary marker.

- When one pull request contains more than one change category, select the title that shows the
  release-relevant primary outcome. It is better to divide the pull request when the changes are
  truly independent.

- A compliant branch history does not guarantee a compliant merge commit. Thus, validate the final
  squash or merge message again.

## Output

When the user asks only for a proposed message, give the exact message in a code block.
Add a short explanation only when the type, the scope, or the release impact is not self-evident.

When the user asks for a commit or for a new pull request, use the validated message directly.
Then tell the user the message after the action succeeds.
