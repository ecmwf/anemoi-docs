##########
 Overview
##########

The *Anemoi* framework provides a complete toolkit to develop
data-driven model from data preparation to inference. The ecosystem is
composed of several packages which target the different components
necessary to construct a data-driven model. Each component collects
metadata that can be used by the others. The framework rely on existing
python tools including PyTorch, Lighting, Hydra, Zarr, Xarray and
earthkit.

.. raw:: html

   <center>
   <object type="image/svg+xml" data="_static/anemoi-ecosystem.svg" width="75%" height="auto">
     <img src="_static/anemoi-ecosystem.png" alt="Fallback image description">
   </object>
   </center>

Possible usages:

-  global deterministic forecast model
-  regional deterministic forecast model (LAM or stretched grid)
-  coupled atmospheric and ocean model
-  downscaling model
-  ensemble model

*****************
 anemoi-datasets
*****************

Anemoi-datasets provides the tools to build Zarr files from a list of
sources and filters. Input format sources include MARS, Grib, netCDF,
Zarr and more and filters allow for data transformation. The output
dataset is optimize for ML training with appropriate chunking and
already computed statistics for normalisation. The package also support
parallel and incremental creation for large datasets.

*************
 anemoi-core
*************

anemoi-training
===============

Anemoi-training provides the code to train models, using torch-lightning
and Hydra. The training is highly configurable via configuration files.
The package includes profiling evaluation, plotting and logging of
defined model and system metrics. The model to train is defined in the
configuration files and refere to an anemoi-models implementation and
the dataset must be Zarr following the anemoi-datasets format.

anemoi-graphs
=============

Anemoi-graphs provides functionality to create graph structure. The
graph indicates how the grid is structured and how the nodes from the
input, latent and output states are connected. The graph contains the
nodes from the input, hidden and output states and the edges connecting
each of them. The graph will be use by the model to know the neighbourg
points of each node in the encoder, processor and decoder weights
calculation.

anemoi-models
=============

Anemoi-models provides the implementation for different type of models.
These models are describe in anemoi-models documentation. They are based
on graph encoder-processor-decoder methods and are implemented over
torch-lighting library. The model contains the weights of the different
layers applied to each node of a graph.

******************
 anemoi-inference
******************

Anemoi-inference package provides the tools to perform the inference of
trained models over chosen data. Default setup for inference is part of
the checkpoint metadata.

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
