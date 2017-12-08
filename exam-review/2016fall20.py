file_list = ["data_1.csv", "data_2.csv", "data_3.csv"]
data = []
IDs = {}

for each in file_list:
    f = open(each, "r")
    rows = f.read().split("\n")
    rows.pop(len(rows) - 1)
    rows = [row.split(",") for row in rows]
    f.close()
    data.append(rows)

for dataset in data:
    for row in dataset:
        ID = row[0]
        row.pop(0)
        if ID in IDs:
            for each in row:
                IDs[ID].append(each)
        else:
            IDs[ID] = row

for each in IDs:
    print(each, IDs[each])
