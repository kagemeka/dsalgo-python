from __future__ import annotations

import typing

import dsalgo.fenwick_tree
from dsalgo.type import S


class FenwickTree(typing.Generic[S]):
    def __init__(self, group: Group[S], arr: list[S]) -> None:
        self.__fw = FenwickTreeAbelianGroup(group, arr)

    def __setitem__(self, i: int, x: S) -> None:
        self.__fw[i] = x

    def get(self, left: int, right: int) -> S:
        return self.__fw.get_range(left, right)


from kgmk.dsa.algebra.abstract.structure.monoid import Monoid
from kgmk.dsa.tree.misc.segment.normal.one_indexed.topdown.non_recursive import (
    SegmentTree,
)

# TODO cut below


T = typing.TypeVar("T")


class SegmentTree(typing.Generic[T]):
    def __init__(
        self,
        monoid: Monoid[T],
        a: list[T],
    ) -> NoReturn:
        self.__seg = SegmentTree(monoid, a)
        self.__monoid = monoid

    def set_point(self, i: int, x: T) -> NoReturn:
        self.__seg[i] = x

    def operate_point(self, i: int, x: T) -> NoReturn:
        self.set_point(i, self.__monoid.op(self.get_point(i), x))

    def get_point(self, i: int) -> T:
        return self.__seg[i]

    def get_range(self, l: int, r: int) -> T:
        return self.__seg.get_range(l, r)


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
