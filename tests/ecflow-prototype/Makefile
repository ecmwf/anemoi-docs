SHELL:=/bin/bash
WELLIES_VERSION = 1.1.0

user:
	module load wellies/$(WELLIES_VERSION); \
	module list; \
	./deploy.py configs/config.yaml configs/execution_contexts.yaml configs/tools.yaml ${ARGS}

default: user
