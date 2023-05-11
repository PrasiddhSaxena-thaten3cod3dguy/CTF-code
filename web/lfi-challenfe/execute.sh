#!/bin/sh
docker build -t scatterred ./
docker run -p 2420:80 -d scatterred

echo "running on port 2420";