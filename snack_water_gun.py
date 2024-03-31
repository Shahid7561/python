# 0 for Snack,1 for Water,2 for Gun
import random
while True:
    comp = random.randint(0,2)
    user = int(input("0 for Snack,1 for Water,2 for Gun: "))
    
    if comp == user:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("Match Draw")
    if comp==0 and user == 1:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("Computer Win")
    if comp==0 and user == 2:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("User Win")
    if user == 0 and comp == 1:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("User Win")
    if user == 0 and comp == 2:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("Computer Win")
    if comp == 1 and user == 2:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("Computer Win")
    if user == 1 and comp == 2:
        print(f"Computer choose: {comp}")
        print(f"User choose: {user}")
        print("User Win")