def tempDict():
    '''
    Функция является хранилищем для словаря
    '''
    return {
        "Майкл Джеффри Джордан": 198,
        "Тимофей Павлович Мозгов": 216,
        "Ярослав Игоревич Королёв": 208
    }

def addInfo(basketballPlayers):
    '''
    Функция отвечает за добавление новых данных в словарь
    '''
    choice = input("Выберете действие:\n 1) Добавить игрока  \n 2) Назад в меню \n").lower()
    match choice:
        case "добавить игрока" | "добавить" | "1":

            addKey = input("Введите ФИО баскетболиста: ")
            addValue = input("Введите рост игрока: ")
            addValue = int(addValue)
            basketballPlayers[addKey] = addValue
            print(f"{addKey} с ростом {addValue} см добавлен в список")
            return addInfo(basketballPlayers)

        case "назад в меню" | "назад" | "2":

            return choiceAction(basketballPlayers)
        case _:

            print("Введена неверная команда \n")
            return

def showInfo(basketballPlayers):
    '''
    Функция отвечает за отображение данных, находящихся в словаре
    '''
    if not basketballPlayers:
        print("Список пуст \n")
        return choiceAction(basketballPlayers)
    else:
        print("Список баскетболистов: ")
        count = 1
        for name in basketballPlayers:
            print(f"{count}) Баскетболист: {name}, Рост: {basketballPlayers.get(name)} см")
            count += 1
        print()
        return choiceAction(basketballPlayers)

def deleteInfo(basketballPLayers):
    '''
    Функция отвечает за удаление данных из словаря
    '''
    if not basketballPLayers:
        print("Cписок пуст \n")
        return choiceAction(basketballPLayers)
    else:
        choice = input("Выберете действие:\n 1) Удалить баскетболиста \n 2) Очистить весь список\n 3) Назад в меню \n").lower()
        match choice:

            case "удалить баскетболиста" | "удалить" | "1":

                delPlayer = input("Введите ФИО баскетболиста, которого хотите удалить: ")
                if delPlayer in basketballPLayers:
                    basketballPLayers.pop(delPlayer)
                    print(f"{delPlayer} успешно удален из списка")
                else:
                    print("Нет такого баскетболиста")
                    return

            case "очистить весь список" | "очистить" | "2":

                checkPoint = input("Вы уверены, что хотите удалить весь список (Y/N)?  ").lower()
                if checkPoint == "y":
                    basketballPLayers.clear()
                    return
                else:
                    return

            case "назад в меню" | "назад" | "3":

                return choiceAction(basketballPLayers)
            case _:
                print("Введена неверная команда \n")
                return

def searchInfo(basketballPLayers):
    '''
    Функция отвечает за поиск данных в словаре
    '''
    if not basketballPLayers:
        print("Список пуст \n")
    else:
        choice = input("Выберете действие:\n 1) Найти баскетболиста \n 2) Назад в меню \n").lower()
        match choice:
            case "найти баскетболиста" | "найти" | "1":

                searchName = input("Введите ФИО баскетболиста, которого хотите найти: ")
                if searchName in basketballPLayers:
                    print(f"Баскетболист: {searchName}, Рост: {basketballPLayers[searchName]} см\n")
                else:
                    print("Нет такого баскетболиста")
                    return

            case "назад в меню" | "назад" | "2":

                return choiceAction(basketballPLayers)
            case _:
                print("Введена неверная команда \n")
                return

def changeInfo(basketballPlayers):
    '''
    Функция отвечает за изменения данных в словаре
    '''
    if not basketballPlayers:
        print("Список пуст \n")
    else:
        choice = input("Выберете действие:\n 1) Заменить ФИО и рост баскетболиста \n 2) Заменить ФИО баскетболиста \n 3) Заменить рост баскетболиста \n 4) Назад в меню \n").lower()
        match choice:
            case "заменить фио и рост баскетболиста" | "заменить фио и рост" | "1":

                changeInfo = input("Введите ФИО баскетболиста: ")
                if changeInfo in basketballPlayers:
                    delKey = changeInfo
                    delValue = basketballPlayers.pop(changeInfo)
                    addKey = input("Введите новое ФИО баскетболиста: ")
                    addValue = input("Введите новый рост игрока: ")
                    addValue = int(addValue)
                    basketballPlayers[addKey] = addValue
                    print(f"Данные изменены - Баскетболист: {delKey} на {addKey}, Рост: {delValue} см на {addValue} см \n")
                    return
                else:
                    print("Нет такого баскетболиста")

            case "заменить фио баскетболиста" | "заменить фио" | "2":

                changeName = input("Введите ФИО баскетболиста: ")
                if changeName in basketballPlayers:
                    delKey = changeName
                    delValue = basketballPlayers.pop(changeName)
                    addKey = input("Введите новое ФИО баскетболиста: ")
                    basketballPlayers[addKey] = delValue
                    print(f"Данные изменены - Баскетболист: {delKey} на {addKey} \n")
                    return
                else:
                    print("Нет такого баскетболиста")

            case "заменить рост баскетболиста" | "заменить рост" | "3":

                changeName = input("Введите ФИО баскетболиста: ")
                if changeName in basketballPlayers:
                    delValue = basketballPlayers[changeName]
                    addValue = input("Введите новый рост баскетболиста: ")
                    addValue = int(addValue)
                    basketballPlayers[changeName] = addValue
                    print(f"Данные изменены - Баскетболист: {changeName}, Рост изменен с {delValue} см на {addValue} см \n")
                    return
                else:
                    print("Нет такого баскетболиста")


            case "назад в меню" | "назад" | "4":
                return choiceAction(basketballPlayers)

def choiceAction (basketballPlayers):
    '''
    Функция отвечает за маршрутизацию и перенаправляет в необходимые функции
    '''
    choice = input(
        "Выберите, необходимое действие:\n 1) Добавить данные\n 2) Удалить данные\n 3) Найти данные\n 4) Изменить данные\n 5) Показать список\n 6) Выход из программы\n").lower()
    while True:
        match choice:
            case "добавить данные" | "добавить" | "1":
                addInfo(basketballPlayers)
            case "удалить данные" | "удалить" | "2":
                deleteInfo(basketballPlayers)
            case "найти данные" | "найти" | "3":
                searchInfo(basketballPlayers)
            case "изменить данные" | "изменить"| "4":
                changeInfo(basketballPlayers)
            case "показать список" | "показать" | "5":
                showInfo(basketballPlayers)
            case "выход из программы" | "выход" | "6":
                print("До свидания!")
                exit()
            case _:
                print("Введена неверная команда \n")


def main ():
    '''
    Основная функция, связывающая хранилище данных (tempDict) и маршрутизатор (choiceAction)
    '''
    print("Приветствую, в данной программе содержится информация о баскетболистах (ФИО и рост баскетболиста):")
    basketballPLayers = tempDict()
    choiceAction(basketballPLayers)


main()