from __future__ import annotations

import subprocess
from pathlib import Path


def commit_subjects(root: Path, revision_range: str | None = None) -> list[str]:
    command = ["git", "log", "--pretty=%s"]
    if revision_range:
        command.insert(2, revision_range)
    else:
        tag = latest_tag(root)
        if tag:
            command.insert(2, f"{tag}..HEAD")

    result = subprocess.run(command, cwd=root, check=True, capture_output=True, text=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def latest_tag(root: Path) -> str | None:
    result = subprocess.run(
        ["git", "describe", "--tags", "--abbrev=0"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None
