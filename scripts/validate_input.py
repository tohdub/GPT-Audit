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
