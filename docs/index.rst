.. _index:

####################################
 Welcome to Anemoi's documentation!
####################################

The *Anemoi* framework provides a complete toolkit to develop
data-driven weather models – from data preparation through to inference.
The framework is composed of several packages which target the different
components necessary to construct data-driven weather models. To aid
development and deployment, each package collects metadata that can be
used by the subsequent packages. The framework builds upon on
established Python tools including `PyTorch <https://pytorch.org>`_,
`Lighting <https://lightning.ai/pytorch-lightning>`_, `Hydra
<https://hydra.cc>`_, `Zarr <https://zarr.dev>`_, `Xarray
<https://xarray.dev>`_ and `earthkit
<https://earthkit.readthedocs.io/>`_.

.. figure:: _static/anemoi-ecosystem.svg
   :align: center
   :scale: 80 %
   :target: _static/anemoi-ecosystem.svg
   :alt: Figure showing the structure of the Anemoi packages

Possible uses of *Anemoi* are for developing:

-  Global deterministic forecast models
-  Regional deterministic forecast models (limited-area models or
   stretched grids)
-  Coupled atmospheric and ocean models
-  Downscaling models
-  Ensemble/probabilistic models

#########
 License
#########

*Anemoi* is available under the open source `Apache License`__.

.. __: http://www.apache.org/licenses/LICENSE-2.0.html

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   Introduction <self>
   getting-started/package-descriptions.rst
   getting-started/installing.rst
   getting-started/tour.rst

.. toctree::
   :maxdepth: 1
   :caption: Contributing

   contributing/contributing.rst
   contributing/roadmap.rst
   contributing/environment.rst
   contributing/guidelines.rst
   contributing/code_style.rst
   contributing/testing.rst
   contributing/documentation.rst

.. toctree::
   :maxdepth: 1
   :caption: Anemoi Package Documentation

   anemoi-datasets <https://anemoi.readthedocs.io/projects/datasets/>
   anemoi-graphs <https://anemoi.readthedocs.io/projects/graphs/>
   anemoi-inference <https://anemoi.readthedocs.io/projects/inference/>
   anemoi-models <https://anemoi.readthedocs.io/projects/models/>
   anemoi-registry <https://anemoi.readthedocs.io/projects/registry/>
   anemoi-training <https://anemoi.readthedocs.io/projects/training/>
   anemoi-transform <https://anemoi.readthedocs.io/projects/transform/>
   anemoi-utils <https://anemoi.readthedocs.io/projects/utils/>
