def get_word_list():
    word_list = []
    with open ("words.txt", 'r') as infile:
        for word in infile:
            word_list.append(word.rstrip().lower())

    return word_list

import random

#target_word = random.choice(word_list)

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


def guess_in_target(guess):
    return guess in target_word

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

def game_loop(guessed_list):
    wrong_guesses = []
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

if __name__ == '__main__':
    wrong_guesses = []
    word_list = get_word_list()
    target_word = random.choice(word_list)
    target_length = len(target_word)
    guessed_list = ['_'] * target_length
    game_loop(guessed_list)
    

