# plotter.py (Aritra Biswas)
# --------------------------
# Generates {Bx, By, Bz} vs {x, y, z} plots from rotationshield output

import numpy as np
import matplotlib.pyplot as plt
import sys

def parse_file(filepath):
    
    f = open(filepath, 'r')

    x = np.array([])
    y = np.array([])
    z = np.array([])
    Bx = np.array([])
    By = np.array([])
    Bz = np.array([])

    for line in f:
        (this_x, this_y, this_z, this_Bx, this_By, this_Bz) = line.split()
        x = np.append(x, this_x)
        y = np.append(y, this_y)
        z = np.append(z, this_z)
        Bx = np.append(Bx, this_Bx)
        By = np.append(By, this_By)
        Bz = np.append(Bz, this_Bz)
    
    f.close()

    return (x, y, z, Bx, By, Bz)

if __name__ == '__main__':

    # handle input flags

    first_arg = 1
    
    no_flags = True
    horiz = 0
    vert = 0

    x_show = False
    y_show = False
    z_show = False
    Bx_show = False
    By_show = False
    Bz_show = False

    for arg in sys.argv:
        if arg == "-x":
            x_show = True
            horiz += 1
            first_arg +=1
        elif arg == "-y":
            y_show = True
            horiz += 1
            first_arg += 1
        elif arg == "-z":
            z_show = True
            horiz += 1
            first_arg += 1
        elif arg == "-Bx":
            Bx_show = True
            vert += 1
            first_arg += 1
        elif arg == "-By":
            By_show = True
            vert += 1
            first_arg += 1
        elif arg == "-Bz":
            Bz_show = True
            vert += 1
            first_arg += 1

    if x_show == False and y_show == False and z_show == False:
        x_show = True
        y_show = True
        z_show = True
    if Bx_show == False and By_show == False and Bz_show == False:
        Bx_show = True
        By_show = True
        Bz_show = True

    if horiz == 0:
        horiz = 3
    if vert == 0:
        vert = 3

    print (horiz, vert)

    fig = plt.figure()

    i = 1
    
    if Bx_show == True and x_show == True:
        Bx_v_x = fig.add_subplot(vert, horiz, i, xlabel = "x", ylabel = "Bx"); i += 1
    if Bx_show == True and y_show == True:
        Bx_v_y = fig.add_subplot(vert, horiz, i, xlabel = "y", ylabel = "Bx"); i += 1
    if Bx_show == True and z_show == True:
        Bx_v_z = fig.add_subplot(vert, horiz, i, xlabel = "z", ylabel = "Bx"); i += 1
    if By_show == True and x_show == True:
        By_v_x = fig.add_subplot(vert, horiz, i, xlabel = "x", ylabel = "By"); i += 1
    if By_show == True and y_show == True:
        By_v_y = fig.add_subplot(vert, horiz, i, xlabel = "y", ylabel = "By"); i += 1
    if By_show == True and z_show == True:
        By_v_z = fig.add_subplot(vert, horiz, i, xlabel = "z", ylabel = "By"); i += 1
    if Bz_show == True and x_show == True:
        Bz_v_x = fig.add_subplot(vert, horiz, i, xlabel = "x", ylabel = "Bz"); i += 1
    if Bz_show == True and y_show == True:
        Bz_v_y = fig.add_subplot(vert, horiz, i, xlabel = "y", ylabel = "Bz"); i += 1
    if Bz_show == True and z_show == True:
        Bz_v_z = fig.add_subplot(vert, horiz, i, xlabel = "z", ylabel = "Bz")

    for i in range(first_arg, len(sys.argv)):
        (x, y, z, Bx, By, Bz) = parse_file(sys.argv[i])
        if Bx_show == True and x_show == True:
            Bx_v_x.plot(x, Bx)
        if Bx_show == True and y_show == True:
            Bx_v_y.plot(y, Bx) 
        if Bx_show == True and z_show == True:
            Bx_v_z.plot(z, Bx)
        if By_show == True and x_show == True:
            By_v_x.plot(x, By)
        if By_show == True and y_show == True:
            By_v_y.plot(y, By)
        if By_show == True and z_show == True:
            By_v_z.plot(z, By)
        if Bz_show == True and x_show == True:
            Bz_v_x.plot(x, Bz)
        if Bz_show == True and y_show == True:
            Bz_v_y.plot(y, Bz)
        if Bz_show == True and z_show == True:
            Bz_v_z.plot(z, Bz)

    plt.show()
