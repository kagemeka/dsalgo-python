


def binary_search(): ... 

def ternary_search(): ...



def find_root_newton(
    y: Numeric,
    n=2,
    x0=1.0,
    tol: float = 1e-8,
):
    def f(x):
        return x ** n - y

    return newton_(f, x0, tol)


from typing import Callable

from scipy.misc import derivative
from scipy.optimize import newton

from .. import Numeric


def newton_(
    f: Callable,
    x0: Numeric,
    tol: float = 1e-8,
):
    x = x0
    while abs(f(x)) > tol:
        der = derivative(
            func=f,
            x0=x,
            dx=tol,
        )
        x -= f(x) / der

    return x
