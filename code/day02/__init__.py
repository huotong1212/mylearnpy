

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def sortByName(L):
#     for entry in L:

def by_name(L):
    return L[1]

L2 = sorted(L,key=lambda dic:dic[1])
print(L2)
print(sorted(L,key=by_name))