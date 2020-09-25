#!/bin/bash

## install requirements if they exist
if [ -f 'requirements.txt' ]; then
    pip3 install -r requirements.txt
fi

## allow for local (dev) exo_vars
if [ "$EXO_ENVIRONMENT" == "DEVELOPMENT" ]; then
    python3 ./development_setup.py
fi

## simple testing support
if [ "$1" == "test" ]; then
    pip3 install pytest && \
    pytest tests/
## actual execution of the Cartridge for all envs
else
    python3 -c "import main; main.execute()"
fi