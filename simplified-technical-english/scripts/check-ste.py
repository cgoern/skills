#!/usr/bin/env python3
"""Mechanical STE checker for markdown text.

Tests only the rules that a script can decide. It does not test meaning, and it
does not test the full 875-word dictionary. A clean run is necessary, not
sufficient: a person must still apply rules 1.1, 1.3, 6.1, and 9.1.

Rules tested: 1.14 (American spelling), 3.5 (-ing as a verb), 4.2 (contractions),
5.1 (20 words), 6.3 (25 words), 6.6 (6 sentences), 8.1 (no semicolon),
9.3 (phrasal verbs), GR-6 (Latin abbreviations), GR-8 (possessive form).

Word count obeys rules 8.4 thru 8.7: a colon ends a sentence in a vertical list,
each list item is a different sentence, text in parentheses counts as one word,
and a hyphenated word or an identifier counts as one word.

Deviations (SKILL.md): code fences, inline code, identifiers, paths, links,
headings, table structure, and the frontmatter block are not tested.

Usage:  check-ste.py [--descriptive] [--quiet] FILE [FILE ...]
Exit:   0 = no findings, 1 = findings, 2 = usage error
"""

import pathlib
import re
import sys
from collections import Counter

PROCEDURAL_LIMIT = 20
DESCRIPTIVE_LIMIT = 25
PARAGRAPH_LIMIT = 6

CODE = "QQCODEQQ"  # stands for one inline-code span or one URL
EXEMPTED = "QQEXQQ"  # stands for an exempt technical noun

# Rule 1.1 frequent errors and software replacements, from references/word-choice.md.
NOT_APPROVED = {
    "ability": "CAN (v)",
    "able": "CAN (v)",
    "achieve": "GET",
    "additional": "MORE",
    "allow": "LET",
    "allows": "LETS",
    "appropriate": "APPLICABLE",
    "ascertain": "MAKE SURE",
    "assist": "HELP",
    "avoid": "PREVENT",
    "cease": "STOP",
    "commence": "START",
    "conduct": "DO",
    "desired": "NECESSARY",
    "employ": "USE",
    "enable": "LET",
    "enables": "LETS",
    "ensure": "MAKE SURE THAT",
    "execute": "DO",
    "executes": "DOES",
    "facilitate": "HELP",
    "generally": "USUALLY",
    "generate": "GIVE",
    "generates": "GIVES",
    "however": "BUT",
    "implement": "DO",
    "indicate": "SHOW",
    "indicates": "SHOWS",
    "insert": "PUT",
    "limitation": "LIMIT",
    "maintain": "KEEP",
    "modify": "CHANGE",
    "obtain": "GET",
    "perform": "DO",
    "performs": "DOES",
    "permit": "LET",
    "portion": "PART",
    "proper": "CORRECT",
    "properly": "CORRECTLY",
    "provide": "GIVE",
    "provides": "GIVES",
    "render": "MAKE",
    "retrieve": "GET",
    "several": "SOME",
    "shall": "MUST",
    "should": "MUST",
    "since": "BECAUSE",
    "terminate": "STOP",
    "therefore": "THUS",
    "throughout": "DURING",
    "toward": "TO",
    "utilize": "USE",
    "various": "DIFFERENT",
    "verify": "MAKE SURE THAT",
    "via": "THROUGH",
    "within": "IN",
    "may": "CAN",
    "might": "CAN",
    "would": "CAN",
    "leverage": "USE",
    "robust": "(recast)",
    "powerful": "(recast)",
    "seamless": "(recast)",
    "simply": "(recast)",
}
PHRASAL = {
    "carry out": "do",
    "turn on": "start",
    "turn off": "stop",
    "set up": "prepare",
    "shut down": "stop",
    "bring up": "show",
    "fill out": "complete",
    "put off": "delay",
    "go through": "read",
    "back up": "make a backup",
}
LATIN = {
    "e.g.": "for example",
    "i.e.": "that is",
    "etc.": "and so on",
    "cf.": "refer to",
    "et al.": "and others",
}
BRITISH = {
    "initialise": "initialize",
    "colour": "color",
    "behaviour": "behavior",
    "cancelled": "canceled",
    "organise": "organize",
    "analyse": "analyze",
    "centre": "center",
    "licence": "license",
    "catalogue": "catalog",
    "façade": "facade",
    "acknowledgements": "acknowledgments",
}
# Grammar and domain technical nouns, exempt from the word-choice test (rule 1.5, category 19).
EXEMPT = [
    "simple present tense",
    "simple past tense",
    "simple future tense",
    "past participle",
    "infinitive form",
    "imperative form",
    "technical noun",
    "technical verb",
    "multi-word noun",
    "active voice",
    "passive voice",
    "auxiliary verb",
    "part of speech",
    "proper noun",
    "operating system",
    "machine learning",
    "large language model",
    "prompt engineering",
]
# -ing words that are technical nouns, or modifiers in one (rule 3.5 permits these).
ING_OK = {
    "during",
    "string",
    "thing",
    "nothing",
    "something",
    "anything",
    "everything",
    "operating",
    "engineering",
    "meaning",
    "warning",
    "heading",
    "setting",
    "according",
    "existing",
    "remaining",
    "following",
    "missing",
    "working",
    "being",
    "having",
    "writing",
    "reading",
    "naming",
    "tracking",
    "routing",
    "rendering",
    "testing",
    "logging",
    "caching",
    "handling",
    "mapping",
    "leading",
    "trailing",
    "encoding",
    "formatting",
    "debugging",
    "learning",
    "using",
    "including",
    "corresponding",
    "underlying",
    "matching",
}


