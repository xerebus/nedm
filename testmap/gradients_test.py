#!/usr/bin/env python2

# gradients_test.py (Aritra Biswas)
# ---------------------------------
# Mimics RotationShield output to test gradients.py

import random
import numpy as np

def create_B():
    '''Generate random parameters and create a B function.'''

    # dx parameters
    xx = random.random()
    yx = random.random()
    zx = random.random()

    # dy parameters
    xy = random.random()
    yy = random.random()
    zy = random.random()

    # dz parameters
    xz = random.random()
    yz = random.random()
    zz = random.random()

    # print out paraments in gradients.py format
   
    print
    
    print "dBx/dx = %f uG/cm" % xx
    print "dBy/dx = %f uG/cm" % yx
    print "dBz/dx = %f uG/cm" % zx
    
    print "dBx/dy = %f uG/cm" % xy
    print "dBy/dy = %f uG/cm" % yy
    print "dBz/dy = %f uG/cm" % zy
    
    print "dBx/dz = %f uG/cm" % xz
    print "dBy/dz = %f uG/cm" % yz
    print "dBz/dz = %f uG/cm" % zz

    print

    def B(x, y, z):
        '''Return B(x, y, z) = (Bx, By, Bz).'''

        # calculate B components
        Bx = xx*x + yx*y + zx*z
        By = xy*x + yy*y + zy*z
        Bz = xz*x + yz*x + zz*z

        return (Bx, By, Bz)

    return B

def write_to_file(B):
    '''Given a function B(x, y, z), write a RotationShield
    output file.'''

    x_array = np.arange(0.0125, 0.0505, 0.001)
    y_array = np.arange(-0.0250, 0.0250, 0.001)
    z_array = np.arange(-0.1000, 0.1000, 0.005)

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
