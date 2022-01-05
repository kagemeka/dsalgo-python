import typing


import typing 

def base_convert_to_ten(
    base: int, 
    digits: typing.Iterable[int],
) -> int:
    p = 1
    n = 0
    for d in digits:
        n += d * p
        p *= base
    return n


def base_convert_from_ten(
    base: int, 
    n: int,
) -> typing.List[int]:
    assert abs(base) >= 2
    if n == 0: return [0]
    digits = []
    while n:
        n, r = divmod(n, base)
        if r < 0:
            r -= base
            n += 1
        digits.append(r)
    return digits

    

class BaseConvert:
    @classmethod
    def nary_to_mary(cls, nums: list[int], n: int, m: int) -> list[int]:
        return cls.int_to_nary(cls.int_from_nary(nums, n), m)

    @staticmethod
    def int_from_nary(nums: list[int], base: int) -> int:
        assert abs(base) >= 2
        n = 0
        d = 1
        for x in nums:
            n += d * x
            d *= base
        return n

    @staticmethod
    def int_to_nary(n: int, base: int) -> list[int]:
        assert abs(base) >= 2
        nums = []
        while True:
            n, r = divmod(n, base)
            if r < 0:
                n += 1
                r -= base
            nums.append(r)
            if n == 0: break
        return nums
