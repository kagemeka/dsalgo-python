import typing

from dsalgo.number_theory.equation.extended_euclidean import (
    extended_euclidean_recurse,
)
from dsalgo.number_theory.euclidean.least_common_multiple import (
    least_common_multiple,
)


def chinese_remainder_theorem_coprime(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> int:
    r"""Chinese Remainder Theorem for coprime values.

    Args:
        mod_0 (int): modulo 0
        rem_0 (int): remainder 0
        mod_1 (int): modulo 1
        rem_1 (int): remainder 1

    Returns:
        int: x
            where:
                x \equiv rem_0 \mod mod_0
                x \equiv rem_1 \mod mod_1

    Constraints:
    - mod_0 and mod_1 should bu coprime.

    Algorithm Summary:
        compute x satisfying
            - x \equiv rem_0 \mod mod_0
            - x \equiv rem_1 \mod mod_1
            - 0 <= x < mod_0mod_1

        because mod_0 and mod_1 are coprime,
        there is a solution for the equation below.
        mod_0p + mod_1q = \gcd(mod_0, mod_1) = 1
        (Bezout's identity)

        mod_0p \equiv 1 \mod mod_1
        mod_1q \equiv 1 \mod mod_0

        here, let
        x := rem_1mod_0p + rem_0mod_1q
        this satisfies,
        x \equiv rem_0 \mod_0
        x \equiv rem_1 \mod_1

        if not 0 <= x < mod_0mod_1, let x := x \mod mod_0mod_1

    """
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, x, _ = extended_euclidean_recurse(mod_0, mod_1)
    assert gcd == 1
    lcm = mod_0 * mod_1
    return (rem_0 + (rem_1 - rem_0) * mod_0 * x) % lcm


# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# https://manabitimes.jp/math/838
def chinese_remainder_theorem(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Optional[int]:
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, x, _ = extended_euclidean_recurse(mod_0, mod_1)
    if (rem_0 - rem_1) % gcd:
        return None
    lcm = mod_0 // gcd * mod_1
    return (rem_0 - (rem_0 - rem_1) // gcd * mod_0 * x) % lcm


def general_crt_coprime(
    mod_rem_pairs: typing.List[typing.Tuple[int, int]],
) -> int:
    assert len(mod_rem_pairs) >= 1
    mod, rem = mod_rem_pairs[0]
    for m, r in mod_rem_pairs[1:]:
        assert 0 <= r < m > 1
        rem = chinese_remainder_theorem_coprime(mod, rem, m, r)
        mod *= m
    return rem


def general_crt(
    mod_rem_pairs: typing.List[typing.Tuple[int, int]],
) -> typing.Optional[int]:
    assert len(mod_rem_pairs) >= 1
    mod, rem = mod_rem_pairs[0]
    for m, r in mod_rem_pairs[1:]:
        assert 0 <= r < m > 1
        result = chinese_remainder_theorem(mod, rem, m, r)
        if result is None:
            return None
        rem = result
        mod = least_common_multiple(mod, m)
    return rem
