#!/bin/sh
docker build -t xss-filter-challenge ./
docker run -p 2408:80 -d xss-filter-challenge

echo "running on port 2408";