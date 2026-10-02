#!/usr/bin/env python3
"""Validate bundled skills and examples. Standard library only."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"\A---\nname: (.+)\ndescription: (.+)\n---\n\n(.+)\Z", re.S)
SECRETS = re.compile(r"SYNTHETIC-DO-NOT-SAVE|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,}")
LINK = re.compile(r"\]\(([^)#\s]+)\)")
# Opt-in tooling skills are gated; skill-scout must trigger on signals in normal work.
GATED = {"skill-curation"}

errors = []


def check(skill_md: Path, generated: bool) -> None:
    folder = skill_md.parent.name
    source = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER.match(source)
    if not match:
        errors.append(f"{skill_md}: frontmatter must be exactly name and description")
        return
    name, description, body = match.groups()
    if name != folder:
        errors.append(f"{skill_md}: name {name!r} does not match folder {folder!r}")
    if not NAME.match(name) or len(name) > 64:
        errors.append(f"{skill_md}: invalid name {name!r}")
    if not 1 <= len(description) <= 1024:
        errors.append(f"{skill_md}: description must be 1-1024 characters")
    gated = description.startswith("Use ONLY when ")
    if gated != (not generated and name in GATED):
        errors.append(f"{skill_md}: 'Use ONLY when' gate is only for {sorted(GATED)}")
    for link in LINK.findall(body):
        if "://" not in link and not (skill_md.parent / link).exists():
            errors.append(f"{skill_md}: broken link {link}")


skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
for path in skills:
    check(path, generated=False)
for path in sorted((ROOT / "examples").glob("*/SKILL.md")):
    check(path, generated=True)

formats = {p.read_bytes() for p in (ROOT / "skills").glob("*/references/skill-format.md")}
if len(formats) > 1:
    errors.append("skills/*/references/skill-format.md copies differ; keep them identical")

# evals/ is excluded: it names the synthetic fixture on purpose.
for shipped in ("skills", "examples", "snippets", "docs"):
    for path in (ROOT / shipped).rglob("*.md"):
        if SECRETS.search(path.read_text(encoding="utf-8")):
            errors.append(f"{path}: contains a secret-like string")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"ok: {len(skills)} skills, examples, and references valid")
