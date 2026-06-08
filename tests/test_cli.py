from changelog_from_commits.cli import main


def test_cli_writes_output_file(tmp_path, monkeypatch) -> None:
    output_path = tmp_path / "CHANGELOG_DRAFT.md"
    monkeypatch.setattr("sys.stdin", ["feat: add report\n"])

    exit_code = main(["--stdin", "--title", "0.2.0", "--output", str(output_path)])

    assert exit_code == 0
    assert "## 0.2.0" in output_path.read_text(encoding="utf-8")
    assert "- Add report" in output_path.read_text(encoding="utf-8")
