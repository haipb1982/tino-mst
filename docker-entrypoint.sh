#!/usr/bin/env bash

export PYTHONPATH=.

# sudo python3 api.py 6666

export FLASK_APP=test1.py
flask run --host 0.0.0.0 --port 5001

# export FLASK_APP=test2.py
# flask run --host 0.0.0.0 --port 5002