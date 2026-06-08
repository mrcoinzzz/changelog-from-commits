from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .generator import generate_changelog
from .gitlog import commit_subjects


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="changelog-from-commits",
        description="Draft a Markdown changelog from git commit subjects.",
    )
    parser.add_argument("path", nargs="?", default=".", help="Repository path")
    parser.add_argument("--range", dest="revision_range", help="Git revision range, for example v0.1.0..HEAD")
    parser.add_argument("--title", default="Unreleased", help="Changelog heading")
    parser.add_argument("--stdin", action="store_true", help="Read commit subjects from stdin")
    parser.add_argument("--output", help="Write the generated changelog to a Markdown file")
    args = parser.parse_args(argv)

    if args.stdin:
        subjects = [line.strip() for line in sys.stdin if line.strip()]
    else:
        try:
            subjects = commit_subjects(Path(args.path), args.revision_range)
        except Exception as error:
            print(f"Could not read git commits: {error}", file=sys.stderr)
            return 2

    changelog = generate_changelog(subjects, args.title)
    if args.output:
        try:
            Path(args.output).write_text(changelog, encoding="utf-8")
        except OSError as error:
            print(f"Could not write changelog: {error}", file=sys.stderr)
            return 2
    else:
        print(changelog, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
