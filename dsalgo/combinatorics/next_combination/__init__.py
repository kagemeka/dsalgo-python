class NextCombination:
    def __call__(self, s: int) -> int:
        i = s & -s
        j = s + i
        return (s & ~j) // i >> 1 | j
