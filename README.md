nedm
====

Personal repository for scripts, etc. written for nEDM project at KRL

`plotter` usage message
-----------------------

    Usage: plotter [options] path1 [path2] ...

    Each path should be either a text file containing Labview VI output
    or a folder containing a Fieldmap.txt created with rotationshield;
    the program will determine which type is being read.

    Options:
      -h, --help          show this help message and exit
      -i, --showx         show x plots
      -j, --showy         show y plots
      -k, --showz         show z plots
      -X, --showBx        show Bx plots
      -Y, --showBy        show By plots
      -Z, --showBz        show Bz plots
      -x SX, --slicex=SX  restrict to points near x = SX
      -y SY, --slicey=SY  restrict to points near y = SY
      -z SZ, --slicez=SZ  restrict to points near z = SZ
      -b BGPATHS          Specify a path to a VI-output text file containing
                          background data. If you use this options, provide either
                          one background file, or one per foreground file.
      --dx=DX             use if measured map is offset by x = DX
      --dy=DY             use if measured map is offset by y = DY
      --dz=DZ             use if measured map is offset by z = DZ
      -n NEWNORM          custom normalization level in mG
      -f, --flip          Flip all plots. Useful to demonstrate anti-symmetry.
