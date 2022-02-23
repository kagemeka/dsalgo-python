from __future__ import annotations

import typing

import dsalgo.abstract_structure
from dsalgo.type import S, F


class SegmentTree(typing.Generic[S]):
    __monoid: dsalgo.abstract_structure.Monoid[S]
    __data: list[S]
    __size: int

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

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> None:
        self.__data[i] = self.__monoid.operation(
            self.__data[i << 1],
            self.__data[i << 1 | 1],
        )

    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__merge(i)

    def __getitem__(self, i: int) -> S:
        return self.__data[(len(self.__data) >> 1) + i]

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self.__data) >> 1
        l, r = n + left, n + right
        vl, vr = self.__monoid.identity(), self.__monoid.identity()
        while l < r:
            if l & 1:
                vl = self.__monoid.operation(vl, self.__data[l])
                left += 1
            if r & 1:
                r -= 1
                vr = self.__monoid.operation(self.__data[r], vr)
            l, r = l >> 1, r >> 1
        return self.__monoid.operation(vl, vr)

    def max_right(self, is_ok: typing.Callable[[S], bool], left: int) -> int:
        n = len(self.__data) >> 1
        assert 0 <= left < self.size
        v, i = self.__monoid.identity(), n + left
        while True:
            i //= i & -i
            if is_ok(self.__monoid.operation(v, self.__data[i])):
                v = self.__monoid.operation(v, self.__data[i])
                i += 1
                if i & -i == i:
                    return self.size
                continue
            while i < n:
                i <<= 1
                if not is_ok(self.__monoid.operation(v, self.__data[i])):
                    continue
                v = self.__monoid.operation(v, self.__data[i])
                i += 1
            return i - n


class SegmentTreeDFS(SegmentTree[S]):
    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__merge(i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        return self.__get(left, right, 0, len(self) >> 1, 1)

    def __get(
        self,
        left: int,
        right: int,
        current_left: int,
        current_right: int,
        i: int,
    ) -> S:
        if current_right <= left or right <= current_left:
            return self.__monoid.identity()
        if left <= current_left and current_right <= right:
            return self.__data[i]
        center = (current_left + current_right) >> 1
        return self.__monoid.operation(
            self.__get(left, right, current_left, center, i << 1),
            self.__get(left, right, center, current_right, i << 1 | 1),
        )


class SegmentTreeDual:
    ...


class SegmentTreeBeats:
    ...


class LazySegmentTree(typing.Generic[S, F]):
    __monoid_s: dsalgo.abstract_structure.Monoid[S]
    __monoid_f: dsalgo.abstract_structure.Monoid[F]
    __data: list[S]
    __lazy: list[F]
    __size: int

    def __init__(
        self,
        monoid_s: dsalgo.abstract_structure.Monoid[S],
        monoid_f: dsalgo.abstract_structure.Monoid[F],
        map_: typing.Callable[[F, S], S],
        arr: list[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid_s.identity() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        lazy = [monoid_f.identity() for _ in range(n)]
        self.__monoid_s, self.__monoid_f, self.__map = monoid_s, monoid_f, map_
        self.__size, self.__data, self.__lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self.__merge(i)

    def __len__(self) -> int:
        return len(self.__data)

    @property
    def size(self) -> int:
        return self.__size

    def __merge(self, i: int) -> None:
        self.__data[i] = self.__monoid_s.operation(
            self.__data[i << 1],
            self.__data[i << 1 | 1],
        )

    def __apply(self, i: int, f: F) -> None:
        self.__data[i] = self.__map(f, self.__data[i])
        if i < len(self.__lazy):
            self.__lazy[i] = self.__monoid_f.operation(f, self.__lazy[i])

    def __propagate(self, i: int) -> None:
        self.__apply(i << 1, self.__lazy[i])
        self.__apply(i << 1 | 1, self.__lazy[i])
        self.__lazy[i] = self.__monoid_f.identity()

    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left += n
        right += n
        height = n.bit_length()

        for i in range(height, 0, -1):
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
        for i in range(1, height + 1):
            if (left >> i) << i != right:
                self.__merge(left >> i)
            if (right >> i) << i != right:
                self.__merge((right - 1) >> i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left, right = n + left, n + right
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self.__propagate(left >> i)
            if (right >> i) << i != right:
                self.__propagate((right - 1) >> i)

        vl, vr = self.__monoid_s.identity(), self.__monoid_s.identity()
        while left < right:
            if left & 1:
                vl = self.__monoid_s.operation(vl, self.__data[left])
                left += 1
            if right & 1:
                right -= 1
                vr = self.__monoid_s.operation(self.__data[right], vr)
            left, right = left >> 1, right >> 1
        return self.__monoid_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        height = n.bit_length()
        for j in range(height, 0, -1):
            self.__propagate(i >> j)
        self.__data[i] = x
        for j in range(1, height + 1):
            self.__merge(i >> j)


class LazySegmentTreeDFS(LazySegmentTree[S, F]):
    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        self.__set(left, right, f, 0, len(self) >> 1, 1)

    def __set(
        self,
        left: int,
        right: int,
        f: F,
        current_left: int,
        current_right: int,
        i: int,
    ) -> None:
        n = len(self) >> 1
        if i < n:
            self.__propagate(i)
        if current_right <= left or right <= current_left:
            return
        if left <= current_left and current_right <= right:
            self.__apply(i, f)
            if i < n:
                self.__propagate(i)
            return
        center = (current_left + current_right) >> 1
        self.__set(left, right, f, current_left, center, i << 1)
        self.__set(left, right, f, center, current_right, i << 1 | 1)
        self.__merge(i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        return self.__get(left, right, 0, len(self) >> 1, 1)

    def __get(
        self,
        left: int,
        right: int,
        current_left: int,
        current_right: int,
        i: int,
    ) -> S:
        n = len(self) >> 1
        if i < n:
            self.__propagate(i)
        if current_right <= left or right <= current_left:
            return self.__monoid_s.identity()
        if left <= current_left and current_right <= right:
            if i < n:
                self.__propagate(i)
            return self.__data[i]
        center = (current_left + current_right) >> 1
        vl = self.__get(left, right, current_left, center, i << 1)
        vr = self.__get(left, right, center, current_right, i << 1 | 1)
        self.__merge(i)
        return self.__monoid_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        self.get(i, i + 1)
        self.__data[n + i] = x
        self.get(i, i + 1)
