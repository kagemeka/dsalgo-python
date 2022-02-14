"""
Container
"""

import typing

from dsalgo.graph_theory.tree.pivot_tree.pivot_tree_recurse import (
    Node,
    find,
    get_kth_node,
    insert,
    lower_bound,
    new_tree_root,
    remove,
    upper_bound,
)


class PivotTreeSet:
    __root: typing.Optional[Node[None]]
    __max_height: int

    def __init__(self, max_height: int) -> None:
        self.__root = None
        self.__max_height = max_height

    @property
    def max_size(self) -> int:
        return (1 << self.__max_height) - 1

    def __len__(self) -> int:
        return 0 if self.__root is None else self.__root.size

    def __contains__(self, key: int) -> bool:
        assert 0 <= key < self.max_size
        return find(self.__root, key + 1) is not None

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self)
        assert self.__root is not None
        node = get_kth_node(self.__root, i)
        assert node is not None
        return node.key - 1

    def insert(self, key: int) -> None:
        assert 0 <= key < self.max_size
        if key in self:
            return
        key += 1
        if self.__root is None:
            self.__root = new_tree_root(self.__max_height, key, None)
        else:
            insert(self.__root, key, None)

    def remove(self, key: int) -> None:
        assert 0 <= key < self.max_size
        self.__root = remove(self.__root, key + 1)

    def lower_bound(self, key: int) -> int:
        return lower_bound(self.__root, key + 1)

    def upper_bound(self, key: int) -> int:
        return upper_bound(self.__root, key + 1)

    def min(self) -> typing.Optional[int]:
        return None if self.__root is None else self[0]

    def max(self) -> typing.Optional[int]:
        return None if self.__root is None else self[len(self) - 1]
