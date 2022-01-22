import enum


class Modulo(enum.IntEnum):
    MOD_1_000_7 = enum.auto()
    MOD_998_244_353 = enum.auto()
    MOD_1_000_000_007 = enum.auto()
    MOD_1_000_000_009 = enum.auto()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
