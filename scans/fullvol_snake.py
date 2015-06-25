#!/usr/bin/python2

xmin = -60
xmax = 60
ymin = -60
ymax = 60
zmin = -200
zmax = 200

xstep = 10
ystep = 10
zstep = 20

speed = 30

if __name__ == "__main__":

    d = 1 # direction: 1 for up, -1 for down

    for x in range(xmin, xmax, xstep):
        for y in range(ymin, ymax, ystep):
            for z in range(zmin, zmax, zstep)[::d]:
                print "%i\t%i\t%i\t%i" % (x, y, z, speed)
            d *= -1

    print "%i\t%i\t%i\t%i" % (0, 0, 0, 30)
