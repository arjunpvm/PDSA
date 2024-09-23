def factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


# print(factors(10))


def is_prime(n):
    if factors(n) == [1, n]:
        return str(n) + " is prime"
    else:
        return str(n) + " is not prime"


print(is_prime(6))


def all_prime(n):
    primes = []
    for i in range(1, n+1):
        if factors(i) == [1, i]:
            primes.append(i)
    return primes


print(all_prime(100))
