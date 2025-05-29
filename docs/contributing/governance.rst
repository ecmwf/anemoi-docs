.. _governance:

###################
 Anemoi Governance
###################

Anemoi is a young and evolving open-source project. As such, the
project's technical governance are still being defined, with a pragmatic
approach to adapt to the needs of the community and the institutions
involved in the development and use of Anemoi.

At present, two groups play key roles in the coordination and
decision-making processes within the project:

-  **Anemoi Technical Subgroup (ATS):** Composed of representatives from
   the various institutions contributing to Anemoi, this group meets
   regularly to discuss the technical direction of the project. ATS
   reviews and approves major changes, proposals, and contributions that
   could impact the broader user and developer community. See the
   :ref:`labelling-guidelines` and :ref:`ats-approval` for how technical
   decisions are flagged and processed through this group.

-  **@anemoisecurity group:** This group is responsible for managing
   access to sensitive components of the project infrastructure,
   including GitHub permissions and package publishing. The group also
   acts as the final gatekeeper for pull request merges that require
   higher scrutiny or formal review through ATS.

As the project matures, we expect to refine and expand the governance
model, potentially including additional roles, working groups, and
decision-making mechanisms to support transparency, scalability and
collaboration.

*********************************
 Anemoi Technical Subgroup (ATS)
*********************************

Anemoi is an open-source machine learning framework co-developed by
several national meteorological institutions in collaboration with
ECMWF. Details about individual contributors can be found in the
`CONTRIBUTORS.md
<https://github.com/ecmwf/anemoi-docs/blob/main/CONTRIBUTORS.md>`_ file
in each package. Inspired by the governance structures of other
open-source projects such as PyTorch and TensorFlow, **Anemoi is guided
by the Anemoi Technical Subgroup (ATS)**, a comitte composed of
representatives from each contributing institution. The ATS meets weekly
in what is known as the ATS meeting, which serves as a forum to
coordinate the project's technical direction. During these meetings, we
discuss ongoing development to ensure that the codebase evolves in a way
that meets the needs of all participating organizations. This includes
reviewing major pull requests (PRs), proposals for new features, and any
changes that could introduce breaking behavior or support new use cases.

PRs and issues intended for ATS discussion are identified using the
``ATS Approval Needed`` label. Refer to the :ref:`labelling-guidelines`
for more information on when and how to apply this label.

Additionally, contributors can tag ``@ATS`` in issues or PRs to
explicitly highlight topics requiring subgroup attention. This can be
especially helpful to summarize a disagreement, flag a potentially
controversial feature, or raise visibility for decisions that require
alignment across institutions.

***********************
 Anemoi Security Group
***********************

The ``@anemoisecurity`` group is a core part of Anemoi’s governance and review process. It is based on GitHub’s `CODEOWNERS <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>`_ mechanism, and is defined at the organization level: https://github.com/orgs/ecmwf/teams/anemoisecurity.

Members of this group are automatically tagged in pull requests that touch sensitive or protected areas of the codebase, as defined in each repository’s ``CODEOWNERS`` file.
Their role is to ensure consistent application of best practices, integrity, and to offer early guidance where there may be ambiguity or technical disagreement—before discussion at the Anemoi Technical Subgroup (ATS).

Responsibilities include:

- Reviewing PRs that affect critical infrastructure, security-sensitive components, or protected files.
- Providing guidance on best practices, code standards, and project conventions.
- Offering support to contributors with doubts about PR scope, reviewability, or technical alignment.
- Helping mediate technical disagreements when they arise, prior to ATS discussion.
- Acting as the merging authority for PRs labeled as ``ATS Approved``, according to the :ref:`labelling-guidelines`.

Contributors are encouraged to tag ``@anemoisecurity`` directly in issues or PRs when seeking early feedback on sensitive changes or when unsure how to proceed.

*****************
 Decision Making
*****************

# ! TODO - finish add section about ROADMAP from Daniele

Uncontroversial Changes
=======================

Primary work happens through issues and pull requests on GitHub.
Maintainers should avoid pushing their changes directly to the PyTorch
repository, instead relying on pull requests. Approving a pull request
by a core or module maintainer allows it to be merged without further
process. Core and module maintainers, as listed on the Maintainers page
and within CODEOWNERS ultimately approve these changes.

Notifying relevant experts about an issue or a pull request is
important. Reviews from experts in the given interest area are strongly
preferred, especially on pull request approvals. Failure to do so might
end up with the change being reverted by the relevant expert.

Controversial Decision Process
==============================

Substantial changes in a given interest area require a GitHub issue to
be opened for discussion. This includes:

Any semantic or syntactic change to the PyTorch framework or library.

Backwards-incompatible changes to the Python or C++ API.

Additions to the core framework or library, including substantial new
functionality within an existing library.

Removal of core features or platform support

Core and module maintainers ultimately approve these changes.
