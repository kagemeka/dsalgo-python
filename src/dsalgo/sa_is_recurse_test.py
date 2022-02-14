import typing
import unittest

import pytest

from dsalgo.string.suffix_array.sa_is_recurse import sa_is_recurse

TEST_DATA_STRING = [
    (
        "mmiissiissiippii",
        [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4],
    ),
    (
        "mississippi",
        [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2],
    ),
]

TEST_DATA = [
    (
        [1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0],
        [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4],
    ),
    (
        [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0],
        [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2],
    ),
]


@pytest.mark.parametrize(("word", "suffix_array"), TEST_DATA_STRING)
def test(word: str, suffix_array: typing.List[int]) -> None:
    arr = [ord(c) for c in word]
    assert sa_is_recurse(arr) == suffix_array


class Test(unittest.TestCase):
    def test(self) -> None:
        arr = [1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0]
        sa = [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4]
        self.assertEqual(sa_is_recurse(arr), sa)
        arr = [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0]
        sa = [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
        self.assertEqual(sa_is_recurse(arr), sa)


if __name__ == "__main__":
    unittest.main()
