# Andrew McCullough (asm4wm)

import math

def big_root (a, b, c):
    # Returns the larger root of the equation.
    root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    if (root1 > root2):
        return root1
    else:
        return root2

def small_root (a, b, c):
    # Returns the smaller root of the equation.
    root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    if (root1 < root2):
        return root1
    else:
        return root2
