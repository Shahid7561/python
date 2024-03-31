# dictionary is a mutable datatype - you can add,update,delete in list
dict1 = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
# print(dict1)

# Print keys of dictionary
# print(dict1.keys())

# Print values of dictionary
# print(dict1.values())

# Print both key and value of dictionary
# print(dict1.items())

# Get value of given key
# print(dict1.get(1))

# Remove element from dictionary
# dict1.pop(3)
# print(dict1)

# Update any key value pair in dictionary
# dict1.update({3:"Three"})
# print(dict1)


# dictionary comprehension
x = {i : i+1 for i in range(5)}
print(x)