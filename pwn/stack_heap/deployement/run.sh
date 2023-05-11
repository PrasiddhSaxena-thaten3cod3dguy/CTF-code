#!/usr/bin/env bash
socat tcp-listen:6194,fork,reuseaddr exec:"/home/ctf/chall"
