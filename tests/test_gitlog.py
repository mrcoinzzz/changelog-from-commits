from pathlib import Path

from changelog_from_commits.gitlog import latest_tag


def test_latest_tag_returns_none_outside_git_repo(tmp_path: Path) -> None:
    assert latest_tag(tmp_path) is None
