import typing
import numba as nb
import numpy as np


@nb.njit(
    cache=True,
)
def test() -> typing.NoReturn:
    a = np.arange(10)
    print(a[:6:-1])
    print(a[:-6:-1])


if __name__ == '__main__':
    test()
