import typing


def prime_factorize(n: int) -> typing.List[typing.Tuple[int, int]]:
    primes: typing.List[int] = []
    counts: typing.List[int] = []
    i = 1
    while i * i < n:
        i += 1
        if n % i:
            continue
        primes.append(i)
        counts.append(0)
        while n % i == 0:
            n //= i
            counts[-1] += 1
    if n > 1:
        primes.append(n)
        counts.append(1)
    return list(zip(primes, counts))


print(prime_factorize(105))
