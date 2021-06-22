# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

# Testing the while loop for the questions.
#test_list = list(range(1,19))

level = 1


#This sets up a money list
global money
money = ['$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000']
loser_money = 

# This is a sample function that we may be able to use to easily ask questions.
def millionaire(level,question,A,B,C,D,correct_answer):
  #print(f"This is the level {level} question. For" {money[level-1]})
  print('Question:', level, "for", money[level-1]) #ML edited original code to include the amount of money it is for.
  print(question)
  print(f"A. {A}")
  print(f"B. {B}")
  print(f"C. {C}")
  print(f"D. {D}")
  answer = input("What is your answer?")
  if answer == correct_answer:
    print("CORRECT! You just earned ", money[level], ". If you walk away now, you'll leave with ", total_money, "but if you answer the next question incorrectly, you'll leave with ", loser_money, ".")
  elif answer == "lifeline":
    help = input("Which lifeline would you like to use?")
    print(help)
  else:
    print("YOU ARE WRONG!")

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

