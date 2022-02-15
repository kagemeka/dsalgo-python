import typing

from dsalgo.algebra.abstract.abstract_structure import Semigroup
from dsalgo.algebra.bit.bit_length import bit_length_table

S = typing.TypeVar("S")


def disjoint_sparse_table(
    semigroup: Semigroup[S],
    arr: list[S],
) -> typing.Callable[[int, int], S]:
    """Disjoint Sparse Table.

    Args:
        semigroup (Semigroup[S]): semigroup.
        arr (list[S]): original array.

    Returns:
        typing.Callable[[int, int], S]: function to get product [left, right).
    """
    n = len(arr)
    assert n > 0
    bit_length = bit_length_table(n << 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] = semigroup.op(
                    data[i][j - k - 1],
                    data[i][j - k],
                )
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] = semigroup.op(
                    data[i][j + k],
                    data[i][j + k + 1],
                )

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[left ^ (right - 1)] - 1
        return semigroup.op(data[k][left], data[k][right - 1])

    return get


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
