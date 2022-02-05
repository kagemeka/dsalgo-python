from kgmk.dsa.algebra.modular.inverse import Inverse


def test():
    mod = 10**9 + 7
    inv = Inverse(1 << 10, mod)
    print(inv(5))
    print(pow(5, mod - 2, mod))


if __name__ == "__main__":
    test()
