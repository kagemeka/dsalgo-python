import typing
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import (
    FenwickTreeIntAdd,
)


class FenwickTreePointAddRangeSum:
    def __init__(self, arr: list[int]) -> None:
        self.__fw = FenwickTreeIntAdd(arr)

    def __setitem__(self, i: int, x: int) -> None:
        self.__fw[i] = x

    def get(self, left: int, right: int) -> int:
        return self.__fw[right] - self.__fw[left]
