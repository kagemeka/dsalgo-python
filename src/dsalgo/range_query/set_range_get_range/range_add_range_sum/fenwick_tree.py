import typing

from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import (
    FenwickTreeIntAdd,
)


class FenwickTreeRangeAddRangeSum:
    """FenwickTreeRangeAddRangeSum.

    Examples:
        >>> a = [0, 1, 2, 3, 4]
        >>> fw = FenwickTreeRangeAddRangeSum(a)
        >>> fw.set(0, 3, 2)
        >>> fw.get(2, 5)
        11

    References:
    - https://penguinshunya.hatenablog.com/entry/2020/02/13/092208
    - http://hos.ac/slides/20140319_bit.pdf
    - https://algo-logic.info/binary-indexed-tree/
    - https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree


    Summary:
    let s(i) := sum of range [0, i)
    let s'(i, x) := sum of range [0, i) after adding x to range [l, r).
    - 0 < i <= l: s'(i, x) = s(i)
    - l < i <= r: s'(i, x) = s(i) + x(i - l) = s(i) + xi - xl
    - r < i < n: s'(i, x) = s(i) + x(r - l) = s(i) + xr - xl
    manage xr and -xl on fw_0, xi on fw_1.
    """

    def __init__(self, arr: typing.List[int]) -> None:
        n = len(arr)
        self.__fw_0 = FenwickTreeIntAdd(arr)
        self.__fw_1 = FenwickTreeIntAdd([0] * n)

    def __len__(self) -> int:
        return len(self.__fw_0)

    def set(self, left: int, right: int, x: int) -> None:
        assert 0 <= left < right <= len(self)
        self.__fw_0[left] = -x * left
        self.__fw_1[left] = x
        if right < len(self):
            self.__fw_0[right] = x * right
            self.__fw_1[right] = -x

    def get(self, left: int, right: int) -> int:
        assert 0 <= left <= right <= len(self)
        fw0, fw1 = self.__fw_0, self.__fw_1
        return fw0[right] + fw1[right] * right - fw0[left] - fw1[left] * left


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
