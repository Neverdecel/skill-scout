# Installation

skill-scout is two folders of Markdown plus an optional snippet. Installing
means putting the folders where your harness discovers skills.

## 1. Skills

Copy `skills/skill-scout` and `skills/skill-curation` into one skills
directory. Use a global directory to use them in every project.

| Harness | Global | Project |
| --- | --- | --- |
| Cross-harness convention | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` |

These paths change over time. If yours is not listed, check your
harness's documentation for "skills" or "SKILL.md". Many harnesses read
several of these directories.

```sh
git clone https://github.com/Neverdecel/skill-scout.git
mkdir -p ~/.agents/skills
cp -r skill-scout/skills/skill-scout skill-scout/skills/skill-curation ~/.agents/skills/
```

To pick up `git pull` updates automatically, symlink the folders instead of
copying them:

```sh
ln -s "$PWD/skill-scout/skills/skill-scout" ~/.agents/skills/skill-scout
ln -s "$PWD/skill-scout/skills/skill-curation" ~/.agents/skills/skill-curation
```

With the [`skills` CLI](https://github.com/vercel-labs/skills):
`npx skills add Neverdecel/skill-scout`.

### Harnesses without native skills

Point the agent at the file from your instructions file, for example:
"When the snippet below says to load `skill-scout`, read
`~/tools/skill-scout/skills/skill-scout/SKILL.md`." Saved skills will then be
plain Markdown procedures that you reference the same way.

### Claude Code: approve the write prompt

Claude Code protects `.claude/`, so every skill save shows a permission
prompt even after you approved the proposal in conversation, including in
accept-edits mode. Approve it. In Claude Code 2.1.286, `permissions.allow`
rules did not lift this protection; only `bypassPermissions` mode did. In
non-interactive `claude -p` runs the write is denied, and the agent reports
that nothing was saved.

## 2. Always-on snippet (optional)

Without it, `skill-scout` runs when you ask for it or when the harness matches
its description. With it, the agent checks for candidates at every natural
stopping point.

Append [`snippets/always-on.md`](../snippets/always-on.md) to the instructions
file your harness always loads:

| Harness | Global | Project |
| --- | --- | --- |
| Most harnesses | — | `AGENTS.md` |
| Claude Code | `~/.claude/CLAUDE.md` | `CLAUDE.md` |
| OpenCode | `~/.config/opencode/AGENTS.md` | `AGENTS.md` |
| Codex | `~/.codex/AGENTS.md` | `AGENTS.md` |
| Gemini CLI | `~/.gemini/GEMINI.md` | `GEMINI.md` |

Put topics you never want suggested under the snippet's ignore list, one per
line.

## 3. Verify

Restart the harness, then ask it to list its skills. `skill-scout` and
`skill-curation` should both appear. Ordinary work should produce no
suggestions; that is expected.

Quick check: describe a repeated, team-specific procedure, say that you keep
having to explain it, and finish the task. The agent should propose a skill in
one or two sentences and **not** write it until you answer.

## Update

`git pull` in the clone. Copied folders need copying again; symlinks don't.

## Uninstall

Delete the two skill folders and remove the snippet. Skills you saved stay on
disk until you delete them.

## Troubleshooting

- **Skills not listed:** wrong directory for this harness, or the harness
  needs a restart. The folder name must match the `name` in `SKILL.md`.
- **No suggestions ever:** expected without the snippet. With it, suggestions
  are still deliberately rare.
- **Too many suggestions:** add topics to the snippet's ignore list, or remove
  the snippet and invoke `skill-scout` only when you want it.
- **Wrote without asking, or saved a poor skill:** this is model behavior, not
  a bypassed guard. Use your harness's write permissions for a hard boundary.
  Report it with the harness and model versions and a sanitized reproduction.
