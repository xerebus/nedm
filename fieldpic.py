#!/usr/bin/env python2

# fieldpic.py (Aritra Biswas)
# ---------------------------
# Generates pictures with field lines from rotationshield output

import turtle as tt
import sys

from plotter import OffsetAxis, Field

from scipy.interpolate import LinearNDInterpolator
import numpy as np

### CLASSES

### HELPER FUNCTIONS

def interpolate(field):
    '''Given a Field object, do multivariate cubic interpolation and output
    a function B(x, y, z) = (Bx, By, Bz).'''

    # check that the field is a simulated one - no support for measured fields yet
    assert field.is_simmap
    # check that there is no axis offset (there shouldn't be in simulated maps)
    assert field.x.V == field.y.V == field.z.V == (0, 0, 0)
    # check position array lengths
    assert len(field.x.array) == len(field.y.array) == len(field.z.array)

    # construct 2D array of known points
    points = np.array([field.x.array, field.y.array, field.z.array]).T
    
    # construct 2D array of known values
    values = np.array([field.Bx, field.By, field.Bz]).T

    return LinearNDInterpolator(points, values)

def draw():

    # hide turtle and drawing process
    tt.hideturtle() 
    tt.tracer(0)

    tt.forward(50)

    for i in range(100):
        tt.left(1)
        tt.forward(1)
        i += 1

    tt.done()

### MAIN ROUTINE

if __name__ == "__main__":

    pass
