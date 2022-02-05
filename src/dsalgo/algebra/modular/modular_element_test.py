import unittest

from dsalgo.algebra.modular.modular_element import (
    define_static_modular_element,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        Mint = define_static_modular_element(10**9 + 7)

        a = 0
        b = Mint(1)
        a += b
        print(a)


if __name__ == "__main__":
    unittest.main()
