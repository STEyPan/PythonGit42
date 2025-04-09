def tempDict():
    '''
    Функция является хранилищем для словаря
    '''
    return {
        "Буря мечей": {"автор": "Джордж Р. Р. Мартин",
                       "жанр": "эпическое фэнтези",
                       "год выпуска": "2004",
                       "количество страниц": "960",
                       "издательство": "АСТ"},

        "Дюна": {"автор": "Фрэнк Герберт",
                 "жанр": "научная фантастика",
                 "год выпуска": "2020",
                 "количество страниц": "768",
                 "издательство": "АСТ"},

        "Война и мир": {"автор": "Лев Николаевич Толстой",
                       "жанр": "роман-эпопея",
                       "год выпуска": "2023",
                       "количество страниц": "1408",
                       "издательство": "АСТ"},
    }

def addInfo(library):
    '''
    Функция отвечает за добавление новых данных в словарь
    '''
    choice = input("Выберете действие:\n 1) Добавить новую книгу \n 2) Назад в меню\n").lower()
    match choice:
        case "добавить новую книгу" | "добавить" | "1":

            addBook = input("Введите название книги: ")
            addWriter = input("Введите ФИО автора книги: ")
            addGenre= input("Введите жанр произведения: ")
            addRelease = input("Введите год выпуска книги: ")
            addPages = input("Введите количество страницы: ")
            addPublisher = input("Введите название издательства: ")
            library[addBook] = {"автор": addWriter,
                                "жанр": addGenre,
                                "год выпуска": addRelease,
                                "количество страниц": addPages,
                                "издательство":addPublisher}
            print(f" Книга: {addBook} - добавлена в базу")
            return addInfo(library)

        case "назад в меню" | "назад" | "2":

            return choiceAction(library)
        case _:

            print("Введена неверная команда \n")
            return

def showInfo(library):
    '''
    Функция отвечает за отображение данных, находящихся в словаре
    '''
    if not library:
        print("Библиотека пуста \n")
        return choiceAction(library)
    else:
        print("Информация о книге: \n")
        count = 1
        for key in library:
            print(f"{count}) Название книги: {key}")
            print(f"Автор произведения: {library[key]["автор"]}")
            print(f"Жанр: {library[key]["жанр"]}")
            print(f"Год выпуска: {library[key]["год выпуска"]}")
            print(f"Количество страниц: {library[key]["количество страниц"]}")
            print(f"Издательство: {library[key]["издательство"]} \n")
            count += 1
        print()
        return choiceAction(library)

def deleteInfo(library):
    '''
    Функция отвечает за удаление данных из словаря
    '''
    if not library:
        print("Библиотека пуста \n")
        return choiceAction(library)
    else:
        print("")
        choice = input("Выберете действие:\n 1) Удалить книгу из базы \n 2) Очистить весь список\n 3) Назад в меню \n").lower()
        match choice:

            case "удалить книгу из базы" | "удалить" | "1":

                delKey = input("Введите название книги: ")
                if delKey in library:
                    library.pop(delKey)
                    print(f" Книга: {delKey} успешно удалена из базы")
                else:
                    print("Книга не найдена")
                    return

            case "очистить всю библиотеку" | "очистить" | "2":

                checkPoint = input("Вы уверены, что хотите очистить всю библиотеку (Y/N)?  ").lower()
                if checkPoint == "y":
                    library.clear()
                    return
                else:
                    return

            case "назад в меню" | "назад" | "3":

                return choiceAction(library)
            case _:
                print("Введена неверная команда \n")
                return

def searchInfo(library):
    '''
    Функция отвечает за поиск данных в словаре
    '''
    if not library:
        print("Библиотека пуста \n")
        return choiceAction(library)
    else:
        choice = input("Выберете действие:\n 1) Найти книгу \n 2) Назад в меню \n").lower()
        match choice:
            case "найти книгу" | "найти" | "1":

                searchKey = input("Введите название книги: ")
                if searchKey in library:
                    print(f"Название книги: {searchKey}")
                    print(f"Автор произведения: {library[searchKey]["автор"]}")
                    print(f"Жанр: {library[searchKey]["жанр"]}")
                    print(f"Год выпуска: {library[searchKey]["год выпуска"]}")
                    print(f"Количество страниц: {library[searchKey]["количество страниц"]}")
                    print(f"Издательство: {library[searchKey]["издательство"]} \n")
                else:
                    print("Книга не найдена")
                    return

            case "назад в меню" | "назад" | "2":

                return choiceAction(library)
            case _:
                print("Введена неверная команда \n")
                return

