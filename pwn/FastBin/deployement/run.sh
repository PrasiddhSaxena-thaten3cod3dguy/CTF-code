#!/usr/bin/env bash
socat tcp-listen:5421,fork,reuseaddr exec:"/home/ctf/chall"
