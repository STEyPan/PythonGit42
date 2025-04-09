def tempDict():
    '''
    Функция является хранилищем для словаря
    '''
    return {
        "Петров Василий Иванович": {"телефон": "89812344925",
                                    "email": "petrov@yandex.ru",
                                    "должность": "начальник отдела антимеметики",
                                    "кабинет": "238",
                                    "skype": "petrov78"},
        "Прыгунов Андрей Альбертович": {"телефон": "89802345470",
                                        "email": "jump_andy@gamil.com",
                                        "должность": "заместитель начальника отдела антимеметики",
                                        "кабинет": "238",
                                        "skype": "jumpandy007"},
        "Васильева Алина Евгеньевна": {"телефон": "898066627",
                                        "email": "alin4ikEEE@mail.ru",
                                        "должность": "секретарь отдела антимеметики",
                                        "кабинет": "238",
                                        "skype": "alinavas99"}
    }

def addInfo(personalInfo):
    '''
    Функция отвечает за добавление новых данных в словарь
    '''
    choice = input("Выберете действие:\n 1) Добавить нового сотрудника \n 2) Назад в меню\n").lower()
    match choice:
        case "добавить нового сотрудника" | "добавить" | "1":

            addName = input("Введите ФИО сотрудника: ")
            addPhone = input("Введите телефон сотрудника: ")
            addEmail = input("Введите Email сотрудника: ")
            addPost = input("Введите должность сотрудника: ")
            addCabinet = input("Введите номер кабинета сотрудника: ")
            addSkype = input("Введите skype сотрудника: ")
            personalInfo[addName] = {"телефон": addPhone,
                                     "email": addEmail,
                                     "должность": addPost,
                                     "кабинет": addCabinet,
                                     "skype":addSkype}
            print(f" Сотрудник: {addName} - добавлен в базу")
            return addInfo(personalInfo)

        case "назад в меню" | "назад" | "2":

            return choiceAction(personalInfo)
        case _:

            print("Введена неверная команда \n")
            return

def showInfo(personalInfo):
    '''
    Функция отвечает за отображение данных, находящихся в словаре
    '''
    if not personalInfo:
        print("База данных пуста \n")
        return choiceAction(personalInfo)
    else:
        print("Данные о сотрудниках: \n")
        count = 1
        for key in personalInfo:
            print(f"{count}) Сотрудник: {key}")
            print(f"Номер телефона: {personalInfo[key]["телефон"]}")
            print(f"Email: {personalInfo[key]["email"]}")
            print(f"Должность: {personalInfo[key]["должность"]}")
            print(f"Кабинет: {personalInfo[key]["кабинет"]}")
            print(f"Skype: {personalInfo[key]["skype"]} \n")
            count += 1
        print()
        return choiceAction(personalInfo)

def deleteInfo(personalInfo):
    '''
    Функция отвечает за удаление данных из словаря
    '''
    if not personalInfo:
        print("База данных пуста \n")
        return choiceAction(personalInfo)
    else:
        print("")
        choice = input("Выберете действие:\n 1) Удалить сотрудника из базы \n 2) Очистить весь список\n 3) Назад в меню \n").lower()
        match choice:

            case "удалить сотрудника" | "удалить" | "1":

                delKey = input("Введите ФИО сотрудника: ")
                if delKey in personalInfo:
                    personalInfo.pop(delKey)
                    print(f" Сотрудник: {delKey} успешно удален(а) из базы")
                else:
                    print("Сотрудник не найден")
                    return

            case "очистить весь список" | "очистить" | "2":

                checkPoint = input("Вы уверены, что хотите удалить весь список (Y/N)?  ").lower()
                if checkPoint == "y":
                    personalInfo.clear()
                    return
                else:
                    return

            case "назад в меню" | "назад" | "3":

                return choiceAction(personalInfo)
            case _:
                print("Введена неверная команда \n")
                return

def searchInfo(personalInfo):
    '''
    Функция отвечает за поиск данных в словаре
    '''
    if not personalInfo:
        print("База данных пуста \n")
        return
    else:
        choice = input("Выберете действие:\n 1) Найти сотрудника \n 2) Назад в меню \n").lower()
        match choice:
            case "найти сотрудника" | "найти" | "1":

                searchKey = input("Введите ФИО сотрудника: ")
                if searchKey in personalInfo:
                    print(f"Сотрудник: {searchKey}")
                    print(f"Номер телефона: {personalInfo[searchKey]["телефон"]}")
                    print(f"Email: {personalInfo[searchKey]["email"]}")
                    print(f"Должность: {personalInfo[searchKey]["должность"]}")
                    print(f"Кабинет: {personalInfo[searchKey]["кабинет"]}")
                    print(f"Skype: {personalInfo[searchKey]["skype"]} \n")
                else:
                    print("Сотрудник не найден")
                    return

            case "назад в меню" | "назад" | "2":

                return choiceAction(personalInfo)
            case _:
                print("Введена неверная команда \n")
                return

