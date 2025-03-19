##########
 Overview
##########

The *Anemoi* framework provides a complete toolkit to develop
data-driven weather models through data preparation to inference. The
ecosystem is composed of several packages which target the different
components necessary to construct a data-driven model. Each component
collects metadata that can be used by the subsequent packages. The
framework rely on existing Python tools including PyTorch, Lighting,
Hydra, Zarr, Xarray and earthkit.

.. raw:: html

   <center>
   <object type="image/svg+xml" data="_static/anemoi-ecosystem.svg" width="75%" height="auto">
     <img src="_static/anemoi-ecosystem.png" alt="Fallback image description">
   </object>
   </center>

Possible uses:

-  Global deterministic forecast models
-  Regional deterministic forecast models (LAM or stretched grid)
-  Coupled atmospheric and ocean models
-  Downscaling models
-  Ensemble/probablistic models

############
 Installing
############

All the Anemoi packages are distributed on `PyPI <https://pypi.org>`_.
To install an Anemoi package, you can use the following command:

.. code:: bash

   pip install anemoi-{package}

*****************
 anemoi-datasets
*****************

Anemoi-datasets provides the tools to build Zarr files from a list of
sources and filters. Input format sources include MARS, Grib, netCDF,
Zarr and more, while the filters allow for complex data transformation
and manipulation. The output dataset is optimised for ML training with
appropriate chunking and precomputed statistics for normalisation. The
package also support parallel and incremental creation for large
datasets.

*************
 anemoi-core
*************

anemoi-training
===============

Anemoi-training provides the code to train models, using
pytorch-lightning and Hydra. The training is highly configurable via
configuration files. The package also includes profiling evaluation,
plotting and logging of defined model and system metrics. The model to
train is also fully defined in the configuration files and utilises
anemoi-models to achieve this. Additionally the dataset must be Zarr
following the anemoi-datasets format.

anemoi-graphs
=============

Anemoi-graphs provides the functionality to create complex global or
local area graphs. The graph contains nodes and edges that indicate how
the grid is structured and how the input, latent and output states are
connected. The graph will then be used by the model to identify the
neighbouring points of each node in the encoder, processor and decoder
communications.

anemoi-models
=============

Anemoi-models provides the implementation for various type of models.
These models are based on a graph encoder-processor-decoder approach and
are implemented over the pytorch library. The model contains the weights
of the different layers applied to each node of a graph.

******************
 anemoi-inference
******************

Anemoi-inference provides the tools to take a trained model and perform
the inference/rollout given some initial conditions. Inference takes
full use of the metadata stored in a checkpoint, allowing for simple
execution.

********************
 Other anemoi tools
********************

The previous packages also use some functionality implemented in other
anemoi subprojects.

-  anemoi-registry: contains the functionality to save a dataset, a
   model or an experiment to the anemoi catalogue
   https://anemoi.ecmwf.int/.

-  anemoi-transform: contains data transformation functions used as
   filter to the datasets.

-  anemoi-utils: contains utility functions for the other subprojects.
