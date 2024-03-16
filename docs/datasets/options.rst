#########
 Options
#########

These are equivalent:

.. code:: python

   open_dataset(path)
   open_dataset(dataset=path)
   open_dataset({"dataset": path})

The last example is useful when the dataset is defined from a
configuration file:

.. code:: python

   with open("config.yaml") as file:
       config = yaml.safe_load(file)

   ds = open_dataset(config)

When defining a dataset from another, you can either use a path or a
dataset:

.. code:: python

   open_dataset(path, statistics=other_path)
   open_dataset(path, statistics=other_dataset)
   open_dataset(path, statistics={"dataset": other_path, ...})

This also applies when combining datasets:

.. code:: python

   open_dataset(ensembles=[dataset1, dataset2, ...])
   open_dataset(ensembles=[path1, path2, ...])
   open_dataset(ensembles=[dataset1, path2, ...])
   open_dataset(ensembles=[{"dataset": path1, ...}, {"dataset": path2, ...}, ...])

*********
 Options
*********

dataset
=======

start
=====

end
===

frequency
=========

select
======

drop
====

reorder
=======

rename
======

.. code:: python

   open_dataset(dataset, rename={"old_name": "new_name", ...})

.. _statistics:

statistics
==========

.. code:: python

   open_dataset(dataset, statistics=other_dataset)

thinning
========

.. code:: python

   open_dataset(dataset, thinning=..., method="every-nth")

area
====

********************
 Combining datasets
********************

When combining datasets, the statistics of the first dataset are used by
default. You can change this by setting the :ref:`statistics` option to
a different dataset, even if it is not part of the combination. See

concat
======

You can concatenate two or more datasets along the dates dimension. The
package will check that all datasets are compatible (same resolution,
same variables, etc.). Currently, the datasets must be given in
chronological order with no gaps between them.

.. code:: python

   from ecml_tools.data import open_dataset

   ds = open_dataset(
       "aifs-ea-an-oper-0001-mars-o96-1940-1978-1h-v2",
       "aifs-ea-an-oper-0001-mars-o96-1979-2022-1h-v2"
   )

.. image:: concat.png
   :alt: Concatenation

Please note that you can pass more than two ``zarr`` files to the
function.

   **NOTE:** When concatenating file, the statistics are not recomputed;
   it is the statistics of first file that are returned to the user.

join
====

You can join two datasets that have the same dates, combining their
variables.

.. code:: python

   from ecml_tools.data import open_dataset

   ds = open_dataset(
       "aifs-ea-an-oper-0001-mars-o96-1979-2022-1h-v2",
       "some-extra-parameters-from-another-source-o96-1979-2022-1h-v2",
   )

.. image:: join.png
   :alt: Join

If a variable is present in more that one file, that last occurrence of
that variable will be used, and will be at the position of the first
occurrence of that name.

.. image:: overlay.png
   :alt: Overlay

Please note that you can join more than two ``zarr`` files.

ensembles
=========

.. code:: python

   open_dataset(ensembles=[dataset1, dataset2, ...])

grids
=====

.. code:: python

   open_dataset(grids=[dataset1, dataset2, ...], method=...)
