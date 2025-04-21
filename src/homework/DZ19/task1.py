def splitExample(example: str) -> (int, float):
    '''
    Функция принимает математический пример(example), разделяет его на <число> <знак> <число>.
    И возвращает первое(first), второе(second) число и знак(sign)
    :param example: математический пример (str)
    :return: первое число(int), второе число(int), знак(str)
    '''
    first = 0
    second = 0
    sign = ""
    temp = ""

    for char in example:
        if char not in "1234567890":
            first = int(temp)
            sign = char
            temp = ""
        else:
            temp += char
    second = int(temp)
    return first, second, sign


def calculator(example) -> (int, float, None):
    '''
    Функция принимает математический пример (example). Получает результаты
    работы функции splitExample(). В зависимости от полученного знака,
    производит математическую операцию.
    :param example: математический пример (str)
    :return: результат математической операции (int, float) или None
    '''
    first, second, sign = splitExample(example)
    match sign:
        case "+":
            return first + second
        case "-":
            return first - second
        case "/":
            return first / second
        case "*":
            return first * second
        case "^":
            return first ** second
        case _: print(f"Нет такой математической операции - {sign}")


def printCalcResult() -> None:
    '''
    Функция запрашивает у пользователя ввести математический пример.
    Далее результат ввода передается в функцию splitExample().
    И если из функции calculator возвращается не None,
    то выводится результат математической операции.
    :return: None
    '''
    example = input("Введите математический пример: ")
    splitExample(example)
    result = calculator(example)
    if result is not None:
        print(f"{example}={result}")