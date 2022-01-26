from dsalgo.number_theory.equation.extended_euclidean import (
    extended_euclidean_recurse,
)


def invert_extended_euclidean(mod: int, n: int) -> int:
    r"""Modular Inverse with extended eucledian GCD algorithm.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Constraints:
        - mod and n are coprime, in other words, gcd(mod, n) must be 1.


    Algorithm Summary:
        definition of modular inver of n
        x := inverse of n.
        nx \equiv 1 \mod m
        nx - 1 = qm (q is arbitral)
        nx - qm = 1
        y := -q
        nx + my = 1 (Bezout identity)
        this equation can be solved by extendex euclidean algorithm.
    """
    assert mod > 1
    gcd, x, _ = extended_euclidean_recurse(n % mod, mod)
    assert gcd == 1
    return x % mod


def invert_extended_euclidean_direct(mod: int, n: int) -> int:
    """Compute Modular inverse directly with Extended Euclidean Algorithm.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Algorithm Summary:
        consider for the equation nx + my = 1.
        y is not needed to be computed.
        s_k := q_kx_k + y_k
        t_k := x_k
        x_{k-1} := s_k
        y_{k-1} := t_k
        y_k = s_k - q_kt_k = x_{k-1} - q_ky_{k-1} = x_{k-1} - q_kx_k
        x_k = t_k = y_{k-1} = x_{k-2} - q_{k-1}x_{k-1} = ...
        (x_0 := 1, x_1 := y_0 = 0, y is not appeared.)

        (x_{i+1}, x_i)^T = [
            [-q_i, 1],
            [1, 0],
        ](x_i, x_{i-1})^T

        (x_1, x_0)^T = (y_0, x_0)^T = (0, 1)^T

        it's only enough to save only second row data.

        transition of (A_10, A_11).
        (0, 1) identity -> (-q_k, 1) -> (-q_k(-q_{k-1}) + 1, -q_k)
    """
    assert mod > 1
    a, b = n % mod, mod
    x10, x11 = 0, 1
    while b:
        q, r = divmod(a, b)
        x10, x11 = -q * x10 + x11, x10
        a, b = b, r
    assert a == 1
    return x11 % mod


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
