nedm
====

Personal repository for scripts, etc. written for nEDM project at KRL

RotationShield
--------------

This repository contains copyrighted software. The original source and
license for RotationShield can be found at <https://github.com/mpmendenhall/rotationshield>.

In order for `plotter` to work properly, there must be a symlink called `rotationshield` in
the root directory of this repository that leads to the RotationShield project source. This
symlink, of course, is not handled by git since RotationShield is maintained on its own.

`plotter` usage message
-----------------------

    Usage: %s [options] path1 [path2] ...
    The path should be either a text file containing Labview VI output
    or a folder containing a Fieldmap.txt created with rotationshield.
    The program will automatically determine which type is being read.


    Options:
      -h, --help  show this help message and exit
      -x          Show x plots
      -y          Show y plots
      -z          Show z plots
      --Bx        Show Bx plots
      --By        Show By plots
      --Bz        Show Bz plots
      -b BGPATH   Specify a path to a VI-output text file containing background
                  data. This data will be subtracted from all other VI-output
                  data.
      -n NEWNORM  Custom normalization level in mG.
