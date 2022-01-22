import typing

from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree_int_add import (
    FenwickTreeIntAdd,
)


class DualFenwickTreeIntAdd:
    """DualFenwickTreeIntAdd."""

    def __init__(self, arr: typing.List[int]) -> None:
        """Initialize.

        Args:
            arr (typing.List[int]): initial array.
        """
        n = len(arr)
        assert n > 0
        delta = [arr[0]]
        for i in range(n - 1):
            delta.append(arr[i + 1] - arr[i])
        self.__fw = FenwickTreeIntAdd(delta)

    def set(self, left: int, right: int, x: int) -> None:
        """Set range.

        Args:
            left (int): add x on [left, right)
            right (int): add x on [left, right)
            x (int): value to add.
        """
        n = len(self.__fw)
        assert 0 <= left < right <= n
        self.__fw[left] = x
        if right < n:
            self.__fw[right] = -x

    def __getitem__(self, i: int) -> int:
        """Get value.

        Args:
            i (int): index of the given array.

        Returns:
            int: arr[i]
        """
        assert 0 <= i < len(self.__fw)
        return self.__fw[i + 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
