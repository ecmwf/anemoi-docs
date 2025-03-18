# anemoi-docs

This repo builds the main [documentation](https://anemoi.readthedocs.io/) for the Anemoi project.

To build it yourself clone this repo and pip install:

```bash
git@github.com:ecmwf/anemoi-docs.git
cd anemoi-docs
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Then, build the documentation:

```bash
cd docs
make html
```
