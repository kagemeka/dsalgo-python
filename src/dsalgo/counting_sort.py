from __future__ import annotations


def counting_sort_index(arr: list[int]) -> list[int]:
    if not arr:
        return []
    mn = min(arr)
    arr = [x - mn for x in arr]
    n, buckets_size = len(arr), max(arr) + 1
    count = [0] * buckets_size
    for x in arr:
        count[x] += 1
    for i in range(buckets_size - 1):
        count[i + 1] += count[i]
    order = [0] * n
    for i in range(n - 1, -1, -1):
        count[arr[i]] -= 1
        order[count[arr[i]]] = i
    return order


def counting_sort(arr: list[int]) -> list[int]:
    return [arr[i] for i in counting_sort_index(arr)]
