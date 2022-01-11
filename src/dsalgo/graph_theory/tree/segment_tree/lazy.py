import typing

from kagemeka.dsa.algebra.abstract.structure import Monoid

S = typing.TypeVar("S")
F = typing.TypeVar("F")


class SegmentTreeLazy:
    def __init__(
        self,
        ms: Monoid[S],
        mf: Monoid[F],
        map_: typing.Callable[[F, S], S],
        a: list[S],
    ) -> NoReturn:
        size = len(a)
        n = 1 << (size - 1).bit_length()
        data = [ms.e() for _ in range(n << 1)]
        data[n : n + size] = a.copy()
        lazy = [mf.e() for _ in range(n)]
        self.__ms, self.__mf, self.__map = ms, mf, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> NoReturn:
        d = self.__data
        d[i] = self.__ms.op(d[i << 1], d[i << 1 | 1])

    def __apply(self, i: int, f: F) -> NoReturn:
        d, lz = self.__data, self.__lazy
        d[i] = self.__map(f, d[i])
        if i < len(lz):
            lz[i] = self.__mf.op(f, lz[i])

    def __propagate(self, i: int) -> NoReturn:
        lz = self.__lazy
        self.__apply(i << 1, lz[i])
        self.__apply(i << 1 | 1, lz[i])
        lz[i] = self.__mf.e()

    def set(self, l: int, r: int, f: F) -> NoReturn:
        assert 0 <= l <= r <= self.size
        n = len(self) >> 1
        l, r = n + l, n + r
        h = n.bit_length()

        for i in range(h, 0, -1):
            if (l >> i) << i != l:
                self.__propagate(l >> i)
            if (r >> i) << i != r:
                self.__propagate((r - 1) >> i)

        l0, r0 = l, r
        while l < r:
            if l & 1:
                self.__apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.__apply(r, f)
            l, r = l >> 1, r >> 1

        l, r = l0, r0
        for i in range(1, h + 1):
            if (l >> i) << i != l:
                self.__merge(l >> i)
            if (r >> i) << i != r:
                self.__merge((r - 1) >> i)

    def get(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        n = len(self) >> 1
        l, r = n + l, n + r
        h = n.bit_length()

        for i in range(h, 0, -1):
            if (l >> i) << i != l:
                self.__propagate(l >> i)
            if (r >> i) << i != r:
                self.__propagate((r - 1) >> i)

        ms, d = self.__ms, self.__data
        vl, vr = ms.e(), ms.e()
        while l < r:
            if l & 1:
                vl = ms.op(vl, d[l])
                l += 1
            if r & 1:
                r -= 1
                vr = ms.op(d[r], vr)
            l, r = l >> 1, r >> 1
        return ms.op(vl, vr)

    def update(self, i: int, x: S) -> NoReturn:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        h = n.bit_length()
        for j in range(h, 0, -1):
            self.__propagate(i >> j)
        self.__data[i] = x
        for j in range(1, h + 1):
            self.__merge(i >> j)


S = typing.TypeVar("S")
F = typing.TypeVar("F")


class SegmentTreeLazyDFS:
    def __init__(
        self,
        ms: Monoid[S],
        mf: Monoid[F],
        map_: typing.Callable[[F, S], S],
        a: list[S],
    ) -> NoReturn:
        size = len(a)
        n = 1 << (size - 1).bit_length()
        data = [ms.e() for _ in range(n << 1)]
        data[n : n + size] = a.copy()
        lazy = [mf.e() for _ in range(n)]
        self.__ms, self.__mf, self.__map = ms, mf, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> NoReturn:
        d = self.__data
        d[i] = self.__ms.op(d[i << 1], d[i << 1 | 1])

    def __apply(self, i: int, f: F) -> NoReturn:
        d, lz = self.__data, self.__lazy
        d[i] = self.__map(f, d[i])
        if i < len(lz):
            lz[i] = self.__mf.op(f, lz[i])

    def __propagate(self, i: int) -> NoReturn:
        lz = self.__lazy
        self.__apply(i << 1, lz[i])
        self.__apply(i << 1 | 1, lz[i])
        lz[i] = self.__mf.e()

    def set(self, l: int, r: int, f: F) -> NoReturn:
        assert 0 <= l <= r <= self.size
        self.__set(l, r, f, 0, len(self) >> 1, 1)

    def __set(self, l: int, r: int, f: F, s: int, t: int, i: int) -> NoReturn:
        n = len(self) >> 1
        if i < n:
            self.__propagate(i)
        if t <= l or r <= s:
            return
        if l <= s and t <= r:
            self.__apply(i, f)
            if i < n:
                self.__propagate(i)
            return
        c = (s + t) >> 1
        self.__set(l, r, f, s, c, i << 1)
        self.__set(l, r, f, c, t, i << 1 | 1)
        self.__merge(i)

    def get(self, l: int, r: int) -> S:
        assert 0 <= l <= r <= self.size
        return self.__get(l, r, 0, len(self) >> 1, 1)

    def __get(self, l: int, r: int, s: int, t: int, i: int) -> S:
        ms = self.__ms
        n = len(self) >> 1
        if i < n:
            self.__propagate(i)
        if t <= l or r <= s:
            return ms.e()
        if l <= s and t <= r:
            if i < n:
                self.__propagate(i)
            return self.__data[i]
        c = (s + t) >> 1
        vl = self.__get(l, r, s, c, i << 1)
        vr = self.__get(l, r, c, t, i << 1 | 1)
        self.__merge(i)
        return ms.op(vl, vr)

    def update(self, i: int, x: S) -> NoReturn:
        assert 0 <= i < self.size
        n = len(self) >> 1
        a = self.get(i, i + 1)
        self.__data[n + i] = x
        a = self.get(i, i + 1)


def __test_segtree_lazy() -> NoReturn:
    s_op = lambda a, b: (a[0] + b[0], a[1] + b[1])
    s_e = lambda: (0, 0)
    ms = Monoid(s_op, s_e, False)
    f_op = lambda f, g: f + g
    f_e = lambda: 0
    mf = Monoid(f_op, f_e, False)
    map_ = lambda f, x: (x[0] + f * x[1], x[1])

    a = [(i, 1) for i in range(10)]
    # seg = SegmentTreeLazy(ms, mf, map_, a)
    seg = SegmentTreeLazyDFS(ms, mf, map_, a)
    print(seg.get(0, 10))
    print(seg.get(0, 5))
    print(len(seg), seg.size)
    seg.update(5, (10, 1))
    print(seg.get(0, 10))
    seg.set(2, 6, 3)
    print(seg.get(3, 10))


__test_segtree_lazy()
