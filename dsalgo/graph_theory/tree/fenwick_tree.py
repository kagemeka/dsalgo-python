import typing

from kagemeka.dsa.algebra.abstract.structure import Monoid

S = typing.TypeVar("S")


class FenwickTree(typing.Generic[S]):
    def __init__(self, monoid: Monoid[S], a: list[S]) -> NoReturn:
        n = len(a)
        fw = [None] * (n + 1)
        fw[1:] = a.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                fw[j] = monoid.op(fw[j], fw[i])
        self.__m, self.__data = monoid, fw

    def __setitem__(self, i: int, x: S) -> NoReturn:
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
        l = 1
        while l << 1 < n:
            l <<= 1
        v, i = m.e(), 0
        while l:
            if i + l < n and is_ok(m.op(v, d[i + l])):
                i += l
                v = m.op(v, d[i])
            l >>= 1
        return i


class FenwickZeroIndexed:
    def __init__(self, n: int) -> NoReturn:
        self.__data = [0] * n

    def __setitem__(self, i: int, x: int) -> NoReturn:
        d = self.__data
        while i < len(d):
            d[i] += x
            i |= i + 1

    def __getitem__(self, i: int) -> int:
        s = 0
        while i >= 0:
            s += self.__d[i]
            i &= i + 1
            i -= 1
        return s
