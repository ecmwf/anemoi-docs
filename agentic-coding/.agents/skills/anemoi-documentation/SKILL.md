---
name: anemoi-documentation
description: Guidelines and best practices for writing documentation in Anemoi packages.
---

# Anemoi documentation

Use this skill when writing or editing documentation for Anemoi code, workflows, and user-facing tools.

## Goals

- Keep documentation accurate, concise, and actionable.
- Explain purpose first, then usage, then implementation details.
- Keep examples aligned with current code behavior.

## Rules

- Prefer task-oriented sections: what, why, how.
- Document public APIs, CLI options, configuration fields, and error cases.
- Keep terminology consistent across packages and pages.
- Include minimal runnable examples when helpful.
- State assumptions, defaults, and constraints explicitly.
- Update documentation in the same change when behavior changes.
- Avoid stale references to removed options, modules, or commands.
- Use British spelling for words like "optimise" and "behaviour" in documentation, unless quoting code or error messages that use American spelling.
- Avoid inline code snippets, prefer including them as separate files, so they can be formatted and tested independently.

## Quality checks

- Verify commands, paths, and option names against the current code.
- Ensure examples are deterministic and do not require hidden setup.
- Remove ambiguity: replace vague wording with explicit requirements.
