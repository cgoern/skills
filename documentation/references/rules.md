# The five rules, with causes and examples

This reference gives the full form of the five rules in [SKILL.md](../SKILL.md). Each rule has a
priority for each channel, the causes, the actions, and an example. Read this file when you must
explain a rule to the user, or when the short form in SKILL.md does not decide a case.

The percentages here are approximate values that the source rule sheet reports. The rule sheet does
not cite the studies. Use the values as a direction, not as exact measurements.

## Contents

- [How agents read the docs](#how-agents-read-the-docs)
- [Rule 1 - Make each section self-contained](#rule-1---make-each-section-self-contained)
- [Rule 2 - Document errors, failure modes, known issues, and edge cases](#rule-2---document-errors-failure-modes-known-issues-and-edge-cases)
- [Rule 3 - Do not reorganize pages for positional bias](#rule-3---do-not-reorganize-pages-for-positional-bias)
- [Rule 4 - Control page length, use structure, and state importance](#rule-4---control-page-length-use-structure-and-state-importance)
- [Rule 5 - Write tool and function definitions as documentation](#rule-5---write-tool-and-function-definitions-as-documentation)

## How agents read the docs

| Channel | What the agent sees | Unit | Consequence for the writer |
| ------- | ------------------- | ---- | -------------------------- |
| Web search and fetch | Search gives only titles and URLs, with no body text. The agent selects a URL by its title, then fetches the page as markdown or plain text. | The full page | Each title must be distinct and descriptive. Five pages with the title "Overview" give the agent nothing to select. Headings, code blocks, and tables survive the conversion. Images, diagrams, and JavaScript content do not. |
| Retrieval (RAG): support bots, docs search, in-repo assistants | The docs are divided into chunks, usually at H2 and H3 headings. Many chunks from unrelated pages go into the context together. | One heading section | The agent reads each section without its neighbors. Retrieval is usually semantic, thus the agent often cannot get "the chunk before this one". |
| Tool or function calling | Tool names, descriptions, and parameter schemas go directly into the context. | One tool definition | These definitions are documentation. An ambiguous name or description causes an incorrect tool choice or incorrect arguments. |

These implications apply to the three channels:

- Do not make a fact depend on a screenshot, a diagram, or a video. Also give the fact in text.
- Content that loads on click, on a tab change, or by client-side routing can be absent for the
  agent. Content that is visually hidden but present in the HTML is satisfactory.
- Code tabs that keep each language variant in the page source are visible to agents. A selector
  that loads a different page is not. The agent sees only the default variant.
- To test a page, tell an agent to fetch it and save the raw output to a file. Content that is not in
that file is not available to any agent.

## Rule 1 - Make each section self-contained

**Priority:** high for retrieval and tool definitions. Lower for a full-page fetch, but it still
helps.

### Causes

- A retrieved chunk arrives without its surroundings. "Use the config object from above" has no
  meaning for the agent.
- When a referenced fact is not there, an agent rarely stops to say so. The agent fills the gap with a
  plausible guess. This is a major cause of hallucinated parameters, paths, and commands.
- Agents have a step limit, often near 100 to 200 actions. Each "see the previous page" uses steps
  to find context instead of to do the task.
- When the same information is divided across more documents, retrieval becomes worse, even at the
  same total length. The rule sheet reports accuracy decreases of up to approximately 20%.
- Self-contained sections also give protection against context compression. If a summary loses a
  constraint from one page, the agent can find it again in a different location.

### Actions

- Do not use backward or forward references: "see above", "as described earlier", "same as before",
  "as mentioned in the previous section", "the steps above".
- Repeat the critical facts instead: the name of the object, the required flag, the env var, the
  version. Do not copy full sections. Repeat only what the section needs to work alone.
- When you must link, link and summarize: "Requires an API token with `write` scope (see
  Authentication)."
- Start each task page with a **Before you begin** block: prerequisites, required versions,
  permissions, env vars, and the assumed state.
- Use the same name for an item everywhere. A chunk cannot tell that "workspace", "project", and
  "org" are the same concept.
- Put repeated setup steps in collapsible blocks. People who did the setup can skip it, and agents
  still get it. This works only when the content is in the page source.
- Write as if a reader can quote each section alone, out of context.

### Example

| Avoid | Prefer |
| ----- | ------ |
| "Now pass the client from step 2 to the handler." | "Pass the `ApiClient` instance (created with your API token) to `registerHandler()`." |
| "Set the same variables as before." | "Set `DATABASE_URL` and `REDIS_URL` (both required)." |
| "Run the command above again with the flag." | "Run `make migrate --dry-run`." |

## Rule 2 - Document errors, failure modes, known issues, and edge cases

**Priority:** high for the three channels. Here the needs of agents and people are most different.
People skim past this content. Agents depend on it.

### Causes

- Agents have the most difficulty with information that nobody wrote down: team conventions,
  workarounds, and project context that general knowledge does not give.
- Agents that get structured failure information recover from errors much better than agents that
  must reason from general knowledge.
- Vague guidance ("consider edge cases", "be careful with X") gives worse results than explicit
  instructions with concrete examples and edge cases. The rule sheet reports accuracy increases of
  approximately 10% to 37%.

### Actions

1. Make an error catalog first. It is the easiest improvement, and it also helps people.
    - Write one entry for each error code, exception type, or exit code.
    - Give each entry the exact message, the type or category, the severity, a description, the
      possible causes, and the possible solutions. Refer to [templates.md](templates.md).
    - Quote error strings, codes, and types exactly as the code emits them. Do not paraphrase. The
      agent searches for the literal string that it saw.
    - If you control the API or the CLI, put a link to the applicable docs entry in the error
      response.
2. Add a debugging or troubleshooting section to each product area or module, not only one global
   page.
3. Then add the edge cases and the known issues.
    - Errors go in central catalog pages.
    - Edge cases go in sections on the page of the feature that they affect.
    - State known bugs and limitations plainly, with the workaround.
4. Find the content in these sources: issues closed as "won't fix", changelogs and release notes
   (breaking changes and behavior changes), support threads, user questions, and frequent CI
   failures. An agent can draft the frequent patterns from these sources. A person must then
   examine the draft.

### Placement that does not clutter the page for people

- Put troubleshooting in collapsible sections at the bottom of each main page. If the pages become
  too long, use a dedicated area in the sidebar or a folder.
- Collapsible content must be in the page source. If the tooling loads it on click, use a separate
  page.

## Rule 3 - Do not reorganize pages for positional bias

**Priority:** low. This rule mostly tells you where not to spend time.

### Causes

- In one model call, the model uses information at the start and at the end of the context more
  reliably than information in the middle ("lost in the middle").
- In an agent loop, neither you nor the agent controls where your page lands in the context. The
  agent can read it at step 2 or at step 47.
- The bias is not stable. Up to approximately half the context window, the start-and-end pattern
  applies. Near the context limit, recency is dominant, and the last content gets the most attention.

### Actions

- Do not change the page structure to control where content falls in the context window.
- Put the most important point first in each section. This still helps people and chunk retrieval.
- Give each page one distinct concept, and keep the page coherent. This helps agents more than an
  order trick.

## Rule 4 - Control page length, use structure, and state importance

**Priority:** high for a full-page fetch. Medium for retrieval and tool definitions.

### Causes

- A long context has a cost. Model performance decreases gradually as the context increases, and
  the decrease is clearer from approximately 30k tokens (approximately 22k words). Few single doc
  pages are that long.
- Task complexity changes the limit. Simple lookups stay accurate in very long contexts. Multi-step
  tasks that need planning and reasoning start to fail at approximately 16k to 33k tokens.
- Those values come from clean, single-call tests. In a real agent run, the context at step 10
  already contains logs, reasoning, tool output, and other pages. Your page gets much less space.
- When the context is full, agents compact it, usually with a model summary of the history. A
  summary predictably removes repeated content, long logs, narrative and meta prose, and
  formatting. Structured content survives much better.

### Actions

Make the length agree with the reasoning complexity, not with the topic size:

| Page kind | Length |
| --------- | ------ |
| Lookup content: parameter and config references, auth details, error tables, CLI flag lists | Long is satisfactory. Be exhaustive but structured. Stay much below approximately 22k words. |
| Multi-step workflows with branches, state, or order | Keep short. Divide into phases that each work alone. |

- State importance in words: _key_, _critical_, _required_, _optional_, _default_, _forbidden_,
  _deprecated_. Do not use only bold or color. Formatting is among the first things that a summary
  removes.
- Put constraints and defaults in a structured form, not in narrative:
    - Tables for parameters: name, type, required, default, allowed values, description.
    - YAML or JSON schemas for config.
    - MUST, SHOULD, and MUST NOT callouts for rules.
- Remove filler: intros that repeat the title, "in this section we will", and marketing text. It
  uses tokens, and a summary removes it first.
- Use this rule together with Rule 1. If a constraint is in more than one self-contained location,
  the loss from one summary does not remove it.

Refer to [templates.md](templates.md) for a constraint callout.

## Rule 5 - Write tool and function definitions as documentation

**Priority:** high when the project exposes tools, functions, or API operations that an agent calls.

### Causes

- The name, the description, and the parameter schema are the full agent knowledge of a tool. They
  are the documentation.
- Inconsistent terms make tool use measurably worse. If descriptions alternate between _rate limit_,
  _quota_, and _throttle_, or between _archive_, _deactivate_, and _disable_, the model must guess
  whether they are one concept or different concepts.
- Models select tools almost only by how well the description agrees with the user request. A
  strong tool with a vague description loses to a weaker tool with a clear description.

### Actions

- Describe what the tool does for the user, not how it is implemented. "Creates a shareable payment
  link for a product and price" is better than "Wraps the link service POST endpoint."
- Use one term for each concept in tool names, descriptions, parameters, error messages, and the
  docs. Keep a glossary and enforce it.
- Use one naming pattern for all tools, for example `verb_noun`: `create_invoice`, `list_invoices`,
  `void_invoice`.
- Do not give two tools overlapping scopes. If two tools can do the same request, merge them, or
  state in each description when to use it instead of the other.
- Give precise parameter descriptions: type, unit, format, allowed values, default, required or
  optional, and an example value. "id: the id" is not a description.
- Document the failure behavior: the errors that the tool can return, and the next action for the
  agent (retry, ask the user, or call a different tool).
- Remove each ambiguity. If a human reviewer must ask "which one?", the model guesses.

### Example

| Avoid | Prefer |
| ----- | ------ |
| `name: handle_auth`, `description: handle auth stuff` | `name: refresh_access_token`, `description: Exchanges a refresh token for a new access token when the current one has expired (HTTP 401). Returns the new token and its expiry in seconds.` |
| `limit: max items` | `limit (integer, optional, 1-100, default 20): maximum number of invoices to return per page.` |
