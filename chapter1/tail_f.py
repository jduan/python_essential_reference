#!/usr/bin/env python

import time

def tail_f(f):
  f.seek(0, 2)
  while True:
    line = f.readline()
    if not line:
      time.sleep(0.1)
      continue
    yield line

g = tail_f(open("/tmp/tail"))
for line in g:
  print line,
