# skill-scout

[![Validate](https://github.com/Neverdecel/skill-scout/actions/workflows/validate.yml/badge.svg)](https://github.com/Neverdecel/skill-scout/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Agent notices. Human decides. The skill library remembers.**

Two [Agent Skills](https://agentskills.io) that let any coding agent notice durable, reusable procedures during normal work and **ask before** saving them as skills. They also keep the library tidy when you ask. They are plain Markdown with no runtime, no hooks, and no dependencies, so they work in any harness that reads `SKILL.md`: Claude Code, OpenCode, Codex, Gemini CLI, Cursor, and others.

> This looks reusable: review the saved Terraform plan with the on-call owner, then apply only that artifact. Save as `terraform-plan-review` (project skill)?

Reply **yes**, **no**, **make it global**, **rename it**, **add X**, or **merge with Y**. Ordinary work should produce no suggestion.

## What's inside

| Path | Role |
| --- | --- |
| [`skills/skill-scout`](skills/skill-scout/SKILL.md) | Notices or mines candidates, proposes them in two sentences, and saves only after approval |
| [`skills/skill-curation`](skills/skill-curation/SKILL.md) | Opt-in review of the existing library: merge, split, edit, prune, all only after approval |
| [`snippets/always-on.md`](snippets/always-on.md) | Five lines for your `AGENTS.md` / `CLAUDE.md` so the agent checks for candidates without being asked |
| [`examples/terraform-plan-review`](examples/terraform-plan-review/SKILL.md) | The shape of a good generated skill (not installed) |

A skill is **one on-demand job**. Its `description` is the only discovery index, and its body is the confirmed procedure the agent would get wrong without it. Always-on rules, personas, commands, and memory are not skills, and skill-scout stays silent about them. Details: [docs/design.md](docs/design.md).

## Install

**1. Install the skills.** Copy both folders into a skills directory your harness reads:

```sh
git clone https://github.com/Neverdecel/skill-scout.git
cp -r skill-scout/skills/* ~/.agents/skills/      # or ~/.claude/skills/, ~/.config/opencode/skills/, ...
```

Or use the [`skills` CLI](https://github.com/vercel-labs/skills), which knows each harness's paths:

```sh
npx skills add Neverdecel/skill-scout
```

**2. Optional but recommended: add the always-on snippet.** Skills load on demand, so without the snippet `skill-scout` runs only when you ask ("mine skills from this session") or when its description happens to match. To have the agent check for candidates at stopping points, append [`snippets/always-on.md`](snippets/always-on.md) to your global or project instructions file (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, ...).

**3.** Restart the harness if it discovers skills only at startup.

Per-harness paths, updates, and uninstalling: [docs/installation.md](docs/installation.md).

## Usage

| You | Agent |
| --- | --- |
| Ordinary work | No extra chatter |
| Confirm a durable team or personal procedure | Short save proposal at a stopping point (with the snippet) |
| "Mine skills from this session" | Lists candidates; writes nothing yet |
| Approve, reject, rename, re-scope, or merge | Writes only the approved change, then shows the path |
| "Never suggest X again" | Stops at once and offers to add X to the snippet's ignore list |
| "Review / clean up my skills" | `skill-curation` proposes changes; writes only on approval |

- **Project skills** are repository or team procedures and live in the project's skills directory. This is the default.
- **Global skills** are how you work across projects and live in your user skills directory.

## Limits

**Consent and secret exclusion are model instructions, not a filesystem guard.** Skill writes use the harness's normal file tools and permissions. If you need a hard boundary, use your harness's permission settings. Behavior depends on the model; see the [evaluation scenarios](evals/SCENARIOS.md) and [recorded results](evals/RESULTS.md).

## Contributing

```sh
python3 scripts/validate.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Successor to [opencode-guided-learning](https://github.com/Neverdecel/opencode-guided-learning), rewritten without the OpenCode plugin.

## License

[MIT](LICENSE). Vulnerability reports: [SECURITY.md](SECURITY.md).
