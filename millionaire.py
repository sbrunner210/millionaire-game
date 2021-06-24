# This is the script for the Silver Snake's "Who Wants to be a Millionaire" Game

# Testing the while loop for the questions.
#test_list = list(range(1,19))

import random
import copy
import json
import requests

# Global Variables
level = 1
money = ['$0','$100','$200','$300','$500','$1,000','$2,000','$4,000','$8,000','$16,000','$32,000','$64,000','$125,000','$250,000','$500,000','$1,000,000']
loser_money = ['$0', '$0', '$0', '$0', '$0', '$1,000', '$1,000', '$1,000', '$1,000', '$1,000', '$32,000', '$32,000', '$32,000', '$32,000', '$32,000']

# Answers dictionary to determine the correct answer.
answers_dict = {
  "a":0,
  "b":1,
  "c":2,
  "d":3
}

# Importing questions from API
easy_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"
med_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
hard_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=hard&type=multiple"

easy_response = requests.get(easy_url) 
med_response = requests.get(med_url)
hard_response = requests.get(hard_url)

easy_questions = json.loads(easy_response.text)
med_questions = json.loads(med_response.text)
hard_questions = json.loads(hard_response.text)

# easy_questions = {
  # "response_code":0,"results":[
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"How would one say goodbye in Spanish?","correct_answer":"Adi&oacute;s","incorrect_answers":["Hola","Au Revoir","Salir"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"On a dartboard, what number is directly opposite No. 1?","correct_answer":"19","incorrect_answers":["20","12","15"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is on display in the Madame Tussaud&#039;s museum in London?","correct_answer":"Wax sculptures","incorrect_answers":["Designer clothing","Unreleased film reels","Vintage cars"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is the Spanish word for &quot;donkey&quot;?","correct_answer":"Burro","incorrect_answers":["Caballo","Toro","Perro"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"According to Sherlock Holmes, &quot;If you eliminate the impossible, whatever remains, however improbable, must be the...&quot;","correct_answer":"Truth","incorrect_answers":["Answer","Cause","Source"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is Tasmania?","correct_answer":"An Australian State","incorrect_answers":["A flavor of Ben and Jerry&#039;s ice-cream","A Psychological Disorder","The Name of a Warner Brothers Cartoon Character"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which country, not including Japan, has the most people of japanese decent?","correct_answer":"Brazil","incorrect_answers":["China","South Korea","United States of America"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"Which of the following is the IATA code for Manchester Airport?","correct_answer":"MAN","incorrect_answers":["EGLL","LHR","EGCC"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What nuts are used in the production of marzipan?","correct_answer":"Almonds","incorrect_answers":["Peanuts","Walnuts","Pistachios"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"When someone is cowardly, they are said to have what color belly?","correct_answer":"Yellow","incorrect_answers":["Green","Red","Blue"]}
    # ]
  # }

# med_questions = {
  # "response_code":0,"results":[
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What is the name of the very first video uploaded to YouTube?","correct_answer":"Me at the zoo","incorrect_answers":["tribute","carrie rides a truck","Her new puppy from great grandpa vern."]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"In 2013 how much money was lost by Nigerian scams?","correct_answer":"$12.7 Billion","incorrect_answers":["$95 Million","$956 Million","$2.7 Billion"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Who is a co-founder of music streaming service Spotify?","correct_answer":"Daniel Ek","incorrect_answers":["Sean Parker","Felix Miller","Michael Breidenbruecker"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Which of these is the name of a Japanese system of alternative medicine, literally meaning &quot;finger pressure&quot;?","correct_answer":"Shiatsu","incorrect_answers":["Ukiyo","Majime","Ikigai"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What is the romanized Japanese word for &quot;university&quot;?","correct_answer":"Daigaku","incorrect_answers":["Toshokan","Jimusho","Shokudou"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What is the name of the popular animatronic singing fish prop, singing such hits such as &quot;Don&#039;t Worry, Be Happy&quot;?","correct_answer":"Big Mouth Billy Bass","incorrect_answers":["Big Billy Bass","Singing Fish","Sardeen"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What is a dead mall?","correct_answer":"A mall with high vacancy rates or low consumer foot traffic","incorrect_answers":["A mall with no stores","A mall that has been condemed","A mall after business hours"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Who invented Pastafarianism?","correct_answer":"Bobby Henderson","incorrect_answers":["Eric Tignor","Bill Nye","Zach Soldi"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"What was the original name of the search engine &quot;Google&quot;?","correct_answer":"BackRub","incorrect_answers":["CatMassage","SearchPro","Netscape Navigator"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"medium","question":"Earl Grey tea is black tea flavoured with what?","correct_answer":"Bergamot oil","incorrect_answers":["Lavender","Vanilla","Honey"]}
    # ]
  # }

# hard_questions = {
  # "response_code":0,"results":[
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Electronic music producer Kygo&#039;s popularity skyrocketed after a certain remix. Which song did he remix?","correct_answer":"Ed Sheeran - I See Fire","incorrect_answers":["Marvin Gaye - Sexual Healing","Coldplay - Midnight","a-ha - Take On Me"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"When was &quot;YouTube&quot; founded?","correct_answer":"February 14, 2005","incorrect_answers":["May 22, 2004","September 12, 2005","July 19, 2009"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Sciophobia is the fear of what?","correct_answer":"Shadows","incorrect_answers":["Eating","Bright lights","Transportation"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"What is the romanized Korean word for &quot;heart&quot;?","correct_answer":"Simjang","incorrect_answers":["Aejeong","Jeongsin","Segseu"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"How many calories are in a 355 ml can of Pepsi Cola?","correct_answer":"150","incorrect_answers":["200","100","155"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"According to Fair Works Australia, how long do you have to work to get Long Service Leave?","correct_answer":"7 years","incorrect_answers":["2 years","8 years","6 months"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Which product did Nokia, the telecommunications company, originally sell?","correct_answer":"Paper","incorrect_answers":["Phones","Computers","Processors"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Originally another word for poppy, coquelicot is a shade of what?","correct_answer":"Red","incorrect_answers":["Green","Blue","Pink"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"Where is Apple Inc. headquartered?","correct_answer":"Cupertino, California","incorrect_answers":["Redwood City, California","Redmond, Washington","Santa Monica, CA"]},
    # {"category":"General Knowledge","type":"multiple","difficulty":"hard","question":"How many notes are there on a standard grand piano?","correct_answer":"88","incorrect_answers":["98","108","78"]}
    # ]
  # }


# Variables to randomly select a question
quest_length = len(easy_questions["results"])
quest_pool = [*range(quest_length)]

# breakpoint()

# This is a sample function that we may be able to use to easily ask questions.
def millionaire(rank,question,incorrect_answers,correct_answer):
  #print(f"This is the level {level} question. For" {money[level-1]})
  global level
  global money
  global loser_money
  print('Question#', rank, "for", money[rank-1]) #ML edited original code to include the amount of money it is for.
  print(question)
  all_answers = copy.copy(incorrect_answers)
  all_answers.append(correct_answer)
  random.shuffle(all_answers)
  index = all_answers.index(correct_answer)
  # breakpoint()
  print(f"A. {all_answers[0]}")
  print(f"B. {all_answers[1]}")
  print(f"C. {all_answers[2]}")
  print(f"D. {all_answers[3]}")
  answer = input("What is your answer?")
  if answer.lower().strip() == "walk":
    print("You are walking away with ", money[rank-1],". Thank you for playing! Enjoy your fake money!")
    level = 17
  elif answer == "lifeline":
    help = input("Which lifeline would you like to use?")
    print(help)
  elif answers_dict[answer.lower().strip()] == index:
    print("CORRECT! If you walk away now, you'll leave with ", money[rank-2], " but if you answer the next question incorrectly, you'll leave with ", loser_money[rank-1], ".")
    level = level + 1
  else:
    print("Ohh, too bad! You're leaving today with ", loser_money[rank-1])
    level = 17
    # breakpoint()


# millionaire(1,questions["results"][0]["question"],questions["results"][0]["incorrect_answers"],questions["results"][0]["correct_answer"])

while level <= 16:
    # index = level - 1
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
    print('Question#', level, "for", money[level])
    print(f"If you answer correctly, you'll win {money[level]}.") 
    print (f"But if you answer incorrectly, you'll leave with {loser_money[level-1]}.")
    print(f"If you walk away now without answering the question, you'll keep {money[level-1]}.")
    quest_num = random.choice(quest_pool)
    # Currently, the loop is eliminating questions from multiple pools. Needs to be fixed.
    millionaire(level,difficulty["results"][quest_num]["question"],difficulty["results"][quest_num]["incorrect_answers"],difficulty["results"][quest_num]["correct_answer"])
    quest_pool.remove(quest_num)
    