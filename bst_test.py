#!/usr/bin/env python

import random
import sys

import numpy as np

from bst_vector import BSTVector
from bst_matrix import BSTMatrix

if '--seed' not in sys.argv:
  seed = random.randint(0, 10000)
  random.seed(seed)
else:
  seed = sys.argv[1 + sys.argv.index('--seed')]
  print "Using seed {}".format(seed)
  seed = int(seed)
  random.seed(seed)

v = BSTVector(100)
a = np.zeros((100,))
for _ in range(1000):
  index = random.randint(0, 99)
  value = random.random()
  v.set(index, value)
  a[index] = value
  assert abs(v.norm2 - np.sum(np.square(a))) < 1e-9, \
    "Vector norm squared check failed; seed {}".format(seed)

m = BSTMatrix(200, 100)
b = np.zeros((200, 100))
for _ in range(10000):
  row = random.randint(0, 199)
  col = random.randint(0, 99)
  value = random.random()
  m.set(row, col, value)
  b[row, col] = value
  assert abs(m.frob_norm2 - np.sum(np.square(b))) < 1e-9, \
    "Matrix norm squared check failed; seed {}".format(seed)


print "All checks passed"
