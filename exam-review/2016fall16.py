def justify (string):
    words = string.split()
    length = 0
    for word in words:
        length += len(word)
    spaces_needed = 80 - length
    while spaces_needed > 0:
        for w, word in enumerate(words[:-1]):
            if spaces_needed > 0:
                words[w] = word + " "
                spaces_needed -= 1

    final = "".join(words)
    print(final)

justify("Here is my nice, normal sentence that has 63 words in it.")
