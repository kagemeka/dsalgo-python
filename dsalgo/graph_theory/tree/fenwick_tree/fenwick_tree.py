import typing
from dsalgo.algebra.abstract.structure.monoid import Monoid
import doctest

S = typing.TypeVar("S")


class FenwickTree(typing.Generic[S]):
    """Fenwick Tree."""

    def __init__(self, monoid: Monoid[S], a: typing.List[S]) -> None:
        """Init Fenwick Tree.

        Args:
            monoid (Monoid[S]): monoid is an abstruct data structure.
            a (typing.List[S]): default array.
            
        Example:
            >>> monoid = Monoid(op=lambda x, y: x + y, e=lambda: 0)
            
        """
        n = len(a)
        data: typing.List[S] = [monoid.e() for _ in range(n + 1)]
        data[1:] = a.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                data[j] = monoid.op(data[j], data[i])
        self.__m, self.__data = monoid, data

    def __setitem__(self, i: int, x: S) -> None:
        d = self.__data
        assert 0 <= i < len(d) - 1
        i += 1
        while i < len(d):
            d[i] = self.__m.op(d[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        m, d = self.__m, self.__data
        assert 0 <= i < len(d)
        v = m.e()
        while i > 0:
            v = m.op(v, d[i])
            i -= i & -i
        return v

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        m, d = self.__m, self.__data
        n = len(d)
        length = 1
        while length << 1 < n:
            length <<= 1
        v, i = m.e(), 0
        while length:
            if i + length < n and is_ok(m.op(v, d[i + length])):
                i += length
                v = m.op(v, d[i])
            length >>= 1
        return i


"""In case implementing as zero-indexed internally.
set:
    i |= i + 1

get:
    i &= i + 1
    i -= 1
"""


if __name__ == '__main__':
    doctest.testmod()
