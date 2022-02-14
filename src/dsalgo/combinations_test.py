import unittest

from dsalgo.combinatorics.combinations import (
    combinations,
    combinations_next_comb,
)

ANSWER_5_3 = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 1, 4),
    (0, 2, 3),
    (0, 2, 4),
    (0, 3, 4),
    (1, 2, 3),
    (1, 2, 4),
    (1, 3, 4),
    (2, 3, 4),
]


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            list(combinations(5, 3)),
            ANSWER_5_3,
        )

    def test_next_comb(self) -> None:
        self.assertEqual(
            sorted(list(combinations_next_comb(5, 3))),
            ANSWER_5_3,
        )


if __name__ == "__main__":
    unittest.main()
