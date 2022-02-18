import unittest

import dsalgo.prime_number


class TestFindPrimeNumbers(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            dsalgo.prime_number.find_prime_numbers(100),
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


class TestPrimeFactorize(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            dsalgo.prime_number.prime_factorize(105),
            [(3, 1), (5, 1), (7, 1)],
        )


class TestPrimeFactorizeLPF(unittest.TestCase):
    def test(self) -> None:
        prime_factorize = dsalgo.prime_number.prime_factorize_lpf(
            max_value=1000
        )
        self.assertEqual(
            prime_factorize(105),
            [(3, 1), (5, 1), (7, 1)],
        )
        self.assertEqual(
            prime_factorize(100),
            [(2, 2), (5, 2)],
        )


class TestLeastPrimeFactor(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            dsalgo.prime_number.least_prime_factor(50)[1:],
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


class TestCountPrimeFactors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            count_prime_factors(20),
            [0, 0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1],
        )


class TestGreatestPrimeFactor(unittest.TestCase):
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
