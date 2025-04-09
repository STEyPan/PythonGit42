from random import randint

def makeRandomTuple() -> tuple:
    '''
    Функция генерирует кортеж со случайными числами в заданом диапазоне
    :return: tuple(кортеж)
    '''
    numberList = []
    for i in range (0, 10):
        numberList.append(randint(0, 5))
    return tuple(numberList)

def intersectionElement(first: tuple, second: tuple, third: tuple) -> list: #task1
    '''
    Функция находит общие элементы, которые есть во всех кортежах
    :param first: кортеж с числами (int)
    :param second: кортеж с числами (int)
    :param third: кортеж с числами (int)
    :return: list: список общих элементов
    '''
    intersectionList = []
    for elem in first:
        if elem in second and elem in third:
            intersectionList.append(elem)
    return list(set(intersectionList))

# def intersectionElement(first: tuple, second: tuple, third: tuple): # более элегантный вариант функции
#     return list(set(first) & set(second) & set(third))

def differenceElement(first: tuple, second: tuple, third: tuple) -> tuple: #task2
    '''
    Функция находит элементы, которые уникальны для каждого списка
    :param first: кортеж с числами (int)
    :param second: кортеж с числами (int)
    :param third: кортеж с числами (int)
    :return: tuple: кортеж содержащий 4 списка:
    уникальные элементы первого, второго, третьего и всех трех кортежей
    '''
    differenceListFirst = []
    differenceListSecond = []
    differenceListThird = []
    for elem in first:
        if elem not in second and elem not in third:
            differenceListFirst.append(elem)

    for elem in second:
        if elem not in first and elem not in third:
            differenceListSecond.append(elem)

    for elem in third:
        if elem not in first and elem not in second:
            differenceListThird.append(elem)

    generalDifference = set(differenceListFirst + differenceListSecond + differenceListThird)

    return (list(set(differenceListFirst)), list(set(differenceListSecond)),
            list(set(differenceListThird)), list(generalDifference))

# def differenceElement(first: tuple, second: tuple, third: tuple):
# более элегантный вариант функции,
# но получаем только общий список уникальных элементов
#     return list(set(first) ^ set(second) ^ set(third))

def isSamePosition(first: tuple, second: tuple, third: tuple) -> list: #task3
    '''
    Функция проверяет есть ли элемент в каждом из кортежей,
    и находится ли он на той же позиции
    :param first: кортеж с числами (int)
    :param second: кортеж с числами (int)
    :param third: кортеж с числами (int)
    :return: list: список с индексом найденого элемента и сам элемент
    '''
    positionList = []
    for i in range(min(len(first), len(second), len(third))):
        if first[i] == second[i] == third[i]:
            positionList.append(f"i[{i}]:{first[i]}")
    return positionList


def main() -> None:
    '''
    Функция инициирует 3 кортежа и выводит результаты выполненных функций
    :return: None
    '''
    tupleFirst = makeRandomTuple()
    tupleSecond = makeRandomTuple()
    tupleThird = (1, 3, 1, 4, 4, 5, 5, 1, 5, 4, 5, 20, 40)
    print(f"Первый кортеж - {tupleFirst}\nВторой кортеж - {tupleSecond}\nТретий кортеж - {tupleThird}")
    print(f"Общие элементы кортежей - {intersectionElement(tupleFirst, tupleSecond, tupleThird)}")
    firstDiff, secondDiff, thirdDiff, generalDiff = differenceElement(tupleFirst, tupleSecond, tupleThird)
    print(f"Уникальные элементы первого кортежа - {firstDiff}\n"
          f"Уникальные элементы второго кортежа - {secondDiff}\n"
          f"Уникальные элементы третьего кортежа - {thirdDiff}\n"
          f"Уникальные элементы всех кортежей - {generalDiff}")
    # print(f"Уникальные элементы всех кортежей - {differenceElement(tupleFirst, tupleSecond, tupleThird)}")
    print(f"Элементы на одинаковых позициях - {isSamePosition(tupleFirst, tupleSecond, tupleThird)}")

main()