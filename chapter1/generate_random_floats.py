#!/usr/bin/env python
# This script generates a list of random floats and print them to the console.

import sys
import random

num_of_lines = int(sys.argv[1]) if len(sys.argv) > 1 else 10
for i in range(num_of_lines):
  print random.random() * 100
