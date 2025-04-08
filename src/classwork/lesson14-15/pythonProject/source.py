def functionPrint(lst: list):
    for elem in lst:
        print(f"Hello, {elem}", end="! | ")
    print()

def functionPrintReverse(lst: list):
    for elem in lst:
        print(f"{elem}, hello", end="! | ")
    print()

def getPrintFunction(reverseFlag: bool) :
    if reverseFlag:
        return functionPrintReverse
    else:
        return functionPrint


def summer(Fisrt: int, Second: int):
    return Fisrt + Second


def minus(Fisrt: int, Second: int):
    return Fisrt - Second


def multiply(Fisrt: int, Second: int):
    return Fisrt * Second

def divisions(Fisrt: int, Second: int):
    if not Second:
        return 0
    else:
        return Fisrt / Second

def steps(Fisrt: int, Second: int):
    return Fisrt ** Second

def getMathFunc(sign):
    match sign:
        case "+": return summer
        case "-": return minus
        case "*": return multiply
        case "/": return divisions
        case "^": return steps