"""
Algebra
Polynomial
"""

import typing

import numpy as np


class ModConvolveToomCook:
    """Mod Convolve with toom cook algorithm

    this algorithm might not be correct because of dealing with floating point.
    """

    def __call__(self, f: np.ndarray, g: np.ndarray) -> np.ndarray:
        mod = self.__mod
        N: typing.Final[int] = 10
        BASE: typing.Final[int] = 1 << N
        f, f0 = np.divmod(f, BASE)
        f2, f1 = np.divmod(f, BASE)
        g, g0 = np.divmod(g, BASE)
        g2, g1 = np.divmod(g, BASE)
        h0 = self.__conv(f0, g0)
        ha = self.__conv(f1, g1)
        h4 = self.__conv(f2, g2)
        h1 = self.__conv(f0 + f1, g0 + g1) - h0 - ha
        h3 = self.__conv(f1 + f2, g1 + g2) - ha - h4
        h2 = self.__conv(f0 + f2, g0 + g2) - h0 - h4 + ha
        h = (h4 << N * 2) + (h3 << N) + h2
        h = (h % mod << N * 2) + (h1 << N) + h0
        return h % mod

    def __conv(self, f: np.ndarray, g: np.ndarray) -> np.ndarray:
        import scipy.signal

        h = scipy.signal.fftconvolve(f, g)
        return np.rint(h).astype(np.int64) % self.__mod

    def __init__(self, mod: int) -> None:
        self.__mod = mod
