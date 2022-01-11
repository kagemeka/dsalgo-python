class PointAddRangeSum:
    __G = Group(
        op=lambda x, y: x + y,
        e=lambda: 0,
        commutative=True,
        inverse=lambda x: -x,
    )

    def __init__(self, a: list[int]) -> NoReturn:
        self.__fw = FenwickTree(self.__G, a)

    def __setitem__(self, i: int, x: S) -> NoReturn:
        self.__fw[i] = x

    def __getitem__(self, i: int) -> S:
        return self.__fw[i]

    def get_range(self, l: int, r: int) -> S:
        G = self.__G
        return G.op(G.inverse(self.__fw[l]), self.__fw[r])

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        return self.__fw.max_right(is_ok)
