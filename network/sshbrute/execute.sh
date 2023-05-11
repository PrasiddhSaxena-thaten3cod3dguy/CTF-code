#!/bin/sh
docker build -t ssh-brute ./
docker run -p 1337:22 -d ssh-brute

echo "Image ssh-brute deployed on port 1337"