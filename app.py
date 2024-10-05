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