def save_list (filename, data):
    f = open(filename, "w")
    for line in data:
        f.write(",".join([str(n) for n in line]))
        f.write("\n")
    f.close()

save_list ("tmp.csv", [[2, 3], [5, 7, 11], [13]])
