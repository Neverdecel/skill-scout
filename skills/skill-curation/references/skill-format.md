# Skill format

Rules for writing or editing a `SKILL.md`. They follow the open
[Agent Skills](https://agentskills.io) format that most agent harnesses read.

## Folder

```
<skills-dir>/<name>/
  SKILL.md
  references/    optional; only when the procedure actually needs it
  scripts/       optional; only when the procedure actually needs it
```

The folder name must equal `name`.

## Frontmatter

Only `name` and `description`, as plain YAML:

```yaml
---
name: terraform-plan-review
description: Review and apply this team's Terraform changes using the saved-plan procedure. Use when preparing, reviewing, or applying Terraform plans for this team's environments.
---
```

- `name`: 1–64 characters, lowercase letters and digits, single hyphens
  between words (`^[a-z0-9]+(-[a-z0-9]+)*$`). Specific, not `helper` or
  `utils`.
- `description`: 1–1024 characters, third person. Say what the skill does,
  when to load it, and concrete trigger terms. It must not collide with
  other known skills' descriptions. Do not use a restrictive
  "Use ONLY when" gate; that gate is for opt-in tooling skills such as
  this one, not for saved procedures.

## Body

- Only the confirmed steps, constraints, and verification the agent
  would get wrong without the skill.
- Give one default with an escape hatch, not a menu of equal options.
- Leave out the reason for saving: no repetition counts, conversation
  references, transcripts, or "needed on the last three rollouts".
- Add nothing the user did not state, not even a sensible safeguard or
  a "what if it fails" step. If something seems missing, ask about it
  in the proposal instead.
- Leave out generic teaching and the current task's status or outcome.
- No secrets. Use placeholders such as `<plan-file>` for values.
- Keep it short. A procedure that needs more than a page probably holds
  two jobs.
