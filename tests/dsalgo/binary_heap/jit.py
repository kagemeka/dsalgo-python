from kgmk.dsa.binary_heap.jit import (
    heappush,
    heappop,
)

import typing
import numba as nb
import numpy as np


@nb.njit(
    cache=True,
)
def test() -> typing.NoReturn:
    hq = [0]
    for i in range(10, 0, -1):
        heappush(hq, i)
        print(hq)
    while hq:
        print(heappop(hq))


if __name__ == '__main__':
    test()
