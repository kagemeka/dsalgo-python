import numpy as np
from \
    kgmk.dsa.algebra.modular \
    .factorial.np \
    import (
        ModFactorial,
    )


def test():
    mod = 10 ** 9 + 7
    np.dot(1, 1)
    fn = ModFactorial(mod)
    a = fn(1 << 22)
    a = fn.inv(1 << 22)
    print(a)


if __name__ == '__main__':
    test()
