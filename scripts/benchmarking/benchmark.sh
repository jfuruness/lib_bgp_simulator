#!/bin/sh

tag=${1}
export PYTHONHASHSEED=0
profile_file="$(hostname)_$(date -Iminutes).profile"
pypy -m cProfile -o $profile_file probe.py $tag
mv $profile_file ./profiles/
