---
name: simplified-technical-english
description: Rewrite or review text in ASD-STE100 Simplified Technical English (STE). STE is controlled English that removes ambiguity for agents, translators, and non-native readers. Covers prompts, system messages, tool and parameter descriptions, agent instructions, log and error messages, code comments, docstrings, READMEs, and AGENTS.md. Use this skill even if the user only says "simplify this" or "make it unambiguous". This skill does not simplify code, logic, or an algorithm - it changes text only.
---

# Simplified Technical English

ASD-STE100 Simplified Technical English (STE) is a controlled natural language and an international standard for technical documentation. STE has two parts:

- Part 1 gives 53 writing rules in nine sections.
- Part 2 gives a dictionary of 875 approved words and 1274 words that are not approved.

The function of STE is to remove ambiguity before a reader, a translation engine, or a different agent gets the text. This skill text obeys the mechanical rules that `scripts/check-ste.py` tests. This skill text also uses the deviations. Refer to [Deviations](#deviations).

## Load the guidance

The workflow below carries a routine rewrite. Do not load a reference file that the task does not
need. Read a reference file only in the condition that its row gives.

| Read                                                        | Only when                                                                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [word-choice.md](references/word-choice.md)                 | You must replace a word that is not approved, you need the project verb glossary, or you must add a technical noun       |
| [software-adaptation.md](references/software-adaptation.md) | The text is a prompt, a tool description, a log or error message, a code comment, a README, or an AGENTS.md file         |
| [writing-rules.md](references/writing-rules.md)             | You must give a rule number in a comparison table, you write a safety instruction, or a sentence has no clear correction |

Steps 3 thru 7 restate the mechanical rules on purpose, so that a routine rewrite needs no reference
file. Do not delete those steps to remove the duplication. The duplication is what makes the
reference files conditional.

Run `scripts/check-ste.py` on the result. The checker tests the mechanical rules, thus you do not
need [writing-rules.md](references/writing-rules.md) for a word count or a banned construction.

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

Record each deliberate deviation. Give the deviations with the result.

### 3. Correct the words

1. Use only approved dictionary words, technical nouns, or technical verbs.

2. Use each approved word only with the part of speech and the meaning that the dictionary gives. A small number of words have two parts of speech.

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

- Each word in the text is an approved word, a technical noun, a technical verb, or a recorded deviation.
- Each sentence obeys its word limit.
- Each instruction is in the imperative form.
- The meaning of the new text is the same as the meaning of the old text.

If a word-for-word replacement changes the meaning, write the sentence again with a different construction. Rule 9.1 lets you use this method.

## Output format

Give the new text first. Do not add an explanation of an unchanged part.

Then give the deviation list, but only when the new text keeps content that does not obey STE. Give one line for each deviation. If the new text keeps no such content, give no list.

When the user asks for a comparison, give a table with one row for each change:

| Rule | Before | After | Cause |
| ---- | ------ | ----- | ----- |

Give the rule number from ASD-STE100 Issue 9 in the first column. Refer to [references/writing-rules.md](references/writing-rules.md) for the numbers.

When the meaning and a rule are in conflict, keep the meaning. Then tell the user which rule the text does not obey, and why.

## Deviations

STE was written for aerospace maintenance documentation. Software content is different. These deviations are permitted, and this skill text uses them:

1. **Technical nouns from software.** Category 19 of rule 1.5 approves computer science terms and information technology terms. Identifiers, file names, and API names are technical nouns.

2. **Markdown structure.** Headings, lists, tables, code fences, and links are format elements. STE does not give rules for text formatting. But rule 8.4 and rule 8.6 still control the word count: count each list item as a different sentence, and count a heading as one word.

3. **Code and quoted text.** Do not translate code, commands, or emitted strings into STE.

4. **The dictionary does not have a word for each software item.** Sometimes no approved word gives the meaning. Then select the shortest clear technical noun or technical verb. Use the same term each time. Record the term in the project glossary in [references/word-choice.md](references/word-choice.md).

5. **The frontmatter `description` field.** Rule 1.1 and rule 1.11 do not control this field. An agent selects a skill from this field alone. Thus the field must contain the words that a user writes, and the field must contain synonyms. Apply only rule 8.1, rule 5.1, and rule 4.3 to this field.

6. **Calibration words.** STE has "must" and "can" only. A technical text also needs a recommendation that is not a requirement. Use "prefer", "usually", and "it is better to" for a recommendation. Do not replace a recommendation with a prohibition.

7. **Cause clauses.** An instruction that gives its cause is more reliable than a bare command. Keep the cause. Put the cause in a second sentence when one sentence is more than the limit of rule 5.1. Use "because", "thus", and "as a result".

Do not use a deviation to keep a word that an approved word can replace.

## Source

ASD-STE100 Simplified Technical English, Issue 9, 2025-01-15. The ASD Simplified Technical English Maintenance Group (STEMG) controls the standard. You can get the specification at no cost from <https://www.asd-ste100.org/>. The references in this skill restate the rules. They are not a copy of the specification, and they do not replace it.
