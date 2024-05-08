"""
FIX COMMENT LENGTH
Utility to fix the length of the comments when above 86 chars.
-----------------------
Author: Hugo Middeldorp
"""
import sys
import re

__version__ = "1.0.0"


def process_file(file_path: str):
    """Given a file path, create a new .temp file with the comment length fixed"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            new_lines = []
            for line in file:
                # Line (any indentation) that starts with #
                comment_line = re.match(r"^\s*#\s", line)
                if comment_line:
                    comment_start = comment_line.group(0)
                while len(line) > 87 and comment_line:
                    # The first (max) 86 characters of the line (won't break words)
                    split_lines = re.findall(r"(.{0,86})(?:\s)", line)
                    new_lines.append(split_lines[0] + "\n")
                    line = f"{comment_start}   {' '.join(split_lines[1:])}\n"
                new_lines.append(line)
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    except FileNotFoundError:
        print("File not found:", file_path)


def main():
    if len(sys.argv) < 2:
        print("Usage: fcl <file_path>")
        sys.exit(1)
    for file_path in sys.argv[1:]:
        process_file(file_path)


if __name__ == "__main__":
    main()
