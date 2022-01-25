import unittest

from dsalgo.number_theory.euclidean.least_common_multiple import lcm


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(lcm(0, 0), 0)
        self.assertEqual(lcm(0, 10), 0)
        self.assertEqual(lcm(10, 0), 0)
        self.assertEqual(lcm(9, 6), 18)


if __name__ == "__main__":
    unittest.main()
