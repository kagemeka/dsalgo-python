from \
    kgmk.dsa.algebra.modular \
    .matrix.np \
    import (
        ModMatrix,
    )
import numpy as np


def test():
    mod = 10 ** 9 + 7
    a = np.arange(1, 10).reshape(
        3, 3
    )
    print(a.dtype)
    fn = ModMatrix(mod)
    a = fn.pow(a, 10000)
    print(a)


if __name__ == '__main__':
    test()
