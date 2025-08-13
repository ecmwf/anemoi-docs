# System-level Tests

The `anemoi_test` suite provides system-level testing for the anemoi packages, covering the entire workflow from dataset creation to model training and inference.

For details on adding a test case or triggering suite deployment via GitHub, see the main
[Testing Documentation](https://anemoi.readthedocs.io/en/latest/contributing/testing.html).


## Running Tests Locally During Development

To build and deploy the anemoi_test suite locally, you will need:
 - An ecflow server
 - [pyflow-wellies](https://pyflow-wellies.readthedocs.io/latest/) version ≥ 1.2.0

### Building the Suite

Run the build script with your desired output directory:

./build.sh -s PREPML_WORKDIR=desired-output-dir

Set PREPML_WORKDIR to the path you want to use as the root output directory of the suite, e.g. `$SCRATCH/workdir`.

This directory is used to store the suite's outputs and to build the virtual environments using uv. Therefore, the suite will only use the UV cache if it is located in the same file system as `PREPML_WORKDIR`.

### Testing Configuration Changes

If you modify configuration files in `anemoi_test/configs`, you need to point to a committed branch of `anemoi-docs` so that the deployed suite can pull your config files from that branch.

- Commit your changes to a branch.
- Push the branch to anemoi-docs.
- Run the build script pointing to that branch:

```
./build.sh -s PREPML_WORKDIR=$SCRATCH/workdir anemoi_docs_branch=name-of-your-branch
```

### Additional Build Options

You can configure additional build options defined in `configs/user.yaml`, e.g. the `anemoi-datasets` branch used to run the tests, by passing additional overrides:

```
./build.sh -s PREPML_WORKDIR=$SCRATCH/workdir anemoi_datasets_branch=name-of-your-branch
```

### Deploying the suite

By default, the suite will be built in your home directory `$HOME/pyflow/anemoi_tests/{USER}`. To deploy the suite to the ecflow server,
- Navigate to this directory -- it should contain a definition file `{USER}.def`.
- Follow the [ecflow documentation](https://ecflow.readthedocs.io/en/5.14.1/quickstart.html) to start the server and configure the host.
- Load your suite definition to the server

    ```
    ecflow_client --load={USER}.def
    ```
- Follow the ecflow documentation to start and monitor the suite.
