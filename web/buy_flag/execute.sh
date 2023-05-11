#!/bin/sh
docker build -t buyflag ./
docker run -p 2420:80 -d buyflag

echo "running on port 2420";