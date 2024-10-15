import math 

A = [3, 2, 1]
B = [5, 7, 8]
MA = 0
MB = 0
MAB = 0 
Dot = 0
total = 0 
AS = []

for i in range(len(A)):
    MA += (A[i]**2)
    
for i in range(len(B)):
    MB += (B[i]**2)
    
for i in range(len(A)):
    MAB += (A[i]**2 + B[i]**2)

print(math.sqrt(MAB)) # 1
print(math.sqrt(MA) + math.sqrt(MB)) # 1

for i in range(len(A)):
    Dot += A[i]*B[i]
    
print(Dot) # 2a)

angle0 = math.acos(Dot/(math.sqrt(MA)*math.sqrt(MB)))
angle1 = 180/math.pi

print(angle1) # 2b)

for i in range(len(A)):
    AS.append(A[i]*A[i])

for i in AS:
    total += i
        
print("%s = %s" % (total, math.sqrt(MA**2))) # 2c) 
