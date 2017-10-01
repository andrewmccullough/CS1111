def check (card):

    i = 0
    everyother = []
    remaining = []

    for digit in str(card):
        print(digit, i)

        if i % 2 == 0:
            doubled = 2 * int(digit)
            for each in str(doubled):
                converted = int(each)
                remaining.append(converted)
        else:
            converted = int(digit)
            everyother.append(converted)

        i = i + 1

    print(remaining)
    print(everyother)

    print(sum(remaining))
    print(sum(everyother))

    if (sum(everyother) + sum(remaining)) % 10 == 0:
        return True
    else:
        return False
