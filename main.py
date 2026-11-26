"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

The entry is a single line of at most 200 characters. Running this program
checks the line (one line only, inside the limit) and drops it into
entry.txt under the output directory the grader provides. The output is
fully fixed: no clock, no randomness, no network, so every run writes the
exact same bytes.
"""

import os
import sys

PUNCHLINE = (
    "The sock looked at me funny, so I did what any self-respecting "
    "vacuum would do: I inhaled the evidence."
)

LIMIT = 200


def resolve_output_dir():
    """Grader directory first, then /output, then a local fallback.

    The grader runs with a read-only working directory, so a relative
    path is never used: the output directory always comes from the
    environment or an absolute fallback.
    """
    for candidate in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output"):
        if candidate:
            return candidate
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def run():
    if len(PUNCHLINE) > LIMIT:
        print(
            "entry is %d characters, over the %d limit" % (len(PUNCHLINE), LIMIT),
            file=sys.stderr,
        )
        return 1
    if any(ch in PUNCHLINE for ch in ("\n", "\r")):
        print("entry must be a single line", file=sys.stderr)
        return 1

    target_dir = resolve_output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(PUNCHLINE)
    with open(target, encoding="utf-8", newline="") as handle:
        if handle.read() != PUNCHLINE:
            print("entry.txt does not match the line", file=sys.stderr)
            return 1
    print(PUNCHLINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
