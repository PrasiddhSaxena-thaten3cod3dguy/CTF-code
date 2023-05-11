#!/bin/bash

export PYTHONDONTWRITEBYTECODE=1
export FLASK_APP=app

flask run -h 0.0.0.0 -p 80