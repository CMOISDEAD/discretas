# Set operations using lists

# remove dublicated element
def removeElements(A: list) -> list:
    B: list = []
    for x in A:
        if x not in B:
            B += [x]
    return B


# list all element
def list_elements(A: list):
    for x in A:
        print(f"{x} is an element of  the set A")


# cardinality of a set
def cardinality(A: list) -> int:
    return removeElements(A)


# A ==> B, return bool of A is subset B
def Subset(A: list, B: list) -> bool:
    for x in A:
        if x not in B:
            return False
    return True


# A <==> B, return bool of A subset B
def Equal(A: list, B: list) -> list:
    if Subset(A, B) and Subset(B, A):
        return True
    else:
        return False


# Union of A and B
def Union(A: list, B: list) -> list:
    C: list = []
    for x in A:
        if x not in C:
            C += [x]
    for x in B:
        if x not in C:
            C += [x]
    return C


# Intersection of A and B
def Intersection(A: list, B: list) -> list:
    C: list = []
    for x in A:
        if x in B:
            if x not in C:
                C += [x]
    return C


# Difference of A and B
def Difference(A: list, B: list) -> list:
    C: list = []
    for x in A:
        if x not in B:
            if x not in C:
                C += [x]
    return C


# Complement of a list
def Complement(U: list, A: list) -> list:
    return Difference(U, A)


# Cartesian Product of a list
def Cartesian(A: list, B: list) -> list:
    C: list = []
    for i in removeElements(A):
        for j in removeElements(B):
            C += [(i, j)]
    return C
