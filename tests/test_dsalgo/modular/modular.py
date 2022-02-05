"""TODO
pip install -e .[dsa]
"""

from kgmk.dsa.algebra.modular.factorial import ModFactorial
from kgmk.dsa.algebra.modular.mod_factory import ModFactory


def test():
    mod = 10**9 + 7
    Mint = ModFactory()(mod)
    # mint = ModFactory(mod)
    a = Mint(-1)
    print(a)
    b = Mint(-3)
    a += b
    print(a)
    c = 1
    c += a
    print(c)
    c -= a
    print(c)
    d = 1 - a
    print(d)
    e = d
    e += 1
    print(e, d)
    print(Mint(2) ** -1)
    print(2**b)

    fn = ModFactorial(mod)
    # fact = fn(1 << 20)
    inv = fn.inv(1 << 21)


if __name__ == "__main__":
    test()
