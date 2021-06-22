# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

# Testing the while loop for the questions.
#test_list = list(range(1,19))

level = 1


#This sets up a money list
global money
money = ['$0','$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000']
loser_money = ['$0', '$0', '$0', '$0', '$0', '$1,000', '$1,000', '$1,000', '$1,000', '$1,000', '$32,000', '$32,000', '$32,000', '$32,000', '$32,000']

# This is a sample function that we may be able to use to easily ask questions.
def millionaire(level,question,A,B,C,D,correct_answer):
  #print(f"This is the level {level} question. For" {money[level-1]})
  print('Question#', level, "for", money[level-1]) #ML edited original code to include the amount of money it is for.
  print(question)
  print(f"A. {A}")
  print(f"B. {B}")
  print(f"C. {C}")
  print(f"D. {D}")
  answer = input("What is your answer?")
  if answer == correct_answer:
    print("CORRECT! If you walk away now, you'll leave with ", money, " but if you answer the next question incorrectly, you'll leave with ", loser_money, ".")
  elif answer == "lifeline":
    help = input("Which lifeline would you like to use?")
    print(help)
  else:
    print("Ohh, too bad! You're leaving today with ", loser_money[level - 1])

while True:
    index = level - 1
    print("-------------------------------------")
    print('Question#', level, "for", money[level])
    print(f"If you answer correctly, you'll win {money[level]}.") 
    print (f"But if you answer incorrectly, you'll leave with {loser_money[level-1]}.")
    print(f"If you walk away now without answering the question, you'll keep {money[level-1]}.")
    answer = input(f"This is a test for question {level}: [yes, no, lifeline]")
    print("-------------------------------------")
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

