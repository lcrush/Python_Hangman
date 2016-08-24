
# coding: utf-8

# # Hangman Game
# ## Second heading
# ### Third heading

# * Hidden words
# * The guesses
# * Display correct guesses
# * Display hangman
# * Players:  Computer vs. Human (Human guessing)
# * Words for guessing

word_list = []
with open ("words.txt", 'r') as infile:
    for word in infile:
        word_list.append(word.rstrip().lower())


import random

target_word = random.choice(word_list)


HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# How to access hangman picture:

print(HANGMANPICS[0])

# ### How to play hangman
# 
# 1. Play 1 (computer) chooses a word
# 2. P1 draw hint dashes for each letter -- need length of hidden word
# 3. Player 2 (human) guesses
# 4. P1 checks to see if hidden word contains a guess
# 5. If it does not contain, then P1 writes the guess in the appropriate spots
# 6. If not, draw next body part
# 7. Check for win or lose
# 8. If not win or lose, go back to step 3

target_length = len(target_word)
print(target_length * '_' )


def guess_in_target(guess):
    return guess in target_word


guessed_list = target_length * '_ '
guessed_list = guessed_list.rstrip().split(' ')


def find_guess(guessed_list, guess):
    if target_word.count(guess) > 1:
        for i, ch in enumerate(target_word):
            if ch == guess:
                guessed_list[i] = ch
                
    elif guess in target_word:
        position = target_word.index(guess)
        print(position)
        guessed_list[position] = guess


    return guessed_list


def have_won(guessed_list):
    if '_' in guessed_list:
        return False
    else:
        print('You can ACTUALLY spell!')
        return True


def have_lost(wrong_guesses):
    if len(wrong_guesses)+1 == len(HANGMANPICS):
        print("IDIOT!!! You can't spell! \nHere's the word dork: ", target_word)
        return True
    else:
        return False        


wrong_guesses = []
def game_loop(guessed_list):
    while not have_won(guessed_list) and not have_lost(wrong_guesses):
        guess = input('Enter your guess: ')
        if guess_in_target(guess):
            guessed_list = find_guess(guessed_list, guess)
            pass
        else:
            wrong_guesses.append(guess)
        wrong_index = len(wrong_guesses)
        print(HANGMANPICS[wrong_index])
        print("Correct guesses: " + str(guessed_list), "\nWrong guesses: " + str(wrong_guesses))
    
    
    
game_loop(guessed_list)