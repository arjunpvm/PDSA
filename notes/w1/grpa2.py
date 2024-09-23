import math


def prime(n):
    (is_prime, i) = (True, 2)
    while (is_prime and i <= math.sqrt(n)):
        if n % i == 0:
            is_prime = False
        i += 1
    return is_prime


def Goldbach(n):
    gb = []
    for i in range(2, int(n/2)+1):
        if prime(i):
            for j in range(2, n):
                if prime(j) and i + j == n:
                    gb += [(i, j)]
    return gb


print(Goldbach(26))
