# Hangman Game in Python
## Overview
Hangman is a simple game that can be used to demonstrate basic understanding of many programming languages. The premise of the game involves a "man" who is supposed to be hanged.However the player is given a chance to save the man. The player is given a set amount of chances to correctly guess the letters in a  randomly selected word. If the 
player is successful, the "man" is not hanged. However, if they do not succeed, then the "man" is hanged.

In this particular implementation, I have ommitted the whole "hanging" part as it unneccessary for the overall game logic. Nonetheless, the rules remain the same.

## Game Logic
- ### Selecting a random word
  A list of words is initialised. They can also be imported or retrieved from an API that can provide a list of words. The ``choice`` function from the ``random`` python library is imported. 
  This will chooce a random word from the list
  #### The Python Random Library
  The [python Random library](https://docs.python.org/3/library/random.html) has a host of predefined functions for generating pseudo-random numbers, random samples as well as a host of other functions involving random numbers. For interest to us is choosing a random element of a list.
  The python random library provides the ``choice`` function that can be used for this.
  
  __Sample code__
  
  ```python
  from random inport choice

  my_list=[0,5,7,8,9,5,6,8]
  random_selection=choice(my_list)

  print(random_selection)
  ```
  This returns a random member of the list e.g. ``0`` or it could print ``8``. It is random

  __Game Implementation__
  ```python
  # A string containing the words for the game
  words='''man woman child car banana potato apple mushroom rice mango pineapple coconut watermelon'''
  # Split the string to a list containing the words separated by a single space
  words_list=words.split(' ')
  #choose a word for the person to guess
  guess_word=choice(words_list)
  correct_word=guess_word
  ```
- ### Guessing mechanism
  The game then asks the user to enter a letter. If the letter is correct that part of the word is revealed, otherwise the player loses a single chance. A placeholder string is used to keep track of which letters have been guessed or not
  The game ends if the user runs out of chances or completely guesses all the words before the chances are over.

# Source Code
```python
#hangman game
from random import choice
def check_guess(word_array):
    return not '_' in word_array

def print_skeleton(word_array):
    final_string=''
    for char in word_array:
        final_string+=char
    print(final_string)


words='''man woman child car banana potato apple mushroom rice mango pineapple coconut watermelon'''
words_list=words.split(' ')

#choose a word for the person to choose
guess_word=choice(words_list)
correct_word=guess_word
chances=len(guess_word)+2
word_skeleton=[]
for letter in guess_word:
    word_skeleton.append('_')

while chances>0:
    print("Guess a letter: ")
    print(f'You have {chances} chances left')
    input_letter=input()
    #check if the input is a letter
    if len(input_letter)>1:
        print("Please enter only a letter")
        continue
    else:
        #check if the entered letter is part of the given word
        check=guess_word.find(input_letter)
        if check!=-1 and input_letter != '*':
            print("Correct letter guessed")
            #Replace the correct letter
            if word_skeleton[check]=="_":
                word_skeleton[check]=input_letter
                guess_word=guess_word.replace(input_letter,'*',1)
                print_skeleton(word_skeleton)
            #To check if the word is complete
            check_list=check_guess(word_skeleton)
            if check_list:
                print("You have won the game !")
                break #exit the loop
        elif check==-1:
            chances=chances-1
            print("Letter is not in the word")
else:
    print(f"Chances are over ! The correct letter is {correct_word}")
```

Enjoy ! :grin:
