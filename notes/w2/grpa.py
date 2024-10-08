# ----- GRPA 1 -----

def combinationSort(strList):
    L1 = sortAlpha(strList)
    L2 = sortNum(strList)

    return (L1, L2)

def insertAlpha(L,v):
   n = len(L)
   if n == 0:
     return([v])
   if v >= L[-1][0]:
     return(L+[v])
   else:
     return(insertAlpha(L[:-1],v)+L[-1:])

def sortAlpha(L):
   n = len(L)
   if n < 1:
      return(L)
   L = insertAlpha(sortAlpha(L[:-1]),L[-1])
   return(L)

SL1 = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77" ]


print(sortAlpha(SL1))


def sortNum(L):
  L = sortAlpha(L)
 


print(sortNum(SL1))


# ----- GRPA 2 -----

def findLargest(L):
  m = len(L)//2
  if L[0] <= L[-1]:
    return L[-1]
  elif L[0] > L[-1]:
    if L[m] > L[0] and L[m] > L[-1]:
      return L[m]
    elif L[m] > L[0]:
      return findLargest(L[m+1 :])
    else:
      return findLargest(L[:m])

print(findLargest([7, 8, 2, 3, 4, 5, 6]))
