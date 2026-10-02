# Security

Report vulnerabilities privately: **Security → Report a vulnerability** on
[Neverdecel/skill-scout](https://github.com/Neverdecel/skill-scout/security/advisories/new).
Do not open a public issue with exploit details or credentials.

## Scope

skill-scout is instructions for an agent. It is **not** a sandbox. Skill writes
use the harness's normal file tools and permissions. Conversational approval is
not a security boundary.

In scope: secrets in shipped skills, examples, or docs; instructions that lead
an agent to exfiltrate data or run unintended code; prompt-injection weaknesses
in the skill text itself.

Out of scope: a model ignoring consent, writing a low-quality skill, or storing
a secret it was told to store. Those are instruction-following failures. Use
your harness's permission settings when you need a hard guard.
