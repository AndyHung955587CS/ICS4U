A = [3, 2, 0, -1]
B = [5, 7, 8, 4]
C = []
A2 = [] 

for i in range(len(A)):
    C.append(A[i] + B[i])

print(C)

print(A + B)

for i in range(len(A)):
    A2.append(A[i]*A[i])
    
print(A2) 
