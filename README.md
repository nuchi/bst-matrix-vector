# Binary Search Tree matrix and vector classes

This implements the sparse matrix and vector classes mentioned in Ewin Tang's paper [A quantum-inspired classical algorithm for recommendation systems](https://eccc.weizmann.ac.il/report/2018/128/). I learned of that paper from [a blog post](https://www.scottaaronson.com/blog/?p=3880) by Scott Aaronson.

The data structures are not original to Tang; apparently they were used earlier by [Kerenidis and Prakash](https://arxiv.org/abs/1603.08675).

The vector class supports storing `w` sparse entries in an `n`-dimensional space in `O(w log^2 n)` space, reading/writing in `O(log^2 n)` time, computing the norm of the vector in `O(1)` time, and sampling the coordinates of a vector, weighted by the square norm of the entries, in `O(log^2 n)` time.

The matrix class supports similar operations; see Tang's paper for details.
