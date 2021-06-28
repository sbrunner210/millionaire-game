# millionaire-game
Who Wants to be a Millionaire

This app is designed to be a replayable trivia game of the classic game show "Who Wants to be a Millionaire?" Questions are randomly pulled from a trivia website according to the category selected by the user. The user then must answer 15 questions in a row to win the game. The user has three (3) 50/50 lifelines to use as needed. Winning this game does not make you a real millionaire. All the money in this game is fake, and just for fun/entertainment purposes.

Good Luck!

## Group Members
* Shane Brunner
* Madeline Grimes
* Mandy Lancour
* Nate Ondricek

## Prerequisites
  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Navigate to the app's folder from the command line:

```sh
cd millionaire-game
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n millionaire-env python=3.8
conda activate millionaire-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Testing
Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```

## Usage

Run the app:

```py
millionaire.py
```
The user is given instructions in how to play the game and answer the questions given. First, the user must select a category from one of the options presented. Once a category is selected, the app then begins to present questions to the user. The user must answer with the letter corresponding to the correct choice. If the user needs assitance, the user can type "lifeline" for help. If the user wants to end the game, the user can type "walk" to walk away with their winnings.

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

## [License](/LICENSE)