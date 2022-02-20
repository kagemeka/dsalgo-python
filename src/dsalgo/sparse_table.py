from __future__ import annotations
import typing
import copy
import dsalgo.bitset
import dsalgo.abstract_structure
from dsalgo.type import S
import typing


def sparse_table(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
    arr: list[S],
) -> typing.Callable[[int, int], S]:
    """Sparse Table.

    Args:
        semigroup (Semigroup[S]):
            semigroup.
            operation must be idepotent.
        arr (list[S]): original array.

    Returns:
        typing.Callable[[int, int], S]: function to get product [left, right).
    """
    n = len(arr)
    assert n > 0
    bit_length = dsalgo.bitset.bit_length_table(n + 1)
    data = [arr.copy()]
    for i in range(bit_length[n - 1] - 1):
        data.append(data[i].copy())
        for j in range(n - (1 << i)):
            data[i + 1][j] = semigroup.operation(
                data[i][j],
                data[i][j + (1 << i)],
            )

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[right - 1 - left] - 1
        return semigroup.operation(data[k][left], data[k][right - (1 << k)])

    return get


def sparse_table_2d(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
    matrix: list[list[S]],
) -> typing.Callable[[int, int, int, int], S]:
    h = len(matrix)
    assert h > 0
    w = len(matrix[0])
    assert w > 0 and all(len(row) == w for row in matrix)
    bit_length = dsalgo.bitset.bit_length_table(max(h, w))
    data = [copy.deepcopy(matrix)]

    for log_dx in range(bit_length[w - 1] - 1):
        i = log_dx
        data.append(copy.deepcopy(data[i]))
        for y in range(h):
            for x in range(w - (1 << i)):
                data[i + 1][y][x] = semigroup.operation(
                    data[i][y][x],
                    data[i][y][x + (1 << i)],
                )
    width = len(data)
    assert len(data) == max(1, bit_length[w - 1])
    for log_dy in range(bit_length[h - 1] - 1):
        for log_dx in range(max(1, bit_length[w - 1])):
            i = log_dy * width + log_dx
            ni = i + width
            data.append(copy.deepcopy(data[i]))
            for y in range(h - (1 << log_dy)):
                for x in range(w - (1 << log_dx)):
                    data[ni][y][x] = semigroup.operation(
                        data[i][y][x],
                        data[i][y + (1 << log_dy)][x],
                    )

    def get(y0: int, x0: int, y1: int, x1: int) -> S:
        assert 0 <= y0 < y1 <= h and 0 <= x0 < x1 <= w
        log_dy = bit_length[y1 - y0 - 1] - 1
        log_dx = bit_length[x1 - x0 - 1] - 1
        if log_dy == log_dx == -1:
            return data[0][y0][x0]
        if log_dy == -1:
            return semigroup.operation(
                data[log_dx][y0][x0],
                data[log_dx][y0][x1 - (1 << log_dx)],
            )
        if log_dx == -1:
            return semigroup.operation(
                data[log_dy][y0][x0],
                data[log_dy][y1 - (1 << log_dy)][x0],
            )
        i = log_dy * width + log_dx
        res = semigroup.operation(
            data[i][y0][x0],
            data[i][y1 - (1 << log_dy)][x1 - (1 << log_dx)],
        )
        res = semigroup.operation(res, data[i][y0][x1 - (1 << log_dx)])
        return semigroup.operation(res, data[i][y1 - (1 << log_dy)][x0])

    return get


def disjoint_sparse_table(
    semigroup: dsalgo.abstract_structure.Semigroup[S],
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
    bit_length = dsalgo.bitset.bit_length_table(n << 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] = semigroup.operation(
                    data[i][j - k - 1],
                    data[i][j - k],
                )
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] = semigroup.operation(
                    data[i][j + k],
                    data[i][j + k + 1],
                )

    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[left ^ (right - 1)] - 1
        return semigroup.operation(data[k][left], data[k][right - 1])

    return get


# from dsalgo.algebra.bit.bit_length import bit_length_table


def disjoint_sparse_table_int_xor(
    arr: list[int],
) -> typing.Callable[[int, int], int]:
    """Disjoint Sparse Table int-xor.

    Args:
        arr (list[int]): original array.

    Returns:
        typing.Callable[[int, int], int]:
            function to get xor product [left, right).
    """
    n = len(arr)
    assert n > 0
    bit_length = dsalgo.bitset.bit_length_table(n << 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] ^= data[i][j - k]
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] ^= data[i][j + k]

    def get(left: int, right: int) -> int:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[left ^ (right - 1)] - 1
        return data[k][left] ^ data[k][right - 1]

    return get


def disjoint_sparse_table_int_sum(
    arr: list[int],
) -> typing.Callable[[int, int], int]:
    """Disjoint Sparse Table int-sum.

    Args:
        arr (list[int]): original array.

    Returns:
        typing.Callable[[int, int], int]:
            function to get sum [left, right).
    """
    n = len(arr)
    assert n > 0
    bit_length = dsalgo.bitset.bit_length_table(n << 1)
    k = max(1, bit_length[n - 1])
    data = [arr.copy()]
    for i in range(1, k):
        data.append(arr.copy())
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] += data[i][j - k]
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] += data[i][j + k]

    def get(left: int, right: int) -> int:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        k = bit_length[left ^ (right - 1)] - 1
        return data[k][left] + data[k][right - 1]

    return get


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
