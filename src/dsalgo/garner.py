"""
Number Theory
Equation
"""


import typing

from dsalgo.algebra.modular.multiplicative_inverse.extended_euclidean import (
    invert_extended_euclidean_direct,
)


def garner_form(
    mod_rem_pairs: list[tuple[int, int]],
) -> typing.Optional[int]:
    # x_0 = r_0
    # x_1 = x_0 + t_0m_0 \equiv r_1 (\mod m_1)
    # x_2 = x_1 + t_1m_0m_1 \equiv r_2 (\mod m_2)
    # ...
    # x_k = x_{k-1} + t_{k-1}\prod_{i=0}^{k-1}m_i \equiv r_k (\mod m_k)
    mod_rem_pairs = [pair for pair in mod_rem_pairs if pair != (1, 0)]
    assert len(mod_rem_pairs) >= 1
    x = 0
    mod_prod = 1
    for mod, rem in mod_rem_pairs:
        inv = invert_extended_euclidean_direct(mod, mod_prod)
        if inv is None:
            return None
        coeff = (rem - x) * inv % mod
        x += coeff * mod_prod
        mod_prod *= mod
        assert 0 <= x < mod_prod
    return x


def garner_form_mod(
    mod: int,
    mod_rem_pairs: list[tuple[int, int]],
) -> typing.Optional[int]:
    mod_rem_pairs = [pair for pair in mod_rem_pairs if pair != (1, 0)]
    n = len(mod_rem_pairs)
    assert n >= 1
    modulos = [mod for mod, _ in mod_rem_pairs] + [mod]
    mod_values = [0] * (n + 1)  # mod_values[i] = x_i \mod modulos[i]
    mod_prod = [1] * (n + 1)
    # mod_prod[i] = (\prod_{j=0}^{j=i-1} modulos[j]) \mod modulos[i]
    for i, (mod, rem) in enumerate(mod_rem_pairs):
        inv = invert_extended_euclidean_direct(mod, mod_prod[i])
        if inv is None:
            return None
        t = (rem - mod_values[i]) * inv % mod
        for j in range(i + 1, n + 1):
            mod_values[j] = (mod_values[j] + t * mod_prod[j]) % modulos[j]
            mod_prod[j] = mod_prod[j] * mod % modulos[j]
    return mod_values[-1]

