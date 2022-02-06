# Author: Ryan S Lewis
# Date: 2022/02/06
#Written in PyCharm 2021.3.2 (Community Edition), Python 3.10

import random


def convertfunc(startingBase, convertingBase):
    limit = input("How high of a upper limit do you want to guess: ")

    decNum = random.randint(0, int(limit))

    if startingBase == "1":
        starting = "Binary"
        startingnum = bin(decNum)
    elif startingBase == "2":
        starting = "Octal"
        startingnum = oct(decNum)
    elif startingBase == "3":
        starting = "Decimal"
        startingnum = decNum
    else:
        starting = "Hexadecimal"
        startingnum = hex(decNum)

    if convertingBase == "1":
        convertingnum = "Binary"
    elif convertingBase == "2":
        convertingnum = "Octal"
    elif convertingBase == "3":
        convertingnum = "Decimal"
    else:
        convertingnum = "Hexadecimal"

    print("You will be converting from " + starting + " with a number " + str(
        startingnum) + " to " + convertingnum + "\n")

    guess = input("What is your answer in " + convertingnum + ": ")

    if convertingBase == "1":
        num2check = int(guess, 2)  # Base 2 or Binary
    elif convertingBase == "2":
        num2check = int(guess, 8)  # Base 8 or Octal
    elif convertingBase == "3":
        num2check = int(guess, 10)  # Base 10 or Decimal... This one maybe redundant.
    else:
        num2check = int(guess, 16)  # Base 16 or Hex

    if num2check == decNum:
        print("Correct! " + guess + " is " + str(startingnum) + " in " + convertingnum)
    else:
        print("Incorrect! Try again but with a different value.")


print("Hello! Want to play a nerdy game?")
print(
    "I'll ask you what base number do you want to convert from and then I'll ask you what base number do you want to convert to.\n")
print("Example: Convert from Binary to Decimal. I give you 0b0111 and you give me 7.")

print("Please select from the following options: 1-Binary, 2-Octal, 3-Decimal, 4-Hexadecimal")

startingBase = input("Please select base to starting: ")
convertingBase = input("Please select base to convert: ")

if ((startingBase == "1") or (startingBase == "2") or (startingBase == "3") or (startingBase == "4")) and (
        (convertingBase == "1") or (convertingBase == "2") or (convertingBase == "3") or (convertingBase == "4")):
    convertfunc(startingBase, convertingBase)
else:
    print("The option selected is not valid. Read the options carefully next time... Goodbye.\n")
