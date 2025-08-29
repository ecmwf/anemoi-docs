import os
from pathlib import Path
from typing import Optional

import pyflow as pf
import wellies as wl
import yaml

SUITE_DIR = Path(__file__).resolve().parent

STATIC_DATA_DIR = Path("$DATA_DIR/anemoi_test_configs")
RESULTS_DIR_TRAINING = Path("$RESULTS_DIR/training")
RESULTS_DIR_DATASETS = Path("$RESULTS_DIR/datasets")


def load_yaml(config_file: Path) -> dict:
    with open(config_file, "r") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config


def dict_to_overrides_string(overrides: dict) -> str:
    return " ".join(f"{key}={value}" for key, value in overrides.items())


class CreateDatasetFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="datasets", **kwargs)
        dataset_config_dir = SUITE_DIR / "configs/datasets"

        with self:
            for folder in os.listdir(dataset_config_dir):
                local_config_folder = dataset_config_dir / folder
                if not local_config_folder.is_dir():
                    continue
                if not (local_config_folder / "dataset_config.yaml").exists():
                    raise FileNotFoundError(f"Dataset test requires a config file: {folder}/dataset_config.yaml")

                create_dataset = DatasetTask(folder, config)
                check_dataset = DatasetCheck(folder, create_dataset.output_path)
                create_dataset >> check_dataset


class DatasetTask(pf.Task):
    def __init__(self, name: str, suite_config: dict):
        config_file_path = STATIC_DATA_DIR / "datasets" / name / "dataset_config.yaml"
        self.output_path = RESULTS_DIR_DATASETS / (name + ".zarr")

        create_command = f"anemoi-datasets create {config_file_path} {self.output_path} --overwrite"

        super().__init__(
            name=name.replace("-", "_"),
            script=[suite_config.tools.load("datasets_env"), create_command],
        )


class DatasetCheck(pf.Task):
    def __init__(self, name: str, dataset_path: Path):
        check_if_dataset_exists = [f"test -d {dataset_path}", f"test -f {dataset_path}/.zattrs"]
        super().__init__(name="check_" + name.replace("-", "_"), script=check_if_dataset_exists)


class TrainingFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="training", **kwargs)
        training_config_dir = SUITE_DIR / "configs/training"

        with self:
            for folder in os.listdir(training_config_dir):
                config_folder = training_config_dir / folder
                if not config_folder.is_dir():
                    continue
                if not (config_folder / "training_config.yaml").exists():
                    raise FileNotFoundError(f"Training test requires a config file: {folder}/training_config.yaml")
                if not (config_folder / "task_config.yaml").exists():
                    raise FileNotFoundError(f"Training test requires a task config file: {folder}/task_config.yaml")

                training = TrainingTask(folder, config)

                task_config = load_yaml(config_folder / "task_config.yaml")
                training.required_datasets = task_config.get("datasets", [])

                check_training = TrainingCheck("check_" + folder, RESULTS_DIR_TRAINING / folder / "checkpoint")
                training >> check_training


class TrainingTask(pf.Task):
    def __init__(self, folder: str, suite_config: dict):
        self.required_datasets: Optional[str] = None

        overrides = {
            "--config-path": STATIC_DATA_DIR / "training" / folder,
            "hardware.paths.output": str(RESULTS_DIR_TRAINING / folder)
            + "/",  # add trailing slash to ensure checkpoints are in ".../global/checkpoint"
            "hardware.paths.data": RESULTS_DIR_DATASETS,
        }
        overrides_string = dict_to_overrides_string(overrides)

        training_command = "anemoi-training train  --config-name=training_config " + overrides_string

        super().__init__(
            name=folder, script=[suite_config.tools.load("training_env"), training_command], submit_arguments="gpu_job"
        )


class TrainingCheck(pf.Task):
    def __init__(self, name: str, checkpoint_path: Path):
        checkpoint_checks = pf.FileScript(SUITE_DIR / "configs/training/basic_check.sh")
        checkpoint_checks.environment_variable("CHECKPOINT_DIR", str(checkpoint_path))
        super().__init__(name=name, script=checkpoint_checks)


class CleanupTask(pf.Task):
    def __init__(self, **kwargs):
        script = ["rm -rf $OUTPUT_ROOT"]
        super().__init__(name="cleanup", script=script, **kwargs)


class InitFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="init", **kwargs)
        with self:
            deploy_tools = wl.DeployToolsFamily(config.tools)
            deploy_data = wl.DeployDataFamily(config.static_data)

            clean_up = CleanupTask()
            clean_up >> deploy_tools
            clean_up >> deploy_data


class MainFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="main", **kwargs)
        with self:
            create_fam = CreateDatasetFamily(config)
            training_fam = TrainingFamily(config)

            for training_task in [task for task in training_fam.all_tasks if isinstance(task, TrainingTask)]:
                if not training_task.required_datasets:
                    raise ValueError(
                        f"Training task '{training_task.name}' requires datasets, but none are specified in task_config.yaml."
                    )
                for dataset in training_task.required_datasets:
                    dataset_task = dataset.replace("-", "_")
                    if dataset_task not in [task.name for task in create_fam.all_tasks]:
                        raise KeyError(
                            f"Dataset '{dataset}' in training task {training_task.name} not found in dataset test cases. Ensure that all datasets match the name of a dataset test case."
                        )
                    create_fam.find_node(dataset_task) >> training_task

            clean_up = CleanupTask()
            create_fam >> clean_up
            training_fam >> clean_up  # only run cleanup if all tests pass


class MainSuite(pf.Family):
    def __init__(self, config, **kwargs):
        super().__init__(defstatus=pf.state.suspended, **kwargs)

        with self:
            f_init = InitFamily(config=config, inlimits=self.work)
            f_main = MainFamily(config=config, inlimits=self.work)
            f_init >> f_main
