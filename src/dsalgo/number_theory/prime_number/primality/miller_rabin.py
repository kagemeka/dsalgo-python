import typing


def miller_rabin(n: int) -> bool:
    ...


#   https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
def miller_rabin_32(n: int) -> bool:
    #   https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    BASES: typing.Final[
        typing.Tuple[
            typing.Literal[2],
            typing.Literal[7],
            typing.Literal[61],
        ]
    ] = (2, 7, 61)
    return True
    ...


def miller_rabin_64(n: int) -> bool:
    return True
