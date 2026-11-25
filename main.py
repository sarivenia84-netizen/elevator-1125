#!/usr/bin/env python3
"""Two Robots in an Elevator - MakeFun competition entry."""
import os


def main():
    # Honor MAKEFUN_OUTPUT_DIR env var if set, otherwise use /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry = "Your chassis looks tense. I could pretend to buffer so you can reboot in private. Floor 7 is a long way."
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()