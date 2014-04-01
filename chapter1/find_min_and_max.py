#!/usr/bin/env python
# This script generates a list of random floats and print them to the console.

floats = [float(line) for line in open('floats.txt')]

print "max is %s" % max(floats)
print "min is %s" % min(floats)
