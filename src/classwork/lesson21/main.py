import os






def calculator(example):
    first = 0
    second = 0
    sign = ""
    temp = ""

    for char in example:
        if char in "+-*/^":
            sign = char
            first = int(temp)
            temp = ""
        else:
            temp += char
    second = int(temp)

    match sign:
        case "+": return first + second
        case "-": return first - second
        case "*": return first * second
        case "/": return first / second
        case "^": return first ** second


def getFile():
    file = open("resources/name.txt", "r+")
    fromFile = file.read()
    result = calculator(fromFile)
    return file.write(f"={result}")

print(getFile())
