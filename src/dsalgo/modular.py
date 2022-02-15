import enum


def add(mod: int, lhs: int, rhs: int) -> int:
    res = lhs + rhs
    if res >= mod:
        res -= mod
    return res


def neg(mod: int, x: int) -> int:
    return mod - x


def subtract(mod: int, lhs: int, rhs: int) -> int:
    return add(mod, lhs, neg(mod, rhs))


def multiply(mod: int, lhs: int, rhs: int) -> int:
    return lhs * rhs % mod


def divide(p: int, lhs: int, rhs: int) -> int:
    return multiply(p, lhs, invert_fermat(p, rhs))


def pow_recurse(mod: int, x: int, n: int) -> int:
    if n == 0:
        return 1
    y = pow_recurse(mod, x, n >> 1)
    y = y * y % mod
    if n & 1:
        y = y * x % mod
    return y


def pow(mod: int, x: int, n: int) -> int:
    y = 1
    while n:
        if n & 1:
            y = y * x % mod
        x = x * x % mod
        n >>= 1
    return y


def invert_naive(mod: int, n: int) -> int:
    """Modular Inverse naive implementation.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, -1, mod)


def invert_euler_theorem(mod: int, n: int) -> int:
    """Modular Inverse by Euler's theorem.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Constraints:

    """
    ...


def invert_fermat(p: int, n: int) -> int:
    """Modular Inverse by Fermat's Little theorem.

    Args:
        p (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, p - 2, p)


def invert_extended_euclidean(mod: int, n: int) -> typing.Optional[int]:
    r"""Modular Inverse with extended eucledian GCD algorithm.

    Args:
        mod (int): an modulo.
        n (int): arbitral integer.

    Returns:
        typing.Optional[int]:
            modular inverse of n.
            if the inverse does not exist, return None.

    Algorithm Summary:
        definition of modular inver of n
        x := inverse of n.
        nx \equiv 1 \mod m
        nx - 1 = qm (q is arbitral)
        nx - qm = 1
        y := -q
        nx + my = 1 (Bezout identity)
        this equation can be solved by extendex euclidean algorithm.
    """
    assert mod > 1
    gcd, x, _ = extended_euclidean_recurse(n % mod, mod)
    if gcd != 1:
        return None
    if x < 0:
        x += mod
    assert 0 <= x < mod
    return x


def invert_extended_euclidean_direct(mod: int, n: int) -> typing.Optional[int]:
    """Compute Modular inverse directly with Extended Euclidean Algorithm.

    Args:
        mod (int): an modulo.
        n (int): arbitral integer.

    Returns:
        typing.Optional[int]:
            modular inverse of n.
            if the inverse does not exist, return None.

    Algorithm Summary:
        consider for the equation nx + my = 1.
        (x_i, y_i)^T = [
            [0, 1],
            [1, -q_i],
        ](x_{i-1}, y_{i-1})^T

        (x_0, y_0)^T = (1, 0)^T  # one of the solution.

        finally, y is not needed to be computed.
        it's only enough to store only first row's data.
    """
    assert mod > 1
    a, b = n % mod, mod
    x00, x01 = 1, 0  # first row of matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        a, b = b, r
    if a != 1:
        return None
    if x00 < 0:
        x00 += mod
    assert 0 <= x00 < mod
    return x00


def inverse_table_naive(p: int, n: int) -> list[int]:
    ...


def inverse_table(p: int, n: int) -> list[int]:
    """Modular Inverse table.

    Args:
        n (int): [description]
        mod (int): [description]

    Returns:
        list[int]: [description]
    """
    b, a = factorial(n, mod), factorial_inverse(n, mod)
    for i in range(n - 1):
        a[i + 1] = a[i + 1] * b[i] % mod
    return a


ADD_IDENTITY = 0
MUL_IDENTITY = 1


class Modulo(enum.IntEnum):
    MOD_1_000_7 = enum.auto()
    MOD_998_244_353 = enum.auto()
    MOD_1_000_000_007 = enum.auto()
    MOD_1_000_000_009 = enum.auto()


class ModularElement(abc.ABC):
    _mod: typing.ClassVar[int]
    __value: int

    def __init__(self, value: int) -> None:
        value %= self.mod
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    @property
    def mod(self) -> int:
        return self._mod

    def __repr__(self) -> str:
        return f"{self.value}"

    # def __clone(self) -> Modular:
    #     return self.__class__(self._value)

    def __add__(self, rhs: ModularElement) -> ModularElement:
        return self.__class__(self.value + rhs.value)

    def __iadd__(self, rhs: ModularElement) -> ModularElement:
        return self + rhs

    def __radd__(self, lhs: int) -> int:
        return (self.__class__(lhs) + self).value

    def __neg__(self) -> ModularElement:
        return self.__class__(-self.value)

    def __sub__(self, rhs: ModularElement) -> ModularElement:
        return self + -rhs

    def __isub__(self, rhs: ModularElement) -> ModularElement:
        return self - rhs

    def __rsub__(self, lhs: int) -> int:
        return (self.__class__(lhs) - self).value

    def __mul__(self, rhs: ModularElement) -> ModularElement:
        return self.__class__(self.value * rhs.value)

    def __imul__(self, rhs: ModularElement) -> ModularElement:
        return self * rhs

    def __rmul__(self, lhs: int) -> int:
        return (self.__class__(lhs) * self).value

    def invert(self) -> ModularElement:
        return self.__class__(invert_fermat(self.mod, self.value))

    def __truediv__(self, rhs: ModularElement) -> ModularElement:
        assert rhs.value >= 1
        return self * rhs.invert()

    def __itruediv__(self, rhs: ModularElement) -> ModularElement:
        return self / rhs

    def __rtruediv__(self, lhs: int) -> int:
        return (self.__class__(lhs) / self).value

    def __floordiv__(self, rhs: ModularElement) -> ModularElement:
        return self / rhs

    def __ifloordiv__(self, rhs: ModularElement) -> ModularElement:
        return self // rhs

    def __rfloordiv__(self, lhs: int) -> int:
        return lhs / self

    def __pow__(self, n: int) -> ModularElement:
        return self.__class__(pow(self.value, n, self.mod))

    def __ipow__(self, n: int) -> ModularElement:
        return self**n

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, ModularElement):
            raise NotImplementedError
        return self.value == rhs.value


def define_static_modular_element(
    prime_mod: int,
) -> typing.Type[ModularElement]:
    class Mint(ModularElement):
        _mod: typing.ClassVar[int] = prime_mod

    return Mint


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
