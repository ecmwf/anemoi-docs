#!/bin/bash

# Creates a local virtual environment
# setup() {
#     python3 -m venv .venv --system-site-packages
#     python3 -m pip install .
# }

# Main function to parse arguments
main() {
    case "$1" in
        # setup)
        #     rm -rf .venv
        #     setup
        #     ;;
        tests)
            python3 -m pytest tests/ -v "${@:2}"
            ;;
        *)
            ./deploy.py "$@"
            ;;
    esac
}

module load wellies/${WELLIES_VERSION:-1.1.0}
module list

# # if local environment doesn't exist create it
# if [ ! -d .venv ]; then
#     setup
# fi
# Activate the virtual environment
# source .venv/bin/activate

# Run the main function with arguments
main "$@"
