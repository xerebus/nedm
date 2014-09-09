#!/usr/bin/env python2

# gradients.py (Aritra Biswas)
# ---------------------------
# Calculates gradients in B cell.

import sys
import numpy as np
import math
from plotter import *

### GLOBAL

spatial_axes = ["x", "y", "z"]
axis_index = {"x" : 0, "y" : 1, "z" : 2}

tolerance = 0.001
half_cube_side = 0.03
newnorm = 600

### HELPER FUNCTIONS

def avg_grad_in_direction(field, spatial_axis):
    '''Return the volume-averaged d{vector_axis in vector_axes}/d(spatial_axis).'''

    #print "[calc] Will be calculating d{Bx, By, Bz}/d%s." % spatial_axis

    # get axes positions
    axes_positions = restrict_axes_positions(get_unique_axes_positions(field), half_cube_side)
    
    # Bx, By, Bz gradient arrays from each line
    array_dBx_dspat = np.array([])
    array_dBy_dspat = np.array([])
    array_dBz_dspat = np.array([])

    # array of positions in the axis along which we are traveling
    spatial_axis_positions = axes_positions[spatial_axis]

    # the two other axes
    orthogonal_axes = spatial_axes[:] # copy spatial axes
    orthogonal_axes.remove(spatial_axis) # remove spatial axis to leave other two
    orth_axis_1 = orthogonal_axes[0]
    orth_axis_2 = orthogonal_axes[1]
    #print "[calc] Orthogonal axes are %s and %s." % (orth_axis_1, orth_axis_2)

    # positions along the two other axes
    orth_axis_1_positions = axes_positions[orth_axis_1]
    orth_axis_2_positions = axes_positions[orth_axis_2]

    # for each orthogonal position
    for orth_pos_1 in orth_axis_1_positions:
        for orth_pos_2 in orth_axis_2_positions:
            
            # travel along the desired spatial axis
            for i in xrange(len(spatial_axis_positions) - 1):
                
                # figure out current and next position along spatial axis
                spatial_pos = spatial_axis_positions[i]
                spatial_pos_next = spatial_axis_positions[i + 1]
                
                #print "[calc] I am currently at:"
                #print "[calc]  (orthogonal axis 1) %s = %f" % (orth_axis_1, orth_pos_1)
                #print "[calc]  (orthogonal axis 2) %s = %f" % (orth_axis_2, orth_pos_2)
                #print "[calc]  (axis of movement) %s = %f" % (spatial_axis, spatial_pos)
                #print "[calc] I am going to:"
                #print "[calc]  (axis of movement) %s = %f" % (spatial_axis, spatial_pos_next)
                
                # get current (x, y, z)
                position = [None, None, None]
                position[axis_index[spatial_axis]] = spatial_pos
                position[axis_index[orth_axis_1]] = orth_pos_1
                position[axis_index[orth_axis_2]] = orth_pos_2
                position = tuple(position)
                #print "[calc] Confirm - I am at: (%f, %f, %f)" % position
                
                # get next (x, y, z)
                position_next = [None, None, None]
                position_next[axis_index[spatial_axis]] = spatial_pos_next
                position_next[axis_index[orth_axis_1]] = orth_pos_1
                position_next[axis_index[orth_axis_2]] = orth_pos_2
                position_next = tuple(position_next)
                #print "[calc] Confirm - I am going to: (%f, %f, %f)" % position

                # get B at both positions
                (Bx, By, Bz) = lookup_B(field, position)
                #print "[calc] B(%f, %f, %f) = (%f, %f, %f)" % (position + (Bx, By, Bz))
                (Bx_n, By_n, Bz_n) = lookup_B(field, position_next)
                #print "[calc] B(%f, %f, %f) = (%f, %f, %f)" % (position_next + (Bx_n, By_n, Bz_n))

                # calculate differences
                dBx = Bx_n - Bx
                dBy = By_n - By
                dBz = Bz_n - Bz
                dspat = spatial_pos_next - spatial_pos

                # calculate gradients
                array_dBx_dspat = np.append(array_dBx_dspat, (float(dBx) / float(dspat)))
                array_dBy_dspat = np.append(array_dBy_dspat, (float(dBy) / float(dspat)))
                array_dBz_dspat = np.append(array_dBz_dspat, (float(dBz) / float(dspat)))

    # get averages
    dBx_dspat = np.average(array_dBx_dspat)
    dBy_dspat = np.average(array_dBy_dspat)
    dBz_dspat = np.average(array_dBz_dspat)

    return (dBx_dspat, dBy_dspat, dBz_dspat)

def get_unique_axes_positions(field):
    '''Given a field, return [array_of_x_positions, array_of_y_positions,
    array_of_z_positions].'''

    axes_positions = {}

    for spatial_axis in spatial_axes:
        axes_positions[spatial_axis] = np.unique(eval("field." + spatial_axis + ".array"))

    return axes_positions

def restrict_axes_positions(axes_positions, half_cube_side):
    '''Narrow down axes positions to points inside a cube around the center.'''
    
    new_axes_positions = {}

    for axis in axes_positions:
        new_axes_positions[axis] = np.extract(np.abs(axes_positions[axis]) < half_cube_side,
        axes_positions[axis])

    return new_axes_positions

def lookup_B(field, (position)):
    '''Return (Bx, By, Bz) = B(position), where position = (x, y, z).'''

    (x, y, z) = position

    # find indices of correct x, y, z
    x_indices = find_indices(np.abs(field.x.array - x) < tolerance)
    y_indices = find_indices(np.abs(field.y.array - y) < tolerance)
    z_indices = find_indices(np.abs(field.z.array - z) < tolerance)

    # find common index
    point_index = np.intersect1d(np.intersect1d(x_indices, y_indices),
    z_indices)

    assert len(point_index) == 1
    index = point_index[0]

    return (field.Bx[index], field.By[index], field.Bz[index])

### MAIN ROUTINE

if __name__ == "__main__":
    
    # create field object
    field = Field(sys.argv[1])
    assert field.is_simmap

    # normalize field
    field.normalize(newnorm)
    print "[norm] Field normalized to %f mG." % newnorm

    # get gradients
    print "[calc] Calculating d{Bx, By, Bz}/dx..."
    (dBx_dx, dBy_dx, dBz_dx) = avg_grad_in_direction(field, "x")
    print "[calc] Calculating d{Bx, By, Bz}/dy..."
    (dBx_dy, dBy_dy, dBz_dy) = avg_grad_in_direction(field, "y")
    print "[calc] Calculating d{Bx, By, Bz}/dz..."
    (dBx_dz, dBy_dz, dBz_dz) = avg_grad_in_direction(field, "z")

    # output
    print "[calc] Done."
    print

    print "Volume was [%f, %f]^3." % (-half_cube_side, half_cube_side)

    print
    
    print "dBx/dx = %f" % dBx_dx
    print "dBy/dx = %f" % dBy_dx
    print "dBz/dx = %f" % dBz_dx
    
    print "dBx/dy = %f" % dBx_dy
    print "dBy/dy = %f" % dBy_dy
    print "dBz/dy = %f" % dBz_dy
    
    print "dBx/dx = %f" % dBx_dz
    print "dBy/dx = %f" % dBy_dz
    print "dBz/dx = %f" % dBz_dz
