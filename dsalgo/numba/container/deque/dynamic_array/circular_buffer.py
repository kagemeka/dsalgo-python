import typing

import numpy as np


def solve() -> NoReturn:

    # TODO cut below

    dq = np.zeros(1 << 20, np.int64)
    dq_l, dq_r = 0, -1

    def deque_append(x):
        nonlocal dq, dq_r
        dq_r += 1
        dq[dq_r] = x

    def deque_appendleft(x):
        nonlocal dq, dq_l
        dq_l -= 1
        dq[dq_l] = x

    def deque_pop():
        nonlocal dq, dq_r
        v = dq[dq_r]
        dq_r -= 1
        return v

    def deque_popleft():
        nonlocal dq, dq_l
        v = dq[dq_l]
        dq_l += 1
        return v

    def deque_empty():
        nonlocal dq_l, dq_r
        return dq_l == dq_r + 1
