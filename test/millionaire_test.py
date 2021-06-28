from app.millionaire import millionaire
import random
import copy
import json
import requests
import html

# Importing questions from API
easy_url = f"https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple"
med_url = f"https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple"
hard_url = f"https://opentdb.com/api.php?amount=5&category=9&difficulty=hard&type=multiple"

easy_response = requests.get(easy_url) 
med_response = requests.get(med_url)
hard_response = requests.get(hard_url)

easy_questions = json.loads(easy_response.text)
med_questions = json.loads(med_response.text)
hard_questions = json.loads(hard_response.text)

# Running Tests
def test_millionaire():
  assert millionaire(level,
                easy_questions["results"][level % 5]["question"],
                easy_questions["results"][level % 5]["incorrect_answers"],
                easy_questions["results"][level % 5]["correct_answer"])
  assert millionaire(level,
                med_questions["results"][level % 5]["question"],
                med_questions["results"][level % 5]["incorrect_answers"],
                med_questions["results"][level % 5]["correct_answer"])
  assert millionaire(level,
                hard_questions["results"][level % 5]["question"],
                hard_questions["results"][level % 5]["incorrect_answers"],
                hard_questions["results"][level % 5]["correct_answer"])