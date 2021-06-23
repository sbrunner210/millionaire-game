# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

# Testing the while loop for the questions.
#test_list = list(range(1,19))

import random

level = 1

answers_dict = {
  "a":0,
  "b":1,
  "c":2,
  "d":3
}

questions = {
  "response_code":0,"results":[
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"How would one say goodbye in Spanish?","correct_answer":"Adi&oacute;s","incorrect_answers":["Hola","Au Revoir","Salir"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"On a dartboard, what number is directly opposite No. 1?","correct_answer":"19","incorrect_answers":["20","12","15"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is on display in the Madame Tussaud&#039;s museum in London?","correct_answer":"Wax sculptures","incorrect_answers":["Designer clothing","Unreleased film reels","Vintage cars"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is the Spanish word for &quot;donkey&quot;?","correct_answer":"Burro","incorrect_answers":["Caballo","Toro","Perro"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"According to Sherlock Holmes, &quot;If you eliminate the impossible, whatever remains, however improbable, must be the...&quot;","correct_answer":"Truth","incorrect_answers":["Answer","Cause","Source"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is Tasmania?","correct_answer":"An Australian State","incorrect_answers":["A flavor of Ben and Jerry&#039;s ice-cream","A Psychological Disorder","The Name of a Warner Brothers Cartoon Character"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which country, not including Japan, has the most people of japanese decent?","correct_answer":"Brazil","incorrect_answers":["China","South Korea","United States of America"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which of the following is the IATA code for Manchester Airport?","correct_answer":"MAN","incorrect_answers":["EGLL","LHR","EGCC"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What nuts are used in the production of marzipan?","correct_answer":"Almonds","incorrect_answers":["Peanuts","Walnuts","Pistachios"]},
    {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"When someone is cowardly, they are said to have what color belly?","correct_answer":"Yellow","incorrect_answers":["Green","Red","Blue"]}
    ]
  }

#This sets up a money list
global money
money = ['$0','$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000']
loser_money = ['$0', '$0', '$0', '$0', '$0', '$1,000', '$1,000', '$1,000', '$1,000', '$1,000', '$32,000', '$32,000', '$32,000', '$32,000', '$32,000']

# This is a sample function that we may be able to use to easily ask questions.
def millionaire(level,question,incorrect_answers,correct_answer):
  #print(f"This is the level {level} question. For" {money[level-1]})
  print('Question#', level, "for", money[level-1]) #ML edited original code to include the amount of money it is for.
  print(question)
  incorrect_answers.append(correct_answer)
  random.shuffle(incorrect_answers)
  index = incorrect_answers.index(correct_answer)
  print(f"A. {incorrect_answers[0]}")
  print(f"B. {incorrect_answers[1]}")
  print(f"C. {incorrect_answers[2]}")
  print(f"D. {incorrect_answers[3]}")
  answer = input("What is your answer?")
  if answers_dict[answer.lower().strip()] == index:
    print("CORRECT! If you walk away now, you'll leave with ", money[0], " but if you answer the next question incorrectly, you'll leave with ", loser_money[0], ".")
  elif answer == "lifeline":
    help = input("Which lifeline would you like to use?")
    print(help)
  else:
    print("Ohh, too bad! You're leaving today with ", loser_money[0])


millionaire(1,questions["results"][0]["question"],questions["results"][0]["incorrect_answers"],questions["results"][0]["correct_answer"])

# while True:
    # index = level - 1
    # print("-------------------------------------")
    # print('Question#', level, "for", money[level])
    # print(f"If you answer correctly, you'll win {money[level]}.") 
    # print (f"But if you answer incorrectly, you'll leave with {loser_money[level-1]}.")
    # print(f"If you walk away now without answering the question, you'll keep {money[level-1]}.")
    # answer = input(f"This is a test for question {level}: [yes, no, lifeline]")
    # print("-------------------------------------")
    # if answer.lower().strip() == "yes":
        # level = level + 1
        # print(f"This was the right answer. Moving onto question {level}")
    # elif answer.lower().strip() == "no":
        # print("Wrong Answer. Sorry. Game Over.")
        # break
    # elif answer.lower().strip() == "lifeline":
        # help = input("Choose a lifeline:")
        # print(f"Your selected lifeline was: {help}")
    # else:
        # print("ERROR")
        # break

