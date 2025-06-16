#!/usr/bin/env python3
import os

import wellies as wl
from suite.nodes import MainSuite

ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))


class Config:
    # Configuration templates global variables
    global_vars = {
        "ROOT": ROOT_DIR,
        "NAME": os.path.splitext(os.path.basename(__file__))[0],
    }

    def __init__(self, args):

        options = wl.parse_yaml_files(args.config_files, args.set, self.global_vars)

        self.name = options["suite_name"]

        self.user = options["user"]

        self.hostname = options["hostname"]
        self.host = wl.get_host(self.hostname, self.user)

        self.deploy_dir = options["deploy_dir"]
        self.deploy_hostname = options.get("deploy_hostname", "localhost")
        self.backup_deploy = options.get("backup_deploy", None)

        self.output_root = options["output_root"]
        self.lib_dir = os.path.join(self.output_root, "local")
        self.data_dir = os.path.join(self.output_root, "data")

        self.job_out = options["job_out"]
        self.workdir = options.get("workdir", "$TMPDIR")

        # other configs parsing and suite variables
        exec_contexts = options.get("execution_contexts", {})
        self.exec_contexts, self.exec_contexts_vars = wl.parse_execution_contexts(exec_contexts)

        self.suite_variables = {
            "SUITE": self.name,
            "OUTPUT_ROOT": self.output_root,
            "LIB_DIR": self.lib_dir,
            "DATA_DIR": self.data_dir,
            **self.exec_contexts_vars,
        }

        tools = options.get("tools", {})
        self.tools = wl.ToolStore("$LIB_DIR", tools)

        static_data = options.get("static_data", {})
        self.static_data = wl.StaticDataStore("$DATA_DIR", static_data)


if __name__ == "__main__":

    # create parser and parse arguments
    parser = wl.get_parser()
    args = parser.parse_args()

    # create config object and suite
    config = Config(args)
    suite = MainSuite(
        config,
        name=config.name,
        host=config.host,
        files=config.deploy_dir,
        variables=config.suite_variables,
        out=config.job_out,
        workdir=config.workdir,
    )

    # deploy suite scripts and definition file
    wl.deploy_suite(
        suite,
        user=config.user,
        name=config.name,
        hostname=config.deploy_hostname,
        deploy_dir=config.deploy_dir,
        backup_deploy=config.backup_deploy,
        build_dir=args.build_dir,
        no_prompt=args.y,
        no_deploy=args.no_deploy,
        message=args.message,
    )
