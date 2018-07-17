#!/usr/bin/env python

import math

from bst_vector import BSTVector


class BSTMatrix(object):
  def __init__(self, rows, cols):
    self._rows = rows
    self._cols = cols
    self._row_norms = BSTVector(rows)
    self._row_trees = [BSTVector(cols) for _ in range(rows)]

  def get(self, row, col):
    return self._row_trees[row].get(col)

  def set(self, row, col, value):
    row_tree = self._row_trees[row]
    row_tree.set(col, value)
    self._row_norms.set(row, math.sqrt(row_tree.norm2))

  def get_row_norm(self, row):
    return self._row_norms.get(row)

  @property
  def frob_norm2(self):
    return self._row_norms.norm2

  def sample_row_norms(self):
    return self._row_norms.sample()

  def sample_row(self, row):
    return self._row_trees[row].sample()

  def __str__(self):
    return "\n".join([r.__str__() for r in self._row_trees])


