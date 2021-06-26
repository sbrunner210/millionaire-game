# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

import random
import copy
import json
import requests
import html

# Global Variables
level = 1
lifelines = 3
money = ['$0','$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000','$1,000,000']
loser_money = ['$0', '$0', '$0', '$0', '$0', '$1,000', '$1,000', '$1,000', '$1,000', '$1,000', '$32,000', '$32,000', '$32,000', '$32,000', '$32,000','$32,000']
category_list = [*range(9,33)]

# Answers dictionary to determine the correct answer.
answers_dict = {
  "a":0,
  "b":1,
  "c":2,
  "d":3
}

# Introductory print statements
print("Welcome to Who Wants to Be a Millionaire! Test your knowledge for the grand prize.")
print("This is how the game works:" + "\n")
print("You will be asked a multiple choice question, with options A, B, C and D.")
print("If you get the correct answer, you earn money and move onto the next question.") 
print("But if you guess incorrectly then you lose the money you have earned,")
print("But don't worry! We're not total monsters. There are checkpoints along the way that allow you to keep a certain amount of money should you get a question wrong further on.")
print("The questions increase in difficulty as you progress but you can make use of a 50/50 lifeline to help you out")
print("This will remove 2 incorrect answers.\nType Lifeline to access")
print("One more thing, when answering, please use either A, B, C or D or you will be disqualified!")

while True:
  category = input("Please enter the number for one of the following categories: \nGeneral Knowledge	9 \nEntertainment:Books	10 \nEntertainment:Film	11 \nEntertainment:Music	12 \nEntertainment:Musicals & Theatres	13 \nEntertainment:Television	14 \nEntertainment:Video Games	15 \nEntertainment:Board Games	16 \nScience & Nature	17 \nScience:Computers	18 \nScience:Mathematics	19 \nMythology	20 \nSports	21 \nGeography	22 \nHistory	23 \nPolitics	24 \nArt	25 \nCelebrities	26 \nAnimals	27 \nVehicles	28 \nEntertainment:Comics	29 \nScience:Gadgets	30 \nEntertainment:Japanese Anime & Manga	31 \nEntertainment:Cartoon & Animations	32 \n")
  print(f"You have selected category {category}")
  if int(category) not in category_list:
    print("OOPS!, Invalid input. Try again.")
  else:
    break

# Importing questions from API
easy_url = f"https://opentdb.com/api.php?amount=5&category={category}&difficulty=easy&type=multiple"
med_url = f"https://opentdb.com/api.php?amount=5&category={category}&difficulty=medium&type=multiple"
hard_url = f"https://opentdb.com/api.php?amount=5&category={category}&difficulty=hard&type=multiple"

easy_response = requests.get(easy_url) 
med_response = requests.get(med_url)
hard_response = requests.get(hard_url)

easy_questions = json.loads(easy_response.text)
med_questions = json.loads(med_response.text)
hard_questions = json.loads(hard_response.text)

# This is a sample function that we may be able to use to easily ask questions.
# Rank is the input variable for the funciton. Level is the variable.
def millionaire(rank,question,incorrect_answers,correct_answer):
  
  global level
  global lifelines
  global money
  global loser_money
  print('Question#', rank, "for", money[rank]) #ML edited original code to include the amount of money it is for.
  # This function reads the ASCII codes so they can be displayed properly in the question.
  print(html.unescape(question))
  all_answers = copy.copy(incorrect_answers)
  all_answers.append(correct_answer)
  random.shuffle(all_answers)
  correct_index = all_answers.index(correct_answer)
  
  print(html.unescape(f"A. {all_answers[0]}"))
  print(html.unescape(f"B. {all_answers[1]}"))
  print(html.unescape(f"C. {all_answers[2]}"))
  print(html.unescape(f"D. {all_answers[3]}"))
  
  answer = input("What is your answer? [Enter your answer, type 'lifeline' for help, or type 'walk' to end the game] \n").lower().strip()
  if answer not in ["a", "b", "c", "d", "walk", "lifeline"]:
    print("OOPS! Invalid input")    
  else:  
    if answer == "walk":
      print("You are walking away with ", money[rank-1],". Thank you for playing! Enjoy your fake money!")
      level = 17
    elif answer == "lifeline":
      if lifelines == 0:
        print("Sorry, you have no lifelines left.")
      else:
        lifelines = lifelines - 1
        keep_index = random.randint(0,2)
        for removed_answers in incorrect_answers:
          if incorrect_answers.index(removed_answers) != keep_index:
            remove_index = all_answers.index(removed_answers)
            all_answers[remove_index] = "..."
      print(html.unescape(f"A. {all_answers[0]}"))
      print(html.unescape(f"B. {all_answers[1]}"))
      print(html.unescape(f"C. {all_answers[2]}"))
      print(html.unescape(f"D. {all_answers[3]}"))
      answer = input("What is your answer? [Enter your answer or type 'walk' to end the game] \n").lower().strip()
      if answer not in ["a", "b", "c", "d", "walk", "lifeline"]:
        print("OOPS! Invalid input")          
      else: 
        if answer == "walk":
          print("You are walking away with ", money[rank-1],". Thank you for playing! Enjoy your fake money!")
          level = 17
        elif answers_dict[answer] == correct_index:
          print("CORRECT! If you walk away now, you'll leave with ", money[rank], " but if you answer the next question incorrectly, you'll leave with ", loser_money[rank], ".")
          level = level + 1
        elif answer in ["a", "b", "c", "d"]:
          print("Ohh, too bad! You're leaving today with ", loser_money[rank-1])
          print(f"The correct answer was {correct_answer}. Better Luck next time!")
          level = 17
    elif answers_dict[answer] == correct_index:
      print("CORRECT! If you walk away now, you'll leave with ", money[rank], " but if you answer the next question incorrectly, you'll leave with ", loser_money[rank], ".")
      level = level + 1
    elif answer in ["a", "b", "c", "d"]:
      print("Ohh, too bad! You're leaving today with ", loser_money[rank-1])
      print(f"The correct answer was {correct_answer}. Better Luck next time!")
      level = 17

while level <= 16:
    print("-------------------------------------")
    if level >= 1 and level <= 5:
      print("Just started! Here's something easy for you!")
      difficulty = easy_questions
    elif level >= 6 and level <= 10:
      print("Let's crank up the heat! Need to make you start sweating!")
      difficulty = med_questions
    elif level >= 11 and level <= 15:
      print("You're on a roll! Are you going to be our next millionaire?!?")
      difficulty = hard_questions
    elif level == 16:
      print("CONGRATULATIONS!!! YOU DID IT! YOU WON A MILLION DOLLARS!\n", 
      "Don't spend it all in one place!")
      break
    print("-------------------------------------")
    millionaire(level,
                difficulty["results"][level % 5]["question"],
                difficulty["results"][level % 5]["incorrect_answers"],
                difficulty["results"][level % 5]["correct_answer"])
