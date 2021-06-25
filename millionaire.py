# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

import random
import copy
import json
import requests
import html

# Global Variables
level = 1
money = ['$0','$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000','$1,000,000']
loser_money = ['$0', '$0', '$0', '$0', '$0', '$1,000', '$1,000', '$1,000', '$1,000', '$1,000', '$32,000', '$32,000', '$32,000', '$32,000', '$32,000','$32,000']

# Answers dictionary to determine the correct answer.
answers_dict = {
  "a":0,
  "b":1,
  "c":2,
  "d":3
}

# Importing questions from API
easy_url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple"
med_url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple"
hard_url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=hard&type=multiple"

easy_response = requests.get(easy_url) 
med_response = requests.get(med_url)
hard_response = requests.get(hard_url)

easy_questions = json.loads(easy_response.text)
med_questions = json.loads(med_response.text)
hard_questions = json.loads(hard_response.text)

# This is a sample function that we may be able to use to easily ask questions.
# Rank is the input variable for the funciton. Level is the variable.
def millionaire(rank,question,incorrect_answers,correct_answer):
  #print(f"This is the level {level} question. For" {money[level-1]})
  global level
  global money
  global loser_money
  print('Question#', rank, "for", money[rank]) #ML edited original code to include the amount of money it is for.
  # This function reads the ASCII codes so they can be displayed properly in the question.
  print(html.unescape(question))
  all_answers = copy.copy(incorrect_answers)
  all_answers.append(correct_answer)
  random.shuffle(all_answers)
  index = all_answers.index(correct_answer)
  # breakpoint()
  print(html.unescape(f"A. {all_answers[0]}"))
  print(html.unescape(f"B. {all_answers[1]}"))
  print(html.unescape(f"C. {all_answers[2]}"))
  print(html.unescape(f"D. {all_answers[3]}"))
  # print(f"The correct answer is {correct_answer}.")
  answer = input("What is your answer? [Enter your answer or type 'walk' to end the game] \n")
  if answer.lower().strip() == "walk":
    print("You are walking away with ", money[rank-1],". Thank you for playing! Enjoy your fake money!")
    level = 17
  elif answer == "lifeline":
    help = input("Which lifeline would you like to use?")
    print(help)
  elif answers_dict[answer.lower().strip()] == index:
    print("CORRECT! If you walk away now, you'll leave with ", money[rank], " but if you answer the next question incorrectly, you'll leave with ", loser_money[rank], ".")
    level = level + 1
  else:
    print("Ohh, too bad! You're leaving today with ", loser_money[rank-1])
    print(f"The correct answer was {correct_answer}. Better Luck next time!")
    level = 17
    # breakpoint()

while level <= 16:
    print("-------------------------------------")
    if level >= 1 and level <= 5:
      print("EASY QUESTIONS PROMPT")
      difficulty = easy_questions
    elif level >= 6 and level <= 10:
      print("MEDIUM QUESTIONS PROMPT")
      difficulty = med_questions
    elif level >= 11 and level <= 15:
      print("HARD QUESTIONS PROMPT")
      difficulty = hard_questions
    elif level == 16:
      print("CONGRATS")
      break
    print("-------------------------------------")
    millionaire(level,
                difficulty["results"][level % 5]["question"],
                difficulty["results"][level % 5]["incorrect_answers"],
                difficulty["results"][level % 5]["correct_answer"])
