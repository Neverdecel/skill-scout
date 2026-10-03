# Design

Maintainer notes. Users can skip this.

## Principles

- **Explain it once.** This is the problem we solve: a user should not
  have to explain a confirmed procedure to the agent again.
- **Agent notices, human decides.** Noticing is cheap; writing needs
  explicit approval of the specific change. Frustration ("I keep telling
  you...") is a signal to propose, not consent to write.
- **Native skills only.** No database, memory store, background job,
  write interceptor, or consent parser. Saved skills are ordinary `SKILL.md`
  folders the harness already discovers.
- **Harness-agnostic.** Plain Markdown in the open Agent Skills format. Any
  harness-specific path is a hint the agent resolves at runtime, not a
  hard-coded assumption.
- **Silence by default.** A suggestion has a cost. Most sessions should
  produce none.

## The skill entity

A **skill** is one on-demand job: a named folder whose `description` is the
only discovery index, and whose body is the confirmed procedure the agent
would get wrong without it.

It must be procedural, on-demand, discoverable (what + when + trigger terms),
non-generic, confirmed, durable, one trigger family, and secret-free.

Not skills: always-on rules (instructions files), personas (agents),
user-invoked prompts (commands), facts (memory), preferences, one-offs.

One job per skill. Split unrelated jobs. Merge when two skills would fire on
the same future prompts and teach the same job. Prefer updating to creating.

The writing rules are in `references/skill-format.md`. That file is copied
into each skill because a skill folder must be self-contained. The validator
checks that the copies stay identical.

## Why two skills and a snippet

The predecessor, `opencode-guided-learning`, injected always-on guidance
through experimental OpenCode hooks and shipped `skill-mining` and
`skill-curation` separately. Without hooks, the parts map like this:

| Before | Now |
| --- | --- |
| System-prompt injection (always on) | `snippets/always-on.md`: a few lines that point at the skill |
| Guidance body + `skill-mining` | `skill-scout`. Both did the same job (capture, propose, approve, save), so by the merge rule above they are one skill. Only the initiative differs. |
| `skill-curation` | `skill-curation` (unchanged job, different triggers) |
| `ignoredTopics` plugin option | An ignore list inside the snippet |
| Compaction hook note | A line in the snippet |
| Skipping title/summary/explore agents | A line in the snippet; harnesses rarely load instructions files there anyway |

The snippet stays short because instructions files cost context on every
request. The full procedure loads only when needed.

## Descriptions

`skill-curation` uses a `Use ONLY when ...` gate so that it never fires during
ordinary work. `skill-scout` has no gate: its description has to match
real signals (a confirmed repeated procedure, an explicit mining request).
Generated skills never use the gate. They state what + when like any normal
skill.

## Limits

Consent and secret exclusion are instructions to the model. They are not a
security boundary. Earlier live runs (OpenCode, two models) showed correct
waiting for approval and secret omission. They also showed failures: a
missing scope in a proposal, overly long proposals, repetition counts copied
into skill bodies, invented constraints, and, before the frustration-is-not-
consent wording, one unapproved write. The current wording addresses each of
these, but any model can still fail. See `evals/SCENARIOS.md`.
