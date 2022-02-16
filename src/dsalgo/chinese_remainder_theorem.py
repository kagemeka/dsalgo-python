
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
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, x, _ = extended_euclidean_recurse(mod_0, mod_1)
    assert gcd == 1
    lcm = mod_0 * mod_1
    return (rem_0 + x * (rem_1 - rem_0) * mod_0) % lcm


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
