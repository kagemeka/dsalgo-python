import unittest

from dsalgo.algebra.modular.multiplicative_inverse.extended_euclidean import (
    invert_extended_euclidean,
    invert_extended_euclidean_direct,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        mod = 17
        x = invert_extended_euclidean(mod, 15)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, mod)
        self.assertEqual(15 * x % mod, 1)
        self.assertEqual(x, 8)

    def test_direct(self) -> None:
        mod = 17
        x = invert_extended_euclidean_direct(mod, 15)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, mod)
        self.assertEqual(15 * x % mod, 1)
        self.assertEqual(x, 8)


if __name__ == "__main__":
    unittest.main()
