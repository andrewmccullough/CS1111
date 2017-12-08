import re

string = "abcdefgh"
expression = re.compile(r"[a-z]")

search = expression.search(string)
print(search)
print(search.groups())

finditer = expression.finditer(string)
print(finditer)

# findall = expression.findall(string)
# print(findall)

for each in finditer:
    result = each.groups()
    print(result)
