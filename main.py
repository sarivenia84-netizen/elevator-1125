#!/usr/bin/env python3
"""Two Robots in an Elevator - MakeFun competition entry."""
import os


def main():
    # Honor MAKEFUN_OUTPUT_DIR env var if set, otherwise use /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry = "My sensor detects tension. Pretending buffer for private reboot. Floor 7 remains distant."
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()