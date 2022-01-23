import typing


def sa_is_recurse(arr: typing.List[int]) -> typing.List[int]:
    mn = min(arr)
    arr = [x - mn + 1 for x in arr]
    arr.append(0)
    n = len(arr)
    m = max(arr) + 1
    is_s = [True] * n
    for i in range(n - 2, -1, -1):
        is_s[i] = is_s[i + 1] if arr[i] == arr[i + 1] else arr[i] < arr[i + 1]
    is_lms = [not is_s[i - 1] and is_s[i] for i in range(n)]
    lms = [i for i in range(n) if is_lms[i]]
    bucket = [0] * m
    for x in arr:
        bucket[x] += 1

    def induce(lms: typing.List[int]) -> typing.List[int]:
        nonlocal n, arr, m, bucket, is_s
        sa = [-1] * n
        sa_idx = bucket.copy()
        for i in range(m - 1):
            sa_idx[i + 1] += sa_idx[i]
        for i in lms[::-1]:
            sa_idx[arr[i]] -= 1
            sa[sa_idx[arr[i]]] = i

        sa_idx = bucket.copy()
        s = 0
        for i in range(m):
            s, sa_idx[i] = s + sa_idx[i], s
        for i in range(n):
            i = sa[i] - 1
            if i < 0 or is_s[i]:
                continue
            sa[sa_idx[arr[i]]] = i
            sa_idx[arr[i]] += 1

        sa_idx = bucket.copy()
        for i in range(m - 1):
            sa_idx[i + 1] += sa_idx[i]
        for i in range(n - 1, -1, -1):
            i = sa[i] - 1
            if i < 0 or not is_s[i]:
                continue
            sa_idx[arr[i]] -= 1
            sa[sa_idx[arr[i]]] = i
        return sa

    sa = induce(lms)
    lms_idx = [i for i in sa if is_lms[i]]
    ranks = [-1] * n
    ranks[-1] = rank = 0
    for i in range(len(lms_idx) - 1):
        j, k = lms_idx[i], lms_idx[i + 1]
        for d in range(n):
            j_is_lms, k_is_lms = is_lms[j + d], is_lms[k + d]
            if arr[j + d] != arr[k + d] or j_is_lms ^ k_is_lms:
                rank += 1
                break
            if d > 0 and j_is_lms | k_is_lms:
                break
        ranks[k] = rank
    ranks = [i for i in ranks if i >= 0]
    if rank == len(lms_idx) - 1:
        lms_order = [-1] * len(lms_idx)
        for i, r in enumerate(ranks):
            lms_order[r] = i
    else:
        lms_order = sa_is_recurse(ranks)
    return induce([lms[i] for i in lms_order])[1:]
