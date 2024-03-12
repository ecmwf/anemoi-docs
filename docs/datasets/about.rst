##################
 Training dataset
##################

Training datasets are large array-like objects encode in Zarr_ format.
They

The array has the following dimensions:

.. figure:: data.png
   :alt: Data layout

The first dimension is the time dimension, the second dimension are the
variables (e.g. temperature, pressure, etc), the third dimension is the
ensemble, and fourth dimension are the grid points values.

This structure provides an efficient way to build the training dataset,
as input and output of the model are simply consecutive slices of the
array.

.. code:: python

   x, y  = ds[n], ds[n+1]
   y_hat = model.predict(x)
   loss  = model.loss(y, y_hat)

.. _zarr: https://zarr.readthedocs.io/
