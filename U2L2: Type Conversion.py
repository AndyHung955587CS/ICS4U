inches = 10 ** 12
(feet, inches_) = divmod(inches, 12)
(yard, feet_) = divmod(feet, 3)
(miles, yard_) = divmod (yard, 1760)
(ETM, miles_) = divmod(miles, 238855) 

print("One trillion inches is the same as going to the moon and back")
print(int(miles/238855), "times, plus an extra", miles_, "miles,", yard_, "yards,", feet_, "feet, and", inches_, "inches.")

def toLower(letter):
    if (letter == letter.upper()):
        return("%s has an Unicode value of %s." % (chr(ord(letter) + 32), ord(letter) + 32))
    else:
        return("Please enter an uppercase letter") 

letter = input("Enter an uppercase letter: ")
print(toLower(letter)) 
