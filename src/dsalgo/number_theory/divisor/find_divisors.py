import typing


def find_divisors(n: int) -> typing.List[int]:
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
    return sorted(divisors)
