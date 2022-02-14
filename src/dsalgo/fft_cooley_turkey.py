"""

Algebra
Polynomial
fft


# Fast Fourier Transform (Cooley-Turkey algorithm)


# keywords
- butterfly
- not recursive


# references
- [furuya blog](https://www.creativ.xyz/fast-fourier-transform/)
- [wiki en](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)



# verify
- [AtCoder ATC001 C - 高速フーリエ変換](https://atcoder.jp/contests/atc001/tasks/fft_c)

"""


import cmath
import typing


class FFT:
    def __butterfly(
        self,
    ) -> None:
        n = self.__n
        a = self.__a
        b = 1
        sign = -1 + 2 * self.__inv
        while b < n:
            for j in range(b):
                w = cmath.rect(1.0, sign * cmath.pi / b * j)
                k = 0
                while k < n:
                    s, t = a[k + j], a[k + j + b] * w
                    a[k + j], a[k + j + b] = s + t, s - t
                    k += 2 * b
            b <<= 1

    def __call__(
        self,
        a: list[complex],
    ) -> list[complex]:
        n = len(a)
        h = n.bit_length() - 1
        assert 1 << h == n
        self.__a = a
        self.__n, self.__h = n, h
        self.__reverse_bits()
        self.__butterfly()
        a = self.__a
        if self.__inv:
            for i in range(n):
                a[i] /= n
        return a

    def __init__(
        self,
        inverse: bool = False,
    ) -> None:
        self.__inv = inverse

    def __reverse_bits(
        self,
    ) -> None:
        a = self.__a
        n, h = self.__n, self.__h
        idx = [-1] * n
        for i in range(n):
            j = 0
            for k in range(h):
                j |= (i >> k & 1) << (h - 1 - k)
            idx[i] = j
        self.__a = [a[i] for i in idx]
