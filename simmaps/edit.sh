#!/bin/bash

RUNLIST=$(ls | grep metglas5mm_ | grep _SG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    sed -i "s/grid 50 50 200/grid 25 25 100/g" exec.sh
    cd ..
done
