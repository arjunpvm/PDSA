
# iterative programs

def maxNum(L):
    maxVal = L[0]
    for i in L:
        if L[i] > maxVal:
            maxVal = L[i]
    return maxVal

# here n is length of the list
# single loop scans all elements
# always takes n steps with overall time O(n)


