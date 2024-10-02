print("location of a =", id(a))
print("location of b =", id(b))
print(a is b)
a = a.replace("e","z")
print(a)
print(b)
print(a is b)
print("location of a =", id(a))
print("location of b =", id(b))

# Predicted Output 
# location of a = 53921728
# location of b = 53921728
# True
# Hzllo
# Hello
# False
# location of a = 53779776
# location of b = 53921728
# The prediction was correct (id(a) and id(b) was checked before) 

A = ["zebra", "kangaroo", "cat", "human", "aardvark"]

def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(C, arr): 
    for i in range(len(C) - 1):
        for j in range(i + 1, len(C)):
            if (C[i] > C[j]):
                swap(C, i, j)

sort(A, A)

print("%s, %s, %s, %s, %s" % (A[0], A[1], A[2], A[3], A[4]))
