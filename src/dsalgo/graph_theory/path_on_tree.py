import typing 

def compute_path_on_tree(
    edges: typing.List[typing.Tuple[int, int]],
    src: int,
    dst: int,
) -> typing.List[int]:
    n = len(edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    rev_path: typing.List[int] = []
    
    def dfs(u: int, parent: int) -> bool:
        if u == dst:
            rev_path.append(u)
            return True
        for v in graph[u]:
            if v == parent or not dfs(v, u):
                continue
            rev_path.append(u)
            return True
        return False
    
    dfs(src, -1)
    return rev_path[::-1]



# edges = [
#     (0, 1),
#     (0, 7),
#     (1, 2),
#     (1, 3),
#     (3, 4),
#     (5, 7),
#     (6, 7),
# ]
# src = 3
# dst = 5

# print(compute_path_on_tree(edges, src, dst))

    