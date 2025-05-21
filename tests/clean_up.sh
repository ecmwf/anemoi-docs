#!/bin/bash
#SBATCH --job-name=clean-up
#SBATCH --output=clean-up-%j.out
#SBATCH --error=clean-up-%j.err
#SBATCH --time=00:10:00
#SBATCH --mem=4G

DATA_DIR="$SCRATCH/anemoi-e2e/dataset"
TRAINING_OUTPUT_DIR="$SCRATCH/anemoi-e2e/output"
VENVS_DIR="$SCRATCH/anemoi-e2e/venvs"

rm -rf "$DATA_DIR" "$TRAINING_OUTPUT_DIR" "$VENVS_DIR"
echo "Cleaned up directories: $DATA_DIR, $TRAINING_OUTPUT_DIR, $VENVS_DIR"
echo "Cleanup complete."
