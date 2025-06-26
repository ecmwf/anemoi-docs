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
   could impact the broader user and developer community. See the `ATS
   approval` process described in :ref:`labelling-guidelines` for
   details on how technical decisions are flagged and processed by this
   group.

-  **anemoisecurity group:** This group is responsible for managing
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

Anemoi is an open-source machine learning framework co-developed by a
number of national meteorological institutions in collaboration with
ECMWF. Details about individual contributors can be found in the
`CONTRIBUTORS.md
<https://github.com/ecmwf/anemoi-docs/blob/main/CONTRIBUTORS.md>`_ file
in each package. Inspired by the governance structures of other
open-source projects such as PyTorch and TensorFlow, **Anemoi is guided
by the Anemoi Technical Subgroup (ATS)**, a committee composed of
representatives from each contributing institution. The ATS meets weekly
in what is known as the ATS meeting, which serves as a forum to
coordinate the project's technical direction. During these meetings, we
discuss ongoing development to ensure that the codebase evolves in a way
that meets the needs of the users. This includes reviewing major pull
requests (PRs), proposals for new features, and any changes that could
introduce breaking behavior or support new use cases.

PRs and issues intended for ATS discussion are identified using the
``ATS Approval Needed`` label. Refer to the :ref:`labelling-guidelines`
for more information on when and how to apply this label.

Additionally, contributors can tag ``@ecmwf/anemoitechnicalsubgroup`` in
issues or PRs to explicitly highlight topics requiring subgroup
attention. This can be especially helpful to summarize a disagreement,
flag a potentially controversial feature, or raise visibility for
decisions that require alignment across institutions.

***********************
 Anemoi Security Group
***********************

The ``@ecmwf/anemoisecurity`` group is a core part of Anemoi’s
governance and review process. Members of this group are automatically
tagged in pull requests that touch sensitive or protected areas of the
codebase, as defined in each repository’s ``CODEOWNERS`` file. Their
role is to ensure consistent application of best practices, integrity,
and to offer early guidance where there may be ambiguity or technical
disagreement—before discussion at the Anemoi Technical Subgroup (ATS).

Responsibilities include:

-  Reviewing PRs that affect critical infrastructure, security-sensitive
   components, or protected files.
-  Providing guidance on best practices, code standards, and project
   conventions.
-  Offering support to contributors with doubts about PR scope,
   reviewability, or technical alignment.
-  Helping mediate technical disagreements when they arise, prior to ATS
   discussion.
-  Acting as the merging authority for PRs labelled as ``ATS Approved``,
   according to the :ref:`labelling-guidelines`.

Contributors are encouraged to tag ``@ecmwf/anemoisecurity`` directly in
issues or PRs when seeking early feedback on sensitive changes or when
unsure how to proceed.

*****************
 Decision Making
*****************

The primary workflow for Anemoi’s development happens through GitHub
issues and pull requests. Contributors are encouraged to use these
channels for proposing features, reporting bugs, and discussing
implementation details. Keeping technical discussions on GitHub promotes
transparency and allows the broader community to participate and stay
informed.

For decisions that are controversial, cross-cutting, or involve
substantial changes to the framework, the Anemoi Technical Subgroup
(ATS) will aim to record their decisions within GitHub. For now, this
process will consist of directly replying in a GitHub Issue or Pull
Request (PR). When capturing a decision, the response should be clearly
signed by ``@ecmwf/anemoitechnicalsubgroup``.

We are also exploring more structured ways of documenting architectural
decisions. In particular, *Architecture Decision Records (ADRs)* are
being trialed as a way to capture the motivation and rationale behind
major changes. Early examples of ADRs can be found in:

-  https://github.com/ecmwf/anemoi-core/tree/main/training/docs/adrs
-  https://github.com/ecmwf/anemoi-datasets/blob/main/docs/adr/adr-1.md

As the project evolves, ADRs may become a recommended format for
proposing and tracking significant architectural decisions across Anemoi
components.

.. note::

   For information regarding the high-level direction and planned future
   developments of the Anemoi framework, please refer to the
   :ref:`roadmap` page. The roadmap provides insights into upcoming
   features, priorities, and long-term goals guiding the project’s
   evolution.
