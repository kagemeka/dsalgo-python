import typing

from dsalgo.descrete.compress_array import compress_array
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree_int_add import (
    FenwickTreeIntAdd,
)


def compute_inversion_number(arr: typing.List[int]) -> int:
    r"""Inversion Number of array.

    Args:
        arr (typing.List[int]): integer array.

    Returns:
        int: inversion number.

    Complexity:
        time: O(N\log{N})
        space: O(N)
        where:
            N: size of arr.
    """
    arr, _ = compress_array(arr)
    fw = FenwickTreeIntAdd([0] * len(arr))
    count = 0
    for i, x in enumerate(arr):
        count += i - fw[x]
        fw[x] = 1
    return count
