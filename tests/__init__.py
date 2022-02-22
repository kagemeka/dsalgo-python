import numba

import dsalgo.bitset

bit_length = numba.njit(dsalgo.bitset.bit_length)
# @numba.njit
# def bit_length(n: int) -> int:
#     return dsalgo.bitset


print(bit_length(5))
