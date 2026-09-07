# (C) Copyright 2026 Anemoi contributors.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import os
from pathlib import Path

import pyflow as pf
import wellies as wl
import yaml

SUITE_DIR = Path(__file__).resolve().parent

STATIC_DATA_DIR = Path("$DATA_DIR/anemoi_test_configs")
RESULTS_DIR_DATASETS = Path("$RESULTS_DIR/datasets")
RESULTS_DIR_TRAINING = Path("$RESULTS_DIR/training")
RESULTS_DIR_INFERENCE = Path("$RESULTS_DIR/inference")


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
                try:
                    task_config = load_yaml(local_config_folder / "task_config.yaml")
                except FileNotFoundError as e:
                    raise FileNotFoundError(
                        f"Dataset test requires a task config file: {folder}/task_config.yaml"
                    ) from e

                dataset_cmd = task_config.get("anemoi_command", "anemoi-datasets create")
                create_dataset = DatasetTask(folder, config, dataset_cmd=dataset_cmd)
                check_dataset = DatasetCheck(folder, create_dataset.output_path)
                create_dataset >> check_dataset


class DatasetTask(pf.Task):
    def __init__(self, name: str, suite_config: dict, dataset_cmd: str = "anemoi-datasets create"):
        config_file_path = STATIC_DATA_DIR / "datasets" / name / "dataset_config.yaml"
        self.output_path = RESULTS_DIR_DATASETS / (name + ".zarr")

        create_command = dataset_cmd + f" {config_file_path} {self.output_path} --overwrite"

        super().__init__(
            name=name.replace("-", "_"),
            script=[suite_config.tools.load("datasets_env"), create_command],
        )


class DatasetCheck(pf.Task):
    def __init__(self, name: str, dataset_path: Path):
        check_if_dataset_exists = [f"test -d {dataset_path}", f"test -f {dataset_path}/.zattrs"]
        super().__init__(name="check_" + name.replace("-", "_"), script=check_if_dataset_exists)


class CreateTrainingFamily(pf.AnchorFamily):
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
                try:
                    task_config = load_yaml(config_folder / "task_config.yaml")
                except FileNotFoundError as e:
                    raise FileNotFoundError(
                        f"Training test requires a task config file: {folder}/task_config.yaml"
                    ) from e

                training_cmd = task_config.get("anemoi_command", "anemoi-training train")
                training = TrainingTask(folder, config, training_cmd=training_cmd)
                check_training = TrainingCheck("check_" + folder, RESULTS_DIR_TRAINING / folder / "checkpoint")
                training >> check_training

                # Attach required datasets to the training task to set triggers in main family
                training.required_datasets = task_config.get("datasets", [])


class TrainingTask(pf.Task):
    def __init__(self, folder: str, suite_config: dict, training_cmd: str = "anemoi-training train"):
        self.required_datasets: str | None = None

        overrides = {
            "--config-path": STATIC_DATA_DIR / "training" / folder,
            "system.output.root": str(RESULTS_DIR_TRAINING / folder)
            + "/",  # add trailing slash to ensure checkpoints are in ".../global/checkpoint"
            "system.input.root": RESULTS_DIR_DATASETS,
            "training.max_epochs": 2,
        }

        training_command = training_cmd + " --config-name=training_config " + dict_to_overrides_string(overrides)

        super().__init__(
            name=folder, script=[suite_config.tools.load("training_env"), training_command], submit_arguments="gpu_job"
        )


class TrainingCheck(pf.Task):
    def __init__(self, name: str, checkpoint_path: Path):
        checkpoint_checks = pf.FileScript(SUITE_DIR / "configs/training/basic_check.sh")
        checkpoint_checks.environment_variable("CHECKPOINT_DIR", str(checkpoint_path))
        super().__init__(name=name, script=checkpoint_checks)


class CreateInferenceFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name="inference", **kwargs)
        config_dir = SUITE_DIR / "configs/inference"

        with self:
            for folder in os.listdir(config_dir):
                config_folder = config_dir / folder
                if not config_folder.is_dir():
                    continue
                try:
                    task_config = load_yaml(config_folder / "task_config.yaml")
                except FileNotFoundError as e:
                    raise FileNotFoundError(
                        f"Inference test requires a task config file: {folder}/task_config.yaml"
                    ) from e

                # Define some variables
                inference_config_path = RESULTS_DIR_INFERENCE / folder / "configs" / "config.yaml"
                output_path = RESULTS_DIR_INFERENCE / folder / "grib"

                # Define a task to generate configuration files for inference
                generate_config = InferenceConfigTask(
                    folder=folder,
                    suite_config=config,
                    checkpoint_path=Path(RESULTS_DIR_TRAINING / folder / "checkpoint"),
                    checkpoint_file=task_config.get("checkpoint_file", "inference-last.ckpt"),
                    config_template_path=STATIC_DATA_DIR / "inference" / folder / "config_template.yaml",
                    output_path=inference_config_path,
                )

                # Define a task to retrieve data for inference
                retrieve_cmd = task_config.get("retrieve_command", "anemoi-inference retrieve")
                overrides = [
                    "--target",
                    "input.grib",
                    "--mars",
                    "--verb",
                    "retrieve",
                    "--date",
                    "20250101T00:00:00",
                    "--input-type",
                    "default-input",
                ]
                retrieve_cmd = " ".join([retrieve_cmd] + overrides)
                retrieve = InferenceRetrieveTask(
                    folder=folder,
                    suite_config=config,
                    config_path=inference_config_path,
                    mars_cmd=task_config.get("mars_command", "mars"),
                    output_path=output_path,
                    retrieve_cmd=retrieve_cmd,
                )

                # Define a task to run inference
                inference_cmd = task_config.get("inference_command", "anemoi-inference run")
                inference = InferenceTask(
                    folder=folder,
                    suite_config=config,
                    config_path=inference_config_path,
                    inference_cmd=inference_cmd,
                    output_path=output_path,
                )

                # Define a task to run inference checks
                check = InferenceCheckTask(
                    folder=folder,
                    suite_config=config,
                    output_path=output_path,
                )

                generate_config >> retrieve >> inference >> check

                # Attach required trainings to the inference task to set triggers in main family
                generate_config.required_trainings = task_config.get("trainings", [])


