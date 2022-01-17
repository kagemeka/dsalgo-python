"""TODO
- disjoint sparse table 
- 2d sparse table
"""


import typing

from dsalgo.algebra.abstract.structure import Semigroup 
from dsalgo.algebra.bit import bit_length_table

S = typing.TypeVar("S")


class SparseTable:
    def __init__(self, sg: Semigroup[S], a: list[S]) -> None:
        # sg operation must be idempotent.
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


        
# pub struct SparseTable<'a, S> {
#     sg: Semigroup<'a, S>,
#     data: Vec<Vec<S>>, 
# }


# impl<'a, S: Default + Clone> SparseTable<'a, S> {
#     /// O(N\log{N})
#     pub fn new(sg: Semigroup<'a, S>, a: &Vec<S>) -> Self {
#         assert!(sg.idempotent && sg.commutative);
#         let n = a.len();
#         assert!(n > 0);
#         let k = std::cmp::max(1, bit_length(n - 1));
#         let mut data = vec![vec![S::default(); n]; k];
#         data[0] = a.clone();
#         for i in 0..k - 1 {
#             data[i + 1] = data[i].clone();
#             for j in 0..n - (1 << i) {
#                 data[i + 1][j] = (sg.op)(&data[i][j], &data[i][j + (1 << i)])
#             }
#         }   
#         Self { sg: sg, data: data }     
#     }

#     /// O(1)
#     pub fn get(&self, l: usize, r: usize) -> S {
#         assert!(l < r && r <= self.data[0].len());
#         let k = bit_length(r - l) - 1;
#         (self.sg.op)(&self.data[k][l], &self.data[k][r - (1 << k)])
#     }
# }





def disjoint_sparse_table(
    semigroup: Semigroup[S],
    arr: typing.List[S],
) -> typing.Callable[[int, int], S]:
    n = len(arr)
    assert n > 0
    bit_length = bit_length_table(n << 1)
    k = max(1, bit_length[n - 1])
    data: typing.List[typing.List[S]] = [[] for _ in range(k)]
    data[0] = arr.copy()
    for i in range(1, k):
        data[i] = arr.copy()
        for j in range(1 << i, n + 1, 2 << i):
            for k in range(1, 1 << i):
                data[i][j - k - 1] = semigroup.op(
                    data[i][j - k - 1],
                    data[i][j - k],
                )
            for k in range((1 << i) - 1):
                if j + k + 1 >= n:
                    break
                data[i][j + k + 1] = semigroup.op(
                    data[i][j + k],
                    data[i][j + k + 1],
                )
    
    def get(left: int, right: int) -> S:
        assert 0 <= left < right <= n
        if right - left == 1:
            return data[0][left]
        right -= 1
        k = bit_length[left ^ right] - 1
        return semigroup.op(data[k][left], data[k][right])
    
    return get


a = list(range(9))
sg = Semigroup[int](
    op=lambda x, y: x + y,
)
get = disjoint_sparse_table(sg, a)
print(get(3, 9))
