# ----- Calculating complexity -----


# iterative programs

# Eg.1: find max element in a list

def maxNum(L):
    maxVal = L[0]
    for i in L:
        if L[i] > maxVal:
            maxVal = L[i]
    return maxVal

# here n is length of the list
# single loop scans all elements
# always takes n steps with overall time O(n)

# Eg.2: find whether a list contains duplicates

def no_duplicates(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] == L[j]:
                return False
    return True

print(no_duplicates([1, 2, 3, 4]))

# there are two loops in this function
# here the worst case is getting True
# for that the two loops will run fully
# time taken is n-1 for first iteration n-2 for second iteration and so on...
# (n-1) + (n-2) + ... + 1 = n(n-1)/2 = n^2 / 2 - n / 2
# to find efficiency we only take the highest degree ie n^2/2
# and remove the constants ie n^2
# this function is O(n^2)


