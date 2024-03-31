# import time

# start_time = time.time()
# num = 10
# for i in range(50):
#     print([True if num > 1 and all(num % i !=0 for i in range(2,int(num**0.5)+1)) else False])
# end_time = time.time()
# print(f"Time taken {end_time-start_time}") # 0.008751392364501953

# start_time = time.time()
# num = 10
# for i in range(50):
#     print([f"{num} is Prime" if num > 1 and all(num % i != 0 for i in range(2,num)) else f"{num} is Not Prime"])
# end_time = time.time()
# print(f"Time taken {end_time-start_time}") # 0.007993936538696289


# Prints prime numbers between specific range
end  = 100
print([n for n in range(end+1) if n > 1 and all(n % i != 0 for i in range(2,n))])