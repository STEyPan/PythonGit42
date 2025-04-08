# Указатели на функции
# Это переменные, которые хранят в себе указатель в памяти
# на конкретную функцию и их можно применять для вызова этой функции, даже
# в тех местах, где она недоступна
# ВАЖНО - Использование указателей на функции приводит к некоторому
# ухудшению читаемости кода ввиду не очевидности данных решений.
# АЖНО - никогда НЕ используйте указаьели на функции в ЛЮБЫХ структурах,
# которые, ДАЖЕ СИЛЬНО ТЕОРИТИЧЕСКИ, могут быть переданы на другой компьютер

from source import getPrintFunction as getFunc

nameList = ("Alex", "Alisa", "Max", "Yosha")
# funcPrint = functionPrint # Указатель на функцию

# func = getFunc(True)
# func(nameList)
#
# func = getFunc(False)
# func(nameList)
#
# func = getFunc(True)(nameList)

# funcPrint(nameList)

# Задача 1 - Пользователь вводит в строку математический прмер состоящий из числа, знака и числа
# Необходимо написать функцию, которая принимает в себя функцию, кооторая принимает в себя этот пример и возвращает ответ

from source import getMathFunc as getMath

def evalExample(example):
    temp = ""
    first = 0
    second = 0
    sign = ""

    for char in example:
        if char in '+-*/^':
            sign = char
            first = int(temp)
            temp = ""
        else:
            temp += char
    second = int(temp)
    func = getMath(sign)
    return func(first, second)

example = input("Введите математический пример: ")
print(f"Ответ: {example}={evalExample(example)}")


