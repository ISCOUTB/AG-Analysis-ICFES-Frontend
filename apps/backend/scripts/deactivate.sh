#!/bin/bash

# Another shorthand to deactivate the env

VENV_DIR="../.venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual Environment does not exists"
    echo "Exiting ..."
    exit 1
fi 

source "$VENV_DIR/Scripts/deactivate"




