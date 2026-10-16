# Agent Skills

A small collection of focused, evidence-driven skills for coding agents. Each skill keeps its operating workflow in `SKILL.md`. Each skill puts the deeper guidance in reference files. An agent reads a reference file only when the task needs it.

## Available skills

| Skill                                                           | Use it for                                                                                                                                                 | Emphasis                                                                                                                                                                                                               |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`conventional-commit`](conventional-commit/)                   | Commit messages, pull-request titles, merge or squash messages, and release notes                                                                          | Conventional Commits 1.0.0 compliance. Type and scope selection. Breaking-change markers and footers. The effect on the semantic version.                                                                              |
| [`documentation`](documentation/)                               | READMEs, tutorials, how-to pages, references, error catalogs, troubleshooting pages, and tool definitions that agents read | Self-contained sections for retrieval. Exact error catalogs. Page length by task complexity. Importance in words. Tool descriptions that agents select correctly. |
| [`gpui-best-practices`](gpui-best-practices/)                   | GPUI Rust code: new code, refactor work, debug work, reviews, tests, and optimization                                                                      | How to resolve the locked GPUI API of the host project. State and entity ownership. Rendering, input, accessibility, async work, tests, and performance.                                                               |
| [`simplified-technical-english`](simplified-technical-english/) | New text or a revision: prompts, tool descriptions, agent instructions, log and error messages, code comments, READMEs, AGENTS.md, and other documentation | The ASD-STE100 Issue 9 writing rules and the approved-word dictionary. The difference between procedural text and descriptive text. How to remove ambiguity for agents, translation pipelines, and non-native readers. |
| [`unslop`](unslop/)                                             | Editing any writing to remove common AI patterns                                                                                                           | Plain words, concrete claims, active voice, and natural phrasing. Preserve meaning and match the intended tone.                                                                                                        |
| [`vertical-slice-architecture`](vertical-slice-architecture/)   | Design, review, and incremental refactor work on systems around end-to-end capabilities                                                                    | Clear ownership and dependency direction. Narrow feature boundaries. Coordination between slices. Disciplined shared code.                                                                                             |

## Installation