class InferenceConfigTask(pf.Task):
    def __init__(
        self,
        folder: str,
        suite_config: dict,
        checkpoint_path: Path,
        checkpoint_file: str,
        config_template_path: Path,
        output_path: Path,
    ):
        self.required_trainings: str | None = None
        script = pf.FileScript(SUITE_DIR / "configs/inference" / folder / "generate_config.sh")
        script.environment_variable("CHECKPOINT_DIR", str(checkpoint_path))
        script.environment_variable("CHECKPOINT_FILE", checkpoint_file)
        script.environment_variable("CONFIG_TEMPLATE", str(config_template_path))
        script.environment_variable("OUTPUT_PATH", str(output_path))
        script.environment_variable("RESULTS_DIR_DATASETS", RESULTS_DIR_DATASETS)
        super().__init__(name="generate_config_" + folder, script=script)


class InferenceRetrieveTask(pf.Task):
    def __init__(
        self, folder: str, suite_config: dict, config_path: Path, mars_cmd: str, retrieve_cmd: str, output_path: Path
    ):
        self.required_trainings: str | None = None
        script = pf.FileScript(SUITE_DIR / "configs/inference/" / folder / "retrieve.sh")
        script.environment_variable("CONFIG_PATH", str(config_path))
        script.environment_variable("MARS_CMD", mars_cmd)
        script.environment_variable("RETRIEVE_CMD", retrieve_cmd)
        script.environment_variable("OUTPUT_PATH", str(output_path))
        super().__init__(name="retrieve_" + folder, script=[suite_config.tools.load("inference_env"), script])


class InferenceTask(pf.Task):
    def __init__(self, folder: str, suite_config: dict, config_path: Path, inference_cmd: str, output_path: Path):
        self.required_trainings: str | None = None
        script = pf.FileScript(SUITE_DIR / "configs/inference/inference.sh")
        script.environment_variable("CONFIG_PATH", str(config_path))
        script.environment_variable("INFERENCE_CMD", inference_cmd)
        script.environment_variable("OUTPUT_PATH", str(output_path))
        super().__init__(
            name="inference_" + folder,
            script=[suite_config.tools.load("inference_env"), script],
            submit_arguments="gpu_job",
        )


class InferenceCheckTask(pf.Task):
    def __init__(self, folder: str, suite_config: dict, output_path: Path):
        checks = pf.FileScript(SUITE_DIR / "configs/inference/basic_check.sh")
        checks.environment_variable("OUTPUT_PATH", str(output_path))
        super().__init__(name="check_" + folder, script=checks)


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
            dataset_fam = CreateDatasetFamily(config)
            training_fam = CreateTrainingFamily(config)
            inference_fam = CreateInferenceFamily(config)

            for training_task in [task for task in training_fam.all_tasks if isinstance(task, TrainingTask)]:
                if not training_task.required_datasets:
                    raise ValueError(
                        f"Training task '{training_task.name}' requires datasets, but none are specified in task_config.yaml."
                    )
                for dataset in training_task.required_datasets:
                    dataset_task = dataset.replace("-", "_")
                    if dataset_task not in [task.name for task in dataset_fam.all_tasks]:
                        raise KeyError(
                            f"Dataset '{dataset}' in training task {training_task.name} not found in dataset test cases. Ensure that all datasets match the name of a dataset test case."
                        )
                    dataset_fam.find_node(dataset_task) >> training_task

            for generate_config_task in [
                task for task in inference_fam.all_tasks if isinstance(task, InferenceConfigTask)
            ]:
                if not generate_config_task.required_trainings:
                    raise ValueError(
                        f"Generate config task '{generate_config_task.name}' requires trainings, but none are specified in task_config.yaml."
                    )

                training = generate_config_task.required_trainings
                training_task = training.replace("-", "_")
                if training_task not in [task.name for task in training_fam.all_tasks]:
                    raise KeyError(
                        f"Training '{training}' in inference task {generate_config_task.name} not found in training test cases. Ensure that all trainings match the name of a training test case."
                    )
                training_fam.find_node(training_task) >> generate_config_task

            clean_up = CleanupTask()
            # only run cleanup if all tests pass
            dataset_fam >> clean_up
            training_fam >> clean_up
            inference_fam >> clean_up


class MainSuite(pf.Family):
    def __init__(self, config, **kwargs):
        super().__init__(defstatus=pf.state.suspended, **kwargs)

        with self:
            f_init = InitFamily(config=config, inlimits=self.work)
            f_main = MainFamily(config=config, inlimits=self.work)
            f_init >> f_main
