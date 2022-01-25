import unittest

from dsalgo.number_theory.prime_number.least_prime_factor import (
    least_prime_factor,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            least_prime_factor(50)[1:],
            [
                1,
                2,
                3,
                2,
                5,
                2,
                7,
                2,
                3,
                2,
                11,
                2,
                13,
                2,
                3,
                2,
                17,
                2,
                19,
                2,
                3,
                2,
                23,
                2,
                5,
                2,
                3,
                2,
                29,
                2,
                31,
                2,
                3,
                2,
                5,
                2,
                37,
                2,
                3,
                2,
                41,
                2,
                43,
                2,
                3,
                2,
                47,
                2,
                7,
            ],
        )


if __name__ == "__main__":
    unittest.main()
