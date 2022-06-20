#!/bin/sh

export PYTHONHASHSEED=0
profile_file="$(hostname)_$(date -Iminutes).profile"
pypy -m cProfile -o $profile_file probe.py
mv $profile_file ./benchmark_profiles/
