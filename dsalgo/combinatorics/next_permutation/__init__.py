import typing


class NextPermutation:
    def __call__(self, a: list[int]) -> NoReturn:
        n = len(a)
        i = -1
        for j in range(n - 2, -1, -1):
            if a[j] >= a[j + 1]:
                continue
            i = j
            break
        if i == -1:
            for i in range(n):
                a[i] = -1
            return
        a[i + 1 :] = a[i + 1 :][::-1]
        for j in range(i + 1, n):
            if a[i] >= a[j]:
                continue
            a[i], a[j] = a[j], a[i]
            break
