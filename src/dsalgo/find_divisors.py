"""
Tag
- numbe theory
- divisor
"""


import typing


def find_divisors(n: int) -> list[int]:
    r"""Find Divisors of n.

    Args:
        n (int): target.

    Returns:
        list[int]: divisors in asending order.

    Complexity:
        time: O(\sqrt{N} + C\log{C})
        space: O(C)
        where:
            C := number of divisors.
    """
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
    return sorted(divisors)
