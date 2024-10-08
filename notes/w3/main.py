for i in range(1, 10):
    print(i)
    
def quicksort(L, l, r): # sorts L from l to r
    if r - l <=1:
        return L
    
    (pivot, first_upper, last_upper) = (L[l], l+1, l+1)
    
    for i in range(l+1, r):
        
        if L[i] > pivot:
            last_upper += 1 # shiht the upper segment
        
        else:
            (L[i], L[first_upper]) = (L[first_upper], L[i]) # swap first_upper with L[i]
            (first_upper, last_upper) = (first_upper+1, last_upper+1) # shift both segments        
    
    # now lets move the pivot between lower and upper segement
    last_lower = first_upper - 1
    (L[l], L[last_lower]) = (L[last_lower], L[l])

    # now sort the lower and upper segments separately
    quicksort(L, l, last_lower)
    quicksort(L, last_lower+1, last_upper)

    return L

L = [22, 31, 23, 15, 867, 7654, 54]
print(quicksort(L, 0, 7))
