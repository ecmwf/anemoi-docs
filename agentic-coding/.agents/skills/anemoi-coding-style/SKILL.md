---
name: anemoi-coding-style
description: Code quality, formatting, file organization, and naming conventions for Anemoi packages.
---

# Anemoi code quality and style

Use this skill when writing or editing code in Anemoi packages. Style is enforced by pre-commit hooks.

## Code formatting

- Follow PEP 8, with a line length of 120 characters (not 79).
- Use `black` for consistent formatting.
- Use `isort` for import sorting: single-line imports, black-compatible formatting, project imports grouped under `anemoi`.
- Import group order: standard library, third-party, anemoi packages.

## Linting

Use `ruff` for linting: code style violations, potential bugs, complexity issues, best practices.

## Documentation style

- Format RST files with `rstfmt`.
- Docstrings must match function signatures (checked by `docsig`).
- Sphinx documentation is linted with `sphinx-lint`.

## Pre-commit checks

All code is automatically checked by pre-commit hooks that verify:

1. **Code formatting**: black formatting, import sorting, line endings and trailing whitespace.
2. **Code quality**: no debugger statements, no merge conflicts, type annotations, no blanket `noqa` statements.
3. **Documentation**: docstring validation, RST formatting, Sphinx linting.

## File organization

### Directory structure

- Core functionality goes in `src/anemoi/<package_name>/`.
- Tests go in `tests/`.
- Documentation goes in `docs/`.
- Group related functionality together in the same module.

When adding new files, ensure they are properly included in `__init__.py` files if they should be part of the public API. Keep `__init__.py` minimal and use it to define package-level exports via `__all__`.

Utility functions:

- Use `utils.py` only for package-specific helper functions that don't fit in other modules.
- If a utility could be useful across multiple packages, move it to the `anemoi-utils` package, document its general-purpose nature, and ensure it remains stateless and reusable.
- Avoid using `utils.py` as a catch-all; if multiple related utilities emerge, create a dedicated module.

### File structure

Within each file:

1. Start with the Anemoi contributors license header, then standard library, third-party, and local imports.
2. Follow with module-level constants or configurations.
3. Define classes and functions in a logical order: base classes before derived classes, related functions grouped together, public API before private implementations.

Use absolute imports within the package. Avoid wildcard (`*`) imports.

## Naming conventions

Use descriptive names that clearly indicate purpose or functionality.

- **Files and modules**: lowercase with underscores.
  - `reduced_gaussian_grid.py` ✅ / `ReducedGaussianGrid.py` ❌ / `rgrid.py` ❌ (too vague)
- **Classes**: PascalCase (CapWords).
  - `ReducedGaussianGridNodes` ✅, `MultiScaleEdges` ✅ / `reduced_gaussian_grid_nodes` ❌ / `Rgn` ❌ (too cryptic)
- **Functions and variables**: snake_case; verbs for functions, nouns for variables.
  - `calculate_edge_weights()` ✅, `get_coordinates()` ✅, `node_attributes` ✅ / `calculateEdgeWeights()` ❌ / `crds` ❌ (too vague)
- **Constants**: uppercase with underscores.
  - `MAX_GRID_RESOLUTION` ✅, `DEFAULT_BATCH_SIZE` ✅ / `MaxGridResolution` ❌
- **Private names**: prefix with a single underscore.
  - `_validate_input()` ✅, `_cached_result` ✅
- **Type variables**: CamelCase, preferably single letters or short names.
  - `T` ✅ (generic type), `NodeType` ✅, `EdgeAttr` ✅
- **Enums**: CamelCase class names, UPPERCASE members.
  - `class NodeType(Enum):` with `SOURCE = "source"`, `TARGET = "target"`
- **Tests**: prefix with `test_` (methods) or `Test` (classes); be descriptive about what is tested, including the scenario and expected outcome.
  - `test_reduced_gaussian_grid_with_invalid_resolution` ✅, `test_edge_builder_handles_empty_graph` ✅, `test_coordinates_are_in_radians` ✅ / `testGrid` ❌ (too vague) / `test1` ❌ (meaningless)

Avoid abbreviations unless widely understood in the domain (e.g. `lat`, `lon`). Clarity is more important than brevity.
