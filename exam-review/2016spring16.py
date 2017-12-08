def word_wrap (paragraph):
    words = paragraph.split()
    lines = []
    current = ""
    while words > 0:
        if len(current + words[0]) <= 80:
            current += words[0]
            words.pop(0)
        else:
            lines.append(current)
            current = ""
    for line in lines:
        print(line)
