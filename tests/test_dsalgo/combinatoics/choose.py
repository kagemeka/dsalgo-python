from kgmk.dsa.combinatorics.choose import Choose


def test():
    mod = 10 ** 9 + 7
    c = Choose(1 << 20, mod)
    assert c(40, 20) == 846527861


if __name__ == "__main__":
    test()
