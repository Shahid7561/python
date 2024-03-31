import time
# Factorial of a number using recursion

# start_time = time.time()
# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = int(input("Enter number: "))

# check if the number is negative
# for i in range(50):
#     if num < 0:
#         print("Sorry, factorial does not exist for negative numbers")
#     elif num == 0:
#         print("The factorial of 0 is 1")
#     else:
#         print("The factorial of", num, "is", recur_factorial(num))
# end_time = time.time()
# print(f"Time using recursion method: {end_time-start_time}") #1.9882769584655762 

# Factorial of a number using loop
# start_time = time.time()
# def fact(n):
#     if n == 1:
#         return n
#     else:
#         fact = 1
#         for i in range(1,n+1):
#             fact *= i
#         return fact
# num =int(input("Enter Number: "))
# for i in range(50):
#     print(f"Factorial of {num} is {fact(num)}")
# end_time = time.time()
# print(f"Time using loop method: {end_time-start_time}") #1.290306568145752

# Factorial of num in one 
start_time = time.time()
n = int(input("Enter number: "))
for i in range(50):
    factorial = lambda n : n if n == 1 else n * factorial(n-1)
    print(factorial(n))
end_time = time.time()
print(f"Time taken by lambda function is : {end_time - start_time}") #1.676337480545044