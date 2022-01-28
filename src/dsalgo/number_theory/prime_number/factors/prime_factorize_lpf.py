import typing

from dsalgo.number_theory.prime_number.finding.least_prime_factor import (
    least_prime_factor,
)


def prime_factorize_lpf(
    max_value: int,
) -> typing.Callable[[int], typing.List[typing.Tuple[int, int]]]:
    lpf = least_prime_factor(max_value)

    def prime_factorize(n: int) -> typing.List[typing.Tuple[int, int]]:
        primes = [0]
        counts = [0]
        while n > 1:
            prime = lpf[n]
            n //= prime
            if prime == primes[-1]:
                counts[-1] += 1
            else:
                primes.append(prime)
                counts.append(1)
        return list(zip(primes[1:], counts[1:]))

    return prime_factorize
