#!/bin/bash

export PYTHONDONTWRITEBYTECODE=1
export FLASK_APP=app
export FLASK_DEBUG=1

flask run -h 0.0.0.0 -p 1337