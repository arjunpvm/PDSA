def gcd(m, n):
    factors = []
    for i in range(1, min(m, n)+1):
        if m % i == 0 and n % i == 0:
            factors.append(i)
    return factors[-1]


print(gcd(4, 12))

# different version of the same code


def gcd2(x, y):
    for i in range(1, min(x, y)+1):
        if x % i == 0 and y % i == 0:
            mrcf = i  # Most recent common factor
    return (mrcf)


print(gcd2(4, 12))


# both methods are proportionate to min(n, m)
# let's see if we can do better
