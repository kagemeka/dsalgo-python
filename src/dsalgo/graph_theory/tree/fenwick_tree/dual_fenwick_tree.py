import typing
from dsalgo.algebra.abstract.structure import Monoid, Group
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import (
    FenwickTree,
)

S = typing.TypeVar("S")


class DualFenwickTree(typing.Generic[S]):
    """DualFenwickTree.

    Examples:
        >>> a = [0, 1, 2, 3, 4]
        >>> g = Group[int](lambda x, y: x + y, lambda: 0, lambda x: -x)
        >>> fw = DualFenwickTree(g, a)
        >>> fw.set(1, 5, 2)
        >>> fw[3]
        5
        >>> fw[0]
        0
    """

    def __init__(self, group: Group[S], arr: typing.List[S]) -> None:
        # given group must be also Abelian Group.
        n = len(arr)
        assert n > 0
        delta = [arr[0]]
        for i in range(n - 1):
            delta.append(group.op(group.invert(arr[i]), arr[i + 1]))
        monoid = Monoid[S](group.op, group.e)
        self.__fw = FenwickTree[S](monoid, delta)
        self.__group = group

    def set(self, left: int, right: int, x: S) -> None:
        n = len(self.__fw)
        assert 0 <= left < right <= n
        self.__fw[left] = x
        if right < n:
            self.__fw[right] = self.__group.invert(x)

    def __getitem__(self, i: int) -> S:
        assert 0 <= i < len(self.__fw)
        return self.__fw[i + 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
