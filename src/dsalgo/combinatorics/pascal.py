import typing

from dsalgo.algebra.abstract.structure import Monoid

T = typing.TypeVar("T")


def pascal_triangle(
    monoid: Monoid[T],
    default: typing.Callable[[], T],
    size: int,
) -> typing.List[typing.List[T]]:
    """Pascal's Triangle.

    Args:
        m (Monoid[T]): abstract structure.
        default (typing.Callable[[], T]): default value function.
        size (int): [description]: size of triangle.

    Returns:
        typing.List[typing.List[T]]: pascal's triangle.
    """
    p = [[monoid.e() for _ in range(size)] for _ in range(size)]
    for i in range(size):
        p[i][0] = default()
    for i in range(1, size):
        for j in range(1, i + 1):
            p[i][j] = monoid.op(p[i - 1][j - 1], p[i - 1][j])
    return p
