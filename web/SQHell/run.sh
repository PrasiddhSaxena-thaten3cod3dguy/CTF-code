#!/bin/bash

export PYTHONDONTWRITEBYTECODE=1
export FLASK_APP=Application
#export FLASK_DEBUG=1

flask run -h 0.0.0.0 -p 80