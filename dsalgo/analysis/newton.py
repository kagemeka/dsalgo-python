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
