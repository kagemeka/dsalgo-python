from .. import Numeric
from . import newton_


def find_root_newton(
    y: Numeric,
    n=2,
    x0=1.0,
    tol: float = 1e-8,
):
    def f(x):
        return x ** n - y

    return newton_(f, x0, tol)
