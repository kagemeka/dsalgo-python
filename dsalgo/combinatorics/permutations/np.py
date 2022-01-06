import typing

import numpy as np


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
