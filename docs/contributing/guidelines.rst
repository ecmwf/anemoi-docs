.. _development-guidelines:

########################
 Development Guidelines
########################

Please follow these development guidelines:

#. Open an issue before starting a feature or bug fix to discuss the
   approach with maintainers and other users.

#. Ensure high-quality code with appropriate tests (see
   :ref:`testing-guidelines`), documentation (see
   :ref:`documentation-guidelines`), linting, and style checks (see
   :ref:`code-style`).

#. Follow the :ref:`labelling-guidelines`.

#. Follow the :ref:`branching-guidelines`.

#. Follow the :ref:`pr-title-guidelines`.

.. _labelling-guidelines:

**********************
 Labelling Guidelines
**********************

As explained in the contributing guidelines, contributors are encouraged
to open issues to discuss new feature proposals or record bugs.
Similarly once those are addressed, PR should be open with the changes
proposed. To identify which issues or Pull Request need to discussed at
ATS, contributors can flag them using the following labels;

-  ``ATS Approval Needed`` – Even if the PR has already been reviewed
   and approved, it must be discussed at ATS before it can be merged.
   Once reviewed in the meeting, the label will be updated to ``ATS
   Approved``.

-  ``ATS Approval Not Needed`` – The PR can be merged if it has been
   reviewed and approved by a developer other than the contributor who
   opened it.

-  ``ATS Approved`` – Indicates that the PR has been reviewed and
   approved during the ATS meeting and is ready to be merged.

It is the responsibility of both the reviewer and the contributor to
ensure that a PR is correctly labeled. If you're unsure which label to
use, default to ``ATS Approval Needed`` or tag ``@anemoisecurity`` for
clarification.

.. note::

   Code must not be merged into any Anemoi packages without the
   appropriate label.

Labelling Issues
================

Per the contributing guidelines: *“Open an issue before starting a
feature or bug fix to discuss the approach with maintainers and other
users.”*

ATS should review newly opened issues that propose new features in order
to:

-  Ensure visibility across teams
-  Identify opportunities for collaboration
-  Discuss motivation and technical direction
-  Propose follow-ups (e.g., GitHub Discussion threads, working groups)
-  Surface potential concerns early on

Labelling PRs
=============

Flagging PRs for ATS helps to:

-  Confirm alignment across institutions
-  Notify users of incoming breaking changes
-  Invite feedback or raise concerns before merging
-  Identify if any organisation can contribute additional review

Examples of PRs that should be labeled ``ATS Approval Needed``:
---------------------------------------------------------------

-  Breaking changes

      -  API changes (e.g., modifying the `open_dataset` interface in
         `anemoi-datasets`)
      -  Configuration format changes that are not backward compatible
         (e.g., new required fields in Pydantic-based configs)

-  Dependency changes:

   -  Introducing new dependencies (especially for inference)
   -  Bumping major versions (e.g., upgrading `torch` from 2.4 to 2.5,
      or `zarr` from 2.x to 3.x)

-  Feature deprecation

-  Refactors or features that significantly expand project scope (these
   should be discussed via an issue first to avoid unmergeable PRs)

Examples of PRs that can be labeled ``ATS Approval Not Needed``:
----------------------------------------------------------------

-  Hotfixes and general bug fixes [*]_

-  A minor new feature such as:

   -  New callbacks
   -  Loss functions
   -  Extensions to metadata lineage in `anemoi-utils`
   -  New filter in `anemoi-transform`
   -  New grid types in `anemoi-graphs`

-  Extensions to testing or CI infrastructure [*]_

-  PRs addressing technical debt [*]_

.. [*]

   Assuming those do not imply any breaking changes or dependency changes
   as explained above

.. _branching-guidelines:

**********************
 Branching Guidelines
**********************

-  Use feature branches for new features (e.g., `feat/your-feature`)
-  Use fix branches for bug fixes (e.g., `fix/your-bug`)
-  Use a descriptive name that indicates the purpose of the branch
-  Keep branches up to date with `main` before opening a Pull Request

.. _pr-title-guidelines:

*********************
 PR Title Guidelines
*********************

The PR title will become the squash commit message when merged to
``main``, so please ensure that it follows these guidelines:

#. Follow the `Conventional Commits guidelines
   <https://www.conventionalcommits.org/>`_. The format is:
   ``type[(scope)][!]: description``. For example:

   -  ``feat(training): add new loss function``
   -  ``fix(graphs): resolve node indexing bug``
   -  ``docs(readme): update installation steps``
   -  ``feat(models)!: change model input format`` (breaking change)
   -  ``refactor!: restructure project layout`` (breaking change)

   Common types include:

   -  ``feat``: New feature.
   -  ``fix``: Bug fix.
   -  ``docs``: Documentation only.
   -  ``style``: Code style changes.
   -  ``refactor``: Code changes that neither fix bugs nor add features.
   -  ``test``: Adding or modifying tests.
   -  ``chore``: Maintenance tasks.

   Add ``!`` after the type/scope to indicate a breaking change. In
   Anemoi, Breaking changes are considered changes in the API or at
   config level that are not backward compatible. Note, backward
   compatibility at checkpoint level is not ensured in Anemoi and we
   don’t have a flag to specifically raise the PRs affecting
   checkpoints.

