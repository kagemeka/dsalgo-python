from dsalgo.algebra.modular.multiplicative_inverse import invert_fermat


def add(mod: int, lhs: int, rhs: int) -> int:
    res = lhs + rhs
    if res >= mod:
        res -= mod
    return res


def neg(mod: int, x: int) -> int:
    return mod - x


def subtract(mod: int, lhs: int, rhs: int) -> int:
    return add(mod, lhs, neg(mod, rhs))


def multiply(mod: int, lhs: int, rhs: int) -> int:
    return lhs * rhs % mod


def divide(p: int, lhs: int, rhs: int) -> int:
    return multiply(p, lhs, invert_fermat(p, rhs))


ADD_IDENTITY = 0
MUL_IDENTITY = 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
