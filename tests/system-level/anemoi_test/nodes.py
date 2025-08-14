import os
from pathlib import Path

import pyflow as pf
import wellies as wl
import yaml

SUITE_DIR = Path(__file__).resolve().parent

STATIC_DATA_DIR = Path("$DATA_DIR/anemoi_test_configs")
RESULTS_DIR_TRAINING = Path("$RESULTS_DIR/training")
RESULTS_DIR_DATASETS = Path("$RESULTS_DIR/datasets")


def get_task_config(directory: Path) -> tuple[dict]:
    task_file = directory / "task_config.yaml"
    if not task_file.exists():
        raise FileNotFoundError(f"Test requires a task config file: {task_file}")
    with open(task_file, "r") as file:
        task_config = yaml.load(file, Loader=yaml.FullLoader)
    return task_config


def dict_to_overrides_string(overrides: dict) -> str:
    return " ".join(f"{key}={value}" for key, value in overrides.items())


class InitFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="init", **kwargs)
        with self:
            # install environments and packages
            wl.DeployToolsFamily(
                config.tools,
            )

            # setup static data (remote/local copy/link)
            wl.DeployDataFamily(
                config.static_data,
            )


class MainFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="main", **kwargs)
        with self:
            create_fam = CreateDatasetFamily(config)
            TrainingFamily(config, dataset_completions=create_fam.completions)


class CreateDatasetFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="datasets", **kwargs)
        dataset_config_dir = SUITE_DIR / "configs/datasets"
        completions = {}

        with self:
            for folder in os.listdir(dataset_config_dir):
                local_config_folder = dataset_config_dir / folder
                if not local_config_folder.is_dir():
                    continue
                if not (local_config_folder / "dataset_config.yaml").exists():
                    raise FileNotFoundError(f"Dataset test requires a config file: {folder}/dataset_config.yaml")

                create = DatasetTask(folder, config)
                completions[folder] = create.complete
        self.completions = completions


class DatasetTask(pf.Task):
    def __init__(self, name: str, suite_config: dict):
        # static_data_dir = "$DATA_DIR/anemoi_test_configs/datasets"
        config_file_path = STATIC_DATA_DIR / "datasets" / name / "dataset_config.yaml"
        self.output_path = RESULTS_DIR_DATASETS / (name + ".zarr")

        create_command = f"anemoi-datasets create {config_file_path} {self.output_path} --overwrite"

        super().__init__(
            name=name.replace("-", "_"),
            script=[suite_config.tools.load("datasets_env"), create_command],
        )


class TrainingFamily(pf.AnchorFamily):
    def __init__(self, config, dataset_completions={}, **kwargs):
        super().__init__(name="training", **kwargs)
        training_config_dir = SUITE_DIR / "configs/training"
        self.dataset_completions = dataset_completions

        with self:
            for folder in os.listdir(training_config_dir):
                config_folder = training_config_dir / folder
                if not config_folder.is_dir():
                    continue

                training = TrainingTask(folder, config)

                task_config = get_task_config(config_folder)
                required_datasets = task_config.get("datasets", [])
                required_datasets_completions = [self.dataset_completions[dataset] for dataset in required_datasets]
                training.triggers = required_datasets_completions[0]
                for dataset_completion in required_datasets_completions[1:]:
                    training.triggers &= dataset_completion


class TrainingTask(pf.Task):
    def __init__(self, folder: str, suite_config: dict):

        overrides = {}
        overrides["--config-path"] = STATIC_DATA_DIR / "training" / folder
        overrides["hardware.paths.output"] = RESULTS_DIR_TRAINING / folder
        overrides["hardware.paths.data"] = RESULTS_DIR_DATASETS
        overrides_string = dict_to_overrides_string(overrides)

        training_command = (
            "anemoi-training train  --config-name=training_config " + overrides_string  # --config-path={config_path} "
        )

        super().__init__(
            name=folder, script=[suite_config.tools.load("training_env"), training_command], submit_arguments="gpu_job"
        )


class MainSuite(pf.Family):
    def __init__(self, config, **kwargs):
        super().__init__(defstatus=pf.state.suspended, **kwargs)

        with self:

            f_init = InitFamily(config=config, inlimits=self.work)
            f_main = MainFamily(config=config, inlimits=self.work)
            f_main.triggers = f_init.complete
