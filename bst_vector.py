#!/usr/bin/env python

import random


class _BSTVectorBase(object):
  def set(self, index, value):
    pass

  def get(self, index):
    pass

  def sample(self):
    pass

  @property
  def norm2(self):
    return self._norm2

  def __repr__(self):
    return "<BSTVector of dimension {}: {}>".format(
      self._dim, self.__str__())


class _BSTVectorLeaf(_BSTVectorBase):
  def __init__(self):
    self.value = 0.0
    self._norm2 = 0.0
    self._dim = 1

  def set(self, index, value):
    self.value = float(value)
    self._update_norm2()

  def get(self, index):
    if index != 0:
      raise IndexError
    return self.value

  def sample(self):
    return 0

  def _update_norm2(self):
    self._norm2 = self.value ** 2

  def __str__(self):
    return self.value.__str__()


class _BSTVectorNode(_BSTVectorBase):
  def __init__(self, dim):
    self._dim = dim
    self._norm2 = 0.0
    self.left = None
    self.right = None

  def set(self, index, value):
    if index < self.cutoff:
      child_side = 'left'
      child_size = self.cutoff
      child_index = index
    else:
      child_side = 'right'
      child_size = self._dim - self.cutoff
      child_index = index - self.cutoff

    if self.__getattribute__(child_side) is None:
      self.__setattr__(child_side, BSTVector(child_size))
    child = self.__getattribute__(child_side)
    child.set(child_index, value)
    if child.norm2 == 0.0:
      self.__setattr__(child_side, None)

    self._update_norm2()

  def get(self, index):
    if index >= self._dim:
      raise IndexError

    if index < self.cutoff:
      child_side = 'left'
      child_index = index
    else:
      child_side = 'right'
      child_index = index - self.cutoff

    child = self.__getattribute__(child_side)
    if child is None:
      return 0.0
    return child.get(child_index)

  def sample(self, seed=None):
    if self.norm2 == 0.0:
      raise ValueError, "No nonzero entries"

    left_norm2 = self.left.norm2 if self.left is not None \
                 else 0.0

    if seed is not None:
      random.seed(seed)

    if random.uniform(0, self.norm2) < left_norm2:
      # DON'T re-seed when calling recursively
      # self.left has to be non-None if the inequality is satisfied,
      # because if it were None then the RHS is zero
      return self.left.sample()
    
    # Likewise, don't re-seed.
    # self.right is non-None because norm2 can't be equal to left_norm2
    # if we're in this branch.
    return self.cutoff + self.right.sample()

  def _update_norm2(self):
    self._norm2 = sum(child.norm2
                      for child in [self.left, self.right]
                      if child is not None)

  @property
  def cutoff(self):
    return self._dim // 2

  def __str__(self):
    if self.left is None:
      left_str = "-" * self.cutoff
    else:
      left_str = self.left.__str__()

    if self.right is None:
      right_str = "-" * (self._dim - self.cutoff)
    else:
      right_str = self.right.__str__()

    return "({} {})".format(left_str, right_str)


def BSTVector(dim):
  if dim == 1:
    return _BSTVectorLeaf()
  else:
    return _BSTVectorNode(dim)
