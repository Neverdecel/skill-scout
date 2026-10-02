# Contributing (agents)

- This repo ships Markdown skills only. Do not add a runtime, hooks, persistence, a consent parser, a write interceptor, or harness-specific code. Design: `docs/design.md`.
- Product skills live in `skills/<name>/SKILL.md`, with frontmatter of only `name` and `description`, and the folder matching `name`. `skill-curation` keeps its `Use ONLY when ` gate. `skill-scout` and generated skills never use it.
- `references/skill-format.md` is copied into each skill. Edit one copy, then copy it to the others; the validator fails if they differ.
- Keep `examples/` outside any skills directory and free of credentials.
- Keep the always-on snippet short; it costs context on every request.
- Harness paths are hints for the agent to resolve, never assumptions. When adding a harness, update `skills/skill-scout/SKILL.md` and `docs/installation.md` together.
- Run `python3 scripts/validate.py` before finishing. It does not test model behavior. For behavior changes, run the relevant cases in `evals/SCENARIOS.md` in an isolated environment, never against a real skill library.
