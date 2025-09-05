#!/bin/bash


module load wellies/${WELLIES_VERSION:-1.2.0}
module list

./deploy.py user "$@"
