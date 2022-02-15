import unittest


class TestLCM(unittest.TestCase):
    def test_lcm(self) -> None:
        self.assertEqual(least_common_multiple(0, 0), 0)
        self.assertEqual(least_common_multiple(0, 10), 0)
        self.assertEqual(least_common_multiple(10, 0), 0)
        self.assertEqual(least_common_multiple(9, 6), 18)


class TestGCD(unittest.Unittest):
    def test_gcd(self) -> None:
        self.assertEqual(greatest_common_divisor(5, 7), 1)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(4, 0), 4)
        self.assertEqual(
            greatest_common_divisor(4, 0), greatest_common_divisor(0, 4)
        )
        self.assertEqual(greatest_common_divisor(9, 6), 3)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_array_gcd(self) -> None:
        self.assertEqual(
            array_gcd([15, 35, 21]),
            1,
        )


class TestExtendedEuclidean(unittest.TestCase):
    def test_recurse(self) -> None:
        self.assertEqual(
            extended_euclidean_recurse(111, 30),
            (3, 3, -11),
        )

    def test(self) -> None:
        self.assertEqual(
            extended_euclidean(111, 30),
            (3, 3, -11),
        )
