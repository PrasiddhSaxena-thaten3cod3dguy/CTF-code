#!/usr/bin/env bash
socat tcp-listen:1325,fork,reuseaddr exec:"/home/ctf/chall"
