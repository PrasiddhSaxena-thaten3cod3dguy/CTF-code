#!/bin/bash

set -m

export FLASK_APP=Application
flask run -h 0.0.0.0 -p 80 &
  
python flag_fcberdfhvu/app.py
 
fg %1
