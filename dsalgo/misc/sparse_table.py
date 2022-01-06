"""TODO
- disjoint sparse table 
- 2d sparse table
"""

import typing

from kagemeka.dsa.algebra.abstract.structure import Semigroup

S = typing.TypeVar("S")


class SparseTable:
    def __init__(self, sg: Semigroup[S], a: list[S]) -> NoReturn:
        assert sg.idempotent
        n = len(a)
        bit_len = bit_length_table(n + 1)
        k = bit_len[n]
        table = [[-1] * n for _ in range(k)]
        table[0] = a.copy()
        for i in range(k - 1):
            table[i + 1] = table[i].copy()
            for j in range(n - (1 << i)):
                table[i + 1][j] = sg.op(table[i][j], table[i][j + (1 << i)])
        self.__table = table
        self.__bit_len = bit_len
        self.__sg = sg

    def get(self, l: int, r: int) -> S:
        k = self.__bit_len[r - l] - 1
        t = self.__table
        return self.__sg.op(t[k][l], t[k][r - (1 << k)])
