def middle (string):
    length = len(string)
    if length % 2 == 0:
        # even length; pick middle 2
        output = string[length // 2 - 1] + string[length // 2]
    else:
        # odd length; pick middle 1
        output = string[length // 2]

    return output

print(middle ("glow"))
