from changelog_from_commits.generator import generate_changelog, group_subjects


def test_group_subjects_sorts_common_commit_types() -> None:
    groups = group_subjects(["feat: add export", "fix: repair parser", "docs: update README"])

    assert groups["Added"] == ["Add export"]
    assert groups["Fixed"] == ["Repair parser"]
    assert groups["Documentation"] == ["Update README"]


def test_generate_changelog_outputs_markdown() -> None:
    changelog = generate_changelog(["feat: add cli"], "0.1.0")

    assert "## 0.1.0" in changelog
    assert "### Added" in changelog
    assert "- Add cli" in changelog
