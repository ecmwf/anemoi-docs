#########
 Options
#########

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

***********
 Combining
***********

ensembles
=========

.. code:: python

   open_dataset(ensembles=[dataset1, dataset2, ...])

grids
=====

.. code:: python

   open_dataset(grids=[dataset1, dataset2, ...], method=...)
