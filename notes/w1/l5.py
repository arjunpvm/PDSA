# Faster ways to find gcd(m, n)

"""
    if m and n are divisible by d, then
    m = ad , n = bd
    m-n = ad - bd
    m-n = (a-b)d
    implies m-n is also divisible by d
"""


def gcd(m, n):
    (a, b) = (max(m, n), min(m, n))

    if a % b == 0:
        return b
    else:
        return gcd(b, a-b)


print(gcd(2, 51))

# but this takes time proportional to max(m, n)
# gcd(2, 9999) will take long time
# will take around half of the max number's iterations(approx 5000 steps)

# So lets look at the Euclid's algorithm

"""
    suppose n doesnt divide m, then
    m = qn + r
    also m = ad, n = bd. then
    m = q(bd) + r
    ad = q(bd) + r
    implies r = cd
"""
"""
    Euclid's algorithm:
        if n divides m then gcd(m, n) = n
        else compute gcd(n, m mod n)
"""


def gcd2(m, n):
    (a, b) = (max(m, n), min(m, n))
    if a % b == 0:
        return b
    else:
        return gcd2(b, a % b)


print(gcd2(2, 9999))


# this takes time proportional to no of digits in max(m, n)
# gcd(2, 9999) will take only 2 iterarions
