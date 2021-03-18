#This is a guess the number game

import random

print('Hello! What is your name?')
name = input()
secretNumber = random.randint(1, 30)
print('Well, ' + name + ', I am thinking of a number between 1 to 30')

# ask the player to take a guess.

for guessnumber in range(1, 6):
    print('Take a guess.')
    guess = int(input())
    if guess > secretNumber:
        print('Nope that is too high')
    elif guess < secretNumber:
        print('Nah that is too low')
    else:
        break # The player guessed it correctly

if guess == secretNumber:
    print('you got right ' + name + '!' + ' You guessed it in '+ str(guessnumber) + ' guesses!')
else:
    print('Sorry, I was thinking ' + str(secretNumber))