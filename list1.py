# List is a immutable data type - you can add,update,delete in List
# List Comprehension
list1 = [n for n in range(20)] #it includes 0-19 in list
# print(list1)

# Append 40 in list
# list1.append(40) 
# print(list1)

# Remove 40 from list
# list1.remove(40)
# print(list1)

# Return index of an value
# print(list1.index(10))

# It will remove and return the given value by default it will take last value
# print(list1.pop())
# print(list1)

# Add new list in existing list
# list2 = [20,21,22,23,24,25]
# list1.extend(list2)
# print(list1)

# Insert an element at specific index
# list1.insert(0,100) # index,value
# print(list1)


# Remove duplicates from list
duList = [1,2,3,1,2,4,5,4]
newList = []

for i in range(len(duList)):
    if duList[i] not in newList:
        newList.append(duList[i])
print(newList)