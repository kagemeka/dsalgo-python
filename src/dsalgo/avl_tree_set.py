import typing

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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
