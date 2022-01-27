import typing

from dsalgo.number_theory.equation._extended_euclidean_mod import (
    extended_euclidean_mod,
)
from dsalgo.number_theory.equation.extended_euclidean import (
    extended_euclidean_recurse,
)
from dsalgo.number_theory.euclidean.least_common_multiple import (
    least_common_multiple,
)


def crt_2_coprime(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Tuple[int, int]:
    r"""Chinese Remainder Theorem for coprime values.

    Args:
        mod_0 (int): modulo 0
        rem_0 (int): remainder 0
        mod_1 (int): modulo 1
        rem_1 (int): remainder 1

    Returns:
        typing.Tuple[int, int]: lcm = mod_0mod_1, x
            where:
                x \equiv rem_0 \mod mod_0
                x \equiv rem_1 \mod mod_1

    Constraints:
    - mod_0 and mod_1 should be coprime.

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
    return lcm, (rem_0 + x * (rem_1 - rem_0) * mod_0) % lcm


# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# https://manabitimes.jp/math/838
def crt_2(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Optional[typing.Tuple[int, int]]:
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, x, _ = extended_euclidean_recurse(mod_0, mod_1)
    if (rem_1 - rem_0) % gcd:
        return None
    lcm = mod_0 // gcd * mod_1
    s = (rem_1 - rem_0) // gcd
    return lcm, (rem_0 + x * s * mod_0) % lcm


def crt(
    mod_rem_pairs: typing.List[typing.Tuple[int, int]],
) -> typing.Optional[typing.Tuple[int, int]]:
    assert len(mod_rem_pairs) >= 1
    mod, rem = mod_rem_pairs[0]
    for m, r in mod_rem_pairs[1:]:
        assert 0 <= r < m > 1
        result = crt_2(mod, rem, m, r)
        if result is None:
            return None
        mod, rem = result
    return mod, rem


def safe_crt_2(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Optional[typing.Tuple[int, int]]:
    r"""Compute CRT without overflow unless lcm(mod_0, mod_1) overflows.

    avoid overflow unless lcm(mod_0, mod_1) overflow.

    Args:
        mod_0 (int): modulo 0
        rem_0 (int): remainder 0
        mod_1 (int): modulo 1
        rem_1 (int): remainder 1

    Returns:
        typing.Optional[int]: [description]

    Algorithm Summary:

        x := rem_0 + p * mod_0
        x \equiv rem_0 \mod mod_0

    """
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, inv_u0 = extended_euclidean_mod(mod_1, mod_0)
    if (rem_1 - rem_0) % gcd:
        return None
    u1 = mod_1 // gcd
    x = ((rem_1 - rem_0) // gcd) % u1 * inv_u0 % u1
    return mod_0 * u1, rem_0 + x * mod_0
