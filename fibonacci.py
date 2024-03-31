# def fib(n):
#     fib = [0,1]
#     for i in range(2, n):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib

# num = int(input("Enter Number: "))
# print(fib(num))

# def fib(n):
#     num1 = 0
#     num2 = 1
#     next_number = num1 
#     count = 1
    
#     while count <= n:
#         print(next_number, end=" ")
#         count += 1
#         num1, num2 = num2, next_number
#         next_number = num1 + num2

# num = int(input("Enter Number: "))
# fib(num)


# Recursive method
def fibonacci(num):
    return num if num<=1 else fibonacci(num-1) + fibonacci(num-2)

nterms = 10
print("Fibonacci numbers: ")
for num in range(nterms):
    print(fibonacci(num))