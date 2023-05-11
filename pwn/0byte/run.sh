#!/usr/bin/env bash
socat tcp-listen:1234,fork,reuseaddr exec:"/home/ctf/chall"