def changeInfo(personalInfo):
    '''
    Функция отвечает за предварительный ввод ФИО сотрудника и выбор подходящего действия
    '''
    if not personalInfo:
        print("База данных пуста \n")
        return
    else:
        getName = input("Введите ФИО сотрудника: ")
        if getName in personalInfo:
            changeInfoMain(personalInfo, getName)
        else:
            print("Сотрудник не найден")
            return

def changeInfoMain(personalInfo, getName):
    '''
    Функция отвечает за изменения данных в словаре
    '''

    commands = ["Заменить ФИО сотрудника", "Заменить номер телефона", "Заменить Email", "Заменить должность",
                "Заменить кабинет", "Заменить Skype", "Выбрать сотрудника", "Назад в меню"]
    print("Выберете действие: ")
    count = 1
    for command in commands:
        print(f" {count}) {command}")
        count += 1
    choice = input("").lower()

    match choice:
        case "заменить фио сотрудника" | "заменить фио" | "1":

            delName = getName
            delInfo = personalInfo.pop(getName)
            addName = input("Введите новое ФИО сотрудника: ")
            personalInfo[addName] = delInfo
            print(f"Данные изменены - {delName} на {addName} \n")
            return

        case "заменить номер телефона" | "заменить номер" | "2":

            delPhone = personalInfo[getName]["телефон"]
            addPhone = input("Введите новый номер телефона: ")
            personalInfo[getName]["телефон"] = addPhone
            print(f"Данные изменены - телефон: {delPhone} на {addPhone} \n")
            return changeInfoMain(personalInfo, getName)

        case "заменить Email" | "3":

            delMail = personalInfo[getName]["email"]
            addMail = input("Введите новый Email: ")
            personalInfo[getName]["email"] = addMail
            print(f"Данные изменены - Email: {delMail} на {addMail} \n")
            return changeInfoMain(personalInfo, getName)

        case "заменить должность" | "4":

            delPost = personalInfo[getName]["должность"]
            addPost = input("Введите новую должность: ")
            personalInfo[getName]["должность"] = addPost
            print(f"Данные изменены - должность: {delPost} на {addPost} \n")
            return changeInfoMain(personalInfo, getName)

        case "заменить кабинет" | "5":

            delCabinet = personalInfo[getName]["кабинет"]
            addCabinet = input("Введите новый кабинет: ")
            personalInfo[getName]["кабинет"] = addCabinet
            print(f"Данные изменены - кабинет: {delCabinet} на {addCabinet} \n")
            return changeInfoMain(personalInfo, getName)

        case "заменить skype" | "6":

            delSkype = personalInfo[getName]["skype"]
            addSkype = input("Введите новый skype: ")
            personalInfo[getName]["skype"] = addSkype
            print(f"Данные изменены - skype: {delSkype} на {addSkype} \n")
            return changeInfoMain(personalInfo, getName)

        case "выбрать сотрудника" | "7":
            return changeInfo(personalInfo)

        case "назад в меню" | "назад" | "8":
            return choiceAction(personalInfo)
        case _:
            print("Введена неверная команда \n")
            return choiceAction(personalInfo)

def choiceAction (personalInfo):
    '''
    Функция отвечает за маршрутизацию и перенаправляет в необходимые функции
    '''
    commands = ["Добавить данные","Удалить данные","Найти данные", "Изменить данные", "Показать список", "Выход из программы"]
    print("Выберите, необходимое действие:")
    count = 1
    for command in commands:
        print(f" {count}) {command}")
        count += 1
    choice = input("").lower()
    while True:
        match choice:
            case "добавить данные" | "добавить" | "1":
                addInfo(personalInfo)
            case "удалить данные" | "удалить" | "2":
                deleteInfo(personalInfo)
            case "найти данные" | "найти" | "3":
                searchInfo(personalInfo)
            case "изменить данные" | "изменить"| "4":
                changeInfo(personalInfo)
            case "показать список" | "показать" | "5":
                showInfo(personalInfo)
            case "выход из программы" | "выход" | "6":
                print("До свидания!")
                exit()
            case _:
                print("Введена неверная команда \n")


def main ():
    '''
    Основная функция, связывающая хранилище данных (tempDict) и маршрутизатор (choiceAction)
    '''
    print("Приветствую, в данной программе под названием 'Фирма' хранится информация о персонале:")
    personalInfo = tempDict()
    choiceAction(personalInfo)


main()