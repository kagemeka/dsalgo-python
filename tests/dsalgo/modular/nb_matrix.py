import numpy as np
from \
    kgmk.dsa.algebra.modular \
    .matrix.jit \
    import (
        mdot,
        matpow,
    )


def test():
    mod = 10 ** 9 + 7
    a = np.arange(
        1,
        10001,
    ).reshape((100, 100))
    a = matpow(a, 1 << 8, mod)
    print(a)
    a = matpow(a, 0, mod)
    print(a)


if __name__ == '__main__':
    test()
