# Word choice in Simplified Technical English

This reference tells you how to select words for STE. It restates the dictionary principles of ASD-STE100 Issue 9 and gives replacement tables. The word lists are factual data from the specification. Get the full dictionary at no cost from <https://www.asd-ste100.org/>.

## Contents

- [The three permitted word classes](#the-three-permitted-word-classes)
- [One word, one part of speech, one meaning](#one-word-one-part-of-speech-one-meaning)
- [How to read a dictionary entry](#how-to-read-a-dictionary-entry)
- [Frequent errors](#frequent-errors)
- [Replacements for software and agent text](#replacements-for-software-and-agent-text)
- [Approved verbs](#approved-verbs)
- [Technical noun categories](#technical-noun-categories)
- [Technical verb categories](#technical-verb-categories)
- [Phrasal verbs](#phrasal-verbs)
- [How to add a technical noun](#how-to-add-a-technical-noun)

## The three permitted word classes

Rule 1.1 permits only three classes of words:

1. **Approved words.** The dictionary gives 875 approved words. They are the most frequent words in technical writing.
2. **Technical nouns.** A technical noun is a noun term for a specified concept in a subject field. The dictionary does not contain technical nouns, because there are too many.
3. **Technical verbs.** A technical verb is a verb term for a specified concept or process in a subject field. The dictionary does not contain technical verbs.

If a word is not in one of these three classes, do not use it. Replace the word, or write the sentence again with a different construction.

## One word, one part of speech, one meaning

STE selects one word from a group of synonyms and rejects the others. For example, STE approves "start". STE does not approve "begin", "commence", "initiate", or "originate".

STE also selects one meaning for each word. For example, the approved meaning of "fall" is "to move down by the force of gravity". The meaning "to decrease" is not approved.

Most approved words have one part of speech only. Rule 1.2 makes this restriction. A small number of words have two parts of speech, for example "control" (noun and verb).

These restrictions have a direct effect on software text:

| Word   | Approved as | Not approved as | Correct STE                     |
| ------ | ----------- | --------------- | ------------------------------- |
| check  | noun        | verb            | Do a check of the exit code.    |
| test   | noun        | verb            | Do a test of the new function.  |
| cover  | noun        | verb            | Put the cover on the container. |
| damage | noun        | verb            | The command can cause damage.   |

## How to read a dictionary entry

The dictionary has four columns:

1. **Word (part of speech).** UPPERCASE shows an approved word. lowercase shows a word that is not approved.
2. **Approved meaning, or ALTERNATIVES.** An approved word gets its one approved meaning. A word that is not approved gets one alternative or more, in uppercase.
3. **STE EXAMPLE.** An example with correct words and correct constructions.
4. **Non-STE example.** An example with words or constructions that STE does not permit.

`(TN)` identifies a technical noun. `(TV)` identifies a technical verb.

The dictionary gives nouns in the singular form only. The plural form of a countable noun is permitted. The dictionary does not give antonyms.

## Frequent errors

The specification gives this list of the errors that writers make most frequently. Learn it first. It removes a large part of the work.

| Not STE          | STE                                        |
| ---------------- | ------------------------------------------ |
| acceptable (adj) | PERMITTED (adj)                            |
| alternate (adj)  | ALTERNATIVE (adj)                          |
| any (adj)        | Use no word, or a different construction   |
| avoid (v)        | PREVENT (v)                                |
| both (adj)       | THE TWO (TN)                               |
| check (v)        | CHECK (n)                                  |
| complete (adj)   | COMPLETED (adj)                            |
| cover (v)        | COVER (TN)                                 |
| damage (v)       | DAMAGE (n)                                 |
| ensure (v)       | MAKE SURE (v)                              |
| fit (v)          | INSTALL (v)                                |
| follow (v)       | OBEY (v)                                   |
| further (adj)    | MORE (adj)                                 |
| further (adv)    | MORE (adv)                                 |
| have to (v)      | Use an action verb in the imperative form  |
| however (adv)    | BUT (conj)                                 |
| insert (v)       | PUT (v)                                    |
| main (adj)       | PRIMARY (adj)                              |
| may (v)          | CAN (v)                                    |
| need (v)         | NECESSARY (adj)                            |
| now (adv)        | AT THIS TIME                               |
| old (adj)        | REMAINING (adj), USED (adj), EXPIRED (adj) |
| over (prep)      | ABOVE (prep), ON (prep), ALONG (prep)      |
| people (n)       | PERSON (n), PERSONNEL (n)                  |
| perform (v)      | DO (v)                                     |
| portion (n)      | PART (n)                                   |
| press (v)        | PUSH (v)                                   |
| reach (v)        | GET (v)                                    |
| repeat (v)       | DO (v) ... AGAIN                           |
| required (v)     | NECESSARY (adj)                            |
| rotate (v)       | TURN (v)                                   |
| secure (v)       | ATTACH (v), SAFETY (v)                     |
| shall (v)        | MUST (v)                                   |
| should (v)       | MUST (v)                                   |
| since (conj)     | BECAUSE (conj)                             |
| test (v)         | TEST (n)                                   |
| therefore (adv)  | THUS (adv), AS A RESULT                    |
| under (prep)     | BELOW (prep), IN (prep), LESS THAN         |
| using (v)        | USE (v), WITH (prep)                       |

## Replacements for software and agent text

These words occur frequently in agent output, prompts, tool descriptions, and code documentation. The dictionary does not approve them. The table gives the approved alternatives.

| Not STE           | STE                                 |
| ----------------- | ----------------------------------- |
| ability (n)       | CAN (v)                             |
| able (adj)        | CAN (v)                             |
| achieve (v)       | GET (v)                             |
| additional (adj)  | MORE (adj)                          |
| allow (v)         | LET (v)                             |
| among (prep)      | IN (prep)                           |
| appropriate (adj) | APPLICABLE (adj)                    |
| ascertain (v)     | MAKE SURE (v)                       |
| assist (v)        | HELP (v)                            |
| attempt (n, v)    | TRY (v)                             |
| cease (v)         | STOP (v)                            |
| commence (v)      | START (v)                           |
| conduct (v)       | DO (v)                              |
| create (v)        | MAKE (v), CAUSE (v)                 |
| delete (v)        | ERASE (v), REMOVE (v)               |
| desired (adj)     | NECESSARY (adj), CORRECT (adj)      |
| determine (v)     | FIND (v), SELECT (v), CALCULATE (v) |
| employ (v)        | USE (v), HAVE (v)                   |
| enable (v)        | LET (v)                             |
| execute (v)       | DO (v)                              |
| facilitate (v)    | HELP (v)                            |
| fast (adv)        | QUICKLY (adv)                       |
| generally (adv)   | USUALLY (adv)                       |
| generate (v)      | GIVE (v), SUPPLY (v)                |
| handle (v)        | MOVE (v), USE (v)                   |
| implement (v)     | DO (v)                              |
| indicate (v)      | SHOW (v), IDENTIFY (v)              |
| limitation (n)    | LIMIT (n)                           |
| maintain (v)      | KEEP (v), HOLD (v)                  |
| modify (v)        | CHANGE (v)                          |
| note (v)          | RECORD (v)                          |
| obtain (v)        | GET (v)                             |
| once (conj)       | WHEN (conj)                         |
| permit (v)        | LET (v)                             |
| persist (v)       | CONTINUE (v)                        |
| process (n)       | PROCEDURE (n)                       |
| process (v)       | DO (v)                              |
| proper (adj)      | CORRECT (adj)                       |
| provide (v)       | GIVE (v), SUPPLY (v)                |
| quick (adj)       | QUICKLY (adv)                       |
| render (v)        | MAKE (v)                            |
| require (v)       | NECESSARY (adj)                     |
| several (adj)     | SOME (adj)                          |
| support (v)       | HOLD (v), SUPPORT (TN)              |
| terminate (v)     | STOP (v)                            |
| throughout (prep) | DURING (prep)                       |
| toward (prep)     | TO (prep)                           |
| trigger (v)       | CAUSE (v), START (v)                |
| upon (prep)       | ON (prep), WHEN (conj)              |
| utilize (v)       | USE (v)                             |
| valid (adj)       | CORRECT (adj), APPLICABLE (adj)     |
| various (adj)     | DIFFERENT (adj)                     |
| verify (v)        | MAKE SURE (v)                       |
| via (prep)        | THROUGH (prep), WITH (prep)         |
| within (prep)     | IN (prep)                           |
| would (v)         | CAN (v)                             |

Some software verbs are technical verbs in category 2. Refer to [Technical verb categories](#technical-verb-categories). You can use them, but only when no approved verb gives the same meaning.

## Approved verbs

These 206 verbs are approved in the dictionary. Use an approved verb before you use a technical verb.

ABSORB, ACCEPT, ACTIVATE, ADAPT, ADD, ADJUST, AGREE, ALIGN, APPLY, ARM, ASSEMBLE, ATTACH, BALANCE, BE, BECOME, BEND, BLEED, BLOW, BOND, BREAK, BREATHE, BURN, BYPASS, CALCULATE, CALIBRATE, CAN, CANCEL, CANNOT, CATCH, CAUSE, CHANGE, CHARGE, CLEAN, CLOSE, COLLECT, COME, COME ON, COMPARE, COMPLETE, COMPRESS, CONNECT, CONTACT, CONTAIN, CONTINUE, CONTROL, CORRECT, COUNT, CUT, DEACTIVATE, DECREASE, DE-ENERGIZE, DEFLATE, DEFUEL, DEPLOY, DISARM, DISASSEMBLE, DISCARD, DISCONNECT, DISENGAGE, DIVIDE, DO, DRAIN, DRINK, DRY, EAT, EJECT, ENERGIZE, ENGAGE, ERASE, EXAMINE, EXPAND, EXTEND, EXTINGUISH, FALL, FEATHER, FEEL, FILL, FIND, FIRE, FLASH, FLOW, FLUSH, FOLD, FOLLOW, FREEZE, GET, GIVE, GO, GO OFF, GROUND, HANG, HAVE, HEAR, HELP, HIT, HOLD, IDENTIFY, IGNORE, ILLUMINATE, INCLUDE, INCREASE, INFLATE, INSTALL, INTERCHANGE, ISOLATE, KEEP, KILL, KNOW, LATCH, LET, LIFT, LISTEN, LOCK, LOOK, LOOSEN, LOWER, LUBRICATE, MAKE, MAKE SURE, MEASURE, MELT, MIX, MONITOR, MOOR, MOVE, MULTIPLY, MUST, OBEY, OCCUR, OPEN, OPERATE, OVERRIDE, PAINT, PARK, POINT, POLISH, PREPARE, PRESSURIZE, PREVENT, PROTRUDE, PULL, PUSH, PUT, PUT ON, READ, RECEIVE, RECOMMEND, RECORD, RECYCLE, REFER, REFUEL, REJECT, RELEASE, REMOVE, REPAIR, REPLACE, RETRACT, RUB, SAFETY, SCHEDULE, SEAL, SEE, SELECT, SEND, SENSE, SET, SHAKE, SHOW, SIMULATE, SMELL, SMOKE, SOAK, SPEAK, SPILL, SPRAY, START, STAY, STOP, STOW, SUBTRACT, SUPPLY, SWALLOW, TAG, TAP, TELL, THINK, TIGHTEN, TILT, TORQUE, TOUCH, TOW, TRANSMIT, TRY, TUNE, TURN, TWIST, UNFOLD, UNLOCK, UNWIND, USE, WAIT, WALK, WANT, WEAR, WEIGH, WILL, WIND, WRITE

Note that "FOLLOW" has the approved meaning "to come after". For the meaning "to comply with", use "OBEY".

## Technical noun categories

Rule 1.5 gives 22 categories. You can use a word as a technical noun when you can put it in one category or more:

1. Official parts information
2. Vehicles or machines, and locations on them
3. Tools and support equipment, their parts, and locations on them
4. Materials, consumables, and unwanted material
5. Facilities, infrastructure, and logistic procedures
6. Systems, components and circuits, their functions, configurations, and parts
7. Mathematical, scientific, engineering terms, and formulas
8. Navigation and geographic terms
9. Numbers, units of measurement and time, and their symbols
10. Quoted text
11. Professional roles, individuals, groups, organizations, and geopolitical entities
12. Parts of the body
13. Common personal effects, food, and beverages
14. Medical terms
15. Official documents, parts of documentation, standards, and guidelines
16. Environmental and operational conditions
17. Colors
18. Damage terms
19. **Computer science, information and communication technology**
20. Civil and military operations
21. Law and regulations
22. Animals, plants, and other life forms

Category 19 is the primary category for software text. The specification gives these examples: add-in, add-on, AI, artificial intelligence, authentication, backup, backup file, bookmark, chatbot, content, cursor, cybersecurity, database, deep learning, digitalization, e-mail, embedding, field, file, firewall, hallucination, HTML, icon, interface, internet, large language model, laptop, machine learning, memory, menu, metadata, network, operating system, plug-in, preset value, prompt engineering, screen, search engine, status bar, store, tablet, token, toolbar, update, XML.

Category 17 makes colors technical nouns. Comparative and superlative forms of colors are not permitted.

## Technical verb categories

Rule 1.12 gives four categories:

1. **Manufacturing processes.** Six subcategories: remove material, add material, attach material, change the properties of a material, change the surface finish, change the shape.
2. **Computer processes and applications.**
    - Input and output: click, digitize, enter, press, print, swipe, tap, type
    - User interface and applications: clear, close, copy, cut, delete, deselect, disable, drag, enable, encrypt, erase, filter, highlight, maximize, minimize, navigate, open, paste, save, scroll, sort, store, validate, zoom in, zoom out
    - System operations: abort, boot, communicate, debug, download, format, install, load, manage, process, reboot, update, upgrade, upload
3. **Instructions and information for applicable subject fields.** Six subcategories: engineering and science, medical, civil and military operations, navigation, automotive and railway, energy and oil and gas.
4. **Law and regulations.**

Category 2 is the primary category for software text.

If an approved verb gives the same instruction or the same information, use the approved verb. Do not use a technical verb when the approved dictionary can make the same sentence.

## Phrasal verbs

Rule 9.3 does not permit phrasal verbs. A phrasal verb has two words or three words, and its meaning is different from the meaning of each word.

| Not STE     | STE               |
| ----------- | ----------------- |
| carry out   | do                |
| turn on     | start, energize   |
| turn off    | stop, de-energize |
| set up      | prepare, install  |
| shut down   | stop              |
| bring up    | show, start       |
| fill out    | complete          |
| put off     | delay             |
| go through  | read, examine     |
| back up (v) | make a backup     |

A verb with a preposition is not a phrasal verb. "The water must go through the filter" is correct STE, because "through" keeps its own meaning.

## How to add a technical noun

Rules 1.8 thru 1.11 control new technical nouns:

1. Make sure that your company, your industry, or your subject field approves the term.
2. Select a term that is short and easy to understand.
3. Do not use a regional word, a slang word, or a jargon word.
4. Use the same term for the same item each time. Do not use a synonym.
5. Record the term in a glossary or a terminology database.
6. Write the term with a maximum of three words (rule 2.1).

A multi-word noun is a lexical unit, and you cannot separate its words. An adjective that gives the condition of an item is not a part of the technical noun. For example, in "stale cached value", "stale" is an adjective and "cached value" is the technical noun.
