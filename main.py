#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117.

Copies the pre-drawn image entry.png (a summary of Tuesday 17 November
2026's world news, drawn with PIL) to the output directory as entry.png.
Standard library only, no network.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"missing entry image: {src}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
