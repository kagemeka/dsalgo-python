import unittest

from dsalgo.number_theory.prime_number.find_prime_numbers import (
    find_prime_numbers,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            find_prime_numbers(100),
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
        )


if __name__ == "__main__":
    unittest.main()
