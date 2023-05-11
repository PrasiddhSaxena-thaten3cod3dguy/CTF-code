#!/usr/bin/env bash
socat tcp-listen:1937,fork,reuseaddr exec:"/home/ctf/chall"
