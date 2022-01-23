import typing

from dsalgo.algebra.abstract.structure import Group
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree_abelian_group import (
    build_with_size,
)


class FenwickTreeMultiset:
    """FenwickTreeMultiset."""

    __max_value: int

    def __init__(self, max_value: int) -> None:
        """Initialize.

        Args:
            max_value (int):
                all values added to the set is [0, max_value)
        """
        self.__fw = build_with_size(
            Group[int](
                op=lambda x, y: x + y,
                e=lambda: 0,
                invert=lambda x: -x,
            ),
            max_value,
        )
        self.__max_value = max_value

    @property
    def max_value(self) -> int:
        """Given max value.

        Returns:
            int: max value.
        """
        return self.__max_value

    def __len__(self) -> int:
        """Length.

        Returns:
            int: size of multiset.
        """
        return self.__fw[self.max_value]

    def __contains__(self, x: int) -> bool:
        """Check whether x is contained or not.

        Args:
            x (int): value to check.

        Returns:
            bool: True if contained else False.
        """
        return self.count(x) >= 1

    def count(self, x: int) -> int:
        """Count of value.

        Args:
            x (int):
                value to count.

        Returns:
            int:
                if value is out of range, return 0.
        """
        if x < 0 or self.max_value <= x:
            return 0
        return self.__fw.get_range(x, x + 1)

    def is_empty(self) -> bool:
        """Is Empty.

        Returns:
            bool: True if multiset is empty else False.
        """
        return len(self) == 0

    def __bool__(self) -> bool:
        """Bool.

        Returns:
            bool: True if multiset is not empty else False.
        """
        return not self.is_empty()

    def insert(self, x: int) -> None:
        """Insert.

        Args:
            x (int):
                value to insert.
                0 <= x < max_value.
        """
        assert 0 <= x < self.max_value
        self.__fw[x] = 1

    def remove(self, x: int) -> None:
        """Remove a value.

        Args:
            x (int):
                value to remove.
        Raises:
            KeyError:
                if x is out of range or not contained in multiset,
                raise KeyError.
        """
        if x not in self:
            raise KeyError(x)
        self.__fw[x] = -1

    def remove_all(self, x: int) -> None:
        """Remove all given values.

        Args:
            x (int):
                value to remove.
                0 <= x < max_value.
        """
        assert 0 <= x < self.max_value
        self.__fw[x] = -self.count(x)

    def __getitem__(self, i: int) -> typing.Optional[int]:
        """Indexing. return i-th element.

        Args:
            i (int): i-th (0-indexed).

        Returns:
            typing.Optional[int]:
                if index out of range, return None.
                otherwise return i-th elemnt.
        """
        if not 0 <= i < len(self):
            return None
        return self.__fw.max_right(lambda v: v < i + 1)

    def min(self) -> typing.Optional[int]:
        """Min element.

        Returns:
            typing.Optional[int]:
                if multiset is empty, return None.
        """
        return None if len(self) == 0 else self[0]

    def max(self) -> typing.Optional[int]:
        """Max element.

        Returns:
            typing.Optional[int]:
                if multiset is empty, return None.
        """
        return None if len(self) == 0 else self[len(self) - 1]

    def lower_bound(self, x: int) -> int:
        """Lower bound.

        Args:
            x (int): target value.

        Returns:
            int: lower bound index.
        """
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        """Upper bound.

        Args:
            x (int): target value.

        Returns:
            int: upper bound index.
        """
        return self.__fw[x + 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
