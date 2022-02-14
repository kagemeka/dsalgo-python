"""
Combinatorics
"""


def next_combination(s: int) -> int:
    lsb = s & -s
    i = s + lsb
    return (s & ~i) // lsb >> 1 | i
