# Compute the prime factorization of an integer.
from math import sqrt


def prime_factorization(x: int) -> None:
    c = x  # remaining product to factor

    while c % 2 == 0:
        print("%ld" % 2)
        c /= 2

    i = 3
    while i <= sqrt(c) + 1:
        if (c % i) == 0:
            print("%ld" % i)
            c /= i
        else:
            i += 2

    if c > 1:
        print("%ld" % c)
