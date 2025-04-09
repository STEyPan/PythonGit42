def printText() -> None:
    '''
    Функция выводит текст в консоль
    :return: None
    '''
    text = ("Don't compare yourself with anyone in this world...\n"
            " if you do so, you are insulting yourself.")
    subText = "Bill Gates"
    print(f' "{text}"\n\t\t\t\t\t\t\t\t\t\t\t{subText}')

# printText() #task1

def isEvenNumbers(begin: int, stop: int) -> str:
    '''
    Функция принимает в качестве параметров два числа: (begin) and (stop),
    которые являются границами диапазона. Далее функция находит среди этого
    диапазона четные числа, и возвращает их в качестве строки (str)
    :param begin: начало диапазона чисел (int)
    :param stop: конец диапазона чисел (int)
    :return: найденные четные числа (str)
    '''
    evens = ""
    for num in range(begin, stop+1):
        if num % 2 == 0:
            evens += f"{num}, "
    return evens[:-2]

def task2() -> None:
    '''
    Функция запрашивает ввести начало и конец диапазона чисел.
    Далее она передает эти переменные в функцию isEvenNumbers()
    и выводит результат этой функции.
    :return: None
    '''
    start = int(input("Введите начальное число из диапазона: "))
    stop = int(input("Введите конечное число из диапазона: "))
    print(isEvenNumbers(start, stop))

# task2()

def printSquare(side: int, sign: str, fill: bool = True) -> None:
    '''
    Функция принимает следующие параметры: длину стороны квадрата (side),
    символ для заполнения (sign) и закрашен ли квадрат (fill).
    В зависимости от введенных данных квадрат выводится в консоль.
    :param side: длина стороны квадрата (int)
    :param sign: символ для заполнения (str)
    :param fill: закрашен ли квадрат (bool)
    :return: None
    '''
    sign = f" {sign} "
    void = "   "
    for row in range(side):
        if fill:
            print(f"{sign*side}")
        else:
            if row == 0 or row == side-1:
                print(f"{sign * side}")
            else:
                print(f"{sign}{void * (side - 2)}{sign}")


def task3() -> None:
    '''
    Функция запрашивает у пользователя ввести длину стороны квадрата,
    символ для заполнения квадрата, и нужно ли закрашивать квадрат.
    Далее она передает эти данные в функцию printSquare()
    :return: None
    '''
    side = int(input("Введите длину стороны квадрата: "))
    sign = input("Введите символ для заполнения квадрата: ")
    fill = input("Закрасить квадрат? (y/n): ")
    print()
    if fill.lower() == "y":
        fill = True
    else:
        fill = False

    printSquare(side, sign, fill)

# task3()


def minNumber(numbers: list) -> int:
    '''
    Функция принимает в качестве параметра список чисел (numbers)
     и находит минимальное из этих чисел
    :param numbers: список чисел (list)
    :return: минимальное число (int)
    '''
    # return min(numbers)
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

def task4() -> None:
    '''
    Функция запрашивает у пользователя ввести 5 чисел,
    далее формирует из список этих чисел, и передает их в функцию minNumbers()
    :return: None
    '''
    count = 0
    numbers = list()
    while count != 5:
        count += 1
        number = int(input(f"Введите {count} число: "))
        numbers.append(number)
    print(f"Минимальное из 5 чисел: {minNumber(numbers)}")

# task4()

def multiplyNumbers(begin: int, stop: int) -> int:
    '''
    Функция получает в качестве параметров два числа (begin) and (stop),
    которые являются границами диапазона. Далее она проверяет, если (begin) > (stop),
    то происходит обмен значениями между этими переменными.
    После этого функция находит произведение всех чисел в заданном диапазоне.
    :param begin: начало диапазона (int)
    :param stop: конец диапазона (int)
    :return: результат произведения чисел (int)
    '''
    if begin > stop:
        begin, stop = stop, begin
    multiply = 1
    for num in range(begin, stop+1):
        multiply = num * multiply

    return multiply

def task5() -> None:
    '''
    Фцнкция запрашивает от пользователя ввести начало и конец дипазаона чисел.
    Далее эти данные она передает в функцию multiplyNumbers(),
    и выводит результат этой функции.
    :return: None
    '''
    begin = int(input("Введите начальное значение дипазона: "))
    stop = int(input("Введите конечное значение дипазона: "))
    print(f"Произведение чисел в заданном диапазоне = {multiplyNumbers(begin, stop)}")

# task5()

def countNumber(number: str) -> int:
    '''
    Функция принимает число в виде строки (number),
    и подсчитывает количество элементов в этом числе.
    :param number: вводимое число (str)
    :return: количество элементов в числе (int)
    '''
    # return len(number)
    count = 0

    for elem in number:
        if elem not in ".,":
            count += 1

    return count

def task6() -> None:
    '''
    Функция запрашивает у пользователя ввести число. Далее в виде строки
    это число передается в функцию countNumber() и выводит результат этой функции.
    :return: None
    '''
    number = input("Введите любое число: ")
    print(f"Количество цифр в числе {number} = {countNumber(number)}")

# task6()

def isPalindrome(native: str) -> bool:
    '''
    Функция принимает число в виде строки (number), зеркально разворачивает
    его и заносит результат в переменную (reverse). Далее сравнивает два
    числа (native) and (reverse), и если они равны возвращает True
    :param native: вводимое число (str)
    :return: результат сравнения
    '''
    reverse = ""
    for i in range(1, len(native) + 1):
        reverse += native[-i]
    if reverse == native:
        return True

def task7() -> None:
    '''
    Функция запрашивает у пользователя ввести число. Далее в виде строки
    это число передается в функцию isPalindrome(). В зависимости от
    возвращаемого значения, выводит сообщение.
    :return:
    '''
    number = input("Введите любое целое число: ")
    if isPalindrome(number):
        print(f"Это палиндром - {number}")
    else:
        print(f"Это не палиндром - {number}")

task7()
