###################
 Developer Install
###################

As a developer, you will want to install all of the **Anemoi** packages
from source. This will allow you to make changes to the code and test
them locally.

If you are only looking to work on one feature at a time, having one
install of the package you are working on may be sufficient. However, if
you are looking to work on multiple features at once, you may wish to
explore worktrees or other methods of managing multiple branches.

.. code:: bash

   # Clone the repositories
   git clone https://github.com/ecmwf/anemoi-utils.git utils
   git clone https://github.com/ecmwf/anemoi-core.git core
   git clone https://github.com/ecmwf/anemoi-inference.git inference
   git clone https://github.com/ecmwf/anemoi-datasets.git datasets
   git clone https://github.com/ecmwf/anemoi-transforms.git transforms

   # Navigate to the project directories and install
   for dir in [utils, inference, datasets, transforms core/graphs core/training core/models]; do
       pushd $dir
       pip install -e .
       popd
   done
