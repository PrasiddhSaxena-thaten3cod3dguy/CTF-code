#!/bin/sh
docker build -t analysis ./
docker run -p 2420:80 -d analysis

echo "running on port 2420";