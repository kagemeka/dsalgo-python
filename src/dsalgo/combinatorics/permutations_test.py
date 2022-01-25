import unittest

from dsalgo.combinatorics.permutations import (
    permutations,
    permutations_dfs,
    permutations_next_perm,
)

ANSWER_4_2 = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 2),
    (1, 3),
    (2, 0),
    (2, 1),
    (2, 3),
    (3, 0),
    (3, 1),
    (3, 2),
]

ANSWER_3 = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            list(permutations(4, 2)),
            ANSWER_4_2,
        )
        self.assertEqual(
            list(permutations(3)),
            ANSWER_3,
        )

    def test_dfs(self) -> None:
        self.assertEqual(
            sorted(list(permutations_dfs(4, 2))),
            ANSWER_4_2,
        )
        self.assertEqual(
            sorted(list(permutations_dfs(3))),
            ANSWER_3,
        )

    def test_next_perm(self) -> None:
        self.assertEqual(
            list(permutations_next_perm(3)),
            ANSWER_3,
        )


if __name__ == "__main__":
    unittest.main()
