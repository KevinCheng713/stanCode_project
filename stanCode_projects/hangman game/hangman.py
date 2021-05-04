"""
File: hangman.py
Name:鄭凱元
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    Before guessing, check to see if there are any remaining lives.

    *current_dash is a string which used to store current progress,
    and new_dash is an empty string used for string manipulation,
    every time you enter for loop syntax scope, it start with an empty one.
    """
    # Hide every English letter in random word with a dash
    word = random_word()
    dash = ''
    for ch in word:
        if ch.isalpha():
            dash += '-'
    current_dash = dash
    # The cumulative number of wrong answers
    count = 0

    print('The word looks like: ' + current_dash)
    print('You have ' + str(N_TURNS - count) + ' guesses left.')
    while count < N_TURNS:
        guess = str(input('Your guess: '))
        guess = guess.upper()
        new_dash = ''
        # only if all the conditions are met(nested if), enter the for loop scope.
        if len(guess) == 1:
            if guess.isalpha():
                if guess in word:
                    for i in range(len(word)):
                        if guess == word[i]:
                            new_dash += word[i]
                        else:
                            new_dash += current_dash[i]
                    current_dash = new_dash
                    print('You are correct!')
                    if '-' in new_dash:
                        print('The word looks like: ' + new_dash)
                        print('You have ' + str(N_TURNS - count) + ' guesses left.')

                    else:
                        print('You win!! \nThe word was: ' + word)
                        break
                else:
                    count += 1
                    if count < N_TURNS:
                        print('There is no ' + guess + "'s in the word.")
                        print('The word looks like: ' + current_dash)
                        print('You have ' + str(N_TURNS - count) + ' guesses left.')
        # In other cases, print illegal format.
            else:
                print('illegal format.')
        else:
            print('illegal format.')
    if count == N_TURNS:
        print('There is no ' + guess + "'s in the word.")
        print('You are completely hung : ( \nThe word was: ' + word)



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
