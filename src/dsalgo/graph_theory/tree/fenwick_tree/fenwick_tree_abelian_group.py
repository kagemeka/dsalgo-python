import typing

from dsalgo.algebra.abstract.structure import Group, Monoid
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import FenwickTree

S = typing.TypeVar("S")


class FenwickTreeAbelianGroup(typing.Generic[S], FenwickTree[S]):
    def __init__(self, group: Group[S], arr: typing.List[S]) -> None:
        monoid = Monoid[S](group.op, group.e)
        super().__init__(monoid, arr)
        self.__group = group

    def get_range(self, left: int, right: int) -> S:
        """Get range product.
        An associative function for FenwickTree.
        Generic Type S must be Abelian Group not only but Monoid.
        so it's needed to pass the inverse function.
        """

        g = self.__group
        return g.op(g.invert(self[left]), self[right])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
