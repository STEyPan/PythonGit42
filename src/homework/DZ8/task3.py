import re


def countingSentece(text: str):
    '''
    Функция считает количество предложений в тексте (text)
    :param text: вводимый текст
    :return:
    '''
    textList = re.split(r'[!?.]', text)
    # Использую re.split и регулярные выражения, чтобы исключить сразу несколько знаков
    if len(textList) == 1:
        lengthList = len(textList)
        print(f"Количество предложений: {lengthList}")
    else:
        textList.pop()
        lengthList = len(textList)
        print(f"Количество предложений: {lengthList}")



text = input(f"Введите текст состоящий из нескольких предложений: ")
countingSentece(text)