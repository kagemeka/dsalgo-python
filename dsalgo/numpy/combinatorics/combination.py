import numpy as np


class Combinations:
    def __call__(
        self,
        n: int,
        r: int,
    ) -> np.array:
        from itertools import combinations

        a = range(n)
        c = combinations(a, r)
        return np.array((*c,))


class Permutations:
    def __call__(
        self,
        n: int,
        r: typing.Optional[int] = None,
    ) -> np.array:
        from itertools import permutations

        a = range(n)
        p = permutations(a, r)
        return np.array((*p,))
