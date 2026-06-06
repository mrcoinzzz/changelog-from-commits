# Changelog From Commits

A small command line tool that drafts a Markdown changelog from git commit messages.

It is designed for maintainers who want a quick release-note starting point without adopting a heavy release system.

## Features

- Reads commit subjects from a local git repository
- Uses the latest tag as the default range when available
- Groups commits into Added, Fixed, Documentation, Changed, and Other
- Supports custom ranges
- Can read commit subjects from stdin for scripts and tests

## Install

```bash
python3 -m pip install -e .
```

## Usage

Generate a changelog for the current repository:

```bash
changelog-from-commits
```

Use an explicit git range:

```bash
changelog-from-commits --range v0.1.0..HEAD
```

Read commit subjects from stdin:

```bash
git log --pretty=%s | changelog-from-commits --stdin
```

## Why this exists

Release notes are important, but they are often written at the end of already-tiring maintainer work. This tool creates a clean first draft so maintainers can focus on judgment and clarity.

## Roadmap

- Conventional Commits support
- GitHub compare links
- Pull request number extraction
- Markdown file output
- Optional OpenAI-powered release summaries

## License

MIT
