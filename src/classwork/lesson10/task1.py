# Задание 1
# Пользователь передает математический пример в виде строки, известно,
# что в этой строке одно действие и 2 числа. Кол-во символов в числе неизвестно


# calculator = input("Введите математическое выражение в виде <число> <символ> <число>: ")
#
# def findSign(list):
#     for sign in list:
#         if sign in "+-*/^":
#             return sign
#
# def findNumber(list, sign):
#     firstNumber = ''
#     secondNumber = ''
#     numbers = ''
#     for char in list:
#         if char != sign:
#             if sign == sign:
#                 firstNumber += char
#             else:
#                 secondNumber += char
#
#
#
#
# sign = findSign(calculator)
# print(sign)
# num = findNumber(calculator, sign)
# print(num)
#
# list = calculator.split(sign)
# print(list)

example = input("Введите математическое выражение в виде <число> <символ> <число>: ")

num_1 = 0
sign = ""
num_2 = 0

number_1 = ""
number_2 = ""
weFind = False

for char in example:
    if char in "+-/*^":
        sign = char
        weFind = True
    elif char == weFind:
        num_1 += char
        num_1 = int(number_1)
    else:
        num_2 += char
        num_2 = int(number_2)

match example:
    case "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    case "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    case "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    case "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    case "^":
        print(f"{num_1} ^ {num_2} = {num_1 ** num_2}")
    case _:
        print("Введен неверный символ")