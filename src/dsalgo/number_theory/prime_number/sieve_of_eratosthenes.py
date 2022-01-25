import typing


def sieve_of_eratosthenes(max_value: int) -> typing.List[bool]:
    assert max_value > 1
    is_prime = [True] * max_value
    is_prime[0] = is_prime[1] = False
    for i in range(2, max_value):
        if i * i >= max_value:
            break
        if not is_prime[i]:
            continue
        for j in range(i * i, max_value, i):
            is_prime[j] = False
    return is_prime
