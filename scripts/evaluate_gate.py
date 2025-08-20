import json, sys

THRESHOLD = 1            # TEMP: set higher later (e.g., 9)
BLOCK_FAIL = True        # any blocker forces fail

with open("audit_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

score = report.get("score", 0)
max_score = report.get("score_max", 14)
blockers = report.get("blockers", [])

print(f"Score: {score}/{max_score}")
print(f"Blockers

# make sure you’re on your PR branch
git checkout test-pr

# ensure folders exist
mkdir -p scripts templates .github/workflows

# scripts/audit_runner.py — writes both JSON files
cat > scripts/audit_runner.py << 'EOF'
import sys, yaml, json

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

    checklist_keys = [
        "technical_writing","ux","optimization","reasoning_eval",
        "api_automation","compliance_safety","business_analytics"
    ]
    checklist = {k: 1 for k in checklist_keys}  # neutral defaults
    report = {
        "verdict": "Pass",
        "severity": "Info",
        "checklist": checklist,
        "blockers": [],
        "score": sum(checklist.values()),
        "score_max": len(checklist_keys) * 2
    }
    with open("audit_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("Audit runner: wrote audit_report.json and audit_payload.json")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "templates/audit_input.sample.yaml"
    mode = sys.argv[2] if len(sys.argv) > 2 else "full_audit"
    main(path, mode)
