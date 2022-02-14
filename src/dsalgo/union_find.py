"""
Graph Theory
"""

import typing


class UnionFind:
    """UnionFind DataStructure."""

    __data: typing.List[int]

    def __init__(self, size: int) -> None:
        """Initialize with size.

        Args:
            size (int): count of nodes in UnionFind Forest.
        """
        self.__data = [-1] * size

    def __len__(self) -> int:
        """Length of data.

        Returns:
            int: equal to the size of nodes.
        """
        return len(self.__data)

    def find_root(self, node: int) -> int:
        """Find root node of the component in which given node contained.

        Args:
            node (int): target node.

        Returns:
            int: root node.
        """
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        self.__data[node] = self.find_root(self.__data[node])
        return self.__data[node]

    def unite(self, node_u: int, node_v: int) -> None:
        """Unite two components.

        Args:
            node_u (int): a node.
            node_v (int): another node.

        Note:
            If node_u and node_v are contained in the same components,
            do nothing and return early.
        """
        assert 0 <= node_u < len(self) and 0 <= node_v < len(self)
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u

    def size(self, node: int) -> int:
        """Size of the component of given node.

        Args:
            node (int): an arbitrary node.

        Returns:
            int: size of the component containing the given node.
        """
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]


def get_labels(uf: UnionFind) -> typing.List[int]:
    """Get labels of nodes.

    Args:
        uf (UnionFind): an union find instance.

    Returns:
        typing.List[int]: labels.
    """
    n = len(uf)
    labels = [-1] * n
    label = 0
    for i in range(n):
        root = uf.find_root(i)
        if labels[root] == -1:
            labels[root] = label
            label += 1
        labels[i] = labels[root]
    return labels


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
