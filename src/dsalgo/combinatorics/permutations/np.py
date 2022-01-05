import numpy as np
import typing


class Permutations():
    def __call__(
        self,
        n: int,
        r: typing.Optional[
            int
        ] = None,
    ) -> np.array:
        from itertools import (
            permutations,
        )
        a = range(n)
        p = permutations(a, r)
        return np.array((*p, ))
