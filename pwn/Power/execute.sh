#!/bin/bash
cd deployement
sudo docker build -t power .
sudo docker run -p 1937:1937 -it power
