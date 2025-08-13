import os
from os import path

import pyflow as pf
import wellies as wl
import yaml

SUITE_DIR = path.join(path.dirname(path.realpath(__file__)))


def get_task_config(directory: str) -> tuple[dict]:
    task_file = path.join(directory, "task_config.yaml")
    if not path.exists(task_file):
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
        dataset_config_dir = path.join(SUITE_DIR, "configs/datasets")
        completions = {}

        with self:
            for folder in os.listdir(dataset_config_dir):
                local_config_folder = path.join(dataset_config_dir, folder)
                if not path.isdir(local_config_folder):
                    continue
                if not path.exists(path.join(local_config_folder, "dataset_config.yaml")):
                    raise FileNotFoundError(
                        f"Dataset test requires a config file: {local_config_folder}/dataset_config.yaml"
                    )

                create = get_dataset_task(folder, config)
                completions[folder] = create.complete
        self.completions = completions


def get_dataset_task(folder: str, config: dict) -> pf.Task:
    static_data_dir = "$DATA_DIR/anemoi_test_configs/datasets"
    config_file_path = path.join(static_data_dir, folder, "dataset_config.yaml")
    output_path = path.join("$DATA_DIR", folder + ".zarr")

    create_command = f"anemoi-datasets create {config_file_path} {output_path} --overwrite"

    create = pf.Task(
        name=folder.replace("-", "_"),
        script=[
            config.tools.load("datasets_env"),
            create_command,
        ],
    )
    return create


class TrainingFamily(pf.AnchorFamily):
    def __init__(self, config, dataset_completions={}, **kwargs):
        super().__init__(name="training", **kwargs)
        training_config_dir = path.join(SUITE_DIR, "configs/training")
        self.dataset_completions = dataset_completions

        with self:
            for folder in os.listdir(training_config_dir):
                config_folder = path.join(training_config_dir, folder)
                if not path.isdir(config_folder):
                    continue

                training = get_training_task(folder, config)

                task_config = get_task_config(config_folder)
                required_datasets = task_config.get("datasets", [])
                required_datasets_completions = [self.dataset_completions[dataset] for dataset in required_datasets]
                training.triggers = required_datasets_completions[0]
                for dataset_completion in required_datasets_completions[1:]:
                    training.triggers &= dataset_completion


def get_training_task(folder: str, config: dict) -> pf.Task:
    data_dir = "$DATA_DIR"
    static_data_dir = "$DATA_DIR/anemoi_test_configs/training/"
    output_root = "$OUTPUT_ROOT"
    training_output_dir = path.join(output_root, "training_output", str(folder))

    overrides = {}
    overrides["hardware.paths.output"] = training_output_dir
    overrides["hardware.paths.data"] = data_dir
    overrides_string = dict_to_overrides_string(overrides)

    training_command = (
        f"anemoi-training train  --config-name=training_config --config-path={static_data_dir}{folder} "
        + overrides_string
    )
    training = pf.Task(
        name=folder,
        script=[
            config.tools.load("training_env"),
            training_command,
        ],
        submit_arguments="gpu_job",
    )
    return training


class MainSuite(pf.Family):
    def __init__(self, config, **kwargs):
        super().__init__(defstatus=pf.state.suspended, **kwargs)

        with self:

            f_init = InitFamily(config=config, inlimits=self.work)
            f_main = MainFamily(config=config, inlimits=self.work)
            f_main.triggers = f_init.complete
