# QN 1

def fun(s):
    p = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] not in s[:i]:
            p += 1
    return p


# print(fun("baba"))

# QN 2

# print(x) undefined variable gives NameError
"""
    print(sum(1, 2))


    def sum(a, b):
        return a + b


    print(sum(1, 2))
"""
# calling function before declaration gives TypeError not NameError

# x = pou(4, 3)

# print(x) misspelled built in func gives NameError

# QN 3


def factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


# print(factors(60))


def f(n):
    s = 0
    for i in range(2, n):
        if n % i == 0 and i % 2 == 1:
            s += 1
    return s


# print(f(60))
# print(f(59))


# QN 4
"""
x = 1
while True:
    if x % 5 = = 0:
        break
    print(x, end=' ')
    x + = 1
"""
# QN 5


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, ' + self.name)


p = Person('Good morning')
# p.say_hi()

# QN 6
"""
a = [1, 2, 3]

try:
    print("second element is %d" % (a[1]))
    print("fourth element is %d" % (a[3]))

except:
    print('an error occured')
"""

# QN 7


def special3Bad(L):
    try:
        if L[0] % L[1] == 0 and L[1] != 0:
            if L[0] / (L[1] ** 2 - L[2]) == 0:
                return True
        return False
    except ZeroDivisionError:
        print('zero division error')


L = [44, 6, 36]
# print(special3Bad(L))

# QN 8


def isSymmetricBad(M):
    try:
        while len(M) > 0:
            if M.pop(0) != M.pop(-1):
                return False
        return True
    except (IndexError):
        print('Index error occured')


M1 = [1, 2, 3, 4, 3, 2, 1]
M2 = [2, 2, 2, 2, 2, 2]
M3 = [1, 1, 1, 1, 1, 1, 1]
M4 = [8]
M5 = [2, 4, 6]

"""
print(isSymmetricBad(M1))
print(isSymmetricBad(M2))
print(isSymmetricBad(M3))
print(isSymmetricBad(M4))
print(isSymmetricBad(M5))

"""

# QN 9


def gcd(m, n):
    (a, b) = (max(m, n), min(m, n))
    if a % b == 0:
        return b
    else:
        print(b, a % b)
        return (gcd(b, a % b))


print(gcd(24, 130))

# gcd(m, n) will be called 3 times other than the first call

# QN 10
