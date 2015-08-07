import numpy as np
import matplotlib.pyplot as plotter
import math

f = open("data.txt", "r")
data = []
for line in f:
    data_row = line.split()
    data.append(data_row)
data = np.array(data)

time = data[:,0]
Bx = data[:,1]

FBx = np.fft.fft(Bx)
FBx_freq = np.fft.fftfreq(time.size, 0.1)
plotter.plot(FBx_freq, FBx.real)
plotter.show()
