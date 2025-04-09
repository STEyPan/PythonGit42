from random import randint

def makeNumbers(begin: int = 1, end: int = 10) -> list:
    '''
    Функция генерирует случайные числа и добавляет их в список.
    :return: список из случайных чисел (list)
    '''
    numbers = []
    for i in range(10):
        numbers.append(randint(begin,end))
    return numbers

def multiplyNumbers(numbers: list) -> int:
    '''
    Функция получает в качестве параметра список чисел (numbers)
    и перемножает все числа данного списка друг на друга.
    :param numbers: список случайных чисел (list)
    :return: результат умножения всех чисел (int)
    '''
    multiply = 1
    for num in numbers:
        multiply = num * multiply
    return multiply

def getMinNumbers(numbers: list) -> int:
    '''
    Функция получает в качестве параметра список чисел (numbers)
    и находит минимальное число в данном списке.
    :param numbers: список случайных чисел (list)
    :return: минимальное число из списка (int)
    '''
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

def countPrimeNumbers(numbers: int) -> int:
    '''
    Функция получает в качестве параметра список чисел (numbers)
    и находит количество простых чисел в ней.
    :param numbers: список случайных чисел (list)
    :return: количество простых чисел в списке (int)
    '''
    primeNumbers = []
    for num in numbers:
        if num <= 1:
            continue
        isPrime = True
        for divider in range(2, num):
            if num % divider == 0:
                isPrime = False
                break
        if isPrime:
            primeNumbers.append(num)

    return len(primeNumbers)

def delElementInList(numbers: list, delElem: int) -> int:
    '''
    Функция принимает в качестве параметров список чисел (numbers) и целое число (delElem),
    удаляет искомый элемент из списка и подсчитывает количество удаленных элементов.
    :param numbers: список случайных чисел (list)
    :param delElem: искомый элемент (int)
    :return: количество удаленных элементов из списка numbers (int)
    '''
    delList = []
    for num in numbers:
        if num == delElem:
            delList.append(numbers.remove(num))
    return len(delList)

def intersectionLists(first: list, second: list) -> list:
    '''
    Функция получает в качестве параметров два списка чисел (first) and (second)
    и находит общие элементы этих двух списков
    :param first: список случайных чисел (list)
    :param second: список случайных чисел (list)
    :return: список с общими элементами двух списков (list)
    '''
    return list(set(first) & set(second))

def evalDegree(numbers: list, degree: int) -> list:
    '''
    Функция принимает в качестве параметров список чисел (numbers) и целое число (degree)
    и возводит каждый элемент из списка numbers в степень degree
    :param numbers: список случайных чисел (list)
    :param degree: число необходимое для возведения в степень (int)
    :return: список чисел возведенных в степень (degree)
    '''
    degreesList = []
    for num in numbers:
        degreesList.append(num ** degree)
    return degreesList

def printResult() -> None:
    '''
    Функция инициализирует три списка случайных чисел и две переменные,
    чтобы использовать их в качестве параметров в других функциях,
    и вывести результат выполнения функций.
    :return: None
    '''
    fisrtNumbers = makeNumbers(1, 4)
    secondNumbers = makeNumbers(-10, 10)
    thirdNumbers = makeNumbers(-10, 100)
    elem = 3
    degree = 4
    print(f"Произведение элементов списка {fisrtNumbers}:"
          f" = {multiplyNumbers(fisrtNumbers)}")
    print(f"Минимальное число из списка {secondNumbers}:"
          f" = {getMinNumbers(secondNumbers)}")
    print(f"Количество простых чисел из списка {thirdNumbers}:"
          f" = {countPrimeNumbers(thirdNumbers)}")
    print(f"Количество удаленных элементов {elem} из списка {fisrtNumbers}:"
          f" = {delElementInList(fisrtNumbers, elem)}")
    print(f"Общие элементы списков {fisrtNumbers}\t&\t{secondNumbers}:"
          f" = {intersectionLists(fisrtNumbers, secondNumbers)}")
    print(f"Числа из списка {fisrtNumbers} в степени {degree} = {evalDegree(fisrtNumbers, degree)}")