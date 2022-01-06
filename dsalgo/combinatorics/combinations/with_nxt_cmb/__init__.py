import typing

from ...next_combination import NextCombination

# TODO cut below


class Combinations:
    def __call__(
        self,
        a: typing.Iterable[
            typing.Any,
        ],
        r: int,
    ) -> typing.AsyncIterator[tuple[typing.Any],]:
        a = tuple(a)
        n = len(a)
        if r < 0 or r > n:
            return
        if r == 0:
            yield ()
            return
        lim = 1 << n
        s = (1 << r) - 1
        while s < lim:
            yield tuple(a[i] for i in range(n) if s >> i & 1)
            s = self.__nxt_cmb(s)

    def __init__(
        self,
    ) -> NoReturn:
        fn = NextCombination()
        self.__nxt_cmb = fn
