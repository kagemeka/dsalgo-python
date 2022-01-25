import unittest

from dsalgo.number_theory.prime_number.greatest_prime_factor import (
    greatest_prime_factor,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            greatest_prime_factor(50)[1:],
            [
                1,
                2,
                3,
                2,
                5,
                3,
                7,
                2,
                3,
                5,
                11,
                3,
                13,
                7,
                5,
                2,
                17,
                3,
                19,
                5,
                7,
                11,
                23,
                3,
                5,
                13,
                3,
                7,
                29,
                5,
                31,
                2,
                11,
                17,
                7,
                3,
                37,
                19,
                13,
                5,
                41,
                7,
                43,
                11,
                5,
                23,
                47,
                3,
                7,
            ],
        )


if __name__ == "__main__":
    unittest.main()
