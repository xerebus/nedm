#!/bin/bash

RUNLIST=$(ls | grep _TS)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    echo "*** Starting simulation job: $FOLDER"
    ./exec.sh > progress.out &
    echo "*** Backgrounded."
    cd ..
done
