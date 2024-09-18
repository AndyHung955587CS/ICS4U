A = [2, 8, 6, 3, 9, 1, 7]
B = [0] * 7

for i in range(len(A)):
    r = ((i + 2) % 7)
    B[i] = A[r]
    
print(B)
