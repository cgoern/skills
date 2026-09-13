---
name: simplified-technical-english
description: Rewrite or review text in ASD-STE100 Simplified Technical English (STE), controlled English that removes ambiguity for agents, translators, and non-native readers. Covers prompts, system messages, tool and parameter descriptions, agent instructions, log and error messages, code comments, docstrings, READMEs, and AGENTS.md - even if the user only says "simplify this" or "make it unambiguous".
---

# Simplified Technical English

ASD-STE100 Simplified Technical English (STE) is a controlled natural language and an international standard for technical documentation. STE has two parts:

- Part 1 gives 53 writing rules in nine sections.
- Part 2 gives a dictionary of 875 approved words and 1274 words that are not approved.

The function of STE is to remove ambiguity before a reader, a translation engine, or a different agent gets the text. This skill text obeys STE. Refer to [Deviations](#deviations).

## Load the guidance

Read the applicable reference before you write or examine a text:

- [references/writing-rules.md](references/writing-rules.md) gives the 53 rules and the eight general recommendations. Read it for all tasks.
- [references/word-choice.md](references/word-choice.md) gives the dictionary principles, the approved verbs, the technical noun and technical verb categories, and the frequent errors. Read it when you select or replace words.
- [references/software-adaptation.md](references/software-adaptation.md) shows how to use STE for prompts, tool descriptions, log messages, code comments, and markdown documentation. Read it when the text is software content.

## Workflow

### 1. Identify the text type

STE has different rules for the two text types. The type controls the sentence length and the permitted verb forms.

| Text type   | Function                           | Verb form            | Maximum words in a sentence |
| ----------- | ---------------------------------- | -------------------- | --------------------------- |
| Procedural  | Tells the reader to do an action   | Imperative (command) | 20                          |
| Descriptive | Gives information, not instruction | Not imperative       | 25                          |

One text can contain the two types. Examine each sentence with the rules for its own type. A safety instruction is procedural. A note is descriptive, and a note must not give an instruction.

### 2. Identify the deviation profile

Some content cannot obey STE. Identify this content first and keep it unchanged:

- Code, identifiers, file paths, commands, and command output
- Quoted text, labels, and error strings that a system emits
- Names of persons, products, organizations, and standards
- Markdown structure, links, and tables

Record each deliberate deviation. Report the deviations with the result.

### 3. Correct the words

1. Use only words that are approved in the dictionary, technical nouns, or technical verbs.
2. Use each approved word with one part of speech and one meaning.
3. Replace each word that is not approved. Refer to the frequent-error list in [references/word-choice.md](references/word-choice.md).
4. Use the same technical noun for the same item each time. Do not use synonyms.
5. Write multi-word nouns with a maximum of three words.
6. Use American English spelling.

### 4. Correct the verbs

1. Use only these verb forms:
    - The infinitive form
    - The imperative form
    - The simple present tense
    - The simple past tense
    - The simple future tense
    - The past participle form, as an adjective
2. Do not use auxiliary verbs to make complex verb constructions.
3. Use the "-ing" form only as a technical noun or as a modifier in a technical noun.
4. Use the active voice. In descriptive writing, use the passive voice only when the agent is unknown.
5. Give the action with a verb, not with a noun.

### 5. Correct the sentences and the paragraphs

1. Write short sentences. Obey the word limit for the text type.
2. Do not omit words and do not use contractions.
3. Put complex content in a vertical list.
4. Use connecting words, for example "and", "but", "then", and "thus".
5. Put an article or a demonstrative adjective before a noun when it is applicable.
6. Write one instruction in each sentence, unless two actions occur at the same time.
7. Give descriptive information gradually. Keep one topic in each paragraph and a maximum of six sentences in each paragraph.

### 6. Correct the safety instructions

Write a warning when a person can get an injury. Write a caution when damage can occur. Start with the command or the condition. Then give the risk.

### 7. Correct the punctuation

Do not use the semicolon. Use hyphens to connect words that are directly related. Count the words with the rules in section 8 of [references/writing-rules.md](references/writing-rules.md).

### 8. Examine the result

Make sure that:

- No word that is not approved stays in the text, or the word is a technical noun, a technical verb, or a recorded deviation.
- Each sentence obeys its word limit.
- Each instruction is in the imperative form.
- The meaning of the new text is the same as the meaning of the old text.

If a word-for-word replacement changes the meaning, write the sentence again with a different construction. Rule 9.1 permits this method.

## Output format

Give the new text only. Do not add an explanation.

When the user asks for a comparison, give a table with one row for each change:

| Rule | Before | After | Cause |
| ---- | ------ | ----- | ----- |

Give the rule number from ASD-STE100 Issue 9 in the first column. Refer to [references/writing-rules.md](references/writing-rules.md) for the numbers.

When you cannot keep the meaning and obey a rule at the same time, keep the meaning. Then tell the user which rule you did not obey, and why.

## Deviations

STE was written for aerospace maintenance documentation. Software content is different. These deviations are permitted, and this skill text uses them:

1. **Technical nouns from software.** Category 19 of rule 1.5 permits computer science and information technology terms. Identifiers, file names, and API names are technical nouns.
2. **Markdown structure.** Headings, lists, tables, code fences, and links are format elements. Rule 8 does not control them. STE does not give rules for text formatting.
3. **Code and quoted text.** Do not translate code, commands, or emitted strings into STE.
4. **The dictionary is not complete for software.** Sometimes no approved word gives the meaning. Then select the shortest clear technical noun or technical verb. Use the same term each time.

Do not use a deviation to keep a word that an approved word can replace.

## Source

ASD-STE100 Simplified Technical English, Issue 9, 2025-01-15. The ASD Simplified Technical English Maintenance Group (STEMG) controls the standard. You can get the specification at no cost from <https://www.asd-ste100.org/>. The references in this skill restate the rules. They are not a copy of the specification, and they do not replace it.
