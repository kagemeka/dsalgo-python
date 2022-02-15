"""
Counting sort
Radix sort 
"""

import typing

from dsalgo.compress_array import compress_array
from dsalgo.counting_sort import counting_sort_index


def suffix_array_doubling_countsort(arr: list[int]) -> list[int]:
    n = len(arr)

    # def counting_sort_key(arr: list[int]) -> list[int]:
    #     cnt = [0] * (n + 2)
    #     for x in arr:
    #         cnt[x + 1] += 1
    #     for i in range(n):
    #         cnt[i + 1] += cnt[i]
    #     order = [0] * n
    #     for i in range(n):
    #         order[cnt[arr[i]]] = i
    #         cnt[arr[i]] += 1
    #     return order

    (rank, _), k = compress_array(arr), 1
    while True:
        second_key = [0] * n
        for i in range(n - k):
            second_key[i] = 1 + rank[i + k]
        order_second = counting_sort_index(second_key)
        first_key = [rank[i] for i in order_second]
        order_first = counting_sort_index(first_key)
        suffix_array = [order_second[i] for i in order_first]
        key = [
            first_key[i] << 30 | second_key[j]
            for i, j in zip(order_first, suffix_array)
        ]
        rank[suffix_array[0]] = 0
        for i in range(n - 1):
            rank_delta = int(key[i + 1] > key[i])
            rank[suffix_array[i + 1]] = rank[suffix_array[i]] + rank_delta
        k <<= 1
        if k >= n:
            break
    return suffix_array


import pytest
import unittest

if __name__ == "__main__":

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
    def test(word: str, suffix_array: list[int]) -> None:
        arr = [ord(c) for c in word]
        assert suffix_array_doubling_countsort(arr) == suffix_array

    class Test(unittest.TestCase):
        def test(self) -> None:
            arr = [1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0]
            sa = [15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4]
            self.assertEqual(suffix_array_doubling_countsort(arr), sa)
            arr = [1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0]
            sa = [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
            self.assertEqual(suffix_array_doubling_countsort(arr), sa)

    unittest.main()
