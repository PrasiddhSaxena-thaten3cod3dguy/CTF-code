#!/bin/bash
cd deployement
sudo docker build -t oob .
sudo docker run -p 3497:3497 -it oob