def parse(text):
    """Yield (lineno, testable_text, kind) with every deviation removed."""
    out, fence, fm, in_list = [], False, False, False
    for i, raw in enumerate(text.splitlines(), 1):
        st = raw.strip()
        if i == 1 and st == "---":
            fm = True
            out.append((i, "", "skip"))
            continue
        if fm:
            out.append((i, "", "skip"))
            if st == "---":
                fm = False
            continue
        if st.startswith("```") or st.startswith("~~~"):
            fence = not fence
            out.append((i, "", "skip"))
            continue
        if (
            fence
            or not st
            or st.startswith("#")
            or st.startswith("|")
            or set(st) <= set("-|: ")
        ):
            if not st:
                in_list = False
            out.append((i, "", "skip"))
            continue
        s = re.sub(r"`[^`]*`", " " + CODE + " ", raw)
        s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"<https?://[^>]*>|https?://\S+", " " + CODE + " ", s)
        if re.match(r"^\s*(\d+\.|[-*+])\s", raw):
            in_list = True
        elif not raw.startswith((" ", "\t")):
            in_list = False
        kind = "procedural" if in_list else "descriptive"
        s = re.sub(r"^\s*(\d+\.|[-*+])\s+", "", s)
        s = re.sub(r"[*_]{1,2}", "", s)
        out.append((i, s, kind))
    return out


def sentences(s):
    """Rule 8.4: a colon ends a sentence in a vertical list."""
    return [x.strip() for x in re.split(r"(?<=[.!?:])\s+", s) if x and x.strip()]


def count_words(s):
    """Rules 8.5 thru 8.7: a parenthetical, an identifier and a hyphenated word each count as one."""
    s = re.sub(r"\([^)]*\)", " " + CODE + " ", s)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9_./@-]*", s))


def check(path, descriptive_default=False):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    found, para = [], 0

    def add(ln, rule, msg, ctx):
        found.append((ln, rule, msg, ctx.strip()[:88]))

    for ln, line, kind in parse(text):
        if not line.strip():
            para = 0
            continue
        low = line.lower()
        masked = low
        for ph in EXEMPT:
            masked = masked.replace(ph, " " + EXEMPTED + " ")

        if ";" in line:
            add(ln, "8.1", "semicolon", line)
        for m in re.finditer(r"\b[A-Za-z]+'(?:s|t|re|ve|ll|d)\b", line):
            g = m.group(0)
            if g.lower().endswith("'s"):
                add(ln, "GR-8", "possessive " + repr(g), line)
            else:
                add(ln, "4.2", "contraction " + repr(g), line)
        for k, v in LATIN.items():
            if k in low:
                add(ln, "GR-6", repr(k) + " -> " + v, line)
        for k, v in PHRASAL.items():
            if re.search(r"\b" + k + r"\b", masked):
                add(ln, "9.3", "phrasal " + repr(k) + " -> " + v, line)
        for k, v in BRITISH.items():
            if k in low:
                add(ln, "1.14", repr(k) + " -> " + v, line)
        for w in sorted(set(re.findall(r"[a-z]+", masked))):
            if w in NOT_APPROVED:
                add(ln, "1.1", repr(w) + " -> " + NOT_APPROVED[w], line)
        for m in re.finditer(r"\b(?:is|are|was|were|be|been)\s+([a-z]+ing)\b", masked):
            add(ln, "3.5", "-ing as a verb " + repr(m.group(1)), line)

        if kind == "procedural":
            para = 0  # rule 6.6 governs a paragraph, and a vertical list is not a paragraph
        for sent in sentences(line):
            n = count_words(sent)
            is_proc = (kind == "procedural") and not descriptive_default
            lim = PROCEDURAL_LIMIT if is_proc else DESCRIPTIVE_LIMIT
            if n > lim:
                add(
                    ln,
                    "5.1" if is_proc else "6.3",
                    str(n) + " words > " + str(lim),
                    sent,
                )
            para += 1
        if para > PARAGRAPH_LIMIT:
            add(
                ln,
                "6.6",
                "paragraph has " + str(para) + " sentences > " + str(PARAGRAPH_LIMIT),
                line,
            )
            para = 0
    return found


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = set(a for a in argv[1:] if a.startswith("--"))
    if not args:
        print(__doc__)
        return 2
    total = 0
    for p in args:
        f = check(p, descriptive_default="--descriptive" in flags)
        total += len(f)
        head = p + ": " + str(len(f)) + " finding(s)"
        print("\n" + head + "\n" + "-" * len(head))
        if f:
            print("  by rule:", dict(Counter(r for _, r, _, _ in f).most_common()))
        if "--quiet" not in flags:
            for ln, rule, msg, ctx in f:
                print(
                    "  "
                    + p
                    + ":"
                    + str(ln)
                    + "  ["
                    + rule
                    + "] "
                    + msg
                    + "\n      "
                    + ctx
                )
    print("\nTOTAL: " + str(total))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
