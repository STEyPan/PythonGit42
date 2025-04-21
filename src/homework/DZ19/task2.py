from random import randint

def makeRandomList() -> list:
    '''
    Функция генерирует список случайных чисел.
    :return: список случайных чисел (list)
    '''
    return [randint(-10,10) for _ in range(20)]

def minElement(numbers: list[int]) -> int:
    '''
    Функция принимает список чисел, и находит среди них минимальное.
    :param numbers: список чисел (list[int])
    :return: минимальное число (int)
    '''
    min = numbers[0]

    for num in numbers[1:]: # Начнем сразу с 2 элемента, так как первый уже обозначен, как минимальный
        if num < min:
            min = num

    return min

def maxElement(numbers: list[int]) -> int:
    '''
    Функция принимает список чисел, и находит среди них максимальное.
    :param numbers: список чисел (list[int])
    :return: максимальное число (int)
    '''
    max = numbers[0]

    for num in numbers[1:]:
        if num > max:
            max = num

    return max

def countNegativeNumbers(numbers: list[int]) -> int:
    '''
    Функция принимает список чисел, и подсчитывает количество чисел меньше нуля.
    :param numbers: список чисел (list[int])
    :return: количество чисел меньше нуля (int)
    '''
    countNegative = 0

    for num in numbers:
        if num < 0:
            countNegative += 1

    return countNegative

def countPositiveNumbers(numbers: list[int]) -> int:
    '''
    Функция принимает список чисел, и подсчитывает количество чисел больше нуля.
    :param numbers: список чисел (list[int])
    :return: количество чисел больше нуля (int)
    '''
    countPositive = 0

    for num in numbers:
        if num > 0:
            countPositive += 1

    return countPositive

def countEqualZero(numbers: list[int]) -> int:
    '''
    Функция принимает список чисел, и подсчитывает количество чисел равных нулю.
    :param numbers: список чисел (list[int])
    :return: количество чисел равных нулю (int)
    '''
    countZero = 0

    for num in numbers:
        if num == 0:
            countZero += 1

    return countZero

def printResultFilters() -> None:
    '''
    Функция инициализирует список случайных чисел, и выводит результат нахождения:
    минимума, максимума, количества чисел больше, меньше и равных нулю
    из списка случайных чисел.
    :return: None
    '''
    randomList = makeRandomList()
    print(randomList)
    print(f"Минимальное значение: {minElement(randomList)}")
    print(f"Максимальное значение: {maxElement(randomList)}")
    print(f"Количество отрицательных элементов: "
          f"{countNegativeNumbers(randomList)}")
    print(f"Количество положительных элементов: "
          f"{countPositiveNumbers(randomList)}")
    print(f"Количество нулевых элементов: "
          f"{countEqualZero(randomList)}")


# def main(): # Отработка лямбда-функции и функции filter
#     randomList = makeRandomList()
#     print(randomList)
#     print(f"Минимальное значение: {min(randomList)}")
#     print(f"Максимальное значение: {max(randomList)}")
#     print(f"Количество отрицательных элементов: "
#           f"{len(list(filter(lambda num: num < 0, randomList)))}")
#     print(f"Количество положительных элементов: "
#           f"{len(list(filter(lambda num: num > 0, randomList)))}")
#     print(f"Количество нулевых элементов: "
#           f"{len(list(filter(lambda num: num == 0, randomList)))}")

