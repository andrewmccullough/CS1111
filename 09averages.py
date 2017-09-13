# Andrew McCullough (asm4wm)

import math

def mean (a, b, c):
    result = (a + b + c) / 3
    return result

def median (a, b, c):
    list = [a, b, c]
    list.sort()
    result = list[1]
    return result

def rms (a, b, c):
    squares = (a ** 2 + b ** 2 + c ** 2) / 3
    result = math.sqrt(squares)
    return result

def middle_average (a, b, c):
    result = median(mean (a, b, c), median (a, b, c), rms (a, b, c))
    return result
