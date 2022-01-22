# reference
# - https://qiita.com/Kiri8128/items/6256f8559f0026485d90

from __future__ import annotations
import typing
import dataclasses

V = typing.TypeVar("V")


@dataclasses.dataclass
class Node(typing.Generic[V]):
    pivot: int
    key: int
    value: V
    left: typing.Optional[Node[V]] = None
    right: typing.Optional[Node[V]] = None
    size: int = 1


def _get_size(root: typing.Optional[Node[V]]) -> int:
    return 0 if root is None else root.size


def _update(root: Node[V]) -> None:
    root.size = _get_size(root.left) + _get_size(root.right) + 1


def new_tree_root(max_height: int, key: int, value: V) -> Node[V]:
    assert max_height >= 1
    assert 1 <= key < 1 << max_height
    return Node[V](1 << (max_height - 1), key, value)


def insert(root: Node[V], key: int, value: V) -> None:
    if key == root.key:
        raise Exception("you cannot insert the same key multiple times.")
    if root.pivot & 1:
        raise Exception("the given key is out of bounds")
    if key < root.key:
        lo_key, lo_value = key, value
        hi_key, hi_value = root.key, root.value
    else:
        lo_key, lo_value = root.key, root.value
        hi_key, hi_value = key, value

    if lo_key < root.pivot:
        root.key, root.value = hi_key, hi_value
        if root.left is None:
            p = root.pivot
            root.left = Node(p - (p & -p) // 2, lo_key, lo_value)
            # return
        else:
            insert(root.left, lo_key, lo_value)
    else:
        root.key, root.value = lo_key, lo_value
        if root.right is None:
            p = root.pivot
            root.right = Node(p + (p & -p) // 2, hi_key, hi_value)
            # return
        else:
            insert(root.right, hi_key, hi_value)
    root.size += 1


def find(root: typing.Optional[Node[V]], key: int) -> typing.Optional[Node[V]]:
    if root is None:
        return None
    if key == root.key:
        return root
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)


def _get_min(root: Node[V]) -> typing.Tuple[int, V]:
    if root.left is None:
        return (root.key, root.value)
    return _get_min(root.left)


def _get_max(root: Node[V]) -> typing.Tuple[int, V]:
    if root.right is None:
        return (root.key, root.value)
    return _get_max(root.right)


def remove(
    root: typing.Optional[Node[V]],
    key: int,
) -> typing.Optional[Node[V]]:
    if root is None:
        return None
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        if root.right is not None:
            root.key, root.value = _get_min(root.right)
            root.right = remove(root.right, root.key)
        elif root.left is not None:
            root.key, root.value = _get_max(root.left)
            root.left = remove(root.left, root.key)
    _update(root)
    return root


def get_kth_node(root: Node[V], k: int) -> typing.Optional[Node[V]]:
    assert k >= 0
    i = _get_size(root.left)
    if k == i:
        return root
    if k < i:
        assert root.left is not None
        return get_kth_node(root.left, k)
    if root.right is None:
        return None
    return get_kth_node(root.right, k - i - 1)


def lower_bound(root: typing.Optional[Node[V]], key: int) -> int:
    if root is None:
        return 0
    if root.key < key:
        return _get_size(root.left) + 1 + lower_bound(root.right, key)
    return lower_bound(root.left, key)


def upper_bound(root: typing.Optional[Node[V]], key: int) -> int:
    if root is None:
        return 0
    if root.key <= key:
        return _get_size(root.left) + 1 + upper_bound(root.right, key)
    return upper_bound(root.left, key)


root: typing.Optional[Node] = new_tree_root(4, 7, 2)
insert(root, 3, 6)
print(find(root, 7))
root = remove(root, 7)
for i in range(5, 10):
    insert(root, i, 1)

print(lower_bound(root, 3))
print(root)
print(get_kth_node(root, 5))


# class PivotTree(typing.Generic[V]):
#     __root: Node[V]
#     __max_size: int
#     __size: int

#     def __init__(self, max_size: int) -> None:
#         self.__max_size = max_size
#         self.__root = new_tree(max_size)
#         self.__size = 0

#     @property
#     def max_size(self) -> int:
#         return self.__max_size

#     def __len__(self) -> int:
#         return self.__size

#     def __contains__(self, key: int) -> bool:
#         assert 0 <= key < self.max_size
#         return find(self.__root, key + 1) is not None

#     def insert(self, key: int, value: typing.Optional[V] = None) -> None:
#         assert 0 <= key < self.max_size
#         if key in self:
#             return
#         insert(self.__root, key + 1, value)
#         self.__size += 1

#     def remove(self, key: int) -> None:
#         assert 0 <= key < self.max_size
#         if key not in self:
#             return
#         remove(self.__root, key + 1)
#         self.__size -= 1


# tree = PivotTree[int](max_size=10)
# tree.insert(2)
# print(len(tree))
# print(2 in tree)
