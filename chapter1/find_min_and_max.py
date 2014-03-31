#!/usr/bin/env python
# This script generates a list of random floats and print them to the console.

with open('floats.txt') as fd:
  lines = fd.readlines()

floats = [float(line) for line in lines]

print "max is %s" % max(floats)
print "min is %s" % min(floats)
