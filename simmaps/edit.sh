#!/bin/bash

RUNLIST=$(ls | grep metglas1mm_ | grep _SG)

for FOLDER in $RUNLIST; do
    cd $FOLDER
    sed -i "s/t -1.08 0.367 1.08 0.367 0.005 10000 120 0/t -1.08 0.367 1.08 0.367 0.001 10000 120 0/g" exec.sh
    cd ..
done
