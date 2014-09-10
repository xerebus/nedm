#!/usr/bin/env python2

# gradients.py (Aritra Biswas)
# ---------------------------
# Calculates gradients in B cell.

import sys
import numpy as np
import math
from plotter import *

### GLOBAL

# cell dimensions
llb = (0.0125, -0.025, -0.10) # lower left back (x, y, z)
urf = (0.0505, 0.025, 0.10) # upper right front (x, y, z)

# preferences that shouldn't need to be changed
tolerance = 0.001 # maximum tolerated position error
newnorm = 600 # desired Bx at center

# for convenience
spatial_axes = ["x", "y", "z"]
axis_index = {"x" : 0, "y" : 1, "z" : 2}

### HELPER FUNCTIONS

def avg_grad_in_direction(field, spatial_axis, axes_positions):
    '''Return the volume-averaged
    d{vector_axis in vector_axes}/d(spatial_axis).'''


    print "[calc] Will be calculating d{Bx, By, Bz}/d%s." % spatial_axis
    
    # arrays to store each component of the gradient
    array_dBx_dspat = np.array([])
    array_dBy_dspat = np.array([])
    array_dBz_dspat = np.array([])

    # array of positions in the axis along which we are traveling
    spatial_axis_positions = axes_positions[spatial_axis]

    # the two other axes
    orthogonal_axes = spatial_axes[:] # copy spatial axes
    orthogonal_axes.remove(spatial_axis) # leave other two axes
    orth_axis_1 = orthogonal_axes[0]
    orth_axis_2 = orthogonal_axes[1]
    print "[calc] Orthogonal axes are %s and %s." % (orth_axis_1, orth_axis_2)

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
                
                print "[calc] I am currently at:"
                print "[calc]  (orthogonal axis 1) %s = %f" % (orth_axis_1, orth_pos_1)
                print "[calc]  (orthogonal axis 2) %s = %f" % (orth_axis_2, orth_pos_2)
                print "[calc]  (axis of movement) %s = %f" % (spatial_axis, spatial_pos)
                print "[calc] I am going to:"
                print "[calc]  (axis of movement) %s = %f" % (spatial_axis, spatial_pos_next)
                
                # get current (x, y, z)
                position = [None, None, None]
                position[axis_index[spatial_axis]] = spatial_pos
                position[axis_index[orth_axis_1]] = orth_pos_1
                position[axis_index[orth_axis_2]] = orth_pos_2
                position = tuple(position)
                print "[calc] Confirm - I am at: (%f, %f, %f)" % position
                
                # get next (x, y, z)
                position_next = [None, None, None]
                position_next[axis_index[spatial_axis]] = spatial_pos_next
                position_next[axis_index[orth_axis_1]] = orth_pos_1
                position_next[axis_index[orth_axis_2]] = orth_pos_2
                position_next = tuple(position_next)
                print "[calc] Confirm - I am going to: (%f, %f, %f)" % position

                # get B at both positions
                (Bx, By, Bz) = lookup_B(field, position)
                print "[calc] B(%f, %f, %f) = (%f, %f, %f)" % (position + (Bx, By, Bz))
                (Bx_n, By_n, Bz_n) = lookup_B(field, position_next)
                print "[calc] B(%f, %f, %f) = (%f, %f, %f)" % (position_next + (Bx_n, By_n, Bz_n))

                # calculate differences
                dBx = Bx_n - Bx
                dBy = By_n - By
                dBz = Bz_n - Bz
                dspat = spatial_pos_next - spatial_pos

                # calculate gradients and add to storage arrays
                array_dBx_dspat = np.append(array_dBx_dspat,
                (np.float64(dBx) / np.float64(dspat)))
                array_dBy_dspat = np.append(array_dBy_dspat,
                (np.float64(dBy) / np.float64(dspat)))
                array_dBz_dspat = np.append(array_dBz_dspat,
                (np.float64(dBz) / np.float64(dspat)))

    # get averages from storage arrays
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

def restrict_axes_positions(axes_positions, llb, urf):
    '''Narrow down axes positions to a cell bounded by corners llb
    (lower left back) and urf (upper right front).'''
    
    new_axes_positions = {}

    # unpack tuples to get lower & upper bound for each axis
    (lx, ly, lz) = llb
    (ux, uy, uz) = urf

    # conditions for whether a point is inside the cell or not
    x_cond = np.logical_and(axes_positions["x"] >= lx, axes_positions["x"] <= ux)
    y_cond = np.logical_and(axes_positions["y"] >= ly, axes_positions["y"] <= uy)
    z_cond = np.logical_and(axes_positions["z"] >= lz, axes_positions["z"] <= uz)

    # crop arrays
    new_axes_positions["x"] = np.extract(x_cond, axes_positions["x"])
    new_axes_positions["y"] = np.extract(y_cond, axes_positions["y"])
    new_axes_positions["z"] = np.extract(z_cond, axes_positions["z"])

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

    # get axes positions
    axes_positions = get_unique_axes_positions(field)
    axes_positions = restrict_axes_positions(axes_positions, llb, urf)

    # get gradients
    print "[calc] Calculating d{Bx, By, Bz}/dx..."
    (dBx_dx, dBy_dx, dBz_dx) = avg_grad_in_direction(field, "x", axes_positions)
    print "[calc] Calculating d{Bx, By, Bz}/dy..."
    (dBx_dy, dBy_dy, dBz_dy) = avg_grad_in_direction(field, "y", axes_positions)
    print "[calc] Calculating d{Bx, By, Bz}/dz..."
    (dBx_dz, dBy_dz, dBz_dz) = avg_grad_in_direction(field, "z", axes_positions)

    print "[calc] Done."
    print

    # summary output
    print "dBx/dx = %f mG/m" % dBx_dx
    print "dBy/dx = %f mG/m" % dBy_dx
    print "dBz/dx = %f mG/m" % dBz_dx
    
    print "dBx/dy = %f mG/m" % dBx_dy
    print "dBy/dy = %f mG/m" % dBy_dy
    print "dBz/dy = %f mG/m" % dBz_dy
    
    print "dBx/dx = %f mG/m" % dBx_dz
    print "dBy/dx = %f mG/m" % dBy_dz
    print "dBz/dx = %f mG/m" % dBz_dz
