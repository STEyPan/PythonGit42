# Задача 1 - вводится строка состоящая из скобочек.
# Необходимо написать функцию, которое валидирует строку на правильность.
# 1. Могут использоваться - () [] {}
# Примеры:
# ()[]{} -> True

def validateBrackets(text: str) -> bool:

    stack = []

    for char in text:
        if char in "({[":
            stack.append(char)

        elif char == ")":
            if stack[len(stack) - 1] == "(":
                stack.pop()
                continue
            else:
                return False

        elif char == "]":
            if stack[len(stack) - 1] == "[":
                stack.pop()
                continue
            else:
                return False

        elif char == "}":
            if stack[len(stack) - 1] == "{":
                stack.pop()
                continue
            else:
                return False

    return False if len(stack) else True

print(validateBrackets("({})"))


def RomanToInt(romeNumber):
    arab_number = 0
    pre_digit = 0

    rome_to_arab = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100
    }
    levels = "IVXLC"
    lvl = 0
    temp = 0
    result = 0

    for digit in romeNumber[::-1]:

        current_digit = rome_to_arab[digit]

        if current_digit < pre_digit:
            arab_number -= current_digit

        else:
            arab_number += current_digit

        pre_digit = current_digit

    return arab_number




print(RomanToInt("XL"))






