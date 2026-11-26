"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line to entry.txt: the apology a smart speaker gives its
owner after it mishears them. Deterministic, stdlib only, no network.
"""

import os

LINE = (
    "Sorry. I heard 'order a pizza' as 'order a divorce.' "
    "I have done neither, but the pizza is on hold."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
