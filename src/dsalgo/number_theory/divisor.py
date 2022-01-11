"""TODO
Implement
    - search highly composite numbers
"""


import typing


def find_divisors(n: int) -> list[int]:
    divs = []
    i = 0
    while True:
        i += 1
        if i * i >= n:
            break
        if n % i:
            continue
        divs.append(i)
        divs.append(n // i)
    if i * i == n:
        divs.append(i)
    return sorted(divs)


def count_divisors(n: int) -> list[int]:
    cnt = [1] * n
    cnt[0] = 0
    for i in range(2, n):
        for j in range(i, n, i):
            cnt[j] += 1
    return cnt


import unittest


def test_find_divisors() -> typing.NoReturn:
    assert 1 == 1


class Test(unittest.TestCase):
    def test_find_divisors(self) -> typing.NoReturn:
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
