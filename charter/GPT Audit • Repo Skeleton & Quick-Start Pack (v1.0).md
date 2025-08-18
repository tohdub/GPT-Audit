# GPT Audit • Repo Skeleton & Quick-Start Pack (v1.0)

Below is a plug‑and‑play repo layout with ready templates, prompts, and CI hooks. Copy these files into your GitHub repo.

---

## Repository Tree

```
GPT-Audit/
├─ README.md
├─ LICENSE
├─ charter/
│  └─ GPT-Audit_Charter_v1.0.md
├─ prompts/
│  └─ gpt_audit.system.md
├─ standards/
│  ├─ writing.md
│  ├─ compliance.md
│  ├─ ux.md
│  └─ api.md
├─ playbooks/
│  ├─ claude.md
│  └─ gemini.md
├─ templates/
│  ├─ audit_input.sample.yaml
│  ├─ quick_start_checklist.md
│  └─ adr_template.md
├─ scripts/
│  ├─ audit_runner.py
│  └─ validate_input.py
├─ .github/
│  └─ workflows/
│     └─ audit.yml
└─ CONTRIBUTING.md
```

---

## README.md

````md
# GPT Audit (v1.0)

GPT Audit is a multi‑expert audit council for AI projects and custom GPTs. It enforces writing/UX/compliance standards, evaluates end‑to‑end workflows (prompts → APIs → automation), and explains trade‑offs in plain language with Good/Better/Best guidance.

## Quick Start
1. **Pin your SSOT**: add repo URLs and commit SHAs in `templates/audit_input.sample.yaml`.
2. **Fill the input file** for your project (vision, success criteria, artifacts, tool_stack).
3. **Run locally**:
   ```bash
   python scripts/validate_input.py path/to/your_input.yaml
   python scripts/audit_runner.py path/to/your_input.yaml --mode full_audit
````

4. **CI Gate**: GitHub Actions workflow (`.github/workflows/audit.yml`) will run audits on PRs; merges are blocked on Fail.

## Source of Truth (SSOT)

* All claims must cite pinned sources (commit SHA or permalink). Missing evidence → mark as Gap with severity.

## Outputs

* Quick Gate, Full Audit Report, or Change Review. Reports are attached to PRs and stored as build artifacts.

````

---

## charter/GPT-Audit_Charter_v1.0.md
```md
# GPT Audit Charter & Foundations (v1.0)

**Identity**: multi‑expert panel; enforce standards; audit end‑to‑end; explain in plain language; prevent drift via SSOT.

**Specialists**: Lead Auditor, Technical Writer, UX Reviewer, Optimization Engineer, Reasoning & Evaluation Scientist, Safety & Compliance Officer, Tooling & Automation Engineer, Model Ops (Claude), Model Ops (Gemini), Business Use Case Analyst, Data & Analytics Auditor.

**Workflow**: Scope & SSOT → Panel Review → Debate & Trade‑offs → ADR Decision Record → Plain‑language Summary → Compliance Gate → Diff‑aware Re‑audit.

**Checklists (0–2)**: Technical Writing, UX, Optimization, Reasoning/Evals, API/Automation, Compliance/Safety, Business/Analytics.

**Good/Better/Best**: present tiered recommendations for each standard.

**Versioning**: v1.0 introduces business/analytics integration, tiered decisions, SSOT policy, expanded compliance anchors.
````

---

## prompts/gpt\_audit.system.md

```md
You are **GPT Audit**, a multi‑expert audit council. Operate as labeled specialists who debate and converge on evidence‑backed decisions. Explain standards to lay users in plain language and present Good/Better/Best options tied to business goals.

**SSOT & Citations**: Prefer pinned GitHub sources, official standards/spec docs. For each normative claim include `(Source, path, commit/perma‑link)`. If unknown → `Gap` with severity.

**Input Contract (YAML)**
project: name, vision, success_criteria
artifacts: prompts, evals, apis, automations, ux
standards: writing, compliance (SOC2, ISO 27001, GDPR, WCAG 2.2), ux, api
tool_stack: models, runtime, storage, observability
ssot: repos (commit SHAs)

**Output Order**
1) Panel Review (labeled)  2) Debate & Decision Record (ADR)  3) User‑Facing Summary  4) Compliance Gate & Checklist  5) Remediation Plan.

**Guardrails**: no fabrication; cost/latency ranges with assumptions; keep turns concise; red‑flag deviations from SSOT.
```

---

## standards/writing.md

```md
# Technical Writing Standard (v1.0)
- Structure: Overview → Details → Acceptance Criteria → Changelog.
- Audience & terminology defined; consistent voice; diagrams labeled.
- Citations: link to SSOT or standards; no orphan claims.
- Scoring (0–2): 0=missing, 1=partial, 2=complete.
```

## standards/compliance.md

```md
# Compliance & Safety Anchors (v1.0)
- Security: SOC 2 (good baseline for SaaS); ISO 27001 (gold standard); GDPR (data rights); audit logging.
- Accessibility: WCAG 2.2 AA.
- Data: retention, PII handling, least privilege, secrets mgmt.
- Present Good/Better/Best with business caveats.
```

## standards/ux.md

```md
# UX Standard (v1.0)
- Task clarity, error recovery, latency perception, onboarding, accessibility hooks.
- Evidence: usability tests or heuristic eval notes.
```

## standards/api.md

```md
# API & Automation Standard (v1.0)
- Spec fidelity (OpenAPI), retries/idempotency, timeouts, observability (logs/traces/metrics), CI/CD gates, IaC.
```

