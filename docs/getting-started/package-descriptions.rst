.. _package-descriptions:

#################
 Anemoi Packages
#################

Detailed below are brief descriptions of the packages which make up the
Anemoi framework.

*****************
 anemoi-datasets
*****************

:ref:`anemoi-datasets <anemoi-datasets:index-page>` provides the tools
to build datasets which are optimised for machine learning training,
with appropriate chunking and precomputed statistics for normalisation.
These datasets can be built from a range of input sources, including
MARS, Grib, NetCDF, Zarr and more. Additionally, a number of filters
have been developed which can be used to support data transformations to
aid model development. Finally, the package also supports parallel and
incremental dataset creation (useful for large datasets).

*****************
 anemoi-training
*****************

:ref:`anemoi-training <anemoi-training:index-page>` provides the
functionality to train machine learning models, using `pytorch-lightning
<https://lightning.ai/pytorch-lightning>`_ and `Hydra
<https://hydra.cc>`_. The training is highly configurable and fully
defined through configuration files (utilising :ref:`anemoi-models
<anemoi-models:index-page>` to achieve this). The package also includes
profiling evaluation, plotting and logging of defined model and system
metrics. :ref:`anemoi-training <anemoi-training:index-page>` is designed
to work with datasets created using :ref:`anemoi-datasets
<anemoi-datasets:index-page>`.

***************
 anemoi-graphs
***************

:ref:`anemoi-graphs <anemoi-graphs:index-page>` provides the
functionality to create complex global or local area graphs. The graph
contains nodes and edges that indicate how the grid is structured and
how the input, latent and output states are connected. The graph can
then be used by the model to identify the neighbouring points of each
node in the encoder, processor and decoder communications.

***************
 anemoi-models
***************

:ref:`anemoi-models <anemoi-models:index-page>` provides implementations
for various type of models. These models are based on a graph
encoder-processor-decoder approach and are implemented using the
`PyTorch <https://pytorch.org>`_ library. The model contains the weights
of the different layers applied to each node of a graph.

******************
 anemoi-inference
******************

:ref:`anemoi-inference <anemoi-inference:index-page>` provides the tools
to take a trained model and perform the inference/rollout given some
initial conditions. Inference makes full use of the metadata stored in a
checkpoint to facilitate simple execution without requiring large
amounts of boilerplate code.

******************
 anemoi-transform
******************

:ref:`anemoi-transform <anemoi-transform:index-page>` provides the tools
to perform data transformations across training and inference. This package
aims to contain common functionality, such as filters, to be used consistently for anemoi-datasets,
anemoi-training and anemoi-infrence. 


***********************
 Other anemoi packages
***********************

The packages described above also use some functionality implemented in
other anemoi subpackages:

-  :ref:`anemoi-registry <anemoi-registry:index-page>`: contains the
   functionality to save a dataset, a model or an experiment to the
   `anemoi catalogue <https://anemoi.ecmwf.int/>`_ so that it can be
   easily shared with others.

-  :ref:`anemoi-utils <anemoi-utils:index-page>`: contains miscellaneous
   utility functions which are used across the other packages.

*******************************
 Dependencies between packages
*******************************

The relationship between the various Anemoi packages is illustrated in
the figure below. Solid lines indicate mandatory dependencies between
packages and dashed lines indicate optional dependencies.

.. raw:: html

   <center>
   <object type="image/svg+xml" data="../_static/dependencies.svg" width="75%" height="auto">
     <img src="../_static/dependencies.png" alt="Figure showing the dependencies across anemoi packages">
   </object>
   </center>
