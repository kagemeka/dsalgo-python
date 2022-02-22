def z_algorithm(s):
    n = len(s)
    a = [0] * n
    a[0] = n
    l = r = -1
    for i in range(1, n):
        if r >= i:
            a[i] = min(a[i - l], r - i)
        while i + a[i] < n and s[i + a[i]] == s[a[i]]:
            a[i] += 1
        if i + a[i] >= r:
            l, r = i, i + a[i]
    return a
