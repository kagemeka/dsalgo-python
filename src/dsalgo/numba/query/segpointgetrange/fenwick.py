import typing

import numba as nb
import numpy as np
from kagemeka.dsa.jit.graph_theory.tree.fenwick_tree import S

# TODO cut below


# set point add, get range sum
@nb.njit
def fw_op(a: int, b: int) -> int:
    return a + b


@nb.njit
def fw_e() -> int:
    return 0


@nb.njit
def fw_inverse(a: int) -> int:
    return -a


# set point gcd get range gcd
from kgmk.dsa.math.gcd.non_recursive.jit import gcd


@nb.njit
def fw_op(a: int, b: int) -> int:
    return gcd(a, b)


@nb.njit
def fw_e() -> int:
    return 0


# set point lcm, get max lcm
from kgmk.dsa.math.lcm.jit import lcm


@nb.njit
def fw_op(a: int, b: int) -> int:
    return lcm(a, b)


@nb.njit
def fw_e() -> int:
    return 1


# set point max, get range max
@nb.njit
def fw_op(a: int, b: int) -> int:
    return max(a, b)


@nb.njit
def fw_e() -> int:
    return -(1 << 60)


# set point min, get range min
@nb.njit
def fw_op(a: int, b: int) -> int:
    return min(a, b)


@nb.njit
def fw_e() -> int:
    return 1 << 60


# set point xor, get range xor
@nb.njit
def fw_op(a: int, b: int) -> int:
    return a ^ b


@nb.njit
def fw_e() -> int:
    return 0


@nb.njit
def fw_inverse(a: int) -> int:
    return a
