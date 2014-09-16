#!/bin/bash

RUNLIST=$(ls | grep metglas2cm_ | grep _SG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    echo "*** Starting simulation job: $FOLDER"
    ./exec.sh > progress.out &
    echo "*** Backgrounded."
    cd ..
done
