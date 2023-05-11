#!/usr/bin/env bash
socat tcp-listen:9856,fork,reuseaddr exec:"/home/ctf/chall"