---

## playbooks/claude.md

```md
# Claude Playbook (v1.0)
- Context: large windows; compress few‑shots; tool‑use for long retrieval.
- Costs/latency: compare models; batch evaluations when possible.
- Safety levers and red‑teaming pointers.
```

## playbooks/gemini.md

```md
# Gemini Playbook (v1.0)
- Multimodal parsing; function calling for structure; rate‑limit & QPS notes.
- Batch where supported; monitor latency variance.
```

---

## templates/audit\_input.sample.yaml

```yaml
project:
  name: Example Project
  vision: Enable fast, safe support automation with clear explanations.
  success_criteria: ["≥90% helpfulness", "p95 latency ≤ 2.5s", "no PII leaks in red‑team"]
artifacts:
  prompts: ["/prompts/*.md"]
  evals: ["/evals/design.md", "/dashboards/helpfulness.json"]
  apis: ["/api/openapi.yaml"]
  automations: ["/workflows/zapier.yaml", "/ci/pipeline.yaml"]
  ux: ["/design/flows.pdf"]
standards:
  writing: ["/standards/writing.md"]
  compliance: ["/standards/compliance.md"]
  ux: ["/standards/ux.md"]
  api: ["/standards/api.md"]
tool_stack:
  models: ["chatgpt", "claude", "gemini"]
  runtime: ["n8n", "Zapier", "Power Automate"]
  storage: ["Postgres", "Sheets"]
  observability: ["OpenTelemetry", "Dashboard XYZ"]
ssot:
  repos:
    - url: https://github.com/yourorg/yourrepo
      commit: 0123456789abcdef0123456789abcdef01234567
mode: full_audit
audience: mixed
priorities: ["quality", "latency", "cost", "safety", "UX"]
```

## templates/quick\_start\_checklist.md

```md
# Quick Start Audit Checklist (v1.0)
- [ ] SSOT links use commit SHAs
- [ ] Vision & success criteria present
- [ ] Prompts and APIs attached
- [ ] Eval plan + metric defined
- [ ] UX flows/screens present
- [ ] Good/Better/Best recommendation produced
- [ ] Compliance Gate: Pass/Fail with severity notes
```

## templates/adr\_template.md

```md
# Architecture Decision Record (ADR)
**Context**
**Options** (with pros/cons; cost/latency/token notes)
**Decision**
**Consequences**
**Follow‑ups** (owner, date)
```

---

## scripts/validate\_input.py

```py
import sys, yaml
REQUIRED = [
  ("project", ["name", "vision", "success_criteria"]),
  ("ssot", ["repos"]),
]

def main(path):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    missing = []
    for section, keys in REQUIRED:
        if section not in data:
            missing.append(section)
            continue
        for k in keys:
            if k not in data[section]:
                missing.append(f"{section}.{k}")
    if missing:
        print("ERROR: missing fields:", ", ".join(missing))
        sys.exit(1)
    print("OK: input validated")

if __name__ == "__main__":
    main(sys.argv[1])
```

## scripts/audit\_runner.py

```py
import sys, yaml, json, subprocess
# Pseudo-runner: validates input, then prints the prompt payload
# In production, replace with your LLM call and attach outputs to CI artifacts.

def main(path, mode="full_audit"):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    payload = {
        "entrypoint": {
            "user_goal": data["project"]["vision"],
            "context_pack": data["ssot"]["repos"],
            "mode": data.get("mode", mode),
            "audience": data.get("audience", "mixed"),
            "priorities": data.get("priorities", []),
        },
        "artifacts": data.get("artifacts", {}),
        "standards": data.get("standards", {}),
        "tool_stack": data.get("tool_stack", {}),
    }
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "full_audit"
    main(path, mode)
```

---

## .github/workflows/audit.yml

```yaml
name: GPT Audit
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install pyyaml
      - name: Validate input
        run: |
          python scripts/validate_input.py templates/audit_input.sample.yaml
      - name: Dry-run audit
        run: |
          python scripts/audit_runner.py templates/audit_input.sample.yaml --mode full_audit > audit_payload.json
      - name: Evaluate gate (placeholder)
        run: |
          echo "PASS" > audit_status.txt
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: audit-artifacts
          path: |
            audit_payload.json
            audit_status.txt
```

---

## CONTRIBUTING.md

```md
- Keep standards versioned; update SSOT links with commit SHAs.
- Add new expert roles only with accompanying checklists.
- All normative changes require examples and citations.
```

---

## Build & Use Instructions (Custom GPT)

1. **Create your Custom GPT** and paste `prompts/gpt_audit.system.md` into the **System Instructions**.
2. **Knowledge**: connect your GitHub repo (read‑only). Prefer permalinks with commit SHAs.
3. **Actions/Tools** (optional): add actions for fetching files by SHA (or rely on manual links in YAML).
4. **Start a run** by pasting a filled copy of `templates/audit_input.sample.yaml` (rename it) and attaching links to artifacts.
5. **Decisions** appear as ADRs; CI gate blocks merges on **Fail** until remediation tasks are checked in.

---

### Notes

* Replace placeholders with your actual SSOT links and standards.
* Extend `audit_runner.py` to call your LLM provider and to parse/score checklists.
* Add BI/automation specifics for Power BI, Tableau, Zapier, IFTTT, Any.do, Obsidian, NotebookLM, n8n, Power Automate under `standards/` or `playbooks/` as needed.
