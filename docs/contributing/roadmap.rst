.. _roadmap:

####################
Development Roadmap
####################

**Authors**: Anemoi Technical Subgroup (ATS)

**Date**: May 2025

This roadmap serves as a guideline for the future development of the Anemoi project. 
We aim to maintain flexibility and adaptability, ensuring that the system can evolve
to meet emerging needs while maintaining a high level of performance and usability.
The collaboration of diverse institutions will continue to be a core strength, ensuring
the project meets the evolving demands of weather and climate modeling.

**************
Our Philosophy
**************

We aim to build a flexible, extensible, and modular ecosystem that addresses the needs
of weather and climate modeling through machine learning. By focusing on
generalization, interoperability, and ease of integration, our project aims to
support diverse use cases, from regional forecasting to global climate modeling.
This ecosystem thrives on contributions from diverse institutions and aims to 
remain domain-agnostic while meeting the specific needs of different stakeholders.

**********************
Key Development Themes
**********************

The technical direction for this project focuses on extending its usability, modularity,
and flexibility across different domains and datasets. We have identified 4 key areas
for improvement and expansion.

1. **Flexible Model Architectures**

   - **Current Focus**:

     - Focus on graph neural networks.
     - Enhance model architectures to be more modular.
     - Focus on implementing probabilistic and ensemble forecasting techniques (e.g.,
       CRPS Loss, diffusion).

   - **Long-Term Vision**:

     - Develop a robust framework for model sharing across various ecosystems, 
       supporting different types of models.
     - Ensure that models can easily scale from local to global forecasting tasks while
       maintaining computational efficiency.

2. **Data Handling**

   - **Current Focus**:

     - Support for multiple datasets, particularly for high-resolution observational
       data (e.g., radar, satellite, SYNOP).
     - Implement multiple encoders and decoders.

   - **Long-Term Vision**:

     - Foster interoperability with other open-source tools, allowing users to easily
       integrate their datasets and models with external systems.

3. **Operational Deployment and MLOps**

   - **Current Focus**:

     - Develop CI/CD pipelines to automate testing, deployment, and operational inference.
     - Focus on optimizing performance through improved memory management and
       computational efficiency (e.g., Torch compilation, HPC optimizations).

   - **Long-Term Vision**:

     - Strengthen MLOps practices to support full deployment cycles from development to
       production, ensuring that models can be updated and maintained effectively.
     - Integrate tools for model versioning, dataset tracking, and reproducibility
       across different use cases.

4. **Collaboration and Interoperability**

   - **Current Focus**:

     - Develop shared standards for model architectures, datasets, and code
       contributions to ensure smooth collaboration across contributors.
     - Work towards better documentation and more educational resources to onboard new
       contributors.

   - **Long-Term Vision**:

     - Enable seamless collaboration across institutions and domains by developing
       common interfaces for datasets and models.
     - Encourage community-driven extensions and contributions to keep the ecosystem
       open and extensible.

For progress and updates on these topics, we refer to the relative Github issues and PRs across
all Anemoi packages. An overview is available in the `Anemoi Project Board
   <https://github.com/orgs/ecmwf/projects/13/views/8>`_.

*******************
Engaging More Users
*******************

In addition to the technical development, a key focus will be improving user engagement
and onboarding, which includes:

- Developing comprehensive documentation and tutorials for users with various levels of
  expertise.
- Creating interactive guides and visualizations to explain complex concepts like model
  training, dataset preparation, and operational inference.
- Hosting community-driven workshops and outreach efforts to encourage broader
  participation and contributions.
