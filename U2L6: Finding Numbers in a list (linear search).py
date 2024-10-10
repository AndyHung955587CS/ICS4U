def linsearch(arr):
    for i in range(len(arr)):
        if (arr[i] == 20 or arr[i] == 25 or arr[i] == 60 or arr[i] == 74 or arr[i] == 97):
            print("The value %s appears at index" % arr[i], i)
        elif(arr[i] != 20 and arr[i] < 21): 
            print("The value 20 does not appear in this array")
        elif(arr[i] != 25 and arr[i] < 26): 
            print("The value 25 does not appear in this array")
        elif(arr[i] != 60 and 59 < arr[i] < 61): 
            print("The value 60 does not appear in this array")
        elif(arr[i] != 74 and 73 < arr[i] < 75): 
            print("The value 74 does not appear in this array")
        elif(arr[i] != 97 and 96 < arr[i] < 98): 
            print("The value 97 does not appear in this array")
    return 0 

myArr = [20, 20, 24, 27, 39, 40, 43, 46, 50, 
         60, 60, 62, 71, 74, 76, 86, 86, 87, 97, 97]

linsearch(myArr)
