a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3]

def isMagic(arr):
    DSum1 = 0
    DSum2 = 0
    DSum1 = a1[0] + a2[1] + a3[2]
    DSum2 = a1[2] + a2[1] + a3[0]
    print(DSum1) 
    print(DSum2)
    for i in range(len(Magic3)):
        CSum = 0
        CSum = a1[i] + a2[i] + a3[i]
        print(CSum)
        temp = Magic3[i]
        RSum = 0
        for j in range(len(temp)): 
            RSum += temp[j]
        print(RSum)
    return 0 
        
isMagic(Magic3) # a) 

for i in range(len(Magic3)):
    temp = Magic3[i]
    for j in range(len(temp)):
        temp[j] += 1
        
isMagic(Magic3) # b)

for i in range(len(Magic3)):
    temp = Magic3[i]
    for j in range(len(temp)):
        temp[j] -= 2 
        
isMagic(Magic3) # c)

for i in range(len(Magic3)):
    temp = Magic3[i]
    for j in range(len(temp)):
        temp[j] *= 2 
        
isMagic(Magic3) # d) 
