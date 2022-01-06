import sys
import typing

import numba as nb
import numpy as np
from kgmk.dsa.tree.misc.segment.lazy.bottomup.jit import (F, S, seg_build,
                                                          seg_get, seg_set,
                                                          seg_update)


@nb.njit
def seg_op_s(a: S, b: S) -> S:
    return a + b


@nb.njit
def seg_e_s() -> S:
    return np.zeros(2, np.int64)


@nb.njit
def seg_op_f(a: F, b: F) -> F:
    return a + b


@nb.njit
def seg_e_f() -> F:
    return 0


@nb.njit
def seg_map(a: F, b: S) -> S:
    b = b.copy()
    b[0] += a * b[1]
    return b


@nb.njit
def build_seg(
    a: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    return seg_build(seg_op_s, seg_e_s, seg_e_f, a)


@nb.njit
def set_range_seg(
    seg: np.ndarray,
    lazy: np.ndarray,
    l: int,
    r: int,
    f: F,
) -> typing.NoReturn:
    seg_set(
        seg,
        lazy,
        seg_op_s,
        seg_op_f,
        seg_e_f,
        seg_map,
        l,
        r,
        f,
    )


@nb.njit
def get_range_seg(
    seg: np.ndarray,
    lazy: np.ndarray,
    l: int,
    r: int,
) -> S:
    return seg_get(
        seg,
        lazy,
        seg_op_s,
        seg_e_s,
        seg_op_f,
        seg_e_f,
        seg_map,
        l,
        r,
    )


@nb.njit
def update_point_seg(
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
    x: S,
) -> typing.NoReturn:
    seg_update(seg, lazy, seg_op_s, seg_op_f, seg_e_f, seg_map, i, x)


@nb.njit(cache=True)
def solve() -> typing.NoReturn:
    w = 100
    a = np.ones((w, 2), np.int64)
    seg, lazy = build_seg(a)
    set_range_seg(seg, lazy, 0, 20, 10)
    # print(seg)
    # print(lazy)
    v = get_range_seg(seg, lazy, 0, 20)
    # print(v)
    update_point_seg(seg, lazy, 10, np.array([1, 1]))
    v = get_range_seg(seg, lazy, 0, 20)
    print(v)


solve()
