from __future__ import annotations

import typing

from kagemeka.dsa.algebra.abstract.structure import Monoid

S = typing.TypeVar("S")


class SegmentTree(typing.Generic[S]):
    def __init__(self, monoid: Monoid[S], a: list[S]) -> NoReturn:
        size = len(a)
        n = 1 << (size - 1).bit_length()
        seg = [monoid.e() for _ in range(n << 1)]
        seg[n : n + size] = a.copy()
        self.__m, self.__size, self.__data = monoid, size, seg
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> NoReturn:
        d = self.__data
        d[i] = self.__m.op(d[i << 1], d[i << 1 | 1])

    def __setitem__(self, i: int, x: S) -> NoReturn:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__merge(i)

    def __getitem__(self, i: int) -> S:
        d = self.__data
        return d[(len(d) >> 1) + i]

    def get(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        m, d = self.__m, self.__data
        n = len(d) >> 1
        l, r = n + l, n + r
        vl, vr = m.e(), m.e()
        while l < r:
            if l & 1:
                vl = m.op(vl, d[l])
                l += 1
            if r & 1:
                r -= 1
                vr = m.op(d[r], vr)
            l, r = l >> 1, r >> 1
        return m.op(vl, vr)

    def max_right(self, is_ok: typing.Callable[[S], bool], l: int) -> int:
        m, d = self.__m, self.__data
        n = len(d) >> 1
        assert 0 <= l < self.size
        v, i = m.e(), n + l
        while True:
            i //= i & -i
            if is_ok(op(v, d[i])):
                v = op(v, d[i])
                i += 1
                if i & -i == i:
                    return self.size
                continue
            while i < n:
                i <<= 1
                if not is_ok(op(v, d[i])):
                    continue
                v = op(v, d[i])
                i += 1
            return i - n


S = typing.TypeVar("S")


class SegmentTreeDFS(typing.Generic[S]):
    def __init__(self, monoid: Monoid[S], a: list[S]) -> NoReturn:
        size = len(a)
        n = 1 << (size - 1).bit_length()
        seg = [monoid.e() for _ in range(n << 1)]
        seg[n : n + size] = a.copy()
        self.__m, self.__size, self.__data = monoid, size, seg
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> NoReturn:
        d = self.__data
        d[i] = self.__m.op(d[i << 1], d[i << 1 | 1])

    def __setitem__(self, i: int, x: S) -> NoReturn:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__merge(i)

    def __getitem__(self, i: int) -> S:
        d = self.__data
        return d[(len(d) >> 1) + i]

    def get(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        return self.__get(l, r, 0, len(self) >> 1, 1)

    def __get(self, l: int, r: int, s: int, t: int, i: int) -> S:
        m = self.__m
        if t <= l or r <= s:
            return m.e()
        if l <= s and t <= r:
            return self.__data[i]
        c = (s + t) >> 1
        return m.op(
            self.__get(l, r, s, c, i << 1),
            self.__get(l, r, c, t, i << 1 | 1),
        )


def __test_segment_tree() -> NoReturn:
    n = 10
    a = list(range(n))
    op = lambda a, b: a + b
    e = lambda: 0
    monoid = Monoid(op, e, False)
    seg = SegmentTree[int](monoid, a)

    print(len(seg))
    print(seg.size)
    print(seg[5])
    print(seg.get(0, 10))
    seg[5] = 10
    print(seg.get(0, 10))


def __test_segment_tree_dfs() -> NoReturn:
    n = 10
    a = list(range(n))
    op = lambda a, b: a + b
    e = lambda: 0
    monoid = Monoid(op, e, False)
    seg = SegmentTreeDFS[int](monoid, a)

    print(len(seg))
    print(seg.size)
    print(seg[5])
    print(seg.get(0, 10))
    seg[5] = 10
    print(seg.get(0, 10))
