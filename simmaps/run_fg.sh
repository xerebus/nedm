#!/bin/bash

RUNLIST=$(ls | grep raised_RTS)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    echo "*** Starting simulation job: $FOLDER"
    ./exec.sh
    echo "*** Simulation done."
    cd ..
done
