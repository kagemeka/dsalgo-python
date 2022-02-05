from kgmk.dsa.algebra.modular.factorial.jit import factorial, inv_factorial


def test():
    mod = 10**9 + 7
    a = factorial(1 << 20, mod)
    print(a[:10])
    a = inv_factorial(
        1 << 20,
        mod,
    )
    print(a[:10])


if __name__ == "__main__":
    test()
