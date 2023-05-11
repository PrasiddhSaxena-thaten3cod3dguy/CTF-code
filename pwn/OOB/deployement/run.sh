#!/usr/bin/env bash
socat tcp-listen:3497,fork,reuseaddr exec:"/home/ctf/chall"
