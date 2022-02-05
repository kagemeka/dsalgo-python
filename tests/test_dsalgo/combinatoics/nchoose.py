from kgmk.dsa.combinatorics.nchoose import NChoose


def test():
    mod = 10**9 + 7
    n = 1 << 30
    r = 1 << 20
    c = NChoose(n, r, mod)
    t = n * (n - 1) // 2 % mod
    assert c[2] == t
    print(len(c))


if __name__ == "__main__":
    test()
