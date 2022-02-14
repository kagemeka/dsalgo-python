import typing

from dsalgo.descrete.compress_array import compress_array


def suffix_array_doubling_countsort(arr: typing.List[int]) -> typing.List[int]:
    n = len(arr)

    def counting_sort_key(arr: typing.List[int]) -> typing.List[int]:
        cnt = [0] * (n + 2)
        for x in arr:
            cnt[x + 1] += 1
        for i in range(n):
            cnt[i + 1] += cnt[i]
        key = [0] * n
        for i in range(n):
            key[cnt[arr[i]]] = i
            cnt[arr[i]] += 1
        return key

    (rank, _), k = compress_array(arr), 1
    while True:
        second = [0] * n
        for i in range(n - k):
            second[i] = 1 + rank[i + k]
        rank_second = counting_sort_key(second)
        first = [rank[i] for i in rank_second]
        rank_first = counting_sort_key(first)
        sa = [rank_second[i] for i in rank_first]
        key = [first[i] << 30 | second[j] for i, j in zip(rank_first, sa)]
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[i + 1] > key[i])
        k <<= 1
        if k >= n:
            break
    return sa
