# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)

# Your code should handle all sorts of errors like :(2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

current_year = 2024
while True:
    try:
        print("\nMenu: ")
        print("1. You need to see when you are going to be 100years old.")
        print("2. You need to see your current age.")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 3:
            raise ValueError("Enter between (1-3)")
        else:
            match choice:
                case 1:
                    age = int(input("\nEnter your age or your birthyear(YYYY): "))
                    if age > current_year:
                        raise ValueError("You are not yet born")
                    else:
                        if len(str(age)) <= 2:
                                if age >= 100:
                                    raise ValueError("You seem to be the oldest person alive")
                                else:
                                    print(f"You are going to be 100 years old in {(100-age) + current_year}\n")

                        elif len(str(age)) == 4:
                            current_age = (current_year-age)
                            print(f"You are going to be 100 years old in {(100-current_age) + current_year}\n")
                case 2:
                    age = int(input("\nEnter your birthyear(YYYY): "))
                    if age > current_year:
                        raise ValueError("You are not yet born")
                    else:
                        print(f"Your current age is {current_year - age}")
                case 3:
                    break
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")        