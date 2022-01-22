import typing

from dsalgo.algebra.abstract.structure import Monoid

S = typing.TypeVar("S")


class FenwickTree2D(typing.Generic[S]):
    """FenwickTree2D."""

    def __init__(
        self,
        monoid: Monoid[S],
        shape: typing.Tuple[int, int],
    ) -> None:
        """Initialize.

        Args:
            shape (typing.Tuple[int, int]): [description]
        """
        self.__monoid = monoid
        n, m = shape
        self.__data = [
            [monoid.e() for _ in range(m + 1)] for _ in range(n + 1)
        ]

    @property
    def shape(self) -> typing.Tuple[int, int]:
        """Shape of Matrix.

        Returns:
            typing.Tuple[int, int]: (height, width)
        """
        return (len(self.__data) - 1, len(self.__data[0]) - 1)

    def set(self, i: int, j: int, x: S) -> None:
        r"""Set value.

        Args:
            i (int): vertical index
            j (int): horizontal index
            x (int): value to operate

        Summary:
            matrix[i][j] = monoid.op(matrix[i][j], x)

        Complexity:
            time: O(\log{n}\log{m})
        """
        n, m = self.shape
        assert 0 <= i < n and 0 <= j < m
        i += 1
        j0 = j + 1
        while i <= n:
            j = j0
            while j <= m:
                self.__data[i][j] = self.__monoid.op(self.__data[i][j], x)
                j += j & -j
            i += i & -i

    def get(self, i: int, j: int) -> S:
        r"""Get.

        Args:
            i (int): max bound in vertical direction.
            j (int): max bound in horizontal direction.

        Returns:
            int: product of rectangle range [0, i) and [0, j)

        Complexity:
            time: O(\log{n}\log{m})
        """
        n, m = self.shape
        assert 0 <= i <= n and 0 <= j <= m
        j0 = j
        v = self.__monoid.e()
        while i > 0:
            j = j0
            while j > 0:
                v = self.__monoid.op(v, self.__data[i][j])
                j -= j & -j
            i -= i & -i
        return v


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
