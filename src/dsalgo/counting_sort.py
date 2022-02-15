from __future__ import annotations


def counting_sort_index(arr: list[int]) -> list[int]:
    if not arr:
        return []
    mn = min(arr)
    n, buckets_size = len(arr), max(arr) - mn + 1
    count = [0] * buckets_size
    for x in arr:
        count[x - mn] += 1
    for i in range(buckets_size - 1):
        count[i + 1] += count[i]
    print(count)
    order = [0] * n
    for i in range(n - 1, -1, -1):
        count[arr[i] - mn] -= 1
        order[count[arr[i] - mn]] = i
    return order
