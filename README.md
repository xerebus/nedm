nedm
====

Personal repository for scripts, etc. written for nEDM project at KRL

`plotter` usage message
-----------------------

    Usage: plotter [options] path1 [path2] ...

    The path should be either a text file containing Labview VI output
    or a folder containing a Fieldmap.txt created with rotationshield.
    The program will automatically determine which type is being read.


    Options:
      -h, --help            show this help message and exit
      -i, --showx           Show x plots
      -j, --showy           Show y plots
      -k, --showz           Show z plots
      -X, --showBx          Show Bx plots
      -Y, --showBy          Show By plots
      -Z, --showBz          Show Bz plots
      -b BGPATH, --background=BGPATH
                            Specify a path to a VI-output text file containing
                            background  data. This data will be subtracted from
                            all other VI-output data.
      -n NEWNORM, --normal=NEWNORM
                            Custom normalization level in mG.
      -x SX, --slicex=SX    Restrict to points near x = SX.
      -y SY, --slicey=SY    Restrict to points near y = SY.
      -z SZ, --slicez=SZ    Restrict to points near z = SZ.
