def count_common (stringA, stringB):
    matches = [] # letters in common
    for character in stringA:
        if character in stringB and character not in matches:
            matches.append(character)
    return len(matches)

print(count_common("seer", "peer"))
