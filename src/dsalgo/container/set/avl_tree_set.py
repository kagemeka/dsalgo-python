import typing
from dsalgo.graph_theory.tree.avl_tree.avl_tree import (
    insert,
    remove,
    get_kth_node,
    find,
    lower_bound,
    upper_bound,
    Node,
    K,
    iterate,
)


class AVLTreeSet(typing.Generic[K]):
    __root: typing.Optional[Node[K, None]]

    def __init__(self) -> None:
        """Initialize.

        No arguments.
        """
        self.__root = None

    def __len__(self) -> int:
        return 0 if self.__root is None else self.__root.size

    def __iter__(self) -> typing.Iterator[K]:
        for node in iterate(self.__root):
            yield node.key

    def __contains__(self, key: K) -> bool:
        return find(self.__root, key) is not None

    def insert(self, key: K) -> None:
        if key not in self:
            self.__root = insert(self.__root, Node(key))

    def remove(self, key: K) -> None:
        if key in self:
            self.__root = remove(self.__root, key)

    def __getitem__(self, k: int) -> typing.Optional[K]:
        assert 0 <= k < len(self), "index ouf of bound."
        assert self.__root is not None
        node = get_kth_node(self.__root, k)
        return None if node is None else node.key

    def max(self) -> typing.Optional[K]:
        return None if self.__root is None else self[len(self) - 1]

    def min(self) -> typing.Optional[K]:
        return None if self.__root is None else self[0]

    def lower_bound(self, key: K) -> int:
        return lower_bound(self.__root, key)

    def upper_bound(self, key: K) -> int:
        return upper_bound(self.__root, key)
