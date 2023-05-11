#!/bin/bash
cd deployement
sudo docker build -t fastbin .
sudo docker run -p 5421:5421 -it fastbin
