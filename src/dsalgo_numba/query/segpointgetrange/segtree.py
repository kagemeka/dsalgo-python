from kagemeka.dsa.jit.graph_theory.tree.segment_tree import S
import typing
import numpy as np
import numba as nb


# set point update, get range minimum
@nb.njit
def seg_op(a: S, b: S) -> S: return min(a, b)


@nb.njit
def seg_e() -> S: return 1 << 60


# set point update, get range xor
@nb.njit
def seg_op(a: S, b: S) -> S: return a ^ b

@nb.njit
def seg_e() -> S: return 0
