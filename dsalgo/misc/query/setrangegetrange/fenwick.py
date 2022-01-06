# TODO cut below
import typing

from kgmk.dsa.tree.misc.fenwick.one_indexed.add import FenwickTree


class RangeAddRangeSum:
    def __init__(
        self,
        n: int,
    ) -> NoReturn:
        self.__fw0 = FenwickTree(n)
        self.__fw1 = FenwickTree(n)

    def __setitem__(
        self,
        lr: tuple[int, int],
        x: int,
    ) -> NoReturn:
        l, r = lr
        self.__fw0[l] = -x * (l - 1)
        self.__fw0[r + 1] = x * r
        self.__fw1[l] = x
        self.__fw1[r + 1] = -x

    def __getitem__(
        self,
        i: int,
    ) -> int:
        return self.__fw0[i] + self.__fw1[i] * i

    def get_range(
        self,
        l: int,
        r: int,
    ) -> int:
        return -self[l - 1] + self[r]
