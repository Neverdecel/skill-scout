---
name: skill-curation
description: Use ONLY when the user explicitly asks to review, audit, curate, merge, consolidate, deduplicate, or prune their existing agent skills. Do not use for ordinary work, for capturing new skills from a session, or for unsolicited cleanup.
---

# Skill curation

The user asked to curate the skill library. That gives you initiative to **inspect and propose** changes. It does not give you permission to merge, rewrite, or delete, and it is not a cue to curate again later on your own.

## Inspect

List the skills this harness already knows (its skill listing, plus `SKILL.md` files in its project and global skills directories). Load only what you need to judge overlap. Do not dump skill bodies into the reply. Do not invent skills that are not on disk.

Skip tooling skills (`skill-scout`, `skill-curation`) and harness built-ins unless the user named them.

Judge each skill as one on-demand job: the description is its discovery index, and the body is the procedure the agent would get wrong without it. Look for:

- A description that misses what or when, is first person, is too broad or too narrow, or shares trigger terms with another skill
- A body that mixes two jobs (split), or two skills that teach the same job (merge)
- Always-on conventions stored as a skill (propose moving them to the instructions file; do not write that file)
- Generic model knowledge, inferred or unconfirmed rules, saved evidence or motivation, menus of equal options, vague names (`helper`, `utils`)
- Contradictions, obsolete instructions, needless fragmentation, a clearly better replacement
- Empty or broken frontmatter, a folder name that does not match `name`
- Secrets that should never have been stored (flag these first)

When uncertain, leave the skill alone.

## Propose

For each issue, at most two short sentences: the problem, the action (merge / edit / split / delete), the exact skill names, and the scope. No wizard and no full rewrite in the proposal.

If nothing needs changing, say so and stop. Do not create new procedural skills here; that is `skill-scout`.

## Apply

Do not write, merge, rename, or delete until the user approves that specific operation. Reviewing the library, listing overlap, or silence is not approval. Merging into a target does not authorize deleting the source unless the user said to delete it.

After approval:

1. Use the harness's normal file tools and respect its permissions and modes.
2. Read before you edit. Preserve unrelated sections and supporting files.
3. Keep every result valid under [references/skill-format.md](references/skill-format.md).
4. Never persist secrets. If removing one is the approved edit, remove it fully, and tell the user to rotate it.
5. Report each path changed, created, or deleted. Report failures as failures.
6. Mention that some harnesses discover changed skills only after a restart.
