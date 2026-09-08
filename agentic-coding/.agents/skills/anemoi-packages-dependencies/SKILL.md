---
name: anemoi-packages-dependencies
description: Guidelines and best practices for managing dependencies in Anemoi packages.
---

Aim: minimise dependencies in Anemoi packages, and avoid unnecessary dependencies.

anemoi-inference will run in operations and therefore should have as few dependencies as possible (internal to anemoi or external libraries); anemoi-training can have more dependencies (e.g. matplotlib, cartopy, etc).

Allowed internal dependencies:

Transitive dependencies imply allowed direct imports. For example, since anemoi-datasets can import anemoi-transform and anemoi-transform can import anemoi-metadata, anemoi-datasets may also directly import anemoi-metadata.

- All anemoi packages can import anemoi-utils.
- anemoi-transform can import anemoi-metadata
- anemoi-models can import anemoi-graphs
- anemoi-datasets can import anemoi-transform
- anemoi-inference can import anemoi-transform
- anemoi-training can import anemoi-models
- anemoi-training can import anemoi-datasets
- anemoi-inference can import anemoi-models

anemoi-inference may optionally use anemoi-datasets if installed, but must not require it as a hard dependency.


Important note:

During training, the model is serialised (pickled) into the checkpoint. It is then unpickled during inference. Therefore, the model class must be available in both training and inference environments. This means that the model should not import unnecessary packages. These need to be imported by anemoi-training (e.g. torch-lightning, we don't want a dependency on torch-lightning in anemoi-inference). anemoi-models must not import packages that are unavailable in the inference environment (e.g. torch-lightning). Its allowed external dependencies are limited to those also permitted for anemoi-inference.
