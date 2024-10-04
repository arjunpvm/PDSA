# ----- GRPA 1 -----

def combinationSort(strList):
    L1 = sortAlpha(strList)
    L2 = sortNum(strList)

    return (L1, L2)

def merge(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)
    while k < m + n:
        a = A[i]
        b = B[j]

        if m == 0:
            C.extend(B)
            k = k + (n - j) 
        elif n == 0:
            C.extend(A)
            k = k + (m - i) 
        elif a[0] < b[0]:
            C.append(i)
            k = k + i
        elif b[0] < a[0]:
            C.append(j)
            k = k + j

    return C


def sortAlpha(strList):
    n = len(strList)
    if n < 1:
        return strList
    for i in range(n)
    return strList

def sortNum(strList):
    n = len(strList)
    if n < 1:
        return strList

    return strList

