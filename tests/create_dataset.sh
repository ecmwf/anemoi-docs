#!/bin/bash
#SBATCH --job-name=create-dataset
#SBATCH --output=create-dataset-%j.out
#SBATCH --error=create-dataset-%j.err
#SBATCH --time=00:10:00
#SBATCH --mem=4G

set -euo pipefail

# Configurable paths
ANEMOI_DOCS_DIR="$HOME/Code/anemoi/anemoi-docs" # Path to anemoi-docs repo

DATA_DIR="$SCRATCH/anemoi-e2e/dataset"
CONFIG_FILE="$ANEMOI_DOCS_DIR/tests/global_test_dataset.yaml"
OUTPUT_PATH="$DATA_DIR/global-test-dataset.zarr" # Matches the path that train_model.sh expects

# Venv setup
VENV_DIR="$SCRATCH/anemoi-e2e/venvs/venv-datasets-${SLURM_JOB_ID:-$$}"
mkdir -p "$VENV_DIR"

echo "Creating dataset in: $OUTPUT_PATH"
mkdir -p "$DATA_DIR"

# Load Python module and set up virtualenv
module load python3/3.12.9-01
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip

pip install anemoi-datasets

# Run dataset creation
anemoi-datasets create "$CONFIG_FILE" "$OUTPUT_PATH"

# Clean up virtualenv
deactivate
rm -rf "$VENV_DIR"
