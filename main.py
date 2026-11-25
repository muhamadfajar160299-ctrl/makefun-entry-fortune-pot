"""Fortune in a Pot entry runner.

Reads the one-line houseplant fortune shipped beside this script and
copies it verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt, so the grader sees
exactly the fortune in entry.txt (plus its trailing newline).
"""

import os
import sys
from pathlib import Path

try:
    src = Path(__file__).resolve().parent / "entry.txt"
    text = src.read_text(encoding="utf-8")
except OSError as exc:
    print(f"cannot read entry.txt: {exc}", file=sys.stderr)
    raise SystemExit(1)

if not text.strip():
    print("entry.txt is empty or whitespace only", file=sys.stderr)
    raise SystemExit(1)

try:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    out.write_text(text, encoding="utf-8")
    os.chmod(out, 0o644)
except (OSError, KeyError) as exc:
    print(f"cannot write output entry.txt: {exc}", file=sys.stderr)
    raise SystemExit(1)
