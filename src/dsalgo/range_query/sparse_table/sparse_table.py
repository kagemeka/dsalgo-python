import typing

from dsalgo.algebra.abstract.structure import Semigroup
from dsalgo.algebra.bit.bit_length import bit_length_table

S = typing.TypeVar("S")


def sparse_table(
    semigroup: Semigroup[S],
    arr: typing.List[S],
) -> typing.Callable[[int, int], S]:
    """Sparse Table.

    Args:
        semigroup (Semigroup[S]): operation must be idempotent.
        arr (typing.List[S]): original array.

    Returns:
        typing.Callable[[int, int], S]: function to get product [left, right).
    """
    n = len(arr)
    assert n > 0
    bit_length = bit_length_table(n + 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(k - 1):
        data.append(data[i].copy())
        for j in range(n - (1 << i)):
            data[i + 1][j] = semigroup.op(data[i][j], data[i][j + (1 << i)])

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[right - 1 - left] - 1
        return semigroup.op(data[k][left], data[k][right - (1 << k)])

    return get


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

