#!/bin/bash

RUNLIST=$(ls | grep neither_TS)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    echo "*** Starting simulation job: $FOLDER"
    ./exec.sh
    echo "*** Simulation done."
    cd ..
done
