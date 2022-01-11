import typing

from kagemeka.dsa.graph_theory.tree.fenwick_tree import FenwickTree

from .compress_array import compress_array


def count_inversion(a: typing.List[int]) -> int:
    a, _ = compress_array(a)
    n = len(a)
    fw = FenwickTree([0] * n)
    c = 0
    for i in range(n):
        x = a[i]
        c += i - fw[x]
        fw[x] = 1
    return c
