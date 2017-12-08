def compare ():
    file1 = input("First file.... ")
    file2 = input("Second file... ")

    f1 = open(file1, "r")
    f2 = open(file2, "r")

    lines1 = f1.readlines()
    lines2 = f2.readlines()

    if len(lines1) > len(lines2):

        for l, line in enumerate(lines1):
            try:
                if line != lines2[l]:
                    print("Line: " + str(l))
                    print("< " + lines1[l], end = "")
                    print("> " + lines2[l], end = "")
            except IndexError:
                print("Line: " + str(l))
                print("< " + lines1[l], end = "")
                print("> [none]")

    else:

        for l, line in enumerate(lines2):
            try:
                if line != lines1[l]:
                    print("Line: " + str(l))
                    print("< " + lines1[l], end = "")
                    print("> " + lines2[l], end = "")
            except IndexError:
                print("Line: " + str(l))
                print("< [none]")
                print("> " + lines2[l], end = "")

compare()
