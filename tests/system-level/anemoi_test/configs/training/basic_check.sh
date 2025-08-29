if [[ ! -d "$CHECKPOINT_DIR" ]]; then
  echo "❌ Checkpoint directory not found: $CHECKPOINT_DIR"
  exit 1
fi
cd "$CHECKPOINT_DIR"

run_dirs=(*/)
if [[ ${#run_dirs[@]} -ne 1 ]]; then
  echo "❌ Expected exactly 1 run directory, found ${#run_dirs[@]}"
  exit 1
fi
run_dir="${run_dirs[0]}"

ckpt_files=( "$run_dir"/anemoi-by_epoch-*.ckpt )
if [[ ${#ckpt_files[@]} -ne 2 ]]; then
  echo "❌ Expected 2 training checkpoints anemoi-by_epoch-*.ckpt, found ${#ckpt_files[@]}"
  exit 1
fi

inf_ckpt_files=( "$run_dir"/inference-anemoi-by_epoch-*.ckpt )
if [[ ${#inf_ckpt_files[@]} -ne 2 ]]; then
  echo "❌ Expected 2 inference checkpoints inference-anemoi-by_epoch-*.ckpt, found ${#inf_ckpt_files[@]}"
  exit 1
fi
