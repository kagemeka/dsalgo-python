import typing
from dsalgo.algebra.abstract.structure import Monoid

S = typing.TypeVar("S")


class FenwickTree(typing.Generic[S]):

    """Fenwick Tree.

    Generic Type S must be commutative over its operations.

    Example:
        >>> monoid = Monoid(op=lambda x, y: x + y, e=lambda: 0)
        >>> arr = [0, 1, 2, 3, 4]
        >>> fw = FenwickTree(monoid, arr)
        >>> fw[3]
        3
        >>> fw[2] = 2
        >>> fw[3]
        5
    """

    def __init__(self, monoid: Monoid[S], arr: typing.List[S]) -> None:
        """Init Fenwick Tree.

        Args:
            monoid (Monoid[S]): monoid is an abstruct data structure.
            arr (typing.List[S]): initial array.
        """
        n = len(arr)
        data: typing.List[S] = [monoid.e() for _ in range(n + 1)]
        data[1:] = arr.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                data[j] = monoid.op(data[j], data[i])
        self.__m, self.__data = monoid, data

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: S) -> None:
        """Set value.

        Args:
            i (int): index on the given array.
            x (S): the value to operate on arr[i].
        """
        d = self.__data
        assert 0 <= i < len(d) - 1
        i += 1
        while i < len(d):
            d[i] = self.__m.op(d[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        """Get value.

        Args:
            i (int): index on initial array.

        Returns:
            S: the result of cummulative opration.
                monoid.op(arr[0], ..., arr[i - 1]).
                return monoid.e() when i = 0.
        """
        m, d = self.__m, self.__data
        assert 0 <= i < len(d)
        v = m.e()
        while i > 0:
            v = m.op(v, d[i])
            i -= i & -i
        return v

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        """Max right.

        Args:
            i (int): index on initial array.

        Returns:
            int: the rightmost index i such that
                is_ok(monoid.op(arr[0], ..., arr[i - 1])) = true.
                monoid.op(arr[0], ..., arr[i - 1]) should be
                monotonous increasing against i.
                return 0 if is_ok(arr[0]) = false.
        """
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


def build_with_size(monoid: Monoid[S], size: int) -> FenwickTree[S]:
    """Build a new FenwickTree of given size.

    The Built one is filled with the value monoid.e().
    """
    return FenwickTree(
        monoid,
        [monoid.e() for _ in range(size)],
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
