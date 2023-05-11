#!/bin/bash
cd deployement
sudo docker build -t l34k .
sudo docker run -p 1325:1325 -it l34k
