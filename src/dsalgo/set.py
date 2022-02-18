class FenwickTree:
    ...


class SegmentTree:
    ...




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




from dsalgo.graph_theory.tree.pivot_tree.pivot_tree_array_recurse import (
    PivotTreeArray,
)

class PivotTreeArraySet(PivotTreeArray):
    ...



from dsalgo.graph_theory.tree.avl_tree.avl_tree_recurse import (
    K,
    Node,
    find,
    get_kth_node,
    insert,
    iterate,
    lower_bound,
    remove,
    upper_bound,
)


class AVLTreeSet(typing.Generic[K]):
    __root: typing.Optional[Node[K, None]]

    def __init__(self) -> None:
        """Initialize.

        No arguments.
        """
        self.__root = None

    def __len__(self) -> int:
        """Size of the set.

        Returns:
            int: size.
        """
        return 0 if self.__root is None else self.__root.size

    def __iter__(self) -> typing.Iterator[K]:
        """Iterate Node in ascending order by key.

        Returns:
            typing.Iterator[K]: iterator object.

        Yields:
            K: yield keys in ascending order.
        """
        for node in iterate(self.__root):
            yield node.key

    def __contains__(self, key: K) -> bool:
        """Check whether a value is contained in the set or not.

        Args:
            key (K): key.

        Returns:
            bool: return True if contained else False
        """
        return find(self.__root, key) is not None

    def insert(self, key: K) -> None:
        """Insert.

        Args:
            key (K):
                key to insert.
                if already contained, do nothing.
        """
        if key not in self:
            self.__root = insert(self.__root, Node(key))

    def remove(self, key: K) -> None:
        """Remove.

        Args:
            key (K):
                key to remove.
                if not contained, do nothing.
        """
        if key in self:
            self.__root = remove(self.__root, key)

    def __getitem__(self, k: int) -> typing.Optional[K]:
        """Indexing.

        Args:
            k (int):
                index of a key.
                if the index is out of range, raise AssertionError.

        Returns:
            typing.Optional[K]: return a key if exist.
        """
        assert 0 <= k < len(self), "index ouf of range."
        assert self.__root is not None
        node = get_kth_node(self.__root, k)
        return None if node is None else node.key

    def max(self) -> typing.Optional[K]:
        """Max key.

        Returns:
            typing.Optional[K]:
                return the maximum key.
                if the set is empty, return None.
        """
        return None if self.__root is None else self[len(self) - 1]

    def min(self) -> typing.Optional[K]:
        """Min key.

        Returns:
            typing.Optional[K]:
                return the minimum key.
                if the set is empty, return None.
        """
        return None if self.__root is None else self[0]

    def lower_bound(self, key: K) -> int:
        """Lower bound.

        Args:
            key (K): target key.

        Returns:
            int: lower bound index.
        """
        return lower_bound(self.__root, key)

    def upper_bound(self, key: K) -> int:
        """Upper bound.

        Args:
            key (K): target key.

        Returns:
            int: upper bound index.
        """
        return upper_bound(self.__root, key)
