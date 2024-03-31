# Get all the even numbers from 0 - 50 using list comprehension

# even_numbers = [x for x in range(51) if x % 2 == 0]
# print(even_numbers)


# Strings that start with "a" and ends with "y"
# options = ["any","albany","apple","world","hello",""]

# valid_strings = [x for x in options if x.startswith("a") and x.endswith("y")]
# valid_strings = [
#                  x for x in options
#                  if len(x)>=2
#                  if x[0] == "a"
#                  if x[-1] == "y"
#                  ]
# print(valid_strings) 


# Flatting a matrix (list of lists)
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# flattend = [num for row in matrix for num in row]
# print(flattend)


# Categorize numbers as even or odd

categorize = ["Even" if num % 2 == 0 else "Odd" for num in range(11)]
print(categorize)