def check (card):

    card = str(card)

    i = 0 # Position iterator.

    everyother = [] # "Form a sum of every other digit, including the right-most digit."
    remaining = [] # "Double each remaining digit, then sum all the digits that creates it."

    while i < len(card):
        position = len(card) - 1 - i

        if i % 2 == 0:
            converted = int(card[position])
            everyother.append(converted)
        else:
            doubled = 2 * int(card[position])
            for each in str(doubled):
                converted = int(each)
                remaining.append(converted)

        i = i + 1 # Advances position iterator.

    if (sum(everyother) + sum(remaining)) % 10 == 0:
        return True
    else:
        return False
