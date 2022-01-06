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
