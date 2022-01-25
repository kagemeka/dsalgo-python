import unittest

from dsalgo.combinatorics.repeated_permutations import (
    repeated_permutations_dfs,
)

ANSWER_4_2 = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 3),
]


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            list(repeated_permutations_dfs(4, 2)),
            ANSWER_4_2,
        )


if __name__ == "__main__":
    unittest.main()
