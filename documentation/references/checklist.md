# Review checklist

Run this checklist for each project. Also run it for each of the pages that agents use most:
README, setup, API reference, errors, and tool definitions. In a review, report each item that
fails, with the file, the heading or line, and the correction.

## Findability and rendering

- [ ] Each page title is distinct and says what the page is for. No duplicate "Overview" or
      "Introduction" titles.
- [ ] No fact is available only in an image, a diagram, or a video.
- [ ] No instruction refers to a visual position or a color ("the button on the right").
- [ ] Content behind tabs, toggles, and collapsible blocks is in the page source, and does not load
      on click.
- [ ] Verified: an agent fetch of a key page, saved to a file, contains each important fact.

## Self-contained sections

- [ ] No "see above", "as before", "previous section", or "the steps above".
- [ ] Each link to a different page also states the one fact that the reader needs from it.
- [ ] Task pages start with a **Before you begin** block: prerequisites, versions, permissions, and
      env vars.
- [ ] A reader can understand and do each H2 and H3 section when it is read alone.
- [ ] One term for each concept, the same across the project.

## Errors and edge cases

- [ ] An error catalog exists, with one entry for each code, exception, or exit code.
- [ ] Each entry has the exact message, the causes, and the solutions.
- [ ] Error strings are quoted exactly from the code.
- [ ] Each module or component has a troubleshooting section.
- [ ] Known bugs, limitations, and edge cases have documented workarounds.
- [ ] "Won't fix" issues, changelogs, and support questions were examined for missing content.

## Length, structure, and importance

- [ ] Multi-step workflows are short, or divided into phases that each work alone.
- [ ] Constraints and defaults are in tables, schemas, or MUST, SHOULD, and MUST NOT callouts, not
      in prose.
- [ ] Importance is stated in words (required, optional, default, critical, forbidden), not only in
      formatting.
- [ ] Critical constraints are in more than one location, never only on a concept page.
- [ ] Each section starts with its most important point. No filler intros.

## Tool and function definitions

- [ ] Descriptions say what the tool does for the user, not how it works.
- [ ] Names follow one consistent pattern.
- [ ] No two tools have overlapping scopes without a statement of when to use which.
- [ ] Each parameter has a type, a unit or format, allowed values, a default, and a required or
      optional status.
- [ ] The possible errors and the next action for each are documented.
