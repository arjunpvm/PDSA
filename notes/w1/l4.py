import math


def factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

# to find if a number is prime


def prime(n):
    return (factors(n) == [1, n])

# to find primes upto some number


def prime_upto(m):
    primes = []
    for i in range(1, m+1):
        if prime(m):
            primes.append(i)
    return primes

# to find first n number of primes


def first_x_primes(x):
    count = 0
    i = 1
    primes = []
    while count < x:
        if prime(i):
            count += 1
            primes.append(i)
        i += 1

    return primes


print(first_x_primes(50))


# different ways to find primes

def prime1(n):
    is_prime = True
    for i in (2, n):
        if n % i == 0:
            is_prime = False
            break  # stops the loop at the first true if statement
    return is_prime

# Using while


def prime2(n):
    (is_prime, i) = (True, 2)
    while (is_prime and i < n):
        if n % i == 0:
            is_prime = False
        i += 1
    return is_prime

# For every number factors occur in pairs.
# let's take n as 10 the factors are [1, 2, 5, 10].
# The first half of the factors are the pairs of the second half.
# So it is enough to check upto the middle of the pairs.
# the middle of the factors can be less than or equal to its sqroot
# For example for 4, 2 is the middle factor. [1, 2, 4]
# Product of two numbs greater than its sqroot is also greater than the number
# It is enough to check upto √10 which is 3.162
# so we can change prime2(n) as follows


def prime3(n):
    (is_prime, i) = (True, 2)
    while (is_prime and i <= math.sqrt(n)):
        if n % i == 0:
            is_prime = False
        i += 1
    return is_prime


print(prime3(4))

# lets find frequency of diff between primes


def prime_diffs(n):
    prime_diff = {}
    last_prime = 2
    for i in range(3, n+1):
        if prime3(i):
            diff = i - last_prime
            last_prime = i
            if diff in prime_diff.keys():
                prime_diff[diff] = prime_diff[diff] + 1
            else:
                prime_diff[diff] = 1
    return prime_diff


print(prime_diffs(10000))
