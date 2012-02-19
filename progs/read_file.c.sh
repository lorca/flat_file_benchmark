#!/bin/sh
gcc -O2 -std=c99 ./progs/read_file.c -o ./progs/read_file && ./progs/read_file "$@"
