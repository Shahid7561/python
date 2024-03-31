# try:
#     num = int(input("Enter number: "))
#     print(num)
# except:
#     print("Invalid Input!")

# list1 = [1,2,3,4,5]
# try:
#     num = int(input("Enter number: "))
#     print(list1[num])
# except ValueError:
#     print("Enter numeric value only: ")
# except IndexError:
#     print("Index out of range!")


# You can also raise an error for specific user action
num = int(input("Enter number between 1 - 100: "))

if num < 1 or num > 100:
    raise ValueError("Enter number between 1 - 100") 
else:
    print(num)