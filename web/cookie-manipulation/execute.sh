#!/bin/sh
docker build -t php-cookie-manipulation ./
docker run -p 5000:80 -d php-cookie-manipulation

echo "running on port 5000";