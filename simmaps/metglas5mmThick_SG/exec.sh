#!/bin/bash

ROTSHIELD="$HOME/rotationshield/RotationShield"

$ROTSHIELD \
    dir . \
    field \
        c \
            geom 15 0.324 2.146 1 \
            kdist 0.005 \
        x \
    x \
    bound \
        n 128 \
        t -1.08 0.367 1.08 0.367 0.005 10000 120 0 \
    x \
    cell \
        range 0.0125 -0.025 -0.10 0.0505 0.025 0.10 \
        grid 50 50 200 \
        svgrd 1 \
    x \
    solve \
    apply \
    meas \
x
