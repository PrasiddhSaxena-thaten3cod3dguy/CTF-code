#!/bin/bash
set -m

python app.py &

python dev.py

fg %1