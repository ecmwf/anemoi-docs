---
name: python-coding-style
description: Guidelines and best practices for writing Python code.
---

# Python coding style

Use this skill when writing or editing Python code.

## Goals

- Keep code readable, explicit, and easy to maintain.
- Prefer small functions with clear names and single responsibilities.
- Minimize duplication by factorizing shared logic.

## Rules

- Follow PEP 8 and standard Python naming conventions.
- Add type hints for function signatures and public APIs.
- Prefer early returns over deep nesting.
- Keep conditionals simple; for multi-case dispatch, prefer `match` or a dispatch table.
- Use exceptions for exceptional cases; avoid silent failures.
- Write docstrings for public functions, classes, and modules.
- Avoid unnecessary comments; only explain non-obvious intent.
- Keep imports organized and remove unused imports.

## Testing expectations

- Add or update tests when behavior changes.
- Cover edge cases for parsing, validation, and error handling.
- Keep tests deterministic and independent.

## Output format

When responding with code changes:

1. Briefly state what changed and why.
2. Provide file-level references for modified files.
3. Mention how correctness was checked (tests, lint, or reasoning).
