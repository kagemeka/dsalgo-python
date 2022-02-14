import typing

from dsalgo.algebra.abstract.abstract_structure import Group, Monoid
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import FenwickTree

S = typing.TypeVar("S")


class FenwickTreeAbelianGroup(FenwickTree[S]):
    """FenwickTreeAbelianGroup."""

    def __init__(self, group: Group[S], arr: typing.List[S]) -> None:
        """Initialize.

        Args:
            group (Group[S]): Abelian Group.
            arr (typing.List[S]): original array.
        """
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


def build_with_size(group: Group[S], size: int) -> FenwickTreeAbelianGroup[S]:
    """Build a new FenwickTreeAbelianGroup of given size.

    Args:
        group (Group[S]): Abelian Group.
        size (int): the size of original array.

    Returns:
        FenwickTreeAbelianGroup[S]:
            The original array is filled with the value group.e().
    """
    return FenwickTreeAbelianGroup[S](
        group,
        [group.e() for _ in range(size)],
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
