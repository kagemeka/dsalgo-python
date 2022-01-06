from collections import deque
from typing import List

from .graph import Graph

# cut below


class GraphBFS:

    level: List[int]

    def __init__(
        self,
        graph: Graph,
    ):
        self.g = graph
        self.inf = float("inf")

    def search(
        self,
        src: int,
    ):
        self.init_level()
        self.level[src] = 0
        self.set_queue()
        que = self.queue
        que.append(src)
        while que:
            x = que.popleft()
            self.explore(x)

    def explore(
        self,
        u: int,
    ):
        g = self.g
        lv = self.level
        que = self.queue
        for e in g.edges[u]:
            v = e.to
            if lv[v] is not None:
                continue
            lv[v] = lv[u] + 1
            que.append(v)

    def set_queue(self):
        que = deque()
        self.queue = que

    def init_level(self):
        lv = [None] * self.g.size
        self.level = lv
