def tempDict():
    '''
    Функция является хранилищем для словаря
    '''
    return {
        "hello": "bonjour",
        "play": "jouer",
        "something": "quelque chose"
    }

def addInfo(dictionaryEngFr):
    '''
    Функция отвечает за добавление новых данных в словарь
    '''
    choice = input("Выберете действие:\n 1) Добавить слова в словарь  \n 2) Назад в меню \n").lower()
    match choice:
        case "добавить слова в словарь" | "добавить" | "1":

            addKey = input("Введите слово на английском: ").lower()
            addValue = input("Введите слово на французском: ").lower()
            dictionaryEngFr[addKey] = addValue
            print(f" Eng: {addKey} - Fr: {addValue}")
            return addInfo(dictionaryEngFr)

        case "назад в меню" | "назад" | "2":

            return choiceAction(dictionaryEngFr)
        case _:

            print("Введена неверная команда \n")
            return

def showInfo(dictionaryEngFr):
    '''
    Функция отвечает за отображение данных, находящихся в словаре
    '''
    if not dictionaryEngFr:
        print("Словарь пуст \n")
        return choiceAction(dictionaryEngFr)
    else:
        print("Англо-французский словарь: ")
        count = 1
        for key in dictionaryEngFr:
            print(f"{count}) Eng: {key}, Fr: {dictionaryEngFr.get(key)}")
            count += 1
        print()
        return choiceAction(dictionaryEngFr)

def deleteInfo(dictionaryEngFr):
    '''
    Функция отвечает за удаление данных из словаря
    '''
    if not dictionaryEngFr:
        print("Словарь пуст \n")
        return choiceAction(dictionaryEngFr)
    else:
        choice = input("Выберете действие:\n 1) Удалить слово и его перевод \n 2) Очистить весь список\n 3) Назад в меню \n").lower()
        match choice:

            case "удалить слово и перевод слова" | "удалить" | "1":

                delKey = input("Введите слово на английском: ").lower()
                if delKey in dictionaryEngFr:
                    delValue = dictionaryEngFr.pop(delKey)
                    print(f" Eng: {delKey} Fr: {delValue} успешно удалены из словаря")
                else:
                    print("Нет такого слова")
                    return

            case "очистить весь список" | "очистить" | "2":

                checkPoint = input("Вы уверены, что хотите удалить весь список (Y/N)?  ").lower()
                if checkPoint == "y":
                    dictionaryEngFr.clear()
                    return
                else:
                    return

            case "назад в меню" | "назад" | "3":

                return choiceAction(dictionaryEngFr)
            case _:
                print("Введена неверная команда \n")
                return

def searchInfo(dictionaryEngFr):
    '''
    Функция отвечает за поиск данных в словаре
    '''
    if not dictionaryEngFr:
        print("Список пуст \n")
    else:
        choice = input("Выберете действие:\n 1) Найти слово и перевод \n 2) Назад в меню \n").lower()
        match choice:
            case "найти слово и перевод" | "найти" | "1":

                searchKey = input("Введите слово на английском: ").lower()
                if searchKey in dictionaryEngFr:
                    print(f"Eng: {searchKey}, Fr: {dictionaryEngFr[searchKey]}\n")
                else:
                    print("Нет такого слова")
                    return

            case "назад в меню" | "назад" | "2":

                return choiceAction(dictionaryEngFr)
            case _:
                print("Введена неверная команда \n")
                return

def changeInfo(dictionaryEngFr):
    '''
    Функция отвечает за изменения данных в словаре
    '''
    if not dictionaryEngFr:
        print("Список пуст \n")
    else:
        choice = input("Выберете действие:\n 1) Заменить ENG и FR перевод \n 2) Заменить ENG перевод \n 3) Заменить FR перевод \n 4) Назад в меню \n").lower()
        match choice:
            case "заменить eng и fr перевод" | "заменить eng и fr" | "1":

                changeInfo = input("Введите слово на английском: ").lower()
                if changeInfo in dictionaryEngFr:
                    delKey = changeInfo
                    delValue = dictionaryEngFr.pop(changeInfo)
                    addKey = input("Введите новое слово на английском: ").lower()
                    addValue = input("Введите новое слово на французском: ").lower()
                    dictionaryEngFr[addKey] = addValue
                    print(f"Данные изменены - Eng: {delKey} на {addKey}, Fr: {delValue} на {addValue} \n")
                    return
                else:
                    print("Нет такого слова")

            case "заменить eng перевод" | "заменить eng" | "2":

                changeKey = input("Введите слово на английском: ").lower()
                if changeKey in dictionaryEngFr:
                    delKey = changeKey
                    delValue = dictionaryEngFr.pop(changeKey)
                    addKey = input("Введите новое слово на английском: ").lower()
                    dictionaryEngFr[addKey] = delValue
                    print(f"Данные изменены - Eng: {delKey} на {addKey} \n")
                    return
                else:
                    print("Нет такого слова")

            case "заменить fr перевод" | "заменить fr" | "3":

                changeKey = input("Введите слово на английском: ").lower()
                if changeKey in dictionaryEngFr:
                    delValue = dictionaryEngFr[changeKey]
                    addValue = input("Введите новое слово на французском: ").lower()
                    dictionaryEngFr[changeKey] = addValue
                    print(f"Данные изменены - Fr: {delValue} на {addValue} \n")
                    return
                else:
                    print("Нет такого слова")


            case "назад в меню" | "назад" | "4":
                return choiceAction(dictionaryEngFr)

def choiceAction (dictionaryEngFr):
    '''
    Функция отвечает за маршрутизацию и перенаправляет в необходимые функции
    '''
    choice = input(
        "Выберите, необходимое действие:\n 1) Добавить данные\n 2) Удалить данные\n 3) Найти данные\n 4) Изменить данные\n 5) Показать список\n 6) Выход из программы\n").lower()
    while True:
        match choice:
            case "добавить данные" | "добавить" | "1":
                addInfo(dictionaryEngFr)
            case "удалить данные" | "удалить" | "2":
                deleteInfo(dictionaryEngFr)
            case "найти данные" | "найти" | "3":
                searchInfo(dictionaryEngFr)
            case "изменить данные" | "изменить"| "4":
                changeInfo(dictionaryEngFr)
            case "показать список" | "показать" | "5":
                showInfo(dictionaryEngFr)
            case "выход из программы" | "выход" | "6":
                print("До свидания!")
                exit()
            case _:
                print("Введена неверная команда \n")


def main ():
    '''
    Основная функция, связывающая хранилище данных (tempDict) и маршрутизатор (choiceAction)
    '''
    print("Приветствую, в данной программе представлен Англо-французский словарь:")
    dictionaryEngFr = tempDict()
    choiceAction(dictionaryEngFr)


main()