#!/usr/bin/env python

def print_matches(matchtest):
  print "Looking for", matchtest
  while True:
    line = (yield)
    if matchtest in line:
      print line,

c = print_matches('python')
c.next()
c.send('hello world')
c.send('python is awesome')
c.close()
