#!/bin/bash

RUNLIST=$(ls | grep _NG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    sed -i "s/range 0.0125 -0.025 -0.10 0.0505 0.025 0.10/range -0.12 -0.12 0.0 0.12 0.12 1.5/g" exec.sh
    cd ..
done
