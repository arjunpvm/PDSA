# ----- SEARCHING A LIST -----

# basic search is just a for loop

def basic_search(x, L):
    for i in L:
        if i == x:
            return True
    return False


