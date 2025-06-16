import os
from os import path

import pyflow as pf
import wellies as wl
import yaml

SUITE_DIR = path.join(path.dirname(path.realpath(__file__)))


def parse_training_directory(training_directory: str) -> tuple[dict]:
    overrides_file = path.join(training_directory, "overrides.txt")
    overrides = load_overrides(overrides_file)

    task_file = path.join(training_directory, "task_config.yaml")
    with open(task_file, "r") as file:
        task_config = yaml.load(file, Loader=yaml.FullLoader)

    return overrides, task_config


def get_overrides_string(overrides: dict, training_output_dir: str, data_dir: str) -> str:
    overrides["hardware.paths.output"] = training_output_dir
    overrides["hardware.paths.data"] = data_dir
    return " ".join(f"{key}={value}" for key, value in overrides.items())


def load_overrides(config_file_path: str) -> dict:
    overrides = {}
    with open(config_file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            overrides[key.strip()] = value
    return overrides


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

        for file in os.listdir(dataset_config_dir):
            if not file.endswith(".yaml"):
                continue
            config_file_path = path.join(dataset_config_dir, file)
            output_path = path.join(config.data_dir, file.replace(".yaml", ".zarr"))
            task_name = file.replace(".yaml", "")

            create_command = f"anemoi-datasets create {config_file_path} {output_path} --overwrite"
            with self:
                create = pf.Task(
                    name=task_name.replace("-", "_"),
                    script=[
                        config.tools.load("datasets_env"),
                        create_command,
                    ],
                )
                completions[task_name] = create.complete
        self.completions = completions


class TrainingFamily(pf.AnchorFamily):
    def __init__(self, config, dataset_completions={}, **kwargs):
        super().__init__(name="training", **kwargs)
        training_config_dir = path.join(SUITE_DIR, "configs/training")
        data_dir = config.data_dir
        self.dataset_completions = dataset_completions

        for folder in os.listdir(training_config_dir):
            config_folder = path.join(training_config_dir, folder)
            if not path.isdir(config_folder):
                continue
            overrides, task_config = parse_training_directory(config_folder)

            training_output_dir = path.join(config.output_root, "training_output", str(folder))
            overrides_string = get_overrides_string(overrides, training_output_dir, data_dir)
            training_template = task_config.get("training_template")

            training_command = f"anemoi-training train --config-name={training_template} " + overrides_string
            with self:
                training = pf.Task(
                    name=folder,
                    script=[
                        config.tools.load("training_env"),
                        training_command,
                    ],
                )

            required_datasets = task_config.get("datasets", [])
            required_datasets_completions = [self.dataset_completions[dataset] for dataset in required_datasets]
            training.triggers = required_datasets_completions[0]
            for dataset_completion in required_datasets_completions[1:]:
                training.triggers &= dataset_completion


class MainSuite(pf.Suite):
    def __init__(self, config, **kwargs):

        # add your execution limits here
        limits = {
            "work": 20,
        }

        labels = {"info": "this is the anemoi test suite"}

        super().__init__(limits=limits, labels=labels, defstatus=pf.state.suspended, **kwargs)

        limits = {k: getattr(self, k) for k in limits.keys()}

        with self:

            f_init = InitFamily(config=config, inlimits=self.work)
            f_main = MainFamily(config=config, inlimits=self.work)
            f_main.triggers = f_init.complete
