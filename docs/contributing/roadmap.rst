#####################
 Development Roadmap
#####################

**Authors**: Anemoi Technical Subgroup (ATS)

**Date**: July 2025

This roadmap outlines the future development of the Anemoi project,
emphasizing flexibility, adaptability, and high performance to meet the
evolving needs of weather and climate modeling. We aim to build a
modular, extensible ecosystem — much like a set of well-defined Lego
blocks — where components such as model layers, training approaches, and
data pipelines can be easily assembled, reused, and adapted to support
diverse use cases, from regional to global forecasting. By promoting
generalization, interoperability, and ease of integration, Anemoi
enables users to experiment with new combinations or build on existing
ones. The collaboration of diverse institutions remains a core strength,
allowing the project to stay domain-agnostic and responsive to the
specific needs of a wide range of stakeholders.

************************
 Key Development Themes
************************

The technical direction for this project focuses on extending its
usability, modularity, and flexibility across different domains and
datasets. We have identified 4 key areas for improvement and expansion.

#. **Flexible Model Architectures**

   -  **Current Focus**:

      -  Focus on graph neural networks.
      -  Enhance model architectures to be more modular.
      -  Focus on implementing probabilistic and ensemble forecasting
         techniques (e.g., CRPS Loss, diffusion).

   -  **Long-Term Vision**:

      -  Develop a robust framework for model sharing across various
         ecosystems, supporting different types of models.

      -  Ensure that the infrastructure for model development and
         training can easily scale from local to global forecasting
         tasks, while maintaining computational efficiency.

#. **Data Handling**

   -  **Current Focus**:

      -  Support for multiple datasets, particularly for high-resolution
         observational data (e.g., radar, satellite, SYNOP).
      -  Implement multiple encoders and decoders.

   -  **Long-Term Vision**:

      -  Foster interoperability with other open-source tools, allowing
         users to easily integrate their datasets and models with
         external systems.

#. **Operational Deployment and MLOps**

   -  **Current Focus**:

      -  Develop CI/CD pipelines to automate testing, deployment, and
         operational inference.

      -  Focus on optimizing performance through improved memory
         management and computational efficiency (e.g., Torch
         compilation, HPC optimizations).

      -  Make inference as lightweight and efficient as possible to
         support real-time and large-scale operational deployment.

   -  **Long-Term Vision**:

      -  Strengthen MLOps practices to support full deployment cycles
         from development to production, ensuring that models can be
         updated and maintained effectively.

      -  Integrate tools for model versioning, dataset tracking, and
         reproducibility across different use cases.

#. **Collaboration and Interoperability**

   -  **Current Focus**:

      -  Develop shared standards for graph representations, model
         architectures, datasets, and code contributions to ensure
         smooth collaboration across contributors.

      -  Work towards better documentation and more educational
         resources to onboard new contributors.

   -  **Long-Term Vision**:

      -  Enable seamless collaboration across institutions and domains
         by developing common interfaces for datasets and models.
      -  Encourage community-driven extensions and contributions to keep
         the ecosystem open and extensible.

For progress and updates on these topics, we refer to the relative
Github issues and PRs across all Anemoi packages. An overview is
available in the `Anemoi Project Board
<https://github.com/orgs/ecmwf/projects/13/views/8>`_.

*********************
 Engaging More Users
*********************

In addition to the technical development, a key focus will be improving
user engagement and onboarding, which includes:

-  Developing comprehensive documentation and tutorials for users with
   various levels of expertise.

-  Creating interactive guides and visualizations to explain complex
   concepts like model training, dataset preparation, and operational
   inference.

-  Hosting community-driven workshops and outreach efforts to encourage
   broader participation and contributions.

Anemoi Community Meeting
========================

The **Anemoi Community Meeting** is a biweekly online gathering for
Anemoi developers and users.

**When:** Every other Tuesday from 11:00 to 12:00 CET, starting from
*July 1st, 2025*.

**Who:** Anyone involved in or interested in the Anemoi ecosystem is
welcome to join — including contributors, developers, researchers, and
representatives from weather and climate modeling projects (e.g., NMS).
Please feel free to share the invitation with colleagues who may benefit
from attending.

**Why:** As the Anemoi framework grows in functionality and usage, the
community meeting is a key touchpoint to maintain alignment, foster
collaboration, and surface new ideas. It's also a great opportunity to
network and discuss shared challenges or feature needs.

**Join:** `Click here to join the Anemoi Community Meeting on Microsoft
Teams
<https://teams.microsoft.com/l/meetup-ajoin/19%3ameeting_OTNjNDNmYWQtYTU0Ny00NDViLThmZjctZmQ1MTg1YjEyZGM0%40thread.v2/0?context=%7b%22Tid%22%3a%2221b711c6-aab7-4d36-9ffb-ac0357bc20ba%22%2c%22Oid%22%3a%225033de80-99cd-43c4-b9e4-f90840044fd6%22%7d>`_
=======
