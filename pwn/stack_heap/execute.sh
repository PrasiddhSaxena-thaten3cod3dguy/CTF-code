#!/bin/bash
cd deployement
sudo docker build -t stack_heap .
sudo docker run -p 6194:6194 -it stack_heap
