.. _setting-up-the-development-environment:

####################
 Development Set-up
####################

To create a development environment follow the steps outlined below.

**********************
 Setting Up Your Fork
**********************

When working with a fork, follow these steps to set up your local
development environment:

#. **Fork the repository:** Create your own copy of the repository on
   GitHub, following `this GitHub tutorial
   <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository>`_.

#. **Clone your fork:** Download your forked repository to your local
   machine as outlined in `this section of the tutorial
   <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#cloning-your-forked-repository>`_.

#. **Add the upstream remote:** Connect your local repository to the
   original repository to fetch updates as described in `this section
   <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#configuring-git-to-sync-your-fork-with-the-upstream-repository>`_.

#. **Prevent accidental pushes to upstream:** After setting up your fork
   and configuring the original repository as an upstream remote, it's a
   good practice to prevent accidental pushes to the upstream
   repository. You can do this by explicitly setting the push URL of the
   upstream remote to no_push. To do this, navigate to your local
   repository and run:

   .. code:: bash

      git remote set-url --push upstream no_push

   Verify the change with:

   .. code:: bash

      git remote -v

   You should see something like this:

   .. code:: bash

      origin    https://github.com/your-username/repository.git (fetch)
      origin    https://github.com/your-username/repository.git (push)
      upstream  https://github.com/original-owner/repository.git (fetch)
      upstream  no_push (push)

   With this configuration, you can still fetch updates from the
   upstream repository but won’t be able to accidentally push changes to
   it.

***********************************
 Creating Your Virtual Environment
***********************************

#. Create and activate a virtual environment with a python version
   >=3.9, and <3.13.

#. Navigate to the repository you cloned and for which you want to
   install the dependencies.

   For packages in anemoi-core, i.e. `anemoi-training`, `anemoi-models`,
   or `anemoi-graphs`, navigate to the relevant package directory

   .. code:: bash

      cd anemoi-core/{package}

   where `{package}` is the package name, e.g. `training`.

   For all other packages:

   .. code:: bash

      cd anemoi-{package}

   where `{package}` is the package name, e.g. `datasets`.

#. Install dependencies:

   .. code:: bash

      # For all dependencies
      pip install -e .

      # For development dependencies
      pip install -e '.[dev]'

#. (macOS only) Install pandoc for documentation building:

   .. code:: bash

      brew install pandoc

.. _pre-commit-hooks:

******************
 Pre-Commit Hooks
******************

We use `pre-commit <https://pre-commit.com>`_ hooks to ensure code
quality and consistency. To set them up:

#. Install pre-commit hooks:

   .. code:: bash

      pre-commit install

#. Run hooks on all files to verify installation:

   .. code:: bash

      pre-commit run --all-files

These pre-commit hooks will run for each commit.
