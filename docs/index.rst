####################################
 Welcome to Anemoi's documentation!
####################################

.. warning::

   This documentation is work in progress. It is not yet ready.

*Anemoi* is a framework for developing machine learning weather
forecasting models. It comprises of components or packages for preparing
training datasets, conducting ML model training and a registry for
datasets and trained models. Anemoi provides tools for operational
inference, including interfacing to verification software. As a
framework it seeks to handle many of the complexities that
meteorological organisations will share, allowing them to easily train
models from existing recipes but with their own data. Using Anemoi and
ECMWF data, ECMWF can train AIFS. Users can use their own their own data
and through Anemoi train models they can name themselves. Anemoi is
built on many open source and widely used tools, for example PyTorch_
and Zarr_.

-  :doc:`overview`
-  :doc:`installing`
-  :doc:`firststeps`
-  :doc:`examples`

.. toctree::
   :maxdepth: 1
   :hidden:

   overview
   installing
   firststeps
   examples

**Models**

-  :doc:`models/components`
-  :doc:`models/examples`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Models

   models/components
   models/examples

**Training**

-  :doc:`training/components`
-  :doc:`training/examples`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Training

   training/components
   training/examples

**Datasets**

-  :doc:`datasets/about`
-  :doc:`datasets/building`
-  :doc:`datasets/using`
-  :doc:`datasets/sources`
-  :doc:`datasets/filters`
-  :doc:`/datasets/options`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Datasets

   datasets/about
   datasets/building
   datasets/using
   datasets/sources
   datasets/filters
   datasets/options

*********
 License
*********

*Anemoi* is available under the open source `Apache License`__.

.. __: http://www.apache.org/licenses/LICENSE-2.0.html

.. _pytorch: https://pytorch.org

.. _zarr: https://zarr.readthedocs.io/
