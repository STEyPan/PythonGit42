def lowerToUp (nativeText: str, keyWord: str):
    '''
    Функция меняет регистр ключевых слов (keyWord) на ВЕРХНИЙ в тексте (nativeText)
    :param nativeText: вводимый текст
    :param keyWord: ключевое слово
    :return:
    '''
    keyWord = keyWord.lower()
    keyList = keyWord.split(',')
    for word in keyList:
        nativeText = nativeText.replace(word, word.upper())
        # C помощью метода replace заменяем ключевое слово нижнего регистра
        # и заменяем на слово в ВЕРХНЕМ регистре

    print(f"Измененный текст: {nativeText}")


nativeText = input(f"Введите Ваш текст: ")
keyWord = input(f"Введите через запятую слова из данного текста, которые Вы хотите выделить: ")
lowerToUp(nativeText, keyWord)