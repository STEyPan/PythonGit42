def calculate(example):
    first = 0
    second = 0
    sign = ""
    temp = ""

    for char in example:
        if char in "+-/*^":
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

def main():
    example = input("Введите математическое выражение: ")
    print(f"{example}={calculate(example)}")

main()