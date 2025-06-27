.. _testing-guidelines:

#########
 Testing
#########

Comprehensive testing is crucial for maintaining the reliability and
stability of the Anemoi packages. This guide outlines our testing
strategy and best practices for contributing tests.

We use pytest as our primary testing framework. Pytest offers a simple
and powerful way to write and run tests for Python projects. For more
details, refer to the `pytest documentation
<https://docs.pytest.org/en/stable/>`_.

****************
 Types of Tests
****************

Unit Tests
==========

-  Test individual components in isolation.
-  Should constitute the majority of test cases.
-  Unit tests reside in `tests/` or, for packages with integration
   tests, in `tests/unit`

Integration Tests
=================

-  Test how different components work together.
-  Important for data processing pipelines and model training workflows.
-  Integration tests reside in `tests/integration`.

***************
 Running Tests
***************

To run all unit tests:

.. code:: bash

   pytest

To run tests in a specific file:

.. code:: bash

   pytest tests/unit/test_specific_feature.py

To run all tests, including slow-running integration tests, set the
`SLOW_TESTS` environment variable to `1`. Follow the package-specific
instructions. For integration tests in anemoi-training, for instance,
ensure that you have GPU available and run:

.. code:: bash

   SLOW_TESTS=1 pytest training/tests/integration/

By convention, we recommend setting `SLOW_TESTS=1` inline with the
pytest command rather than exporting it into your shell environment.
This keeps the scope of the setting limited to that command and avoids
accidentally running slow tests in unrelated runs:

.. code:: bash

   SLOW_TESTS=1 pytest

This syntax works in most common shells (e.g. bash, zsh, sh). In other
environments -- such as SLURM job scripts or alternative shells -- you
may prefer to use export the variable instead:

.. code:: bash

export LONGTESTS=1 pytest training/tests/integration/

Remember to unset the variable afterwards if you use export:

.. code:: bash

unset LONGTESTS

By default (when LONGTESTS is unset or not 1), slow-running tests will
be skipped.

***************
 Writing Tests
***************

General Guidelines
==================

#. Write tests for all new features and bug fixes.
#. Aim for high test coverage, especially for critical components.
#. Keep tests simple, focused, and independent of each other.
#. Use descriptive names for test functions, following the pattern
   `test_<functionality>_<scenario>`.
#. Follow the :ref:`naming-conventions` for test files.
#. Keep tests fast: Optimize slow tests or mark them for separate
   execution.
#. Use appropriate assertions: pytest provides a rich set of assertions.
#. Test edge cases and error conditions, not just the happy path.
#. Regularly review and update tests as the codebase evolves.
#. Document complex test setups or scenarios.

By following these guidelines and continuously improving our test suite,
we can ensure the reliability and maintainability of Anemoi Training.

Example Test Structure
======================

.. code:: python

   import pytest
   from anemoi.training import SomeFeature


   def test_some_feature_normal_input():
       feature = SomeFeature()
       result = feature.process(normal_input)
       assert result == expected_output


   def test_some_feature_edge_case():
       feature = SomeFeature()
       with pytest.raises(ValueError):
           feature.process(invalid_input)

Tests features
==============

Here are some pytest features commonly used in the Anemoi packages.

Pytest's `parametrize
<https://docs.pytest.org/en/stable/how-to/parametrize.html>`_ decorator
can be used to run the same test with different inputs.

.. code:: python

   @pytest.mark.parametrize(
       "input,expected",
       [
           (2, 4),
           (3, 9),
           (4, 16),
       ],
   )
   def test_square(input, expected):
       assert square(input) == expected

Pytest's `fixtures
<https://docs.pytest.org/en/stable/how-to/fixtures.html>`_ can be used
to set up common test data or objects.

.. code:: python

   @pytest.fixture
   def sample_dataset():
       # Create and return a sample dataset
       pass


   def test_data_loading(sample_dataset):
       # Use the sample_dataset fixture in your test
       pass

Mocking external dependencies or complex objects can be achieved using
`unittest.mock <https://docs.python.org/3/library/unittest.mock.html>`_
or `pytest-mock <https://pytest-mock.readthedocs.io/en/latest/>`_.

.. code:: python

   def test_api_call(mocker):
       mock_response = mocker.Mock()
       mock_response.json.return_value = {"data": "mocked"}
       mocker.patch("requests.get", return_value=mock_response)

       result = my_api_function()
       assert result == "mocked"

***************************
 Writing Integration Tests
***************************

Marking Long-Running Tests
==========================

For long-running integration tests, we use the `SLOW_TESTS` environment
variable to ensure that they are run only when necessary. This means
that you should add the correspondong decorator to these tests:

.. code:: python

   from anemoi.utils.testing import skip_slow_tests

   @skip_slow_tests
   def test_slow():
         pass

Configuration Handling
======================

Integration tests in anemoi-training, anemoi-datasets, etc., rely on
appropriate handling of configuration files. Configuration management is
essential to ensure that the tests remain reliable and maintainable. Our
approach includes:

#. Using Configuration Templates: Always start with a configuration
   template from the repository to minimize redundancy and ensure
   consistency. We expect the templates to be consistent with the code
   base and have integration tests that check for this consistency.

#. Test-specific Modifications: Apply only the necessary
   use-case-specific (e.g. related to the dataset) and testing-specific
   (e.g. batch_size or restricted date range) modifications to the
   template.

#. Reducing Compute Load: Where possible, reduce the number of batches,
   epochs, batch sizes, number of dates etc.

#. Debugging and Failures: When integration tests fail, check the config
   files (e.g. in `training/src/anemoi/training/config`) for
   inconsistencies with the code and update the config files if
   necessary. Also check if test-time modifications have introduced
   unintended changes.

For more details and package-specific examples, please refer to the
package-level documentation.

***************
 Test Coverage
***************

We use pytest-cov to measure test coverage. To check coverage:

.. code:: bash

   pytest --cov=anemoi_training

Aim for at least 80% coverage for new features, and strive to maintain
or improve overall project coverage.
