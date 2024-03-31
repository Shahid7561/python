# Let's play kaun banega crorepati

Question = ["1.What is the capital of India?\nA.Delhi\tB.Mumbai\nC.Ahmedabad\tD.Surat",
            "2.What is the capital of Gujarat?\nA.Delhi\tB.Gandhinagar\nC.Ahmedabad\tD.Surat",
            "3.What is national bird of india?\nA.Sparrow\tB.Peacock\nC.Lion\tD.Parrot",
            "4.In which state ahmedabad is located?\nA.Gujarat\tB.Maharastra\nC.Rajasthan\tD.Andra Pradesh",
            "5.In which state pune is located?\nA.Gujarat\tB.Maharastra\nC.Rajasthan\tD.Andra Pradesh"]

Answers = ["A","B","B","A","B"]
money = 0
print("Welcome To Kaun Banega Crorepati")
print("You need to answers the following questions and for each right answer you got 1000rs.")
print("If you dont know answer you can quit the game.\n")

for i in range(len(Question)):
    print(Question[i])
    user_ans = input("Enter correct option: ")
    if user_ans == Answers[i]:
        money += 1000
        print("\nCorrect Answer")
        print(f"You win {money}\n")
    elif user_ans == "Quit":
        print("Thank you for playing game\n")
        print(f"You win {money}")
        break
    else:
        print("Wrong Answer\n")
        print(f"Correct Answer is : {Answers[i]}")
        print(f"You win {money}")
        break
