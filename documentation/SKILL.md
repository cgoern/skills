---
name: documentation
description: Write, restructure, or review project documentation so that coding agents, retrieval systems, and people can all use it. Covers READMEs, tutorials, getting-started guides, how-to pages, API, CLI, and config references, concept and architecture pages, error catalogs, troubleshooting pages, and the tool or function definitions that an agent calls. Use this skill when the user asks to write docs, improve docs, audit docs, make docs agent-friendly or LLM-friendly, add an error catalog or a troubleshooting section, or document a tool schema, even if the user does not mention agents. This skill controls the structure and the content of a page - self-contained sections, errors and edge cases, page length, and importance markers. For sentence-level wording, use simplified-technical-english.
---

# Documentation

Agents now read documentation more than people do. An agent reads a page in fragments, out of
order, with a limited budget of steps and context. Thus write each section so that it works alone.
Put errors and code before prose. State importance in words.

Do not write a separate set of "agent docs". Almost every rule in this skill also makes the docs
better for people. Where agent needs and human needs are in conflict, the rule gives a layout that
serves the two.

## Load the guidance

This file carries the workflow and the five rules in short form. Do not load a reference file that
the task does not need. Read a reference file only in the condition that its row gives.

| Read                                            | Only when                                                                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [rules.md](references/rules.md)                 | You must give the cause or the evidence for a rule, you need a before-and-after example, or a rule is not clear |
| [doc-types.md](references/doc-types.md)         | You write or restructure a tutorial, a how-to page, a reference page, a concept page, or a troubleshooting page |
| [templates.md](references/templates.md)         | You write an error entry, a constraint callout, a parameter table, or a tool definition |
| [checklist.md](references/checklist.md)         | The user asks for a review or an audit, or you complete a large documentation change                            |

## Workflow

### 1. Identify how agents get the docs

Agents get documentation through three channels. Find the channels that apply to the project, and
optimize for those first.

| Channel                     | Unit that the agent reads | Main consequence                                                                     |
| --------------------------- | ------------------------- | ------------------------------------------------------------------------------------ |
| Web search and fetch        | The full page             | Search shows only titles and URLs. Images, diagrams, and JavaScript content are lost. |
| Retrieval (RAG, docs search) | One H2 or H3 section      | Each section arrives without its neighbors. "See above" points at nothing.           |
| Tool or function calling    | One tool definition       | The name, the description, and the parameter schema are the full documentation.      |

For each channel:

- Do not put a fact only in an image, a diagram, or a video. Also give the fact in text. Write
  "click **Save**", not "click the green button in the image".
- Make sure that content behind tabs, toggles, and collapsible blocks is in the page source. An agent
  does not see content that loads on click or on a route change.

### 2. Identify the doc type

The doc type controls the priorities. Read [doc-types.md](references/doc-types.md) for the full
list of each type.

| Doc type                  | Goal                         | First priority                                              |
| ------------------------- | ---------------------------- | ----------------------------------------------------------- |
| Tutorial, getting started | Zero to a working result     | One happy path, with a verification checkpoint after each major step |
| How-to (task page)        | Do one specific task         | Goal in the title, prerequisites first, "Common failures and recovery" last |
| Reference                 | Look up exact facts          | Exhaustive and structured, minimal prose                    |
| Concept, architecture     | Explain why and how          | Never the only location of an important fact                |
| Error, troubleshooting    | Go from a symptom to a fix   | One entry for each error, with the literal message as the heading |
| Tool definition           | Correct tool and arguments   | What the tool does for the user, and one term for each concept |

### 3. Collect the facts from the source

Take each error string, default value, flag, environment variable, version, and prerequisite from
the code, the config, the changelog, or the tests. Do not write these facts from memory. An agent
that reads the docs searches for the literal string that it saw.

If you cannot find a fact, do not guess. Mark the gap as an open question for the user.

### 4. Apply the five rules

**Rule 1 - Make each section self-contained.** A retrieved chunk arrives alone. When a referenced
fact is not there, an agent usually guesses and does not stop.

