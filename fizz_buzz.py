# Return "fizz" if number is divisible by 3,
# Return "buzz" if number is divisible by 5,
# Return "fizzbuzz" if number is divisible by 3 and 5,else return number

num = int(input("Enter Number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)