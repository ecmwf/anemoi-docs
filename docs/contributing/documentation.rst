.. _documentation-guidelines:

###############
 Documentation
###############

We welcome contributions to the documentation of Anemoi, whether
improving existing documentation or adding documentation for specific
use cases or features. Your contributions help make Anemoi better for
everyone.

******************************
 Documentation on ReadTheDocs
******************************

When adding a new feature, modifying existing functionality, or working
on an undocumented use case, please consider updating the high-level
documentation. This ensures other users can understand and build upon
your work.

Steps for contributing documentation:

-  Follow the workflow for :ref:`contributing` to Anemoi, including
   creating an issue and submitting a Pull Request.

-  Identify the most appropriate place for your addition (e.g., overall
   `Anemoi documentation <https://github.com/ecmwf/anemoi-docs>`_,
   package-level documentation), and the relevant section (e.g., user
   guide, getting started, or developer guide).

-  You find the documentation in the `docs` directory of the Anemoi
   repository. The documentation is written in reStructuredText (reST)
   format. Add your changes to the appropriate file in the `docs`
   directory and pay attention to the following:

   -  Consider maintainability — are interfaces still evolving?
   -  Write clear and concise documentation using simple, direct
      sentences.
   -  Add references to related sections or external documentation where
      applicable.
   -  Include plots or diagrams where appropriate, and place them in the
      `docs/_static` folder.

-  Incorporate feedback from your reviewer regarding documentation
   clarity and completeness.

If you are unsure where to add documentation or how to structure it,
please feel free to ask for help on the issue you opened at any point.

Building Documentation
======================

For each Pull Request that modifies the files in the `docs` folder,
documentation is automatically built and hosted on ReadTheDocs for
review. It is automatically linked in the PR description. Please check
that the generated links point to the correct documentation and that
your changes render as expected.

If the links do not work or the documentation fails to render, review
the CI workflow “Read the Docs PR Preview” that builds the preview.
Check the logs for errors. You can see an example of a successful build
`here
<https://app.readthedocs.org/projects/anemoi-training/builds/27886217/>`_.
If you can’t identify the problem or are unsure, please ask for help in
the issue you opened.

You can also build the documentation locally to preview changes before
submitting a Pull Request. We use Sphinx for documentation.

You can install the dependencies for building the documentation with:

.. code:: bash

   pip install '.[docs]'

To build the documentation locally:

.. code:: bash

   cd docs
   make html

The terminal output will show the progress of the build process. If
everything goes well, you will see a message indicating that the
documentation has been built successfully:

.. code:: bash

   Running Sphinx v8.1.3
   loading translations [en]... done
   [...]
   writing additional pages... search done
   dumping search index in English (code: en)... done
   dumping object inventory... done
   build succeeded, 1 warning.

   The HTML pages are in _build/html.

The generated documentation will be in `docs/_build/html/index.html`.

.. note::

<<<<<<< HEAD
   When trying to build the docs locally with versions of Sphinx =>8.2,
   an environment with Python 3.11 or greater is required.
=======
   To build the docs locally, you will need Python 3.11 or greater.
>>>>>>> main

Viewing the Documentation
=========================

You can view the documentation built locally by opening the `index.html`
file in `docs/_build/html/` in your web browser:

.. code:: bash

   open docs/_build/html/index.html # macOS
   xdg-open docs/_build/html/index.html # Linux
   start docs/_build/html/index.html # Windows

Alternatively, you can serve the documentation using a local server:

.. code:: bash

   cd docs/_build/html
   python -m http.server

Then, open your web browser and navigate to `http://localhost:8000` to
view the documentation.

If you are working in an hpc environment and don't have a GUI or web
browser, there are several options to view the docs:

-  You can copy the docs to your local machine after building them, and
   view them in a browser.
-  You can serve the docs over an ssh tunnel.

************
 Docstrings
************

We follow the `NumPy docstring style
<https://numpydoc.readthedocs.io/en/latest/format.html>`_. All Python
files should include proper documentation using the following
guidelines:

Module Docstrings
=================

Each module should start with a docstring explaining its purpose:

.. code:: python

   """
   Module for building and managing reduced Gaussian grid nodes.

   This module provides functionality to create and manipulate nodes based on
   ECMWF's reduced Gaussian grid system, supporting both original and octahedral
   grid types.
   """

Class Docstrings
================

Classes should have detailed docstrings following this format:

.. code:: python

   class ReducedGaussianGridNodes:
       """Nodes from a reduced gaussian grid.

       A gaussian grid is a latitude/longitude grid. The spacing of the latitudes
       is not regular. However, the spacing of the lines of latitude is
       symmetrical about the Equator.

       Attributes
       ----------
       grid : str
           The reduced gaussian grid identifier (e.g., 'O640')
       name : str
           Unique identifier for the nodes in the graph

       Methods
       -------
       get_coordinates()
           Get the lat-lon coordinates of the nodes.
       register_nodes(graph, name)
           Register the nodes in the graph.

       Notes
       -----
       The grid identifier format follows ECMWF conventions:
       - 'N' prefix for original reduced Gaussian grid
       - 'O' prefix for octahedral reduced Gaussian grid
       - Number indicates latitude lines between pole and equator

       For example, 'O640' represents an octahedral grid with 640
       latitude lines between pole and equator.
       """

Function Docstrings
===================

Functions should have clear docstrings with parameters, returns, and
examples:

.. code:: python

   def get_coordinates(self) -> torch.Tensor:
       """Get the coordinates of the nodes.

       Returns
       -------
       torch.Tensor
           A tensor of shape (num_nodes, 2) containing the latitude and longitude
           coordinates in radians.

       Examples
       --------
       >>> nodes = ReducedGaussianGridNodes("O640", "data")
       >>> coords = nodes.get_coordinates()
       >>> print(coords.shape)
       torch.Size([6599680, 2])
       """

Property Docstrings
===================

Properties should have concise but clear docstrings:

.. code:: python

   @property
   def num_nodes(self) -> int:
       """Number of nodes in the grid."""
       return len(self.coordinates)

Type Hints
==========

Always combine docstrings with type hints for better code clarity and
catch potential errors:

.. code:: python

   def register_nodes(
       self, graph: HeteroData, attrs_config: dict[str, dict] | None = None
   ) -> HeteroData:
       """Register nodes in the graph with optional attributes.

       Parameters
       ----------
       graph : HeteroData
           The graph to add nodes to
       attrs_config : dict[str, dict] | None
           Configuration for node attributes

       Returns
       -------
       HeteroData
           The updated graph with new nodes
       """

Private Methods
===============

Even private methods should have basic documentation:

.. code:: python

   def _validate_grid(self) -> None:
       """Validate the grid identifier format.

       Raises
       ------
       ValueError
           If grid identifier doesn't match expected format
       """

.. note::

   -  Keep docstrings clear and concise while being informative.

   -  Include examples for non-obvious functionality.

   -  Document exceptions that might be raised.

   -  Update docstrings when changing function signatures.

   -  Use proper indentation in docstrings for readability.

   -  Add inline comments for complex logic or algorithms.

   -  To reference other documentation sections, use:

      -  ``:ref:`section-name``` for internal documentation links
      -  ```Section Title <link>`_`` for external links

      Example:

      .. code:: python

         """
         Process nodes in the graph.

         See Also
         --------
         :ref:`graphs-post-processor` : Documentation about post-processing nodes
         `PyG Documentation <https://pytorch-geometric.readthedocs.io/>`_ : External docs
         anemoi.graphs.nodes.TriNodes : Reference to another class
         """
