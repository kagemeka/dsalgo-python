import typing

from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree_int_add import (
    FenwickTreeIntAdd,
)
from dsalgo.descrete.compress_array import compress_array


def compute_inversion_number(arr: typing.List[int]) -> int:
    arr, _ = compress_array(arr)
    fw = FenwickTreeIntAdd([0] * len(arr))
    count = 0
    for i, x in enumerate(arr):
        count += i - fw[x]
        fw[x] = 1
    return count
