#!/bin/bash

ROTSHIELD="$HOME/rotationshield/RotationShield"

$ROTSHIELD \
    dir . \
    field \
        c \
            geom 15 0.324 0.752 1 \
            kdist 0.005 \
        x \
    x \
    bound \
        n 128 \
        t -1.256 0.360 1.256 0.360 0.005 10000 120 0 \
    x \
    cell \
        range -0.060 -0.060 -0.200 0.060 0.060 0.200 \
        grid 24 24 80 \
        svgrd 1 \
    x \
    solve \
    apply \
    meas \
x
