#!/bin/bash

pushd "$(dirname "$0")" 
pip install -r requirements.txt
pip install -e .
popd