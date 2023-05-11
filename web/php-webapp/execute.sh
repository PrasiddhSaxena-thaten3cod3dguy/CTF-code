#!/bin/sh
docker build -t php-cookie-brute ./
docker run -p 3000:80 -d php-cookie-brute

echo "running on port 3000";