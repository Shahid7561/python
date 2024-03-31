import random

randomNum = random.randint(1,100)
guesses = 10
print("Welcome to the Guess the Number game!")
print(f"You need to thinking of a number between 1 and 100. You have {guesses} attempts.")

while guesses > 0:
    userNum = int(input("Enter Number between 1 to 100: "))
    if userNum < 1 or userNum > 100:
        raise ValueError("Enter Number between 1 to 100")
    else:
        if userNum < randomNum:
            print(f"{userNum} is less than random number")
            guesses -= 1
            print(f"{guesses} guesses left")
        elif userNum > randomNum:
            print(f"{userNum} is greter than random number")
            guesses -= 1
            print(f"{guesses} guesses left")
        elif userNum == randomNum:
            print(f"You guessed it right!!!,You take {10-guesses} guess to guess the number")
            break
if guesses == 0:
    print("Sorry you lose the Game")
