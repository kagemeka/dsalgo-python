import unittest

from dsalgo.number_theory.euler_totient.euler_totient_lpf import (
    euler_totient_lpf,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        # https://primefan.tripod.com/Phi500.html
        euler_totient = euler_totient_lpf(1 << 10)
        self.assertEqual(
            euler_totient(100),
            40,
        )

        self.assertEqual(euler_totient(13), 12)


if __name__ == "__main__":
    unittest.main()