def changeInfo(library):
    '''
    Функция отвечает за предварительный ввод ФИО сотрудника и выбор подходящего действия
    '''
    if not library:
        print("Библиотека пуста \n")
        return choiceAction(library)
    else:
        getBook = input("Введите название книги: ")
        if getBook in library:
            changeInfoMain(library, getBook)
        else:
            print("Книга не найдена")
            return

def changeInfoMain(library, getBook):
    '''
    Функция отвечает за изменения данных в словаре
    :param library: словарь, содержащий информацию о книге
    :param getBook: название книги, являющееся ключом словаря (library)
    :return:
    '''

    commands = ["Заменить название книги", "Заменить автора произведения", "Заменить жанр", "Заменить год выпуска",
                "Заменить количество страниц", "Заменить издательство", "Выбрать книгу", "Назад в меню"]
    print("Выберете действие: ")
    count = 1
    for command in commands:
        print(f" {count}) {command}")
        count += 1
    choice = input("").lower()

    match choice:
        case "заменить название книги" | "заменить название" | "1":

            delBook = getBook
            delInfo = library.pop(getBook)
            addName = input("Введите новое название книги: ")
            library[addName] = delInfo
            print(f"Данные изменены - {delBook} на {addName} \n")
            return

        case "заменить автора произведения" | "заменить автора" | "2":

            delWriter = library[getBook]["автор"]
            addWriter = input("Введите нового автора произведения: ")
            library[getBook]["автор"] = addWriter
            print(f"Данные изменены - автор произведения: {delWriter} на {addWriter} \n")
            return changeInfoMain(library, getBook)

        case "заменить жанр" | "3":

            delGenre = library[getBook]["email"]
            addGenre = input("Введите новый жанр: ")
            library[getBook]["жанр"] = addGenre
            print(f"Данные изменены - жанр: {delGenre} на {addGenre} \n")
            return changeInfoMain(library, getBook)

        case "заменить год выпуска" | "4":

            delRelease = library[getBook]["год выпуска"]
            addRelease = input("Введите новый год выпуска: ")
            library[getBook]["год выпуска"] = addRelease
            print(f"Данные изменены - год выпуска: {delRelease} на {addRelease} \n")
            return changeInfoMain(library, getBook)

        case "заменить количество страниц" | "5":

            delPage = library[getBook]["количество страниц"]
            addPage = input("Введите новое количество страниц: ")
            library[getBook]["количество страниц"] = addPage
            print(f"Данные изменены - количество страниц: {delPage} на {addPage} \n")
            return changeInfoMain(library, getBook)

        case "заменить издательство" | "6":

            delPublisher = library[getBook]["издательство"]
            addPublisher = input("Введите новое издательство: ")
            library[getBook]["издательство"] = addPublisher
            print(f"Данные изменены - издательство: {delPublisher} на {addPublisher} \n")
            return changeInfoMain(library, getBook)

        case "выбрать книгу" | "7":
            return changeInfo(library)

        case "назад в меню" | "назад" | "8":
            return choiceAction(library)
        case _:
            print("Введена неверная команда \n")
            return choiceAction(library)

def choiceAction (library):
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
                addInfo(library)
            case "удалить данные" | "удалить" | "2":
                deleteInfo(library)
            case "найти данные" | "найти" | "3":
                searchInfo(library)
            case "изменить данные" | "изменить"| "4":
                changeInfo(library)
            case "показать список" | "показать" | "5":
                showInfo(library)
            case "выход из программы" | "выход" | "6":
                print("До свидания!")
                exit()
            case _:
                print("Введена неверная команда \n")


def main ():
    '''
    Основная функция, связывающая хранилище данных (tempDict) и маршрутизатор (choiceAction)
    '''
    print("Приветствую, в данной программе под названием 'Книжная коллекция' хранится информация о книгах имеющихся в нашей библиотеке:")
    library = tempDict()
    choiceAction(library)


main()