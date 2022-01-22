import typing


class FenwickTreeIntAdd2D:
    def __init__(self, shape: typing.Tuple[int, int]) -> None:
        """Initialize.

        Args:
            shape (typing.Tuple[int, int]): [description]
        """
        n, m = shape
        self.__data = [[0] * (m + 1) for _ in range(n + 1)]

    @property
    def shape(self) -> typing.Tuple[int, int]:
        """Shape of Matrix.

        Returns:
            typing.Tuple[int, int]: (height, width)
        """
        return (len(self.__data) - 1, len(self.__data[0]) - 1)

    def set(self, i: int, j: int, x: int) -> None:
        r"""Set value.

        Args:
            i (int): vertical index
            j (int): horizontal index
            x (int): value to operate

        Summary:
            matrix[i][j] += x

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
                self.__data[i][j] += x
                j += j & -j
            i += i & -i

    def get(self, i: int, j: int) -> int:
        r"""Get.

        Args:
            i (int): max bound in vertical direction.
            j (int): max bound in horizontal direction.

        Returns:
            int: sum of rectangle range [0, i) and [0, j)

        Complexity:
            time: O(\log{n}\log{m})
        """
        n, m = self.shape
        assert 0 <= i <= n and 0 <= j <= m
        j0 = j
        v = 0
        while i > 0:
            j = j0
            while j > 0:
                v += self.__data[i][j]
                j -= j & -j
            i -= i & -i
        return v

    def get_range(self, i0: int, j0: int, i1: int, j1: int) -> int:
        """Get range value.

        Args:
            i0 (int): min bound in vertical direction.
            j0 (int): min bound in horizontal direction.
            i1 (int): max bound in vertical direction.
            j1 (int): max bound in horizontal direction.

        Returns:
            int: sum of rectangle range [i0, i1) and [j0, j1)
        """
        v = self.get(i1, j1)
        v -= self.get(i1, j0)
        v -= self.get(i0, j1)
        v += self.get(i0, j0)
        return v


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
