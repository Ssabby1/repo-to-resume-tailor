#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from repo_to_resume_tailor_cli.installer import run


if __name__ == "__main__":
    raise SystemExit(run(["init", *sys.argv[1:]]))
