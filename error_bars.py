#!/usr/bin/env python2

# error_bars.py (Aritra Biswas)
# -----------------------------
# Prints maximum error for a map.

from plotter import *
import numpy as np
import sys

assert len(sys.argv) == 2, "Can only take one argument"

# create field object from path
field = Field(sys.argv[1])

# print errors
print "[errs] Errors: (%s, %s, %s)" % field.get_max_errors()
