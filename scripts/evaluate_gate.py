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
