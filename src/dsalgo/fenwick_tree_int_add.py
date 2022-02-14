import typing


class FenwickTreeIntAdd:
    """FenwickTreeIntAdd.

    Complexity:
        space: O(N)
        where:
            N: length of original array.
    """

    def __init__(self, arr: typing.List[int]) -> None:
        """Initialize.

        Args:
            arr (typing.List[int]): original array.

        Complexity:
            time: O(N)
        """
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] += data[i]
        self.__data = data

    def __len__(self) -> int:
        """Length.

        Returns:
            int: length of original array.

        Complexity:
            time: O(1)
        """
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        r"""Set.

        Args:
            i (int): index to add.
            x (int): value to add.

        Complexity:
            time: O(\log{N})
        """
        assert 0 <= i < len(self.__data) - 1
        i += 1
        while i < len(self.__data):
            self.__data[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        r"""Get.

        Args:
            i (int): upper bound of sum [0, i)

        Returns:
            int: sum [0, i)

        Complexity:
            time: O(\log{N})
        """
        assert 0 <= i < len(self.__data)
        v = 0
        while i > 0:
            v += self.__data[i]
            i -= i & -i
        return v


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
