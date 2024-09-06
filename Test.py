# Code from last year 

def check(word, first, last):
    if (last - first <= 0): 
        return True
    else:
        if word[first].lower() == word[last].lower() :
            return check(word, first + 1, last - 1) 
        else:
            return False
            
print("Palindrome program!")
eop = False 
while not eop:
    word = input("Please enter a word, and I will decide if it is a palindrome: ")
    if check(word, 0, len(word) - 1) == True:
        print("%s is a palindrome!" % word)
    else:
        print("%s is not a palindrome." % word)
    repeat = input("Do another(y/n) ")
    if repeat.lower() == "n":
        print("Goodbye")
        eop = True 
    elif repeat.lower() != "y":
        print("Type n to end the program.") 
