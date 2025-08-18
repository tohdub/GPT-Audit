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
