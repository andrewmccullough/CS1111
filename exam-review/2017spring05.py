integer = None
integers = []
while integer != 0:
    integer = int(input("Type a number: "))
    integers.append(integer)
integers.sort()
print(integers)
