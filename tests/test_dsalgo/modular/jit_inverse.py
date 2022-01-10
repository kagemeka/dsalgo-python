from kgmk.dsa.algebra.modular.inverse.jit import inverse


def test():
    mod = 10 ** 9 + 7
    inv = inverse(1 << 20, mod)
    print(inv[:6])
    print(pow(5, mod - 2, mod))


if __name__ == "__main__":
    test()
