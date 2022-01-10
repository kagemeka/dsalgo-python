import typing

import dsalgo
from dsalgo.number_theory.divisor import find_divisors


def test() -> typing.NoReturn:
    n = 100
    assert find_divisors(n) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
