# STE for software and agent text

ASD-STE100 was written for aerospace maintenance documentation. This reference tells you how to use STE for software text and agent text. It gives the text-type classification, the deviation profile, and a worked example for each artifact type.

## Contents

- [Why STE helps a software text](#why-ste-helps-a-software-text)
- [Classify the artifact](#classify-the-artifact)
- [The deviation profile](#the-deviation-profile)
- [Prompts, system messages, and agent instructions](#prompts-system-messages-and-agent-instructions)
- [Tool descriptions and parameter descriptions](#tool-descriptions-and-parameter-descriptions)
- [Log messages and error messages](#log-messages-and-error-messages)
- [Code comments and docstrings](#code-comments-and-docstrings)
- [README files and markdown documentation](#readme-files-and-markdown-documentation)
- [AGENTS.md and agent configuration files](#agentsmd-and-agent-configuration-files)
- [The before-and-after comparison](#the-before-and-after-comparison)
- [What STE does not control](#what-ste-does-not-control)

## Why STE helps a software text

A software text has three readers: a person, a translation engine, and a different agent. The three readers fail in the same way. They fail when one sentence has two meanings.

STE removes the frequent causes of two meanings:

- A word with two parts of speech. "Check the lock state" can be a command or a noun phrase.
- A long multi-word noun. "user request rate limit config" has no clear structure.
- A pronoun with two possible referents. "It returns null" does not identify the function.
- The passive voice with no agent. "The file is deleted" does not tell you what deletes it.
- A phrasal verb. "Back up the store" and "back up" have different meanings.

A model that reads an ambiguous instruction must select one meaning. STE removes the selection.

## Classify the artifact

The text type controls the sentence limit and the verb form.

| Artifact                       | Type        | Verb form  | Limit    |
| ------------------------------ | ----------- | ---------- | -------- |
| Agent instruction, work step   | Procedural  | Imperative | 20 words |
| Tool description (what it is)  | Descriptive | Present    | 25 words |
| Tool description (when to use) | Procedural  | Imperative | 20 words |
| Parameter description          | Descriptive | Present    | 25 words |
| Log message, error message     | Descriptive | Present    | 25 words |
| Error remedy                   | Procedural  | Imperative | 20 words |
| Code comment, docstring        | Descriptive | Present    | 25 words |
| README overview                | Descriptive | Present    | 25 words |
| README installation steps      | Procedural  | Imperative | 20 words |
| AGENTS.md rule                 | Procedural  | Imperative | 20 words |

One file contains the two types. Classify each sentence, not each file.

## The deviation profile

Keep this content unchanged. STE does not control it:

1. **Code.** Source code, commands, configuration, and command output.
2. **Identifiers.** Function names, variable names, type names, file paths, and URLs. They are technical nouns in category 19, and rule 2.1 does not count their internal words.
3. **Emitted strings.** An error string that a system emits is quoted text (category 10). It counts as one word (rule 8.6).
4. **Markdown structure.** Headings, lists, tables, code fences, links, and frontmatter. STE does not give rules for formatting.
5. **Proper nouns.** Product names, organization names, and standard names.

Record each deviation. Do not use a deviation to keep a word that an approved word can replace.

## Prompts, system messages, and agent instructions

A prompt is procedural text. Each instruction must be a command. Remove each modal verb that is not "must" or "can".

> Not STE: You should try to ensure that the response is formatted appropriately, and you may want to include examples if it would be helpful.
>
> STE: Write the response in the specified format. If an example makes the format clear, include one example.

Rules that the example uses: 5.3 (imperative), 3.4 (no complex auxiliary construction), 1.1 (`ensure`, `appropriately`, and `helpful` are not approved), 5.1 (20 words).

Give one instruction in each sentence (rule 5.2). Put a list of conditions in a vertical list (rule 4.3).

> Not STE: Before making changes, review the existing tests, check the build configuration, and make sure you haven't broken any downstream consumers.
>
> STE: Before you change the code, do these steps:
>
> 1. Read the existing tests.
> 2. Do a check of the build configuration.
> 3. Make sure that the downstream consumers still operate.

## Tool descriptions and parameter descriptions

A tool description has two parts. The first part tells the model what the tool is. The second part tells the model when to use the tool. Write the first part in descriptive style and the second part in procedural style.

> Not STE: Utility that can be leveraged to retrieve records from the datastore, optionally filtering by a variety of criteria. Should be used whenever you need data.
>
> STE: This tool reads records from the datastore. You can filter the records by date, by owner, or by status.
>
> Use this tool when you must get a record and you know the record identifier. Do not use this tool to write a record.

Rules that the example uses: 1.1 (`utility`, `leverage`, `retrieve`, `criteria` are not approved), 3.6 (active voice), 3.5 (no `-ing` form as a verb), 5.3 (imperative), 9.4 (consistent terminology for `record`).

Write a parameter description as one descriptive sentence. Give the type, the meaning, and the default value.

> Not STE: timeout - How long to wait (optional)
>
> STE: `timeout` - The maximum time in seconds before the request stops. The default is 30.

Use the same technical noun each time (rule 1.11). Do not write "record" in one sentence and "entry", "row", or "item" in the next sentence.

## Log messages and error messages

A log message is descriptive. It tells the reader what occurred. Use the simple past tense or the simple present tense.

> Not STE: Failed retrieving user prefs; falling back to defaults
>
> STE: The server did not read the user preferences. The server uses the default preferences.

Rules that the example uses: 8.1 (no semicolon), 3.5 (no `-ing` form as a verb), 4.2 (no omitted words), 3.6 (active voice, with an agent).

An error message has two parts. The first part is descriptive and gives the cause. The second part is procedural and gives the remedy.

> Not STE: Invalid configuration
>
> STE: The configuration file has an incorrect value for `port`. Set `port` to a number between 1 and 65535.

Identify the item that caused the error. Do not write "it" or "this" (GR-3 and GR-4).

## Code comments and docstrings

A comment is descriptive. Give the topic first, then the details (rule 6.1). Keep one topic in each paragraph (rule 6.5).

> Not STE: This is a bit of a hack - basically we're just working around the fact that the upstream lib doesn't handle nulls properly, so we're pre-filtering.
>
> STE: The upstream library causes an error when a value is null. Thus, this function removes each null value before it calls the library.

Rules that the example uses: 1.1 (`hack`, `basically`, `properly` are not approved), 1.10 (no slang), 4.2 (no contractions), 3.5 (no `-ing` form as a verb), 3.6 (active voice).

Write a docstring summary as one sentence in the simple present tense. Do not use the imperative form, because a docstring is descriptive.

> Not STE: Parse the config and return a dict.
>
> STE: This function reads the configuration file and gives a dictionary.

## README files and markdown documentation

Classify each block. An overview is descriptive. An installation procedure is procedural.

> Not STE: Simply run the installer and you should be good to go - it'll handle all the dependencies for you automatically.
>
> STE: Run the installer. The installer gets all the dependencies.

Give the information gradually (rule 6.1). Write a maximum of six sentences in each paragraph (rule 6.6).

Use a vertical list when a sentence contains three items or more (rule 4.3). Each list item is a different sentence, and each item has its own word limit (rule 8.4).

Do not use marketing words. The dictionary does not approve "powerful", "seamless", "robust", "blazing", or "simply".

## AGENTS.md and agent configuration files

An AGENTS.md file gives instructions to an agent. Thus, it is procedural text.

> Not STE: Tests should generally be run before committing, though it's fine to skip them for docs-only changes.
>
> STE: Run the tests before you make a commit. If the commit changes only documentation, you can skip the tests.

Rules that the example uses: 5.3 (imperative), 1.1 (`should` and `generally` are not approved), 4.2 (no contractions), 5.1 (20 words).

Write a rule as a command, not as a preference. STE has "must" and "can". It does not have "should", "may", "might", or "would". This removes the ambiguity between a requirement and a recommendation.

| Intent         | STE form                                 |
| -------------- | ---------------------------------------- |
| Requirement    | Use the imperative form, or "must"       |
| Prohibition    | "Do not ..." or "must not"               |
| Permission     | "You can ..."                            |
| Recommendation | "It is better to ..." or "RECOMMEND (v)" |

## The before-and-after comparison

The default output is the new text only. When the user asks for a comparison, give a table. Give one row for each change, and give the rule number.

| Rule | Before                          | After                                              | Cause                                           |
| ---- | ------------------------------- | -------------------------------------------------- | ----------------------------------------------- |
| 1.1  | ensure                          | make sure that                                     | `ensure` is not approved in the dictionary      |
| 3.6  | The file is deleted             | The agent deletes the file                         | Passive voice with a known agent                |
| 5.1  | 34 words                        | Two sentences                                      | A procedural sentence has a maximum of 20 words |
| 2.1  | request rate limit config value | the configuration value for the request rate limit | A multi-word noun has a maximum of three words  |
| 8.1  | `a; b`                          | `a. b`                                             | STE does not permit the semicolon               |

When a rule and the meaning are in conflict, keep the meaning. Then tell the user which rule you did not obey, and why. Rule 9.1 lets you write the sentence again with a different construction, and this method usually removes the conflict.

## What STE does not control

The specification states that STE does not give rules for these subjects:

- **Abbreviations.** Different industries use different abbreviations.
- **Text formatting.** Typeface, numbering, and lettering are not in scope.
- **Units of measurement.** The project or the company must select the method.
- **General punctuation.** Refer to an external style guide.

STE cannot operate alone. Use it with your project style guide and your terminology database. A high level of English is necessary to write STE correctly.
