from __future__ import annotations

import dataclasses
import typing


@dataclasses.dataclass
class Node:
    ...


@dataclasses.dataclass
class Edge:
    from_: int
    to: int
    weight: typing.Optional[int] = (None,)
    capacity: typing.Optional[int] = None


@dataclasses.dataclass
class Graph:
    nodes: list[Node]
    edges: list[list[Edge]]

    @classmethod
    def from_size(
        cls,
        n: int,
    ) -> Graph:
        nodes = [Node() for _ in range(n)]
        edges = [[] for _ in range(n)]
        return cls(nodes, edges)

    def add_edge(
        self,
        e: Edge,
    ) -> NoReturn:
        self.edges[e.from_].append(e)

    def add_edges(
        self,
        edges: list[Edge],
    ) -> NoReturn:
        for e in edges:
            self.add_edge(e)

    @property
    def size(self) -> int:
        return len(self.nodes)
