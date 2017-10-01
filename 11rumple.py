# Andrew McCullough (asm4wm)

print("You will never win the game, for Boaty McBoatface is my name.")

name = "Boaty McBoatface"
correct = False
while correct == False:
    guess = input("Guess my name: ")
    if (guess == name):
        correct = True
        print("No! How did you guess?")
    else:
        print("Ha! You'll never guess!")
