import unittest


class TestElement(unittest.TestCase):
    def test(self) -> None:
        Mint = define_static_modular_element(10**9 + 7)

        a = 0
        b = Mint(1)
        a += b
        print(a)


class TestInvertExtendedEuclidean(unittest.TestCase):
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
