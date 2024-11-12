n = int(input("Enter an upper limit value for the first term: "))
for a in range(3, n + 1):
    if ((a**2) % 4 == 0):
        d = (a**2)/4
        b = d - 1  
        c = d + 1
    if ((a % 2) != 0):
        d = int(a/2)
        b = d*(a + 1)  
        c = d*(a + 1) + 1 
    if (a**2 + b**2) == c**2:
        print("(%.0f, %.0f, %.0f) => (%.0f, %.0f, %.0f)" % (a, b, c, a**2, b**2, c**2)) 
