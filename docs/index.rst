####################################
 Welcome to Anemoi's documentation!
####################################

*Anemoi* is a framework for developing machine learning weather
forecasting models. It comprises of components or packages for preparing
training datasets, conducting ML model training and a registry for
datasets and trained models. Anemoi provides tools for operational
inference, including interfacing to verification software. As a
framework it seeks to handle many of the complexities that
meteorological organisations will share, allowing them to easily train
models from existing recipes but with their own data.

.. toctree::
   :maxdepth: 1
   :caption: The Anemoi Framework

   overview

.. toctree::
   :maxdepth: 1
   :caption: Contributing

   contributing/contributing.rst
   contributing/environment.rst
   contributing/guidelines.rst
   contributing/code_style.rst
   contributing/testing.rst
   contributing/documentation.rst

**************
 Dependencies
**************

.. raw:: html

   <center>
   <object type="image/svg+xml" data="_static/dependencies.svg" width="75%" height="auto">
     <img src="_static/dependencies.png" alt="Fallback image description">
   </object>
   </center>

Arrows indicate dependencies between packages. Dashed lines indicate
optional dependencies.

*****************
 Anemoi packages
*****************

-  :ref:`anemoi-datasets <anemoi-datasets:index-page>`
-  :ref:`anemoi-graphs <anemoi-graphs:index-page>`
-  :ref:`anemoi-inference <anemoi-inference:index-page>`
-  :ref:`anemoi-models <anemoi-models:index-page>`
-  :ref:`anemoi-registry <anemoi-registry:index-page>`
-  :ref:`anemoi-training <anemoi-training:index-page>`
-  :ref:`anemoi-transform <anemoi-transform:index-page>`
-  :ref:`anemoi-utils <anemoi-utils:index-page>`

*********
 License
*********

*Anemoi* is available under the open source `Apache License`__.

.. __: http://www.apache.org/licenses/LICENSE-2.0.html
