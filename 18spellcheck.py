import urllib.request

with urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/words.txt") as f:
    html = f.read().decode("utf-8")
    dictionary = html.split("\n")
    dictionary.pop()

print("Type text; enter a blank line to end.")
newline = input()

while (newline != ""):
    words = newline.split()

    for word in words:
        word = word.strip(".?!,()'\"")
        # word = word.replace(".", "").replace("?", "").replace("!", "").replace(",", "").replace("(", "").replace(")", "").replace("\"", "").replace("'", "")

        if word not in dictionary:
            if word.lower() not in dictionary:
                print("  MISSPELLED: " + word)

    newline = input()
