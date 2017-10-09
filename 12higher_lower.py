# Andrew McCullough (asm4wm)

import random

answer = int(input("What should the answer be? "))
guesses = int(input("How many guesses? "))

if answer == -1:
    answer = random.randrange(1, 100)

correct = False
g = 0

while correct == False and g < guesses:
    guess = int(input("Guess a number: "))

    g += 1

    if guess == answer:
        correct = True
    elif answer > guess:
        if g < guesses:
            print("The number is higher than that.")
    elif answer < guess:
        if g < guesses:
            print("The number is lower than that.")

if correct == True:
    print("You win!")
else:
    print("You lose; the number was " + str(answer) + ".")
