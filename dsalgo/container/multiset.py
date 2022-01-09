"""TODO: implement
- multiset
    - with fenwick tree
    - with segment tree
    - with red black tree

"""


class FenwickTreeMultiset:
    def __init__(self, n: int) -> None:
        self.__fw = PointAddRangeSum([0] * n)
        self.__n = n

    def size(self) -> int:
        return self.__fw[self.__n - 1]

    def add(self, x: int) -> None:
        self.__fw[x] = 1

    def pop(self, x: int) -> None:
        fw = self.__fw
        assert fw.get_range(x, x + 1) > 0
        fw[x] = -1

    def get(self, i: int) -> None:
        fw = self.__fw
        assert 0 <= i < fw[self.__n - 1]

        def is_ok(v: S) -> bool:
            return v < i + 1

        return fw.max_right(is_ok)

    def max(self) -> int:
        return self.get(self.size() - 1)

    def min(self) -> int:
        return self.get(0)

    def lower_bound(self, x: int) -> int:
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        return self.__fw[x + 1]


def __test() -> None:
    multiset = FenwickTreeMultiset(1 << 19)
    try:
        multiset.min()
    except Exception as e:
        print(e)

    multiset.add(5)
    multiset.add(1000)
    print(multiset.min())
    print(multiset.max())
    print(multiset.lower_bound(5))
    print(multiset.upper_bound(5))
    print(multiset.lower_bound(6))
    print(multiset.upper_bound(4))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
