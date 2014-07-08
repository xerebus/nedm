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

    fig = plt.figure()

    for i in range(1, len(sys.argv)):
        (x, y, z, Bx, By, Bz) = parse_file(sys.argv[i])
        Bx_v_x = fig.add_subplot(3, 3, 1)
        Bx_v_y = fig.add_subplot(3, 3, 2)
        Bx_v_z = fig.add_subplot(3, 3, 3)
        By_v_x = fig.add_subplot(3, 3, 4)
        By_v_y = fig.add_subplot(3, 3, 5)
        By_v_z = fig.add_subplot(3, 3, 6)
        Bz_v_x = fig.add_subplot(3, 3, 7)
        Bz_v_y = fig.add_subplot(3, 3, 8)
        Bz_v_z = fig.add_subplot(3, 3, 9)
        Bx_v_x.plot(x, Bx)
        Bx_v_y.plot(y, Bx)
        Bx_v_z.plot(z, Bx)
        By_v_x.plot(x, By)
        By_v_y.plot(y, By)
        By_v_z.plot(z, By)
        Bz_v_x.plot(x, Bz)
        Bz_v_y.plot(y, Bz)
        Bz_v_z.plot(z, Bz)

    plt.show()
