from kagemeka.dsa.algebra.numeral_system import base_convert_from_ten


def lucas_theorem(p: int, n: int, k: int) -> int:
    r"""Lucas's Theorem.
    references
        - https://en.wikipedia.org/wiki/Lucas%27s_theorem
    """
    if k < 0 or n < k:
        return 0
    a = base_convert_from_ten(p, n)
    b = base_convert_from_ten(p, k)
    ...
