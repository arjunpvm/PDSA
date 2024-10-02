# ----- SEARCHING A LIST -----

# basic search is just a for loop

def basic_search(x, L):
    for i in L:
        if i == x:
            return True
    return False

# worst case is O(n)

# What if the list is sorted

# use the midpoint method

def mid_search(x, L):
    if L == []:
        return False
    
    m = len(L) // 2

    if x == L[m]:
        return True
    
    elif x > L[m]:
        return mid_search(x, L[m+1:])
    else:
        return mid_search(x, L[:m])

# this is called binary search

# worst case is O(log(n))

"""
T(n) is the time to search a list of length n
    if n = 0, we exit so T(n) = 1
    if n > 0, then T(n) = T(n // 2) + 1

So the recurrence for T(n) using binary search is
    T(0) = 1
    T(n) = T(n // 2) + 1 , n > 0

T(n // 2) = (T(n // 4) + 1) + 1 = T(n//2^2) + 1 + 1
so T(k) = T(n//2^k) + k

after log n steps

T(n) = T(1) + k for k = log n
T(n) = (T(0) + 1) + k since 1//2 = 0

T(n) = 2 + log n
""" 
