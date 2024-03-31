# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string  
task = input("You want to Decode or Code the String?: ")
if task == "Code":
    str1 = input("Enter String to Code: ")
    if len(str1) < 3:
        print(f"Coded String is {str1[::-1]}")
    else:
        newstr = list(str1)
        # for i in range(len(newstr)):
        newstr.append(str1[0])
        newstr.remove(newstr[0])
        for i in range(0,3):
            randomLetter = random.choice(string.ascii_letters)
            newstr.insert(i,randomLetter.lower())
        for i in range(0,3): 
            randomLetter = random.choice(string.ascii_letters)
            newstr.append(randomLetter.lower())
        print(str(''.join(newstr))) #olehahidSegm
elif task == "Decode":
    str1 = input("Enter String to Decode: ")
    if len(str1) < 3:
        print(f"Original String is {str1[::-1]}")
    else:
        newstr = list(str1)
        l,r = 0,len(newstr)-1
        for i in range(3):
            newstr.remove(newstr[l])
            newstr.remove(newstr[r])
            l+=1
            r-=1
        print(newstr)