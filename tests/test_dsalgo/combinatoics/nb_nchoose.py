from kgmk.dsa.combinatorics.nchoose.jit import nchoose


def test():
    mod = 10 ** 9 + 7
    n = 1 << 30
    r = 1 << 20
    c = nchoose(n, r, mod)
    print(c)
    print(c.size)
    t = n * (n - 1) // 2 % mod
    assert c[2] == t


if __name__ == "__main__":
    test()
