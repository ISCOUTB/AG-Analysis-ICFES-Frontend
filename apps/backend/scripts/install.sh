#!/bin/bash

# Just shorthand to installing packages

VENV_DIR="../.venv"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual Environment not found"
    echo "Creating ..."

    python -m venv "$VENV_DIR"
fi

# Locate pip executable
PIP_EXE=$(ls "$VENV_DIR/Scripts" | grep pip | head -n 1)

# Check if pip executable is found
if [ -z "$PIP_EXE" ]; then
    echo "PIP_EXE not found ..."
    exit 1
fi

# Activate the virtual environment
source "$VENV_DIR/Scripts/activate"

# Check if a package name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <package_name>"
    exit 1
fi

# Install the package
PACKAGE_NAME="$1"
"$VENV_DIR/Scripts/$PIP_EXE" install "$PACKAGE_NAME"
