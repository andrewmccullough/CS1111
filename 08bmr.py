def st_jeor (mass, height, age, sex):
    if (sex == "male"):
        s = 5
    elif (sex == "female"):
        s = -161
    else:
        print("Not a valid sex.")
        exit()

    p = 10.0 * mass + 6.25 * height - 5.0 * age + s
    return p

def harris_benedict (mass, height, age, sex):
    if (sex == "male"):
        p = 13.7516 * mass + 5.0033 * height - 6.7550 * age + 66.4730
    elif (sex == "female"):
        p = 9.5634 * mass + 1.8496 * height - 4.6756 * age + 655.0955
    else:
        print("Not a valid sex.")
        exit()

    return p

def revised_harris_benedict (mass, height, age, sex):
    if (sex == "male"):
        p = 13.397 * mass + 4.799 * height - 5.677 * age + 88.362
    elif (sex == "female"):
        p = 9.247 * mass + 3.098 * height - 4.330 * age + 447.593
    else:
        print("Not a valid sex.")
        exit()

    return p
