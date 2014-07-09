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
`./plotter [-x] [-y] [-z] [-Bx] [-By] [-Bz] path1 [path2] ...`
 * For rotationshield output, the path should be a folder name with
    a trailing slash.
 * For FieldMapping VI output, the path should be the text file.
 * Option flags must precede the list of paths.

