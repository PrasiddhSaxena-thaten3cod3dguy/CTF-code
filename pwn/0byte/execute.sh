#!/bin/bash
cd deployement
sudo docker build -t 0byte .
sudo docker run -p 1234:1234 -it 0byte
