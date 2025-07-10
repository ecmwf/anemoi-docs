import os

import wellies as wl

ROOT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))


class Config:
    # Configuration templates global variables
    global_vars = {
        "ROOT": ROOT_DIR,
        "NAME": os.path.splitext(os.path.basename(__file__))[0],
    }

    def __init__(self, args):

        # Parse the configuration files
        options = wl.parse_profiles(
            args.profiles,
            config_name=args.name,
            set_variables=args.set,
        )

        # put everything from the yaml into class variables
        self.__dict__.update(options)

        # Ecflow server options
        self.ecflow_server = wl.EcflowServer(**options["ecflow_server"])

        # HPC server options
        self.host, submit_variables = wl.get_host(**options["host"])

        # Optional suite deployment
        self.backup_deploy = options.get("backup_deploy", None)

        # Tools
        tools = options.get("tools", {})
        self.tools = wl.ToolStore("$LIB_DIR", tools)

        # Static data
        static_data = options.get("static_data", {})
        self.static_data = wl.StaticDataStore("$DATA_DIR", static_data)

        # Suite variables
        self.suite_variables = {
            "SUITE": self.name,
            **options.get("ecflow_variables", {}),
            **submit_variables,
        }
