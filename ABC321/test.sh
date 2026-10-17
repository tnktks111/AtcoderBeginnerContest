#!/bin/bash
DIR='/Users/tsukasa-tanaka/projects/ABC/ABC321'
i=0
while true; do
    i=$((i+1))
    python3 "$DIR/gen.py" > input.txt

    python3 "$DIR/E.py" < input.txt > out1.txt 2> err.txt
    status=$?
    if [ $status -ne 0 ]; then
        echo "Runtime Error (exit code $status) at case $i"
        echo "--- input ---"
        cat input.txt
        echo "--- stderr ---"
        cat err.txt
        exit 1
    fi
done