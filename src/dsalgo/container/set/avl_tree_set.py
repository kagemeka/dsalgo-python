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
)


class AVLTreeSet(typing.Generic[K]):
    __root: typing.Optional[Node[K, None]]

    def __init__(self) -> None:
        self.__root = None
        self.__size = 0

    def __len__(self) -> int:
        return 0 if self.__root is None else self.__root.size

    def __contains__(self, key: K) -> bool:
        return find(self.__root, key) is not None

    def insert(self, key: K) -> None:
        if key not in self:
            self.__root = insert(self.__root, Node(key))

    def remove(self, key: K) -> None:
        if key in self:
            self.__root = remove(self.__root, key)

    def __getitem__(self, k: int) -> typing.Optional[K]:
        assert 0 <= k < len(self)
        assert self.__root is not None
        node = get_kth_node(self.__root, k)
        return None if node is None else node.key

    def max_value(self) -> typing.Optional[K]:
        return None if self.__root is None else self[len(self) - 1]

    def min_value(self) -> typing.Optional[K]:
        return None if self.__root is None else self[0]

    def lower_bound(self, key: K) -> int:
        return lower_bound(self.__root, key)

    def upper_bound(self, key: K) -> int:
        return upper_bound(self.__root, key)


s = AVLTreeSet[int]()

s.insert(1)
s.insert(0)
s.insert(4)
s.insert(2)


print(len(s))
print(s.min_value())
print(s.max_value())

print(s.lower_bound(2))
print(s.lower_bound(3))
print(s.lower_bound(4))
print(s.upper_bound(4))
print(s.upper_bound(3))
print(s.upper_bound(2))
print(s.upper_bound(0))
