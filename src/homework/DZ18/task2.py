import random


def makeSecretList():
    '''
    Функция генерирует список из ЧЕТЫРЕХ неповторяющихся цифр от 0 до 9
    :return:
    '''
    return random.sample(range(0, 10), 4)
    # генерируем 4 цифры от 0 до 9, параметр counts по-умолчанию 0 (цифры не будут повторяться)


def playGame(secretList, attempts=0):
    '''
    Функция отвечает за основную логику игры. Используется сгенерированный список (secretList)
    и количество попыток (attempts)
    :param secretList: внешний список из функции (main)
    :param attempts: Количество попыток (по-умолчанию - 0)
    :return:
    '''
    playerInput = input(f"Введите целое 4-значное число: ")
    if len(playerInput) == 4 and playerInput.isdigit():
        # Убеждаемся, что пользователь ввел ЧЕТЫРЕ ЦИФРЫ, а не три или пять символов
        playerList = [int(digit) for digit in playerInput]
        # генератор списка, который проходит по каждому символу (цифре)
        # в строке playerInput, преобразует его в целое число с помощью int(digit)
    else:
        print(f"Введите корректное 4-значное число")
        return playGame(secretList)

    attempts += 1

    cows = sum(1 for i in range(4) if secretList[i] == playerList[i])
    # Эта функция генерирует последовательность чисел от 0 до 3 (всего 4 числа).
    # Условие проверяет, равны ли элементы на позиции i в обоих списках.
    # Если они равны, то добавляется 1 в последовательность.
    # sum() - суммирует количество единиц
    # Получаем "коров" - cows

    # cows = 0       # Более развернутый вариант функции
    # for i in range(4):
    #     if secretList[i] == playerList[i]:
    #         cows += 1

    commonValues = set(secretList) & set(playerList)
    # Превращаем списки в множества и находим общие значения
    bulls = len(commonValues) - cows
    # Считаем количество общих значений и вычитаем коров (cows) и получаем быков (bulls)

    if cows == 4:
        print(f"Победа! Вы угадали число за {attempts} попыток")
    else:
        print(f"Быки: {bulls}. Коровы: {cows} Попробуйте ещё раз!")
        return playGame(secretList, attempts)


def main():
    '''
    Основная функция, которая передает значение из функции makeSecretList в playGame.
    Также функция выводит сообщение перед началом игры, чтобы игрок знал, что нужно делать.
    :return:
    '''
    secretList = makeSecretList()
    print(secretList) #Для отладки
    print(f"Я загадал 4-значное число, угадай его! Быки - сколько цифр числа угадано. Коровы - сколько цифр угадано и стоит на нужном месте")
    playGame(secretList)


main()