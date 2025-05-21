#!/bin/bash
#SBATCH --job-name=train-model
#SBATCH --output=train-model-%j.out
#SBATCH --error=train-model-%j.err
#SBATCH --time=00:40:00
#SBATCH --mem=4G

set -euo pipefail

# Configurable paths
ANEMOI_DOCS_DIR="$HOME/Code/anemoi/anemoi-docs" # Path to anemoi-docs repo

DATA_DIR="$SCRATCH/anemoi-e2e/dataset"  # Dataset dir used by create_dataset.sh
DATASET_NAME="global-test-dataset.zarr" # Name of the dataset file created by create_dataset.sh
OVERRIDES_FILE="$ANEMOI_DOCS_DIR/tests/training_overrides_global.txt"

# Output & temp dirs
VENV_DIR="$SCRATCH/anemoi-e2e/venvs/venv-train-${SLURM_JOB_ID:-$$}"
OUTPUT_DIR="$SCRATCH/anemoi-e2e/output"

mkdir -p "$VENV_DIR" "$OUTPUT_DIR"

# Load Python and create virtualenv
module load python3/3.12.9-01
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip

pip install anemoi-training==0.4.0 anemoi-models==0.5.0 anemoi-graphs==0.5.1

# Read overrides from the file and add additional overrides
# to set the dataset path and output directory
mapfile -t OVERRIDES < "$OVERRIDES_FILE"
OVERRIDES+=(
  "hardware.paths.output=$OUTPUT_DIR"
  "hardware.paths.data=$DATA_DIR"
  "hardware.files.dataset=$DATASET_NAME"
)

echo "Running training with config.yaml and overrides from $OVERRIDES_FILE"
echo "Dataset: $DATASET_NAME"

# Run training
anemoi-training train --config-name=config "${OVERRIDES[@]}"

# Cleanup
deactivate
rm -rf "$VENV_DIR"
