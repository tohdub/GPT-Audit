# GPT Audit • Repo Skeleton & Quick-Start Pack (v1.0)

Below is a plug‑and‑play repo layout with ready templates, prompts, and CI hooks. Copy these files into your GitHub repo. At the end, we also include **branch protection instructions** so you can gate merges on audit results.

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

4. **CI Gate**: GitHub Actions workflow (`.github/workflows/audit.yml`) will run audits on PRs; merges are blocked on Fail once branch protection is enabled.

## Source of Truth (SSOT)

* All claims must cite pinned sources (commit SHA or permalink). Missing evidence → mark as Gap with severity.

## Outputs

* Quick Gate, Full Audit Report, or Change Review. Reports are attached to PRs and stored as build artifacts.

````

---

## Branch Protection Setup (Public Repo)
Since you made the repo **public**, branch protection rules now apply on the free tier.

### Steps:
1. Go to **Settings → Branches → Add rule**.
2. **Branch name pattern:** `main`
3. Enable:
   - ✅ Require pull request before merging
   - ✅ Require status checks to pass before merging
   - Select `GPT Audit` workflow as required check
   - ✅ (Recommended) Require conversation resolution
   - ✅ (Optional) Require signed commits
   - ✅ (Optional) Require linear history
4. Save.

Now every PR to `main` must pass the GPT Audit workflow before merging.

---

## Next Steps
- Extend `audit_runner.py` to parse outputs and assign Fail/Pass based on checklist scores.
- Add BI/automation specifics (Power BI, Tableau, Zapier, IFTTT, Any.do, Obsidian, NotebookLM, n8n, Power Automate) under `/standards/` or `/playbooks/`.
- Consider setting **severity gates** (Blocker=Fail, Score threshold required).

---

✅ With this skeleton and branch protection in place, GPT Audit can now block merges until your project passes standards-based audits.



---

## Branch Protection Setup (Public Repo)
Branch protection **is enforced** on public repositories, so you can gate merges immediately.

### Steps
1. Go to **Settings → Branches → Add rule**.
2. **Branch name pattern:** `main`
3. Enable:
   - **Require a pull request before merging**
   - **Require status checks to pass before merging**
   - After one PR run, select the workflow checks from **GPT Audit** as **Required**
   - *(Optional)* **Require conversation resolution**
   - *(Optional)* **Require signed commits**
   - *(Optional)* **Require linear history**
4. Save.

Now every PR to `main` must pass the GPT Audit workflow.

---

## Add a Real Gate (copy–paste files)
Paste the two code blocks below into your repo to turn the audit into a **hard gate**:

### `scripts/audit_runner.py` (replace existing)
```py
import sys, yaml, json

# Reads YAML input, emits two files:
# 1) audit_payload.json – normalized inputs (for debugging)
# 2) audit_report.json  – placeholder report with a checklist and blockers list
# In production, replace the placeholder scoring with your model's real output.

def main(path, mode="full_audit"):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    payload = {
        "entrypoint": {
            "user_goal": data.get("project", {}).get("vision", ""),
            "context_pack": data.get("ssot", {}).get("repos", []),
            "mode": data.get("mode", mode),
            "audience": data.get("audience", "mixed"),
            "priorities": data.get("priorities", []),
        },
        "artifacts": data.get("artifacts", {}),
        "standards": data.get("standards", {}),
        "tool_stack": data.get("tool_stack", {}),
    }

    with open("audit_payload.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    # Placeholder report: treat missing critical sections as minors; no blockers by default
    checklist_keys = [
        "technical_writing", "ux", "optimization", "reasoning_eval",
        "api_automation", "compliance_safety", "business_analytics"
    ]
    checklist = {k: 1 for k in checklist_keys}  # neutral defaults
    blockers = []

    report = {
        "verdict": "Pass",              # change to Fail if blockers or low score
        "severity": "Info",
        "checklist": checklist,
        "blockers": blockers,
        "score": sum(checklist.values()),
        "score_max": len(checklist_keys) * 2
    }

    with open("audit_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps({"status": "ok", "emitted": ["audit_payload.json", "audit_report.json"]}, indent=2))

if __name__ == "__main__":
    path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "full_audit"
    main(path, mode)
````

### `scripts/evaluate_gate.py` (new)

```py
import json, sys

THRESHOLD = 9            # minimal acceptable checklist score (out of 14)
BLOCK_FAIL = True        # any blocker forces fail

with open("audit_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

score = report.get("score", 0)
max_score = report.get("score_max", 14)
blockers = report.get("blockers", [])

print(f"Score: {score}/{max_score}")
print(f"Blockers: {len(blockers)}")

if BLOCK_FAIL and blockers:
    print("Gate: FAIL (blockers present)")
    sys.exit(1)

if score < THRESHOLD:
    print("Gate: FAIL (score below threshold)")
    sys.exit(1)

print("Gate: PASS")
```

### `.github/workflows/audit.yml` (replace with this)

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
      - name: Run audit (placeholder)
        run: |
          python scripts/audit_runner.py templates/audit_input.sample.yaml --mode full_audit
      - name: Evaluate gate
        run: |
          python scripts/evaluate_gate.py
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: audit-artifacts
          path: |
            audit_payload.json
            audit_report.json
```

---

## Next Steps

* Update `audit_runner.py` later to produce a **real** `audit_report.json` with Blockers/Minors and per‑section scores taken from the model output.
* In **Branch protection → Required status checks**, select the **GPT Audit / audit** job so merges are blocked on failures.

✅ With these files, PRs to `main` will be blocked if the report has blockers or the score is below threshold.
