# ASD-STE100 writing rules

This reference restates the 53 writing rules and the eight general recommendations of ASD-STE100 Simplified Technical English, Issue 9 (2025-01-15). The rule numbers agree with the specification. The wording and the examples are not a copy of the specification. Get the specification at no cost from <https://www.asd-ste100.org/>.

Issue 9 changed some terms. If you read an older source, note these changes:

| Issue 8 term   | Issue 9 term    |
| -------------- | --------------- |
| Technical name | Technical noun  |
| Noun cluster   | Multi-word noun |
| Helping verb   | Auxiliary verb  |
| Rule 2.3       | Rule 4.5        |

## Contents

- [Section 1 - Words](#section-1---words)
- [Section 2 - Multi-word nouns](#section-2---multi-word-nouns)
- [Section 3 - Verbs](#section-3---verbs)
- [Section 4 - Sentences](#section-4---sentences)
- [Section 5 - Procedural writing](#section-5---procedural-writing)
- [Section 6 - Descriptive writing](#section-6---descriptive-writing)
- [Section 7 - Safety instructions](#section-7---safety-instructions)
- [Section 8 - Punctuation and word count](#section-8---punctuation-and-word-count)
- [Section 9 - Writing practices](#section-9---writing-practices)
- [General recommendations](#general-recommendations)
- [Limits](#limits)

## Section 1 - Words

**Rule 1.1** Use only these words: words that are approved in the dictionary, technical nouns, and technical verbs.

**Rule 1.2** Use an approved word only as the part of speech that the dictionary gives.

> Not STE: Oil the bearing. (`oil` is a noun, not a verb.)
>
> STE: Apply oil to the bearing.

> Not STE: Check the exit code. (`check` is a noun, not a verb.)
>
> STE: Do a check of the exit code. Or: Examine the exit code.

**Rule 1.3** Use an approved word only with the meaning that the dictionary gives.

> Not STE: These rules do not apply to the test file.
>
> STE: These rules are not applicable to the test file.

**Rule 1.4** Use only the approved forms of verbs and adjectives.

**Rule 1.5** You can use a word when you can put it in one of the 22 technical noun categories. Refer to [word-choice.md](word-choice.md).

**Rule 1.6** A word that is not approved in the dictionary is permitted only as a technical noun, or as a part of a technical noun.

**Rule 1.7** Do not use a technical noun as a verb.

> Not STE: Guide the cable into the slot.
>
> STE: Move the cable into the slot.

**Rule 1.8** Use technical nouns that your company, your industry, or your subject field approves. Keep them in a glossary or a terminology database.

**Rule 1.9** When you must select a technical noun, select one that is short and easy to understand.

**Rule 1.10** Do not use regional words, slang words, or jargon words as technical nouns.

**Rule 1.11** Do not use different technical nouns for the same item.

> Not STE: The handler reads the payload. The callback then writes the body.
>
> STE: The handler reads the request body. The handler then writes the request body.

**Rule 1.12** You can use a verb when you can put it in one of the four technical verb categories. Refer to [word-choice.md](word-choice.md).

**Rule 1.13** Do not use a technical verb as a noun.

**Rule 1.14** Use American English spelling, unless an official directive tells you differently.

> Not STE: initialise, colour, behaviour, cancelled
>
> STE: initialize, color, behavior, canceled

## Section 2 - Multi-word nouns

**Rule 2.1** Write a multi-word noun with a maximum of three words.

> Not STE: request body validation error message
>
> STE: the error message for a validation error in the request body

**Rule 2.2** When a technical noun has more than three words, write it in full one time. Then use one of these two methods to keep the technical noun clear:

- Give a shorter form of the technical noun.
- Put hyphens between the words that you use as one unit.

> STE: The Cross-Origin Resource Sharing policy (CORS policy) controls the response. The CORS policy is in the configuration file.

## Section 3 - Verbs

**Rule 3.1** Use only the verb forms that the dictionary gives.

**Rule 3.2** Use only these verb forms and tenses:

- The infinitive form
- The imperative form (the command form)
- The simple present tense
- The simple past tense
- The simple future tense
- The past participle form, as an adjective

> Not STE: The server has been listening on port 8080.
>
> STE: The server listens on port 8080.

> Not STE: We have received the report.
>
> STE: We received the report.

**Rule 3.3** Use the past participle form as an adjective.

> STE: The cached value is stale.

**Rule 3.4** Do not use auxiliary verbs to make complex verb constructions.

> Not STE: The job will have been completed before the timeout occurs.
>
> STE: The job completes before the timeout occurs.

**Rule 3.5** Use the "-ing" form of a verb only as a technical noun, or as a modifier in a technical noun.

> Not STE: The agent is parsing the response.
>
> STE: The agent parses the response.

> STE: The operating system supplies the file handle. (`operating system` is a technical noun.)

**Rule 3.6** Use the active voice. In descriptive writing, you can use the passive voice only when the agent of the action is unknown.

> Not STE: The wires were disconnected by the technician.
>
> STE: The technician disconnected the wires.

> Not STE: The file must be deleted.
>
> STE: Delete the file.

**Rule 3.7** Give an action with an approved verb, not with a noun or a different part of speech.

> Not STE: Do the adjustment of the timeout carefully.
>
> STE: Adjust the timeout carefully.

> Not STE: The tool does the validation of the schema.
>
> STE: The tool validates the schema.

## Section 4 - Sentences

**Rule 4.1** Write short and clear sentences. Keep one topic in each sentence.

**Rule 4.2** Do not omit words and do not use contractions to make a sentence shorter.

> Not STE: Don't run if config's missing.
>
> STE: If the configuration file is not available, do not run the command.

**Rule 4.3** Put complex content in a vertical list.

> Not STE: The command accepts a file path, an output directory, a log level, and a timeout value in seconds.
>
> STE: The command accepts these parameters:
>
> - A file path
> - An output directory
> - A log level
> - A timeout value in seconds

**Rule 4.4** Use connecting words and connecting phrases to connect sentences that contain related topics. Approved connecting words include "and", "but", "then", and "thus". Approved connecting phrases include "as a result" and "at the same time".

> STE: The cache is empty. Thus, the agent reads the file again.

**Rule 4.5** When it is applicable, put an article (the, a, an) or a demonstrative adjective (this, these) before a noun or a multi-word noun.

> Not STE: Set flag in config file.
>
> STE: Set the flag in the configuration file.

Do not put an article before a general statement or a general concept.

> STE: Solvents can cause damage to paint.
>
> STE: Retries increase the load on the server.

## Section 5 - Procedural writing

Procedural writing tells the reader to do an action.

**Rule 5.1** Write short sentences. Use a maximum of 20 words in each sentence.

**Rule 5.2** Write only one instruction in each sentence. If two actions or more occur at the same time, you can write them in one sentence.

> Not STE: Open the file, read the header, and then close the handle.
>
> STE: 1. Open the file. 2. Read the header. 3. Close the handle.

**Rule 5.3** Write each instruction in the imperative form (the command form).

> Not STE: The user should now set the environment variable.
>
> STE: Set the environment variable.

**Rule 5.4** When the reader must know a condition first, start the instruction with a descriptive statement. Then put a comma between the statement and the command.

> STE: If the response code is 429, wait for 30 seconds.
>
> STE: With the debug flag set, run the command again.

**Rule 5.5** Write a note only to give information. A note must not give an instruction.

> Not STE: Note: Delete the temporary files.
>
> STE: Note: The temporary files stay in the cache directory.

## Section 6 - Descriptive writing

Descriptive writing gives information, not instructions. Thus, the imperative form is not permitted.

**Rule 6.1** Give the information gradually. Give the topic first. Then give the details.

**Rule 6.2** Use key words and key phrases to give the text a logical structure. Do not change a key word after you use it.

**Rule 6.3** Write short sentences. Use a maximum of 25 words in each sentence.

**Rule 6.4** Use a paragraph to show information that is related.

**Rule 6.5** Keep only one topic in each paragraph.

**Rule 6.6** Write a maximum of six sentences in each paragraph.

## Section 7 - Safety instructions

A safety instruction tells the reader that a procedure or a work step can be dangerous, or can cause damage.

**Rule 7.1** Use an applicable word to identify the level of risk. Usually, "warning" shows a risk of injury or death, and "caution" shows a risk of damage.

**Rule 7.2** Start a safety instruction with a clear and accurate command or condition.

**Rule 7.3** Give an explanation that shows the risk or the possible result.

> Not STE: Care must be taken because data loss is possible with this command.
>
> STE: CAUTION: MAKE A BACKUP OF THE DATABASE BEFORE YOU RUN THIS COMMAND. THE COMMAND DELETES ALL THE RECORDS AND YOU CANNOT GET THEM AGAIN.

## Section 8 - Punctuation and word count

**Rule 8.1** You can use all standard English punctuation marks, but not the semicolon (;).

> Not STE: Examine the removed parts; replace the damaged ones.
>
> STE: Examine the removed parts for damage. Replace each damaged part.

**Rule 8.2** Use hyphens to connect words that are directly related. A hyphen is different from a dash.

**Rule 8.3** You can use parentheses for these functions:

- To make a reference to an illustration or to text
- To include a letter or a number that identifies an item
- To identify a work step in a procedure
- To include an abbreviation
- To give the singular and the plural forms of a noun at the same time
- To explain a word or a part of a sentence
- To include an alternative

**Rule 8.4** In a vertical list, a colon has the same effect on the word count as a period. The colon shows the end of a sentence. Count each list item as a different sentence.

**Rule 8.5** Text in parentheses counts as one word in its sentence. The text in the parentheses is also a different sentence, and you count its words separately.

**Rule 8.6** Count each of these elements as one word:

- A number
- A number with its unit of measurement
- An abbreviation
- An alphanumeric identifier
- Quoted text
- A title, a heading, a placard, or a label
- A proper noun of a person, a group, an organization, or a geopolitical entity

**Rule 8.7** A hyphenated word counts as one word.

STE does not give rules for general punctuation. Refer to an external style guide.

## Section 9 - Writing practices

**Rule 9.1** When a word-for-word replacement is not sufficient, write the sentence again with a different construction.

> Not STE: A value of 2 mm is acceptable.
>
> Word-for-word: A value of 2 mm is permitted.
>
> Different construction: The oil level must be visible during the test. -> During the test, make sure that you can see the oil level.

**Rule 9.2** Use each approved word correctly.

**Rule 9.3** When you use two words together, do not make a phrasal verb.

> Not STE: Carry out the test.
>
> STE: Do the test.

> Not STE: Turn on the power.
>
> STE: Start the power supply.

> Not STE: The technical writer must go through the document.
>
> STE: The technical writer must read the document.

**Rule 9.4** Use a consistent style when you select terminology and wording.

## General recommendations

The specification gives eight general recommendations (GR-1 thru GR-8). They are recommendations, not rules.

**GR-1 The conjunction "that".** Use "that" as much as possible after verbs such as "make sure", "show", and "recommend". Many languages cannot omit the equivalent word.

> Not STE: Make sure the valve is open.
>
> STE: Make sure that the valve is open.

**GR-2 The preposition "with".** The word "with" can cause ambiguity. Read the sentence again and make sure that it has only one meaning.

> Ambiguous: Install the panel with the green fasteners.
>
> STE: Use the green fasteners to install the panel.

**GR-3 How to use pronouns.** If a pronoun can refer to more than one noun, replace the pronoun with the noun.

> Ambiguous: If you engage the pins incorrectly with the seats, they can become damaged.
>
> STE: If you engage the pins incorrectly with the seats, the pins can become damaged.

**GR-4 The pronoun "this".** Make sure that the reader knows the item that "this" refers to. If "this" can refer to more than one item, give the context again.

> Ambiguous: Make sure that the cover is not locked (this can cause damage to the probe).
>
> STE: Make sure that the cover is not locked. If the cover is locked, damage to the probe can occur.

**GR-5 False friends.** A false friend is a word that looks the same as a word in a different language, but has a different meaning. Make sure that the English meaning is correct.

**GR-6 Latin abbreviations.** Do not use Latin abbreviations. Use English words.

> Not STE: e.g., i.e., etc., cf., et al., via
>
> STE: for example, that is, and so on, refer to, and others, with

**GR-7 Inclusive language.** Use gender-neutral language. STE does not permit "he", "she", "man", or "woman", unless the context makes them necessary.

**GR-8 Possessive form.** The possessive form is permitted, but many languages do not have it. If you are not sure that your sentence is correct, do not use the possessive form.

## Limits

| Limit                                   | Value  | Rule |
| --------------------------------------- | ------ | ---- |
| Maximum words in a procedural sentence  | 20     | 5.1  |
| Maximum words in a descriptive sentence | 25     | 6.3  |
| Maximum sentences in a paragraph        | 6      | 6.6  |
| Maximum words in a multi-word noun      | 3      | 2.1  |
| Text in parentheses counts as           | 1 word | 8.5  |
| A hyphenated word counts as             | 1 word | 8.7  |
| Technical noun categories               | 22     | 1.5  |
| Technical verb categories               | 4      | 1.12 |
