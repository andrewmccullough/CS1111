# Andrew McCullough (asm4wm)

def binop (string):
    string = string.replace(" ", "")

    i = 0
    CONTINUE = False

    a = ""
    operator = ""
    b = ""

    while CONTINUE == False:
        character = string[i]
        try:
            int(character)
            a += character
        except:
            operator = character
            CONTINUE = True
        i += 1

    while i < len(string):
        character = string[i]
        b += character
        i += 1

    a = int(a)
    b = int(b)

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "/":
        return a / b
    elif operator == "*":
        return a * b
