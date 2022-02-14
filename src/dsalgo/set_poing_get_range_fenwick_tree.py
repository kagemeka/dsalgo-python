import typing

from dsalgo.algebra.abstract.abstract_structure import Group
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import (
    FenwickTreeAbelianGroup,
)

S = typing.TypeVar("S")


class FenwickTreePointSetRangeGet(typing.Generic[S]):
    def __init__(self, group: Group[S], arr: typing.List[S]) -> None:
        self.__fw = FenwickTreeAbelianGroup(group, arr)

    def __setitem__(self, i: int, x: S) -> None:
        self.__fw[i] = x

    def get(self, left: int, right: int) -> S:
        return self.__fw.get_range(left, right)
