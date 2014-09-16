#!/bin/bash

GRAD_EXEC="../../gradients"
RUNLIST=$(ls | grep _SG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    if [ ! -f gradients.out ]; then
        echo "*** Starting gradients job: $FOLDER"
        $GRAD_EXEC $(pwd) > gradients.out &
        echo "*** Backgrounded."
    fi
    cd ..
done
