# Andrew McCullough (asm4wm)

import math

age = int(input("How old are you? "))
max = math.floor(age * 2 - 13)
min = math.floor(age / 2 + 7)
print("You can date people between", min, "and", max, "years old")
