#!/bin/bash

RUNLIST=$(ls | grep _NG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    sed -i "s/grid 25 25 75/grid 50 5 75/g" exec.sh
    cd ..
done
