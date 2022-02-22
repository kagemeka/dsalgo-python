# def __test_segment_tree() -> None:
#     n = 10
#     a = list(range(n))
#     op = lambda a, b: a + b
#     e = lambda: 0
#     monoid = Monoid(op, e, False)
#     seg = SegmentTree[int](monoid, a)

#     print(len(seg))
#     print(seg.size)
#     print(seg[5])
#     print(seg.get(0, 10))
#     seg[5] = 10
#     print(seg.get(0, 10))


# def __test_segment_tree_dfs() -> None:
#     n = 10
#     a = list(range(n))
#     op = lambda a, b: a + b
#     e = lambda: 0
#     monoid = Monoid(op, e, False)
#     seg = SegmentTreeDFS[int](monoid, a)

#     print(len(seg))
#     print(seg.size)
#     print(seg[5])
#     print(seg.get(0, 10))
#     seg[5] = 10
#     print(seg.get(0, 10))


# def __test_segtree_lazy() -> NoReturn:
#     s_op = lambda a, b: (a[0] + b[0], a[1] + b[1])
#     s_e = lambda: (0, 0)
#     ms = Monoid(s_op, s_e, False)
#     f_op = lambda f, g: f + g
#     f_e = lambda: 0
#     mf = Monoid(f_op, f_e, False)
#     map_ = lambda f, x: (x[0] + f * x[1], x[1])

#     a = [(i, 1) for i in range(10)]
#     # seg = SegmentTreeLazy(ms, mf, map_, a)
#     seg = SegmentTreeLazyDFS(ms, mf, map_, a)
#     print(seg.get(0, 10))
#     print(seg.get(0, 5))
#     print(len(seg), seg.size)
#     seg.update(5, (10, 1))
#     print(seg.get(0, 10))
#     seg.set(2, 6, 3)
#     print(seg.get(3, 10))