Use the [Skills CLI](https://www.skills.sh/docs/cli) to select skills interactively:

```sh
npx skills add https://github.com/cgoern/skills
```

To install only one skill, select it by name:

```sh
npx skills add https://github.com/cgoern/skills --skill conventional-commit
npx skills add https://github.com/cgoern/skills --skill documentation
npx skills add https://github.com/cgoern/skills --skill gpui-best-practices
npx skills add https://github.com/cgoern/skills --skill simplified-technical-english
npx skills add https://github.com/cgoern/skills --skill unslop
npx skills add https://github.com/cgoern/skills --skill vertical-slice-architecture
```

For a manual installation, copy the full skill directory into the skills location of your agent. Keep `SKILL.md` and its `references/` directory together.

## Usage

When the installation is completed, tell your agent to use a skill by name. Or give your agent a task that matches the description of the skill. For example:

```text
Use vertical-slice-architecture to map this codebase's capability boundaries and propose an incremental refactor.

Use gpui-best-practices to diagnose this focus bug against the GPUI revision locked by the project.

Use conventional-commit to write the message for the staged changes and the matching pull-request title.

Use documentation to audit docs/ for agent readers, and add an error catalog from the exceptions in src/.

Use simplified-technical-english to rewrite this tool description, and show me which rule each change fixes.

Use unslop to edit this draft for AI patterns while preserving its meaning and tone.
```

Each skill adapts to the host project:

- `conventional-commit` obeys the Conventional Commits 1.0.0 specification. The skill also keeps each type and each scope that the host project uses in addition to the specification.
- `vertical-slice-architecture` does not depend on a technology. The skill keeps the conventions of the host project while it groups the code around cohesive capabilities.
- `gpui-best-practices` uses the resolved GPUI source of the host project as the authority. The bundled source map of the skill is historical research. The source map is not a substitute for the locked API.
- `documentation` takes error strings, defaults, and flags from the source of the host project, not from memory. The skill controls the structure and the content of a page. Use `simplified-technical-english` for the wording.
- `simplified-technical-english` restates ASD-STE100 Issue 9. The skill also records a deviation profile for code, identifiers, emitted strings, and markdown structure. The bundled word lists are a working subset, not the full dictionary.
- `unslop` removes common AI writing patterns while preserving the intended meaning and tone. It disables automatic model invocation, so invoke it explicitly by name.

## Repository structure

```text
<skill-name>/
├── SKILL.md          # Metadata, activation description, and operating workflow
├── references/       # Optional. Detailed guidance loaded for the task at hand
└── scripts/          # Optional. Bundled validators
```

`SKILL.md` stays concise. `SKILL.md` sends the agent to the smallest applicable reference set. This progressive-disclosure structure gives depth. At the same time, the structure does not load unrelated material into every task.

## Use a skill in a project

An installed skill is portable. It does not know your directory layout, your accepted values, or
your validation command. Add one or two bullets for each installed skill to the `AGENTS.md` file of
that project.

Replace each `<PLACEHOLDER>`. Delete a bullet that has no local fact.

### conventional-commit

```markdown
- Use `conventional-commit` when you write a commit message, a pull-request title, or a release entry. The accepted types are in `<TYPES_FILE>`.
- A commit scope must be a directory name from `<FEATURE_PATH>/`. A subject has a maximum of <N> characters.
```

### vertical-slice-architecture

```markdown
- Use `vertical-slice-architecture` when you add a capability, or when you move code between features. Feature code is in `<FEATURE_PATH>/<capability>/`.
- Cross-slice calls use `<MECHANISM_NAME>`. Do not restructure `<FROZEN_PATH>/`.
```

### gpui-best-practices

```markdown
- Use `gpui-best-practices` for each change to the interface code in `<UI_PATH>/`. Use the local wrappers in `<WRAPPER_PATH>/`, not the raw framework elements.
- The locked GPUI revision is in `<LOCKFILE>`. If guidance disagrees with the locked source, obey the locked source.
```

### documentation

```markdown
- Use `documentation` when you write or change the pages in `<DOCS_PATH>/`, or the tool definitions in `<TOOLS_PATH>`. The error classes are in `<ERRORS_FILE>`.
- Keep the page templates in `<TEMPLATE_PATH>/`. Do not edit the generated reference in `<GENERATED_PATH>/`.
```

### simplified-technical-english

```markdown
- Use `simplified-technical-english` when you write or change the text in `<DOCS_PATH>/`, `README.md`, or `<MESSAGE_GLOB>`. Use this skill also for the documentation comments and the docstrings in `<SOURCE_PATH>/`.
- Do not rewrite `<GENERATED_PATH>`, or the strings in `<FIXTURE_PATH>/`. The tests compare these strings exactly.
```

### unslop

```markdown
- Use `unslop` when I explicitly request an edit for AI writing patterns in `<DOCS_PATH>` or `<CONTENT_PATH>`.
- Preserve quoted source text and the exact strings in `<FIXTURE_PATH>`.
```

### Keep the bullets small

An agent selects a skill from the `description` field of that skill, at session start. A bullet
above does not make a skill load. A bullet tells the agent where the work is in your project, and
gives the values that the skill cannot know.

Thus keep each bullet short, and obey these limits:

- Write a maximum of two bullets for each skill.
- Do not copy the rules of the skill. The skill gives them when it loads, and your copy goes stale.
- Do not write "always use skill X". A one-line change then loads a full procedure.
- Do not add trigger words because a skill did not activate. Correct the `description` field instead.
- Delete a bullet when you cannot name the incorrect action that occurs without it.

The `simplified-technical-english` skill bundles a checker. Run it on any markdown file:

```sh
python3 simplified-technical-english/scripts/check-ste.py README.md
```

## Contributing

When you add or change a skill, obey these rules:

1. Use a lowercase, kebab-case directory. Keep the directory name the same as the `name` in the `SKILL.md` frontmatter.
2. Write a precise `description` that says what the skill does and when an agent must use it. Keep the field below 1024 characters.
3. Keep the primary workflow focused. Keep `SKILL.md` below 500 lines and below 5000 tokens. Move detailed or topic-specific guidance into `references/`.
4. Before you add a skill, do a check of its quality against a no-skill baseline. Keep the instruction only when the skill changes the result.
5. It is better to use evidence, the conventions of the host project, and proportionate validation than a universal prescription. Keep an instruction only when the answer is yes: "Does an agent get this wrong without this instruction?"
6. Make sure that every relative link resolves. Keep each version-sensitive source explicitly pinned, or add a caveat to the source.
