# Contributing

Keep it small: agent instructions, human approval, native skills. Read
[docs/design.md](docs/design.md) before changing skill behavior.

## Checks

```sh
python3 scripts/validate.py
```

This checks frontmatter, names, folder matches, description gates, links,
identical `skill-format.md` copies, and secret-like strings. CI runs the same
script. It does **not** test whether a model follows the skills.

## Behavior changes

Wording changes can change model behavior. Run the affected cases in
[evals/SCENARIOS.md](evals/SCENARIOS.md) in a disposable environment, with at
least one harness and one model. In the PR, include the harness and model
versions and what you saw, including failures. Review the actual proposals and
saved files, not only whether something was written.

## Pull requests

1. Branch from `main` and keep the change focused.
2. Update `README.md` and `docs/` when behavior or install paths change.
3. The `validate` check must pass.

## Issues

Include the harness and model versions and a minimal, sanitized reproduction.
Do not post credentials, private config, or session exports. Security reports
go through [SECURITY.md](SECURITY.md).
