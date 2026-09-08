---
name: anemoi-testing
description: Guidelines and best practices for writing and maintaining tests in Anemoi packages.
---

# Anemoi testing

Use this skill when adding, updating, or reviewing tests for Anemoi Python packages.

## Goals

- Keep tests deterministic, fast, and focused on behavior.
- Validate scientific and data-processing logic with explicit expectations.
- Prevent regressions with clear coverage of normal, edge, and failure paths.

## Rules

- Use `pytest` and prefer function-scoped fixtures unless broader scope is required.
- Name tests by behavior, including expected outcome and relevant condition.
- Cover success, edge, and error cases for public APIs and critical internals.
- Avoid network, clock, and filesystem flakiness; mock or isolate external effects.
- Keep assertions specific; do not rely on broad truthiness checks when exact values matter.
- For floating-point behavior, use tolerances and explain chosen thresholds.
- Keep test data minimal and representative of real meteorological workflows.
- When fixing a bug, add a regression test that fails before and passes after the fix.

## Quality checks

- Ensure tests pass locally with `pytest` before finalizing changes.
- Keep runtime reasonable by avoiding redundant parametrizations and oversized fixtures.
- Remove dead tests and update outdated expectations when behavior intentionally changes.

## Output format

When responding with testing changes:

1. State what behavior is validated and why it matters.
2. List modified test files and the scenarios covered.
3. Report how correctness was checked (test run, targeted subset, or reasoning when execution is unavailable).
