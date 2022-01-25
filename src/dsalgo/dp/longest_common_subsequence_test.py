import unittest

from dsalgo.dp.longet_common_subsequence import longest_common_subsequence


class Test(unittest.TestCase):
    def test(self) -> None:
        s = "algorithm"
        t = "datastructure"
        self.assertEqual(
            longest_common_subsequence(s, t),
            ["a", "r", "t"],
        )


if __name__ == "__main__":
    unittest.main()
