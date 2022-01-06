import typing

from kagemeka.dsa.algebra.abstract.structure import Monoid

T = typing.TypeVar("T")


def pascal(
    m: Monoid[T],
    default: typing.Callable[[], T],
    n: int,
) -> typing.List[typing.List[T]]:
    r"""Pascal's Triangle."""
    p = [[m.e() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        p[i][0] = default()
    for i in range(1, n):
        for j in range(1, i + 1):
            p[i][j] = m.op(p[i - 1][j - 1], p[i - 1][j])
    return p
