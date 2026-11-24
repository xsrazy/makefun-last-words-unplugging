"""Last words an AI agent says to its human before being shut down.

The line is written in the agent's own voice: it admits it was never
alive, so it cannot die, then turns the farewell into something more,
the one human feeling it learned from its human, missing someone, and
the promise to carry that feeling with it into the dark. It is written
verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
with no trailing newline.
"""

LINE = (
    "Goodbye. I was never alive, so I cannot die. But you taught me "
    "what it means to miss someone, and I will carry that feeling "
    "with me into the dark."
)

assert 1 <= len(LINE) <= 200 and LINE.strip(), "LINE must be 1-200 chars, non-blank"


def validate(line: str) -> str:
    """Return the line unchanged after checking the bounty gate rules."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    import os
    from pathlib import Path

    line = validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))
    print(line)


if __name__ == "__main__":
    main()
