# Rules by doc type

Use this reference for the page that you write or restructure now. Do not apply each list to each
page. A page that has two types, for example a README with a quick start and a config reference, gets
the rules of each part.

## Tutorials and getting-started guides

_Goal: take a new user from zero to a working result._

- Keep one happy path. Do not let the page become a decision tree.
- State the prerequisites, the required setup, and the expected end state at the start. Put them
  inline or in a collapsible block.
- After each major step, add a concrete verification checkpoint: "You should now see
  `Server listening on :8080`."
- Move detours, alternatives, and corner cases to separate how-to pages.
- End each major stage with a short troubleshooting list. Or link to a central troubleshooting
  section, and give a one-line summary of its content.

## How-to guides (task pages)

_Goal: do one specific task._

- State the goal in the title and in the first sentence. Make each title distinct enough that an
  agent can select it from a list of search results.
- List the prerequisites, constraints, required permissions, and defaults, so that the page works
  alone.
- End with a **Common failures and recovery** section.
- For a long workflow, divide the page into phases. Make each phase work alone, with its own
  prerequisites and its own verification.
- Make sure that no step needs a screenshot or other media to be understood.

## Reference (API, CLI, config, schema)

_Goal: let the reader find exact facts._

- Be exhaustive but structured. Length is satisfactory here, because lookups degrade much less than
  planning tasks. Still keep the length reasonable.
- Use stable, predictable headings and one term for each concept.
- Give each parameter: name, type, required, default, allowed values, description, and example.
- Keep prose to a minimum.

## Concepts and architecture explanations

_Goal: explain why and how something works._

- Do not make an explanation page the only location of an important fact. A summary removes prose
  first. Repeat each constraint on the reference pages and the task pages.
- Add a short block of concepts and definitions for project terms. An agent that comes from search
  or from a different page can then identify each term.
- Add comparison tables, for example "X vs Y" or "when to use which". Tables survive the text
  conversion, and an agent can fetch them easily.

## Error and troubleshooting pages

_Goal: go from a symptom to a fix._

- Write one entry for each error, with the exact message, the causes, and the solutions. Refer to
  the error entry in [templates.md](templates.md).
- Use the error code or the literal message as the title or heading, so that search and retrieval
  find it.
- Group the entries by component or module, not in one very long list.

## README files

A README is usually the first page that an agent fetches. It has more than one part. Apply these
rules in addition to the rules of each part:

- In the first paragraph, state what the project does and for whom. Do not start with badges,
  history, or marketing text.
- Give the install command and the first command to run near the top, with the expected output.
- Link to the full docs, and give the one fact that the reader needs from each link.
- Put the supported versions and the required environment in a table or a list, not in prose.
- Keep the README a landing page. For errors, give a table with one line for each code or exit
  status. Put the full error entries on an errors page. If no errors page exists and the user did
  not ask for one, name it as a suggestion.
