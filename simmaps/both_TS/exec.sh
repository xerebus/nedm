#!/bin/bash

ROTSHIELD="$HOME/rotationshield/RotationShield"

$ROTSHIELD \
    dir . \
    field \
        c \
            geom 15 0.324 0.810 1 \
            kdist 0.005 \
        x \
    x \
    bound \
        n 128 \
        t -0.405 0.367 0.405 0.367 0.005 10000 120 0 \
        t 0.410 0.076 0.410 0.337 0.03 0 120 0 \
        t -0.410 0.000 -0.410 0.337 0.03 0 120 0 \
    x \
    cell \
        range 0.0125 -0.025 -0.10 0.0505 0.025 0.10 \
        grid 25 25 100 \
        svgrd 1 \
    x \
    solve \
    apply \
    meas \
x
