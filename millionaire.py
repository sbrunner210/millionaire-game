# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

# Testing the while loop for the questions.
test_list = list(range(1,19))

level = 1

while True:
    index = level - 1
    answer = input(f"This is a test for question {level}: [yes, no, lifeline]")
    if answer.lower().strip() == "yes":
        level = level + 1
        print(f"This was the right answer. Moving onto question {level}")
    elif answer.lower().strip() == "no":
        print("Wrong Answer. Sorry. Game Over.")
        break
    elif answer.lower().strip() == "lifeline":
        help = input("Choose a lifeline:")
        print(f"Your selected lifeline was: {help}")
    else:
        print("ERROR")
        break