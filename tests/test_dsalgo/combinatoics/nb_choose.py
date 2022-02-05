import numba as nb
import numpy as np
from kgmk.dsa.algebra.modular.factorial.jit import factorial, inv_factorial


@nb.njit
def choose(
    n: int,
    r: int,
) -> int:
    global mod, fact, ifact
    ok = (0 <= r) & (r <= n)
    c = fact[n] * ok
    c = c * ifact[n - r] % mod
    return c * ifact[r] % mod


def test():
    global mod
    mod = 10**9 + 7
    n = 1 << 20
    global fact, ifact
    fact = factorial(n, mod)
    ifact = inv_factorial(n, mod)

    c = choose
    assert c(40, 20) == 846527861
    for i in range(100):
        c(np.arange(1 << 20), 3)


if __name__ == "__main__":
    test()
