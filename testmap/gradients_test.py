#!/usr/bin/env python2

# gradients_test.py (Aritra Biswas)
# ---------------------------------
# Mimics RotationShield output to test gradients.py

import random
import numpy as np

def create_B():
    '''Generate random parameters and create a B function.'''

    dBx_dx = random.random()
    dBx_dy = random.random()
    dBx_dz = random.random()

    dBy_dx = random.random()
    dBy_dy = random.random()
    dBy_dz = random.random()

    dBz_dx = random.random()
    dBz_dy = random.random()
    dBz_dz = random.random()

    # print out paraments in gradients.py format
   
    print
    
    print "dBx/dx = %f uG/cm" % dBx_dx
    print "dBy/dx = %f uG/cm" % dBy_dx
    print "dBz/dx = %f uG/cm" % dBz_dx
    
    print "dBx/dy = %f uG/cm" % dBx_dy
    print "dBy/dy = %f uG/cm" % dBy_dy
    print "dBz/dy = %f uG/cm" % dBz_dy
    
    print "dBx/dz = %f uG/cm" % dBx_dz
    print "dBy/dz = %f uG/cm" % dBy_dz
    print "dBz/dz = %f uG/cm" % dBz_dz

    print

    def B(x, y, z):
        '''Return B(x, y, z) = (Bx, By, Bz).'''

        # calculate B components
        Bx = (dBx_dx)*x + (dBx_dy)*y + (dBx_dz)*z
        By = (dBy_dx)*x + (dBy_dy)*y + (dBy_dz)*z
        Bz = (dBz_dx)*x + (dBz_dy)*y + (dBz_dz)*z

        return (Bx, By, Bz)

    return B

def write_to_file(B):
    '''Given a function B(x, y, z), write a RotationShield
    output file.'''

    x_array = np.arange(0.0125, 0.0505, 0.01)
    y_array = np.arange(-0.0250, 0.0250, 0.01)
    z_array = np.arange(-0.1000, 0.1000, 0.01)

    points = len(x_array) * len(y_array) * len(z_array)
    print "[test] Need to write %i points." % points

    f = open('Fieldmap.txt', 'w')

    for x in x_array:
        for y in y_array:
            for z in z_array:
                (Bx, By, Bz) = B(x, y, z)
                f.write("%f\t%f\t%f\t%f\t%f\t%f\n" % (x, y, z, Bx, By, Bz))

if __name__ == '__main__':

    print "[test] Creating random B..."
    B = create_B()

    print "[test] Writing file..."
    write_to_file(B)

    print "[test] Done."
