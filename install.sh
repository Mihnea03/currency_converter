#!/bin/bash

echo "Initializing environment..."
python3 -m venv env
source env/bin/activate

echo "Installing required packages..."
python3 -m pip install -U -r requirements.txt

echo "Installation completed succesfully! Type 'python3 main.py' to start the Currency Converter"