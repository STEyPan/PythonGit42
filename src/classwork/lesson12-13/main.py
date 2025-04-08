# Задание 1
# Пользователь вводит строчку текста и символ, необходимо написать функцию, которая проходится
# по строке и считает кол-во раз


def CountSignList(text, sign, count = 0):
    for item in text:
        if item.lower() == sign.lower():
            count += 1
    return count


def task1():
    text = input("Введите любой текст: ")
    sign = input("Введите любой символ: ")
    print(f"Символ {sign} встречается {CountSignList(text, sign)}")

# task1()


# Задание 2
# Написать функции, первая - создает полную таблицу умножения, вторая выводит её на экран
# Таблица должна хранится в виде списка списков


def makeMultiTable():
    table = []
    for first in range(1,11):
        subTable = []
        for second in range(1,11):
            subTable.append(f"{first}*{second}={first*second}")
        table.append(subTable)

    return table


def printTable(table):
    for list in table:
        for num in list:
            print(f"{num:7}", end="  ")
        print()

# printTable(makeMultiTable())

# Задание 3
# Пользователь вводит последовательность чисел. Необходимо написать функции,
# которые принимают в себя этот список и возвращают другой список, пока не встретиться -1:
# 1) Возвращает факториалы этих чисел
# 2) Возвращает квадраты этих чисел
# 3) Возвращает только четные числа
# 4) Возвращает только минимальное, максимальное и среднее арифметическое в виде списка


def factorialNumbers(numbers: list):
    numbersFcList = []
    fcNumber = 1
    for number in numbers:
        while number > 1:
            fcNumber *= number
            number -= 1
        numbersFcList.append(fcNumber)
    return numbersFcList

def multiplyNumbers(numbers):
    multiplyList = []
    for number in numbers:
        multiplyList.append(number*number)
    return multiplyList

def evenList(numbers):
    evenList = []
    for number in numbers:
        if number % 2 == 0:
            evenList.append(number)
    return evenList

def maxMinMidList(numbers):
    maxNumber = numbers[0]
    minNumber = numbers[0]
    middleNumber = 0
    maxNumbersList = []
    minNumbersList = []
    middleNumbersList = []
    for number in numbers:
        middleNumber += number
        middleNumbersList.append(middleNumber / 2)
        if number > maxNumber:
            maxNumber = number
        maxNumbersList.append(maxNumber)
        if number < minNumber:
            minNumber = number
        minNumbersList.append(minNumber)
    return maxNumbersList, minNumbersList, middleNumbersList
# Пупупу

def task3() -> list:
    numbers = []
    number = 0
    while number != -1:
        number = int(input("Введите последовательность чисел: "))
        numbers.append(number)
    else:
        print(f"Факториал чисел - {factorialNumbers(numbers)}")
        print(f"Квадраты чисел - {multiplyNumbers(numbers)}")
        print(f"Четные числа - {evenList(numbers)}")
        max, min, mid = maxMinMidList(numbers)
        print(f"Максимальные числа - {max}\nМиниальные числа - {min} \nСреднее арифметическое - {mid} \n")


task3()






