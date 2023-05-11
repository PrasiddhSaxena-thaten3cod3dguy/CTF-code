#!/bin/bash
cd deployement
sudo docker build -t no_leak .
sudo docker run -p 9856:9856 -it no_leak
