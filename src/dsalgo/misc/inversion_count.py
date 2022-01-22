import typing

from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import (
    FenwickTreeIntAdd,
)
from dsalgo.misc.compress_array import compress_array


def count_inversion(arr: typing.List[int]) -> int:
    arr, _ = compress_array(arr)
    n = len(arr)
    fw = FenwickTreeIntAdd([0] * n)
    c = 0
    for i, x in enumerate(arr):
        c += i - fw[x]
        fw[x] = 1
    return c
