import typing

from kgmk.dsa.algebra.abstract.structure.monoid import Monoid
from kgmk.dsa.tree.misc.segment.normal.one_indexed.topdown.non_recursive import \
    SegmentTree

# TODO cut below


T = typing.TypeVar("T")


class SetPointGetRange(typing.Generic[T]):
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
