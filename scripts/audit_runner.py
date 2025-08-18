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