- Do not write "see above", "as before", "the previous section", or "the steps above".
- Repeat the critical facts that the section needs: the object name, the flag, the env var, the
  version. Do not copy full sections.
- Repeat a fact only in a section that needs it to work alone. Do not add a summary section, for
  example "Critical rules" or "Notes for agents", that repeats the other sections of the same page.
  A repeat in each section protects against retrieval. A summary of repeats only makes the page
  longer.
- When you link, also give the one fact that the reader needs from the link:
  "Requires an API token with `write` scope (see Authentication)."
- Start each task page with a **Before you begin** block: prerequisites, versions, permissions,
  env vars, and the state that the page assumes.
- Use one name for each item everywhere. A chunk cannot tell that "workspace" and "project" are the
  same item.

**Rule 2 - Document errors, failure modes, known issues, and edge cases.** People skim this content.
Agents depend on it.

- Make an error catalog first. Write one entry for each error code, exception type, or exit code.
- Quote each error string exactly as the code emits it. Do not paraphrase.
- Add a troubleshooting section to each module or product area, not only one global page.
- Put each edge case next to the feature that it affects. State each known bug with its workaround.
- Find the absent content in "won't fix" issues, changelogs, release notes, support threads, and
  frequent CI failures.

**Rule 3 - Do not reorganize pages for positional bias.** You cannot control where a page lands in
the agent context. Put the most important point first in each section, and keep one concept on each
page. Do not spend more time on the order.

**Rule 4 - Control page length, use structure, and state importance in words.**

- Make the length agree with the reasoning complexity, not the topic size. A lookup page can be
  long and exhaustive. Keep a multi-step workflow short, or divide it into phases that each work
  alone.
- State importance with words: _required_, _optional_, _default_, _critical_, _forbidden_,
  _deprecated_. Context compression removes bold and color first.
- Put constraints and defaults in tables, YAML or JSON schemas, or MUST, SHOULD, and MUST NOT
  callouts. Do not put them in narrative prose.
- Remove filler: intros that repeat the title, "in this section we will", and marketing text.
- Put each long lookup part on its own page: the full error catalog, the full config reference.
  On the task page, give a one-line summary and a link. A revision that doubles the length of a
  page needs a cause that you can name.

**Rule 5 - Write tool and function definitions as documentation.**

- Describe what the tool does for the user, not how it works.
- Use one term for each concept in names, descriptions, parameters, errors, and docs. Do not
  alternate between synonyms, for example "rate limit", "quota", and "throttle".
- Use one naming pattern for all tools, for example `create_invoice`, `list_invoices`.
- Do not give two tools overlapping scopes. If two tools can do the same request, state in each
  description when to use it instead of the other.
- Give each parameter its type, unit or format, allowed values, default, required or optional
  status, and an example value.
- State the errors that the tool can return, and the next action for each: retry, ask the user, or
  call a different tool.

### 5. Verify the result

1. When the docs are published, fetch one key page with an agent and save the raw output to a file.
   Content that is not in that file is not available to any agent.
2. Read each changed H2 and H3 section alone. Make sure that you can do the task from that section.
3. Run [checklist.md](references/checklist.md) for a review, an audit, or a large change.

## Output format

For a new page or a revision, give the page first. Then give a short list of the structural changes,
and the open questions for facts that you could not find in the source.

For a review, give the findings grouped by the sections of [checklist.md](references/checklist.md).
For each finding, give the file, the heading or line, the rule, and the correction. Give the
findings with the most effect on agents first: missing errors, broken self-containment, and missing
constraints.

Do not restructure a full documentation set when the user asks for one page. Record the other
findings as suggestions.

## Source

This skill restates the "Docs for Agents - Guide & Checklist" rule sheet by Christopher Görn
(2026-10-16). The percentages in [rules.md](references/rules.md) are approximate values that
the rule sheet reports.

The skill does not cite the original studies. Use the percentages as a
direction, not as exact measurements.
