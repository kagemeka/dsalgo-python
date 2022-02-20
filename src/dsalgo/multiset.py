"""
Container
"""

import typing

from dsalgo.algebra.abstract.abstract_structure import Group
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree_abelian_group import (
    build_with_size,
)


class FenwickTreeMultiset:
    """FenwickTreeMultiset."""

    __max_value: int

    def __init__(self, max_value: int) -> None:
        """Initialize.

        Args:
            max_value (int):
                all values added to the set musb in range [0, max_value).
        """
        self.__fw = build_with_size(
            Group[int](
                op=lambda x, y: x + y,
                e=lambda: 0,
                invert=lambda x: -x,
            ),
            max_value,
        )
        self.__max_value = max_value

    @property
    def max_value(self) -> int:
        """Given max value.

        Returns:
            int: max value.
        """
        return self.__max_value

    def __len__(self) -> int:
        """Length.

        Returns:
            int: size of multiset.
        """
        return self.__fw[self.max_value]

    def __contains__(self, x: int) -> bool:
        """Check whether x is contained or not.

        Args:
            x (int): value to check.

        Returns:
            bool: True if contained else False.
        """
        return self.count(x) >= 1

    def count(self, x: int) -> int:
        """Count of value.

        Args:
            x (int):
                value to count.

        Returns:
            int:
                if value is out of range, return 0.
        """
        if x < 0 or self.max_value <= x:
            return 0
        return self.__fw.get_range(x, x + 1)

    def is_empty(self) -> bool:
        """Is Empty.

        Returns:
            bool: True if multiset is empty else False.
        """
        return len(self) == 0

    def __bool__(self) -> bool:
        """Bool.

        Returns:
            bool: True if multiset is not empty else False.
        """
        return not self.is_empty()

    def insert(self, x: int) -> None:
        """Insert.

        Args:
            x (int):
                value to insert.
                0 <= x < max_value.
        """
        assert 0 <= x < self.max_value
        self.__fw[x] = 1

    def remove(self, x: int) -> None:
        """Remove a value.

        Args:
            x (int):
                value to remove.
        Raises:
            KeyError:
                if x is out of range or not contained in multiset,
                raise KeyError.
        """
        if x not in self:
            raise KeyError(x)
        self.__fw[x] = -1

    def remove_all(self, x: int) -> None:
        """Remove all given values.

        Args:
            x (int):
                value to remove.
                0 <= x < max_value.
        """
        assert 0 <= x < self.max_value
        self.__fw[x] = -self.count(x)

    def __getitem__(self, i: int) -> typing.Optional[int]:
        """Indexing. return i-th element.

        Args:
            i (int): i-th (0-indexed).

        Returns:
            typing.Optional[int]:
                if index out of range, return None.
                otherwise return i-th elemnt.
        """
        if not 0 <= i < len(self):
            return None
        return self.__fw.max_right(lambda v: v < i + 1)

    def min(self) -> typing.Optional[int]:
        """Min element.

        Returns:
            typing.Optional[int]:
                if multiset is empty, return None.
        """
        return None if len(self) == 0 else self[0]

    def max(self) -> typing.Optional[int]:
        """Max element.

        Returns:
            typing.Optional[int]:
                if multiset is empty, return None.
        """
        return None if len(self) == 0 else self[len(self) - 1]

    def lower_bound(self, x: int) -> int:
        """Lower bound.

        Args:
            x (int): target value.

        Returns:
            int: lower bound index.
        """
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        """Upper bound.

        Args:
            x (int): target value.

        Returns:
            int: upper bound index.
        """
        return self.__fw[x + 1]


class SegmentTree:
    ...


class RedBlackTree:
    ...


class AVLTree:
    ...



import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, List, TypeVar, Union

T = TypeVar("T")


class BucketSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a: Iterable[T] = []) -> None:
        """
        Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)
        """
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x:
            return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0:
            self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for a in self.a:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

if __name__ == "__main__":
    import doctest

    doctest.testmod()
