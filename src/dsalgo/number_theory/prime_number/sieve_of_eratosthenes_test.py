import unittest

from dsalgo.number_theory.prime_number.sieve_of_eratosthenes import (
    sieve_of_eratosthenes,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            sieve_of_eratosthenes(max_value=20),
            [
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
            ],
        )


if __name__ == "__main__":
    unittest.main()
