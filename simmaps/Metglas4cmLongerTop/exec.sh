#!/bin/bash

ROTSHIELD="$HOME/rotationshield/RotationShield"

$ROTSHIELD dir . field c geom 15 0.324 2.146 1 kdist 0.005 x x bound n 128 t -1.08 0.392 1.12 0.392 0.03 10000 120 0 x cell range -0.12 -0.12 0.0 0.12 0.12 1.5 grid 25 25 75 svgrd 1 x solve apply meas x
