# Agent Skills

A small collection of focused, evidence-driven skills for coding agents. Each skill keeps its operating workflow in `SKILL.md` and places deeper guidance in references that are loaded only when needed.

## Available skills

| Skill                                                         | Use it for                                                                                | Emphasis                                                                                                                                          |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`conventional-commit`](conventional-commit/)                 | Writing commit messages, pull-request titles, merge or squash messages, and release notes | Conventional Commits 1.0.0 compliance; type and scope selection; breaking-change markers and footers; semantic-version impact                     |
| [`gpui-best-practices`](gpui-best-practices/)                 | Creating, refactoring, debugging, reviewing, testing, or optimizing GPUI Rust code        | Resolving the target project's locked GPUI API; state and entity ownership; rendering, input, accessibility, async work, testing, and performance |
| [`vertical-slice-architecture`](vertical-slice-architecture/) | Designing, reviewing, or incrementally refactoring systems around end-to-end capabilities | Clear ownership and dependency direction; narrow feature boundaries; cross-slice coordination; disciplined shared code                            |

## Installation

Use the [Skills CLI](https://www.skills.sh/docs/cli) to choose skills interactively:

```sh
npx skills add https://github.com/cgoern/skills
```

To install only one skill, select it by name:

```sh
npx skills add https://github.com/cgoern/skills --skill conventional-commit
npx skills add https://github.com/cgoern/skills --skill gpui-best-practices
npx skills add https://github.com/cgoern/skills --skill vertical-slice-architecture
```

For a manual installation, copy the complete skill directory into the skills location used by your agent. Keep `SKILL.md` and its `references/` directory together.

## Usage

Once installed, ask your agent to use a skill explicitly or give it a task that matches the skill's description. For example:

```text
Use vertical-slice-architecture to map this codebase's capability boundaries and propose an incremental refactor.

Use gpui-best-practices to diagnose this focus bug against the GPUI revision locked by the project.

Use conventional-commit to write the message for the staged changes and the matching pull-request title.
```

The skills are designed to adapt to the repository they are used in:

- `conventional-commit` follows the Conventional Commits 1.0.0 specification and respects the additional types and scopes a repository already uses.
- `vertical-slice-architecture` is technology-agnostic and preserves host conventions while organizing code around cohesive capabilities.
- `gpui-best-practices` treats the target project's resolved GPUI source as authoritative. Its bundled source map is historical research, not a substitute for the locked API.

## Repository structure

```text
<skill-name>/
├── SKILL.md          # Metadata, activation description, and operating workflow
└── references/       # Detailed guidance loaded for the task at hand
```

`SKILL.md` stays concise and routes the agent to the smallest relevant reference set. This progressive-disclosure structure provides depth without loading unrelated material into every task.

## Contributing

When adding or changing a skill:

1. Use a lowercase, kebab-case directory and keep its name aligned with the `name` in `SKILL.md` frontmatter.
2. Write a precise `description` that says both what the skill does and when it should activate.
3. Keep the main workflow focused; move detailed or topic-specific guidance into `references/`.
4. Prefer evidence, host-project conventions, and proportionate validation over universal prescriptions.
5. Verify every relative link and keep version-sensitive sources explicitly pinned or caveated.
