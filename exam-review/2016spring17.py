def most_common_names (names):
    most_common = ""
    max_common = 0
    for name in names:
        count = names.count(name)
        if count > max_common:
            most_common = name
            max_common = count
    print(most_common)
