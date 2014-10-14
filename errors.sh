#!/bin/bash

RUNLIST=$(ls measmaps | grep .txt)

echo $RUNLIST

for FILE in $RUNLIST; do
    ./error_bars "measmaps/$FILE"
done
