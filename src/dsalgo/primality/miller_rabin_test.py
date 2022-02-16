import unittest

from dsalgo.number_theory.prime_number.primality.miller_rabin import (
    miller_rabin_test,
    miller_rabin_test_32,
    miller_rabin_test_64,
    miller_rabin_test_64_v2,
)


class Test(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
