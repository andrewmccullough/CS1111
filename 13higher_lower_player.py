# Andrew McCullough (asm4wm)

print("Think of a number between 1 and 100 and I'll guess it.")
guesses = int(input("How many guesses do I get? "))

possible = [0, 100]

guess = 0
correct = False

while guess < guesses and correct == False:
    # print("Low: " + str(possible[0]) + " High: " + str(possible[1]))

    current = (possible[1] - possible[0]) // 2 + possible[0]
    response = input("Is the number higher, lower, or the same as " + str(current) + "? ")

    if response == "same":
        correct = True
    elif response == "lower":
        possible[1] = current
        if possible[1] - possible[0] <= 1:
            print("Wait; how can it be both higher than " + str(possible[0]) + " and lower than " + str(possible[1]) + "?")
            exit()
    elif response == "higher":
        possible[0] = current
        if possible[1] - possible[0] <= 1:
            print("Wait; how can it be both higher than " + str(possible[0]) + " and lower than " + str(possible[1]) + "?")
            exit()

    guess += 1

if correct == True:
    print("I won!")
else:
    answer = int(input("I lost; what was the answer? "))
    if answer < possible[0]:
        print("That can't be; you said it was higher than " + str(possible[0]) + "!")
    elif answer > possible[1]:
        print("That can't be; you said it was lower than " + str(possible[1]) + "!")
    else:
        print("Well played!")
