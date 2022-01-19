import typing

from dsalgo.algebra.abstract.structure import Semigroup
from dsalgo.algebra.bit import bit_length_table

S = typing.TypeVar("S")


def sparse_table(
    semigroup: Semigroup[S],
    arr: typing.List[S],
) -> typing.Callable[[int, int], S]:
    # [left, right)
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


def disjoint_sparse_table(
    semigroup: Semigroup[S],
    arr: typing.List[S],
) -> typing.Callable[[int, int], S]:
    # [left, right)
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


# a = list(range(9))[::-1]
# sg = Semigroup[int](
#     op=min
# )
# get = sparse_table(sg, a)
# print(get(0, 9))


# a = list(range(9))
# sg = Semigroup[int](
#     op=lambda x, y: x + y,
# )
# get = disjoint_sparse_table(sg, a)
# print(get(3, 9))


def sparse_table_2d():
    ...
