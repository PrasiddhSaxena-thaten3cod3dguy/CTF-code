#!/bin/sh
docker build -t crack ./
docker run -p 2420:80 -d crack

echo "running on port 2420";