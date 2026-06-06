from __future__ import annotations

from collections import OrderedDict


GROUPS = ("Added", "Fixed", "Documentation", "Changed", "Other")


def group_subjects(subjects: list[str]) -> OrderedDict[str, list[str]]:
    groups: OrderedDict[str, list[str]] = OrderedDict((group, []) for group in GROUPS)
    for subject in subjects:
        clean = subject.strip()
        if not clean:
            continue
        groups[_group_for(clean)].append(_clean_subject(clean))
    return groups


def generate_changelog(subjects: list[str], title: str = "Unreleased") -> str:
    groups = group_subjects(subjects)
    lines = [f"## {title}", ""]
    wrote_group = False

    for group, entries in groups.items():
        if not entries:
            continue
        wrote_group = True
        lines.extend((f"### {group}", ""))
        lines.extend(f"- {entry}" for entry in entries)
        lines.append("")

    if not wrote_group:
        lines.append("_No commits found._")

    return "\n".join(lines).rstrip() + "\n"


def _group_for(subject: str) -> str:
    lowered = subject.lower()
    if lowered.startswith(("feat:", "feature:", "add ", "added ")):
        return "Added"
    if lowered.startswith(("fix:", "bugfix:", "repair ")) or " fix " in f" {lowered} ":
        return "Fixed"
    if lowered.startswith(("docs:", "doc:")) or "readme" in lowered or "documentation" in lowered:
        return "Documentation"
    if lowered.startswith(("refactor:", "change:", "update:", "improve:")):
        return "Changed"
    return "Other"


def _clean_subject(subject: str) -> str:
    prefixes = ("feat:", "feature:", "fix:", "bugfix:", "docs:", "doc:", "refactor:", "change:", "update:", "improve:")
    lowered = subject.lower()
    for prefix in prefixes:
        if lowered.startswith(prefix):
            return subject[len(prefix) :].strip().capitalize()
    return subject
