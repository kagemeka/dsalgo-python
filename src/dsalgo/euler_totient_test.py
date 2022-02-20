import unittest

from dsalgo.number_theory.euler_totient.euler_totient import euler_totient


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(euler_totient(100), 40)


if __name__ == "__main__":
    unittest.main()
