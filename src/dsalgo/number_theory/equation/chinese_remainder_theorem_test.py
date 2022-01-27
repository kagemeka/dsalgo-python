import unittest

from dsalgo.number_theory.equation.chinese_remainder_theorem import (
    crt,
    crt_2,
    crt_2_coprime,
    safe_crt_2,
)


class Test(unittest.TestCase):
    def test_2_coprime(self) -> None:
        result = crt_2_coprime(15, 2, 17, 8)
        assert result is not None
        mod, x = result
        self.assertEqual(x % 15, 2)
        self.assertEqual(x % 17, 8)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 15 * 17)
        self.assertEqual(x, 212)

    def test_2(self) -> None:
        result = crt_2(10, 3, 14, 7)
        assert result is not None
        mod, x = result
        self.assertIsNotNone(x)
        self.assertEqual(x % 10, 3)
        self.assertEqual(x % 14, 7)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 10 // 2 * 14)
        self.assertEqual(x, 63)

        self.assertIsNone(crt_2(10, 3, 14, 6))

        self.assertEqual(
            crt_2(15, 2, 17, 8),
            (255, 212),
        )

    def test_general(self) -> None:
        pairs = [
            (15, 2),
            (17, 8),
        ]
        self.assertEqual(
            crt(pairs),
            (255, 212),
        )

        pairs = [
            (10, 3),
            (14, 6),
        ]
        self.assertIsNone(crt(pairs))

    def test_safe_2(self) -> None:
        result = safe_crt_2(10, 3, 14, 7)
        assert result is not None
        mod, x = result
        self.assertIsNotNone(x)
        self.assertEqual(x % 10, 3)
        self.assertEqual(x % 14, 7)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 10 // 2 * 14)
        self.assertEqual(x, 63)

        self.assertIsNone(safe_crt_2(10, 3, 14, 6))

        self.assertEqual(
            safe_crt_2(15, 2, 17, 8),
            (255, 212),
        )


if __name__ == "__main__":
    unittest.main()
