import math
import typing

from ...next_permutation import NextPermutation

# TODO cut below


class Permutations:
    def __call__(
        self,
        n: int,
    ) -> typing.AsyncIterator[tuple[int]]:
        fn = NextPermutation()
        a = list(range(n))
        m = math.factorial(n)
        for _ in range(m):
            yield a
            a = fn(a)
