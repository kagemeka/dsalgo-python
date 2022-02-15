"""
Number Theory
Equation
"""

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
) -> int:
    r"""Chinese Remainder Theorem for coprime values.

    Args:
        mod_0 (int): modulo 0
        rem_0 (int): remainder 0
        mod_1 (int): modulo 1
        rem_1 (int): remainder 1

    Returns:
        tuple[int, int]: lcm = mod_0mod_1, x
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
    return (rem_0 + x * (rem_1 - rem_0) * mod_0) % lcm


# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# https://manabitimes.jp/math/838
def crt_2(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Optional[int]:
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, x, _ = extended_euclidean_recurse(mod_0, mod_1)
    if (rem_1 - rem_0) % gcd:
        return None
    lcm = mod_0 // gcd * mod_1
    s = (rem_1 - rem_0) // gcd
    return (rem_0 + x * s * mod_0) % lcm


def crt(
    mod_rem_pairs: list[tuple[int, int]],
) -> typing.Optional[int]:
    mod_rem_pairs = [pair for pair in mod_rem_pairs if pair != (1, 0)]
    assert len(mod_rem_pairs) >= 1
    mod, rem = mod_rem_pairs[0]
    assert 0 <= rem < mod > 1
    for m, r in mod_rem_pairs[1:]:
        assert 0 <= r < m > 1
        result = crt_2(mod, rem, m, r)
        if result is None:
            return None
        rem = result
        mod = least_common_multiple(mod, m)
        assert 0 <= rem < mod
    return rem


def safe_crt_2(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Optional[int]:
    r"""Compute CRT without overflow unless lcm(mod_0, mod_1) overflows.

    avoid overflow unless lcm(mod_0, mod_1) overflow.

    Args:
        mod_0 (int): modulo 0
        rem_0 (int): remainder 0
        mod_1 (int): modulo 1
        rem_1 (int): remainder 1

    Returns:
        typing.Optional[tuple[int, int]]:
            return (lcm = mod_0mod_1, x)
            where:
                x \equiv rem_0 \mod mod_0
                x \equiv rem_1 \mod mod_1
            if x does not exist, return None.

    Algorithm Summary:

        x := rem_0 + p * mod_0
        x \equiv rem_0 \mod mod_0
        let the answer x = r.
        r := rem_0 + x * mod_0 and compute x.
        m := lcm(mod_0, mod_1)
        because 0 <= r < m and r >= max(rem_0, rem_1),
        0 <= x < (m - rem_0) / mod_0 <= m / mod_0.

        because x \equiv rem_1 \mod mod_1,
        r = rem_0 + x * mod_0 \equiv rem_1 \mod mod_1
        <-> x * mod_0 \equiv rem_1 - rem_0 \mod mod_1

        g := gcd(mod_0, mod_1)
        mod_0 := g * u0
        mod_1 := g * u1

        if x exist, rem_1 \equiv rem_0 \mod g.
        thus x * g * u0 \equiv g * (rem_1 - rem_0) / g \mod (g * u1)
        <-> x * u0 \equiv (rem_1 - rem_0) / g \mod u1
        <-> x \equiv (rem_1 - rem_0) / g * u0^{-1} \mod u1

        finally, it's only enough to compute u0^{-1} \mod u1 without overflow.
    """
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, inv_u0 = extended_euclidean_mod(mod_1, mod_0)
    if (rem_1 - rem_0) % gcd:
        return None
    u1 = mod_1 // gcd
    x = ((rem_1 - rem_0) // gcd) % u1 * inv_u0 % u1
    value = rem_0 + x * mod_0
    assert max(rem_0, rem_1) <= value < mod_0 * u1
    return value


def safe_crt(
    mod_rem_pairs: list[tuple[int, int]],
) -> typing.Optional[int]:
    mod_rem_pairs = [pair for pair in mod_rem_pairs if pair != (1, 0)]
    assert len(mod_rem_pairs) >= 1
    mod, rem = mod_rem_pairs[0]
    assert 0 <= rem < mod > 1
    for m, r in mod_rem_pairs[1:]:
        assert 0 <= r < m > 1
        result = safe_crt_2(mod, rem, m, r)
        if result is None:
            return None
        rem = result
        mod = least_common_multiple(mod, m)
        assert 0 <= rem < mod
    return rem
