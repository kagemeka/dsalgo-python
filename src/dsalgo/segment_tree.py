from __future__ import annotations

import typing

import dsalgo.abstract_structure
from dsalgo.type import S


class SegmentTree(typing.Generic[S]):
    def __init__(
        self,
        monoid: dsalgo.abstract_structure.Monoid[S],
        arr: list[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid.identity() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        self.__monoid, self.__size, self.__data = monoid, size, data
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:  # buffer size
        return len(self.__data)

    @property
    def size(self) -> int:  # original array size
        return self.__size

    def __merge(self, i: int) -> None:
        d = self.__data
        d[i] = self.__monoid.operation(d[i << 1], d[i << 1 | 1])

    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__merge(i)

    def __getitem__(self, i: int) -> S:
        d = self.__data
        return d[(len(d) >> 1) + i]

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        m, d = self.__m, self.__data
        n = len(d) >> 1
        l, r = n + left, n + right
        vl, vr = m.e(), m.e()
        while l < r:
            if l & 1:
                vl = m.op(vl, d[l])
                left += 1
            if r & 1:
                r -= 1
                vr = m.op(d[r], vr)
            l, r = l >> 1, r >> 1
        return m.op(vl, vr)

    def max_right(self, is_ok: typing.Callable[[S], bool], left: int) -> int:
        m, d = self.__m, self.__data
        n = len(d) >> 1
        assert 0 <= left < self.size
        v, i = m.e(), n + left
        while True:
            i //= i & -i
            if is_ok(m.op(v, d[i])):
                v = m.op(v, d[i])
                i += 1
                if i & -i == i:
                    return self.size
                continue
            while i < n:
                i <<= 1
                if not is_ok(m.op(v, d[i])):
                    continue
                v = m.op(v, d[i])
                i += 1
            return i - n


class SegmentTreeDFS(typing.Generic[S]):
    def __init__(self, monoid: Monoid[S], arr: list[S]) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        seg = [monoid.e() for _ in range(n << 1)]
        seg[n : n + size] = arr.copy()
        self.__m, self.__size, self.__data = monoid, size, seg
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> None:
        d = self.__data
        d[i] = self.__m.op(d[i << 1], d[i << 1 | 1])

    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__merge(i)

    def __getitem__(self, i: int) -> S:
        d = self.__data
        return d[(len(d) >> 1) + i]

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        return self.__get(left, right, 0, len(self) >> 1, 1)

    def __get(self, left: int, right: int, s: int, t: int, i: int) -> S:
        m = self.__m
        if t <= left or right <= s:
            return m.e()
        if left <= s and t <= right:
            return self.__data[i]
        c = (s + t) >> 1
        return m.op(
            self.__get(left, right, s, c, i << 1),
            self.__get(left, right, c, t, i << 1 | 1),
        )


class SegmentTreeDual:
    ...


class SegmentTreeBeats:
    ...


F = typing.TypeVar("F")


class LazySegmentTree(typing.Generic[S, F]):
    def __init__(
        self,
        monoid_s: Monoid[S],
        monoid_f: Monoid[F],
        map_: typing.Callable[[F, S], S],
        arr: list[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid_s.e() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        lazy = [monoid_f.e() for _ in range(n)]
        self.__ms, self.__mf, self.__map = monoid_s, monoid_f, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> None:
        d = self.__data
        d[i] = self.__ms.op(d[i << 1], d[i << 1 | 1])

    def __apply(self, i: int, f: F) -> None:
        d, lz = self.__data, self.__lazy
        d[i] = self.__map(f, d[i])
        if i < len(lz):
            lz[i] = self.__mf.op(f, lz[i])

    def __propagate(self, i: int) -> None:
        lz = self.__lazy
        self.__apply(i << 1, lz[i])
        self.__apply(i << 1 | 1, lz[i])
        lz[i] = self.__mf.e()

    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left, right = n + left, n + right
        h = n.bit_length()

        for i in range(h, 0, -1):
            if (left >> i) << i != left:
                self.__propagate(left >> i)
            if (right >> i) << i != right:
                self.__propagate((right - 1) >> i)

        l0, r0 = left, right  # backup
        while left < right:
            if left & 1:
                self.__apply(left, f)
                left += 1
            if right & 1:
                right -= 1
                self.__apply(right, f)
            left, right = left >> 1, right >> 1

        left, right = l0, r0
        for i in range(1, h + 1):
            if (left >> i) << i != right:
                self.__merge(left >> i)
            if (right >> i) << i != right:
                self.__merge((right - 1) >> i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left, right = n + left, n + right
        h = n.bit_length()

        for i in range(h, 0, -1):
            if (left >> i) << i != left:
                self.__propagate(left >> i)
            if (right >> i) << i != right:
                self.__propagate((right - 1) >> i)

        ms, d = self.__ms, self.__data
        vl, vr = ms.e(), ms.e()
        while left < right:
            if left & 1:
                vl = ms.op(vl, d[left])
                left += 1
            if right & 1:
                right -= 1
                vr = ms.op(d[right], vr)
            left, right = left >> 1, right >> 1
        return ms.op(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        h = n.bit_length()
        for j in range(h, 0, -1):
            self.__propagate(i >> j)
        self.__data[i] = x
        for j in range(1, h + 1):
            self.__merge(i >> j)


class LazySegmentTreeDFS(typing.Generic[S, F]):
    def __init__(
        self,
        monoid_s: Monoid[S],
        monoid_f: Monoid[F],
        map_: typing.Callable[[F, S], S],
        arr: list[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid_s.e() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        lazy = [monoid_f.e() for _ in range(n)]
        self.__ms, self.__mf, self.__map = monoid_s, monoid_f, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> None:
        d = self.__data
        d[i] = self.__ms.op(d[i << 1], d[i << 1 | 1])

    def __apply(self, i: int, f: F) -> None:
        d, lz = self.__data, self.__lazy
        d[i] = self.__map(f, d[i])
        if i < len(lz):
            lz[i] = self.__mf.op(f, lz[i])

    def __propagate(self, i: int) -> None:
        lz = self.__lazy
        self.__apply(i << 1, lz[i])
        self.__apply(i << 1 | 1, lz[i])
        lz[i] = self.__mf.e()

    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        self.__set(left, right, f, 0, len(self) >> 1, 1)

    def __set(
        self, left: int, right: int, f: F, s: int, t: int, i: int
    ) -> None:
        n = len(self) >> 1
        if i < n:
            self.__propagate(i)
        if t <= left or right <= s:
            return
        if left <= s and t <= right:
            self.__apply(i, f)
            if i < n:
                self.__propagate(i)
            return
        c = (s + t) >> 1
        self.__set(left, right, f, s, c, i << 1)
        self.__set(left, right, f, c, t, i << 1 | 1)
        self.__merge(i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        return self.__get(left, right, 0, len(self) >> 1, 1)

    def __get(self, left: int, right: int, s: int, t: int, i: int) -> S:
        ms = self.__ms
        n = len(self) >> 1
        if i < n:
            self.__propagate(i)
        if t <= left or right <= s:
            return ms.e()
        if left <= s and t <= right:
            if i < n:
                self.__propagate(i)
            return self.__data[i]
        c = (s + t) >> 1
        vl = self.__get(left, right, s, c, i << 1)
        vr = self.__get(left, right, c, t, i << 1 | 1)
        self.__merge(i)
        return ms.op(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        self.get(i, i + 1)
        self.__data[n + i] = x
        self.get(i, i + 1)
