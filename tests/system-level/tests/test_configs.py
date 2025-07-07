import os

import pyflow as pf
import pytest
import yaml
from anemoi_test.config import Config
from anemoi_test.nodes import Suite

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
profiles_file = os.path.join(ROOT_DIR, "profiles.yaml")
with open(profiles_file, "r") as file:
    configs = yaml.load(file, Loader=yaml.SafeLoader)
# Convert configs dictionary into a list of (name, config) tuples
CONFIGS = list(configs.keys())


class Args:
    def __init__(self, name):
        self.name = name
        self.profiles = profiles_file
        self.set = None


def build_suite(config_name):
    args = Args(config_name)
    config = Config(args)

    # Initialize the Suite object
    suite = Suite(
        config,
        name=config.name,
        host=config.host,
        files=config.ecflow_server.deploy_dir,
        variables=config.suite_variables,
        limits=config.limits,
        labels=config.labels,
    )
    return suite


@pytest.mark.parametrize("config_name", CONFIGS)
def test_deployment(config_name):
    suite = build_suite(config_name)
    suite.deploy_suite(target=pf.Notebook)
    suite.ecflow_definition()
