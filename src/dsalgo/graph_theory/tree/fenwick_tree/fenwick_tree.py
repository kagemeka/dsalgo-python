import typing

from dsalgo.algebra.abstract.structure import Monoid, Group

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


class FenwickTreeAbelianGroup(typing.Generic[S], FenwickTree[S]):
    def __init__(self, group: Group[S], arr: typing.List[S]) -> None:
        monoid = Monoid[S](group.op, group.e)
        super().__init__(monoid, arr)
        self.__group = group

    def get_range(self, left: int, right: int) -> S:
        """Get range product.
        An associative function for FenwickTree.
        Generic Type S must be Abelian Group not only but Monoid.
        so it's needed to pass the inverse function.
        """

        g = self.__group
        return g.op(g.invert(self[left]), self[right])


class FenwickTreeIntAdd:  # version not using dataclass for performance.
    def __init__(self, arr: typing.List[int]) -> None:
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] += data[i]
        self.__data = data

    def __set__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self.__data) - 1
        i += 1
        while i < len(self.__data):
            self.__data[i] += x
            i += i & -i

    def __get__(self, i: int) -> int:
        assert 0 <= i < len(self.__data)
        v = 0
        while i > 0:
            v += self.__data[i]
            i -= i & -i
        return v



if __name__ == "__main__":
    import doctest

    doctest.testmod()
