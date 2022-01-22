import typing


def inverse_table_naive(p: int, n: int) -> typing.List[int]:
    ...


def inverse_table(p: int, n: int) -> typing.List[int]:
    """Modular Inverse table.

    Args:
        n (int): [description]
        mod (int): [description]

    Returns:
        typing.List[int]: [description]
    """
    b, a = factorial(n, mod), factorial_inverse(n, mod)
    for i in range(n - 1):
        a[i + 1] = a[i + 1] * b[i] % mod
    return a
