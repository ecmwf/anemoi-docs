.. _installing:

############
 Installing
############

****************
 Python Version
****************

-  Python (> 3.9, <3.13)

Anemoi agrees to follow Python's official releases
https://devguide.python.org/versions/

.. note::

   Python 3.9 will be deprecated from the Anemoi Ecosystem before it's
   official End-of-Life (EOL) in October. At the moment Python 3.13 is
   not support accross the packages, since we have NumPy<2.0 pinned.

************
 Installing
************

All the Anemoi packages are distributed on `PyPI <https://pypi.org>`_.
To install an Anemoi package, you can use the following command:

.. code:: bash

   pip install anemoi-{package}

where ``{package}`` is one of the anemoi packages, e.g. ``datasets`` or
``training``.
