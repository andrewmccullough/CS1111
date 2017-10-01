integer = int(input("Enter an integer: "))
numeral = ""
if integer > 0 and integer < 4000:
    thousands = integer // 1000
    numeral += "M" * thousands
    integer = integer % 1000

    hundreds = integer // 100

    if hundreds == 9:
        numeral += "CM"
        integer -= 900
    elif hundreds >= 5:
        numeral += "D"
        integer -= 500

        hundreds = integer // 100
        numeral += "C" * hundreds
        integer = integer % 100

    elif hundreds == 4:
        numeral += "CD"
        integer -= 400
    else:
        numeral += "C" * hundreds
        integer = integer % 100

    tens = integer // 10

    if tens == 9:
        numeral += "XC"
        integer -= 90
    elif tens >= 5:
        numeral += "L"
        integer -= 50

        tens = integer // 10
        numeral += "X" * tens
        integer = integer % 10
    elif tens == 4:
        numeral += "XL"
        integer -= 40
    else:
        numeral += "X" * tens
        integer = integer % 10

    if integer == 9:
        numeral += "IX"
    elif integer >= 5:
        numeral += "V"
        integer -= 5

        numeral += "I" * integer
    elif integer == 4:
        numeral += "IV"
    else:
        numeral += "I" * integer

    print(numeral)

else:
    print("Input must be between 1 and 3999")
