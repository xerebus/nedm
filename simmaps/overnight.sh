#!/bin/bash

RUNLIST=$(ls | grep _SG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    ./exec.sh
    cd ..
done
