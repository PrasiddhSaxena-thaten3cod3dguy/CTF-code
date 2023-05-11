#!/bin/sh
docker build -t inaccessible ./
docker run -p 2420:80 -d inaccessible

echo "running on port 2420";