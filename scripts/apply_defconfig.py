import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: apply_defconfig.py <defconfig_file> <fragment_file>")
        sys.exit(1)

    defconfig_path = sys.argv[1]
    fragment_path = sys.argv[2]

    with open(fragment_path, "r") as f:
        fragment_lines = f.read().splitlines()

    config_map = {}
    for line in fragment_lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#") and line.endswith("is not set"):
            # e.g. # CONFIG_LTO_CLANG_FULL is not set
            parts = line.split()
            if len(parts) >= 3:
                key = parts[1]
                config_map[key] = line
        elif not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            if val == "n":
                config_map[key] = f"# {key} is not set"
            else:
                config_map[key] = line

    with open(defconfig_path, "r") as f:
        orig_lines = f.readlines()

    new_lines = []
    found_keys = set()
    for line in orig_lines:
        sline = line.strip()
        replaced = False
        for key, full in config_map.items():
            if sline == f"# {key} is not set" or sline.startswith(f"{key}="):
                new_lines.append(full + "\n")
                found_keys.add(key)
                replaced = True
                break
        if not replaced:
            new_lines.append(line)

    for key, full in config_map.items():
        if key not in found_keys:
            new_lines.append(full + "\n")

    with open(defconfig_path, "w") as f:
        f.writelines(new_lines)
    print("Successfully merged defconfig options in-place.")

if __name__ == "__main__":
    main()
