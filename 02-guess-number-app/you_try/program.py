import random

print('--------------------------------')
print('     GUESS THE NUMBER GAME')
print('--------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('What is your name ?')

while guess != the_number:
    guess_number = input("Guess the number ")
    guess = int(guess_number)
    if guess > the_number:
        print("Sorry {0}, Your Guess {1} was too High".format(name, guess))
    elif guess < the_number:
        print("Sorry {0}, Your Guess {1} was too Less".format(name, guess))
    else:
        print('Excellent {}, You Win. It was {}'.format(name, guess))

print("Done")
