def checkPalidrom (native: str):
    '''
    Функция проверяет вводимое слово или слова (native)
    на принадлежность к палидрому
    :param native: вводимое слово или слова
    :return:
    '''
    nativeCopy = native.lower()
    nativeList = nativeCopy.split()
    nativeCopy = ''.join(nativeList)
    # переводим список в строку
    reversedText = ''.join(reversed(nativeCopy))
    # переводим список в строку и переворачиваем её
    if reversedText == nativeCopy:
        print(f"{native} - это палидром")
    else:
        print(f"{native} - это не палидром")


nativeText = input("Введите любой текст: ")
checkPalidrom(nativeText)