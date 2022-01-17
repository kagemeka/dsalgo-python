
import typing 
from dsalgo.graph_theory.tree_bfs import tree_bfs 


def lca_binary_lifting(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    n = len(tree_edges) + 1
    parent, depth = tree_bfs(tree_edges, root)
    k = max(1, max(depth).bit_length())
    ancestor = [[n] * n for _ in range(k)]
    ancestor[0] = parent
    ancestor[0][root] = root
    for i in range(k - 1):
        for j in range(n):
            ancestor[i + 1][j] = ancestor[i][ancestor[i][j]]
    
    def get(u: int, v: int) -> int:
        if depth[u] > depth[v]:
            u, v = v, u
        d = depth[v] - depth[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                v = ancestor[i][v]
        if v == u:
            return u
        for a in ancestor[::-1]:
            nu, nv = a[u], a[v]
            if nu != nv:
                u, v = nu, nv
        return parent[u]
    
    return get 



# /// Lowest Common Ancestor with Tarjan's offline algorithm.
# /// O(V + Q) preprocessing, O(1) per query.
# /// references
# /// - https://cp-algorithms.com/graph/lca_tarjan.html 
# /// - https://en.wikipedia.org/wiki/Tarjan%27s_off-line_lowest_common_ancestors_algorithm
# /// - https://tjkendev.github.io/procon-library/python/graph/lca-tarjan.html
# pub fn tarjan_offline(g: &Vec<(usize, usize)>, uv: &Vec<(usize, usize)>, root: usize) -> Vec<usize> {
#     fn dfs(
#         g: &Vec<Vec<usize>>, 
#         q: &Vec<Vec<(usize, usize)>>, 
#         visited: &mut Vec<bool>, 
#         uf: &mut UnionFind, 
#         ancestor: &mut Vec<usize>, 
#         lca: &mut Vec<usize>,
#         u: usize,
#     ) {
#         visited[u] = true;
#         ancestor[u] = u;
#         for &v in g[u].iter() {
#             if visited[v] { continue; }            
#             dfs(g, q, visited, uf, ancestor, lca, v);
#             uf.unite(u, v);
#             ancestor[uf.find(u)] = u;
#         }
#         for &(v, i) in q[u].iter() {
#             if visited[v] { lca[i] = ancestor[uf.find(v)]; }
#         }
#     }
#     let n = g.len() + 1;
#     let mut t = vec![vec![]; n];
#     for &(u, v) in g.iter() {
#         t[u].push(v);
#         t[v].push(u);
#     }
#     let mut q = vec![vec![]; n];
#     for (i, &(u, v)) in uv.iter().enumerate() {
#         q[u].push((v, i));
#         q[v].push((u, i));
#     }
#     let mut visited = vec![false; n];
#     let mut uf = UnionFind::new(n);
#     let mut ancestor = vec![n; n];
#     let mut lca = vec![n; uv.len()];
#     dfs(&t, &q, &mut visited, &mut uf, &mut ancestor, &mut lca, root);
#     lca
# }




# pub fn with_hl_decomposition() {}


# pub mod eulertour_rmq {

#     use super::{SparseTable, DisjointSparseTable, euler_tour_node, Semigroup};
#     use super::{SegmentTree, Monoid};


#     pub struct WithSparseTable<'a, S> {
#         first_idx: Vec<usize>,
#         sp: DisjointSparseTable<'a, S>,
#     }
#     impl<'a> WithSparseTable<'a, (usize, usize)> {
#         pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
#             let (tour, first_idx, _, _, depth) = euler_tour_node(g, root);
#             let sg = Semigroup::<'a, (usize, usize)> {
#                 op: &|x, y| std::cmp::min(*x, *y),
#                 commutative: true,
#                 idempotent: true,
#             };
#             let mut a = Vec::with_capacity(tour.len());
#             for &i in tour.iter() {
#                 a.push((depth[i as usize], i as usize));
#             }
#             let sp = DisjointSparseTable::new(sg, &a);
#             Self { first_idx: first_idx, sp: sp }
#         }

#         pub fn get(&self, u: usize, v: usize) -> usize {
#             let mut l = self.first_idx[u];
#             let mut r = self.first_idx[v];
#             if l > r { std::mem::swap(&mut l, &mut r); }
#             self.sp.get(l, r + 1).1
#         }
#     }


#     pub struct WithSegmentTree<'a, S: Copy> {
#         first_idx: Vec<usize>,
#         seg: SegmentTree<'a, S>,
#     }
#     impl<'a> WithSegmentTree<'a, (usize, usize)> {
#         pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
#             let (tour, first_idx, _, _, depth) = euler_tour_node(g, root);
#             let m = Monoid::<'a, (usize, usize)> {
#                 op: &|x, y| std::cmp::min(*x, *y),
#                 e: &|| (std::usize::MAX, 0),
#                 commutative: true,
#                 idempotent: false,
#             };
#             let mut a = Vec::with_capacity(tour.len());
#             for &i in tour.iter() {
#                 a.push((depth[i as usize], i as usize));
#             }
#             let seg = SegmentTree::from_vec(m, &a);
#             Self { first_idx: first_idx, seg: seg }
#         }

#         pub fn get(&self, u: usize, v: usize) -> usize {
#             let mut l = self.first_idx[u];
#             let mut r = self.first_idx[v];
#             if l > r { std::mem::swap(&mut l, &mut r); }
#             self.seg.get(l, r + 1).1
#         }
#     }


#     pub struct WithSqrtDecomposition {}

# }

# /// references
# /// - https://ei1333.hateblo.jp/entry/2018/05/29/011140
# /// - https://www.slideshare.net/iwiwi/2-12188845
# pub struct WithHLD {}

def lca_euler_tour_rmq(): 
    # sparse table
    ...


def lca_tarjan_offline():
    ...


def lca_hld_decomposition():
    ...