#. Reference relevant issue numbers in commit messages when applicable
   (e.g., "fix: resolve data loading issue #123").

These guidelines are enforced for PR titles because our automated
release process (`release-please
<https://github.com/googleapis/release-please>`_) relies on conventional
commits to generate changelogs and determine version bumps
automatically.

For commits more generally, we recommend to follow these conventions but
do not enforce them. We furthermore encourage you to

#. Make small, focused commits with clear and concise messages.
#. Use present tense and imperative mood in commit messages (e.g., "Add
   feature" not "Added feature").

.. _pullrequest-guidelines:

*************************
 Pull Request Guidelines
*************************

When submitting Pull Requests (PRs), please follow these guidelines:

#. Open a draft Pull Request early in your development process. This
   helps:

   -  Make your work visible to other contributors.
   -  Get early feedback on your approach.
   -  Avoid duplicate efforts.
   -  Track progress on complex changes.

#. Fill the PR template completely, including:

   -  Clear description of the changes.

   -  Link to related issues using GitHub keywords (e.g., "Fixes #123").

   -  List of notable changes.

   -  Any breaking changes or deprecations.

   -  Testing instructions if applicable.

   -  For ``refactors``, contributors are encouraged to include proof of
      regression tests or evidence demonstrating that existing
      functionality remains unaffected when completing the PR template.

   -  For ``new features``, such as loss functions or model blocks,
      contributors should provide benchmarking results that showcase the
      added performance or benefits in training ML models, building
      datasets, or other package-specific tasks.

   -  New features must also include relevant documentation and
      appropriate test coverage. This may range from unit tests to
      integration tests when new use cases are introduced. For detailed
      testing guidelines, refer to the :ref:`testing` section.

   -  It is the **reviewer's responsibility** to ensure that these
      criteria are met and to request additional information or tests if
      any of the above elements are missing.

#. Ensure the PR title follows the :ref:`pr-title-guidelines`, as this
   will become the squash commit message when merged to ``main``.

#. Keep your PR focused and of reasonable size:

   -  One PR should address one concern.
   -  Split large changes into smaller, logical PRs.
   -  Update documentation along with code changes.

#. Before marking as ready for review:

   -  Ensure all tests pass locally.
   -  Address any automated check failures.
   -  Review your own changes.
   -  Update based on any feedback received while in draft.

#. When ready for review:

   -  Mark the PR as "Ready for Review"
   -  Request reviews from appropriate team members.
   -  Be responsive to review comments.
   -  Update the PR description if significant changes are made.

#. After approval:

   -  PRs are merged using squash merge to maintain a clean history.
   -  The squash commit message will use the PR title and the
      description.
   -  It is the merger's responsibility to ensure that the commit
      message is clear and readable, following the PR template.

.. _merging-guidelines:

*********************************
 Pull Request Merging Guidelines
*********************************

Once a PR has been reviewed and the appropriate label is in place, the
following merging rules apply:

-  For PRs labeled ``ATS Approval Not Needed``: The PR can be merged by
   the reviewer once it has been approved, provided the reviewer is not
   the original contributor.

-  For PRs labeled ``ATS Approved``: These PRs will be merged by the
   ``@anemoisecurity`` group after they have been reviewed in the ATS
   meeting and marked with the ``ATS Approved`` label.

.. note::

   PRs that do not have either label **must not be merged**. When in
   doubt, apply the ``ATS Approval Needed`` label or consult
   ``@anemoisecurity`` for guidance.

***************
 Documentation
***************

Ensure that changes are appropriately documented, both with respect to
docstrings and more extensive documentation, following the guidelines on
:ref:`documentation-guidelines`.

.. _testing:

*********
 Testing
*********

All code changes must include appropriate tests. For more details and
examples, see the guidelines on :ref:`testing-guidelines`.

Key points:

#. Use pytest for all test cases.
#. Run tests locally before submitting PRs (``pytest``).
#. Add tests for both success and failure cases.

****************************
 Performance Considerations
****************************

Performance is critical in scientific computing. Follow these guidelines
to ensure efficient code:

Profiling and Monitoring
========================

Profile code to identify bottlenecks:

   -  Use ``cProfile`` for Python profiling.
   -  Use ``torch.profiler`` for PyTorch operations.
   -  Monitor memory usage with ``memory_profiler``.

Data Operations
===============

Optimize data handling:

   -  Use vectorized operations (NumPy/PyTorch) instead of loops.
   -  Batch process data when possible.
   -  Consider using ``torch.compile`` for PyTorch operations.
   -  Minimize data copying and type conversions.

Memory Management
=================

Be mindful of memory usage:

   -  Release unused resources promptly.
   -  Use generators for large datasets.
   -  Clear GPU memory when no longer needed.

Algorithm Optimization
======================

Choose efficient algorithms and data structures:

   -  Use appropriate data structures (e.g., sets for lookups).
   -  Cache expensive computations when appropriate.

.. note::

   Always benchmark performance improvements and document any critical
   performance considerations in docstrings. Balance code readability
   with performance optimizations.

************************
 Continuous Integration
************************

All unit tests are run automatically on our CI/CD pipeline for every
pull request after the initial review by maintainers. Ensure all tests
pass before submitting your PR.
