from __future__ import annotations

import typing

import dsalgo.abstract_structure
from dsalgo.type import F, S


class SegmentTree(typing.Generic[S]):
    _monoid: dsalgo.abstract_structure.Monoid[S]
    _data: list[S]
    _size: int

    def __init__(
        self,
        monoid: dsalgo.abstract_structure.Monoid[S],
        arr: list[S],
    ) -> None:
        size = len(arr)
        n = 1 << (size - 1).bit_length()
        data = [monoid.identity() for _ in range(n << 1)]
        data[n : n + size] = arr.copy()
        self._monoid, self._size, self._data = monoid, size, data
        for i in range(n - 1, 0, -1):
            self._merge(i)

    def __len__(self) -> int:
        return len(self._data)

    @property
    def size(self) -> int:
        return self._size

    def _merge(self, i: int) -> None:
        self._data[i] = self._monoid.operation(
            self._data[i << 1],
            self._data[i << 1 | 1],
        )

    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self._data[i] = x
        while i > 1:
            i >>= 1
            self._merge(i)

    def __getitem__(self, i: int) -> S:
        return self._data[(len(self._data) >> 1) + i]

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self._data) >> 1
        l, r = n + left, n + right
        vl, vr = self._monoid.identity(), self._monoid.identity()
        while l < r:
            if l & 1:
                vl = self._monoid.operation(vl, self._data[l])
                left += 1
            if r & 1:
                r -= 1
                vr = self._monoid.operation(self._data[r], vr)
            l, r = l >> 1, r >> 1
        return self._monoid.operation(vl, vr)

    def max_right(self, is_ok: typing.Callable[[S], bool], left: int) -> int:
        n = len(self._data) >> 1
        assert 0 <= left < self.size
        v, i = self._monoid.identity(), n + left
        while True:
            i //= i & -i
            if is_ok(self._monoid.operation(v, self._data[i])):
                v = self._monoid.operation(v, self._data[i])
                i += 1
                if i & -i == i:
                    return self.size
                continue
            while i < n:
                i <<= 1
                if not is_ok(self._monoid.operation(v, self._data[i])):
                    continue
                v = self._monoid.operation(v, self._data[i])
                i += 1
            return i - n


class SegmentTreeDFS(SegmentTree[S]):
    def __setitem__(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        i += len(self) >> 1
        self._data[i] = x
        while i > 1:
            i >>= 1
            self._merge(i)

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
            return self._monoid.identity()
        if left <= current_left and current_right <= right:
            return self._data[i]
        center = (current_left + current_right) >> 1
        return self._monoid.operation(
            self.__get(left, right, current_left, center, i << 1),
            self.__get(left, right, center, current_right, i << 1 | 1),
        )


class SegmentTreeDual:
    ...


class SegmentTreeBeats:
    ...


class LazySegmentTree(typing.Generic[S, F]):
    _monoid_s: dsalgo.abstract_structure.Monoid[S]
    _monoid_f: dsalgo.abstract_structure.Monoid[F]
    _data: list[S]
    _lazy: list[F]
    _size: int

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
        self._monoid_s, self._monoid_f, self.__map = monoid_s, monoid_f, map_
        self._size, self._data, self._lazy = size, data, lazy
        for i in range(n - 1, 0, -1):
            self._merge(i)

    def __len__(self) -> int:
        return len(self._data)

    @property
    def size(self) -> int:
        return self._size

    def _merge(self, i: int) -> None:
        self._data[i] = self._monoid_s.operation(
            self._data[i << 1],
            self._data[i << 1 | 1],
        )

    def _apply(self, i: int, f: F) -> None:
        self._data[i] = self.__map(f, self._data[i])
        if i < len(self._lazy):
            self._lazy[i] = self._monoid_f.operation(f, self._lazy[i])

    def _propagate(self, i: int) -> None:
        self._apply(i << 1, self._lazy[i])
        self._apply(i << 1 | 1, self._lazy[i])
        self._lazy[i] = self._monoid_f.identity()

    def set(self, left: int, right: int, f: F) -> None:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left += n
        right += n
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self._propagate(left >> i)
            if (right >> i) << i != right:
                self._propagate((right - 1) >> i)

        l0, r0 = left, right  # backup
        while left < right:
            if left & 1:
                self._apply(left, f)
                left += 1
            if right & 1:
                right -= 1
                self._apply(right, f)
            left, right = left >> 1, right >> 1

        left, right = l0, r0
        for i in range(1, height + 1):
            if (left >> i) << i != right:
                self._merge(left >> i)
            if (right >> i) << i != right:
                self._merge((right - 1) >> i)

    def get(self, left: int, right: int) -> S:
        assert 0 <= left <= right <= self.size
        n = len(self) >> 1
        left, right = n + left, n + right
        height = n.bit_length()

        for i in range(height, 0, -1):
            if (left >> i) << i != left:
                self._propagate(left >> i)
            if (right >> i) << i != right:
                self._propagate((right - 1) >> i)

        vl, vr = self._monoid_s.identity(), self._monoid_s.identity()
        while left < right:
            if left & 1:
                vl = self._monoid_s.operation(vl, self._data[left])
                left += 1
            if right & 1:
                right -= 1
                vr = self._monoid_s.operation(self._data[right], vr)
            left, right = left >> 1, right >> 1
        return self._monoid_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        i += n
        height = n.bit_length()
        for j in range(height, 0, -1):
            self._propagate(i >> j)
        self._data[i] = x
        for j in range(1, height + 1):
            self._merge(i >> j)


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
            self._propagate(i)
        if current_right <= left or right <= current_left:
            return
        if left <= current_left and current_right <= right:
            self._apply(i, f)
            if i < n:
                self._propagate(i)
            return
        center = (current_left + current_right) >> 1
        self.__set(left, right, f, current_left, center, i << 1)
        self.__set(left, right, f, center, current_right, i << 1 | 1)
        self._merge(i)

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
            self._propagate(i)
        if current_right <= left or right <= current_left:
            return self._monoid_s.identity()
        if left <= current_left and current_right <= right:
            if i < n:
                self._propagate(i)
            return self._data[i]
        center = (current_left + current_right) >> 1
        vl = self.__get(left, right, current_left, center, i << 1)
        vr = self.__get(left, right, center, current_right, i << 1 | 1)
        self._merge(i)
        return self._monoid_s.operation(vl, vr)

    def update(self, i: int, x: S) -> None:
        assert 0 <= i < self.size
        n = len(self) >> 1
        self.get(i, i + 1)
        self._data[n + i] = x
        self.get(i, i + 1)
