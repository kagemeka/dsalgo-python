import unittest

from dsalgo.number_theory.prime_number.primality.sieve_of_eratosthenes import (
    sieve_of_eratosthenes,
)


class TestSieveOfEratosThenes(unittest.TestCase):
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



from dsalgo.number_theory.prime_number.primality.miller_rabin import (
    miller_rabin_test,
    miller_rabin_test_32,
    miller_rabin_test_64,
    miller_rabin_test_64_v2,
)


class TestMillerRabin(unittest.TestCase):
    def test(self) -> None:
        for _ in range(100):
            self.assertFalse(miller_rabin_test(561))
            self.assertFalse(miller_rabin_test(512461))

    def test_32(self) -> None:
        self.assertFalse(miller_rabin_test_32(561))
        self.assertFalse(miller_rabin_test_32(512461))

    def test_64(self) -> None:
        self.assertFalse(miller_rabin_test_64(561))
        self.assertFalse(miller_rabin_test_64(512461))

    def test_64_v2(self) -> None:
        self.assertFalse(miller_rabin_test_64_v2(561))
        self.assertFalse(miller_rabin_test_64_v2(512461))


class TestFermat(unittest.TestCase):
    def test(self) -> None:
        for _ in range(100):
            self.assertTrue(fermat_test(998244353))
            self.assertFalse(fermat_test(561, check_times=100))
            self.assertFalse(fermat_test(512461, check_times=200))





if __name__ == "__main__":
    unittest.main()
