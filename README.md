# GPT Audit (v1.0)

GPT Audit is a multi‑expert audit council for AI projects and custom GPTs. It enforces writing/UX/compliance standards, evaluates end‑to‑end workflows (prompts → APIs → automation), and explains trade‑offs in plain language with Good/Better/Best guidance.
  
## Quick Start
1. **Pin your SSOT**: add repo URLs and commit SHAs in `templates/audit_input.sample.yaml`.
2. **Fill the input file** for your project (vision, success criteria, artifacts, tool_stack).
3. **Run locally**:
   ```bash
   python scripts/validate_input.py path/to/your_input.yaml
   python scripts/audit_runner.py path/to/your_input.yaml --mode full_audit_Test PR to trigger GPT Audit workflow_
