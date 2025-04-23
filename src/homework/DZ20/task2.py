def inputGrades(grades="") -> list[int]:
    '''
    Функция запрашивает у пользователя ввести 10 чисел (оценок).
    :return: список из 10 чисел (list[int])
    '''
    grades = [10,12,10,12,12,12,12,8,9,10]

    print("Введите 10 оценок от 1 до 12.")
    while len(grades) < 10:
        for count in range(1,11):
            grade = int(input(f"Введите оценку по {count} предмету: "))

            if 1 <= grade <= 12:
                grades.append(grade)

            else:
                print("Оценка вышла из диапазона. Попробуйте снова")
                break

    return grades


def printGrades(grades: list[int]) -> str:
    '''
    Функция принимает список из 10 чисел (оценки), и возвращает их в виде строки
    :param grades: список из 10 чисел (list[int])
    :return: строка из 10 чисел (str)
    '''
    #grades_str = [str(num) for num in grades]
    #return ",".join(grades_str)
    grades_str = ""
    for num in grades:
        grades_str += f"{num},"

    return grades_str[:-1]

def retakeExam(grades: list[int]) -> list[int]:
    '''
    Функция принимает список из 10 чисел (оценки). Запрашивает у пользователя
    ввести номер предмета и новую оценку, и возвращает измененный список.
    :param grades: список из 10 чисел (list[int])
    :return: измененный список из 10 чисел (grades[int])
    '''

    while True:
        index = int(input("\nВведите номер предмета от 1 до 10: "))

        if 1 <= index <= 10:
            new_grade = int(input("\nНа какую оценку пересдали экзамен от 1 до 12? "))

            if 1 <= new_grade <= 12:
                old_grade = grades[index-1]
                grades[index-1] = new_grade
                print(f"\nОценка по предмету №{index} изменена с {old_grade} на {new_grade}")
                return grades
            else:
                print("\nОценка вышла из диапазона. Попробуйте снова")
        else:
            print("\nНет такого предмета. Попробуйте снова")

def isGrants(grades: list[int]) -> str:
    '''
    Функция принимает список из 10 чисел (оценки). Высчитывает среднее арифметическое списка
     и в зависимости от выполненных условий, возвращает результат в виде сообщения.
    :param grades: список из 10 чисел (list[int])
    :return: результат в виде сообщения (str)
    '''
    mean_grades = sum(grades) / len(grades)

    if mean_grades >= 10.7:
        return "\nУра, Вы будете получать стипендию!!!"

    return "\nК сожалению в этом семестре у Вас не будет стипендии :("

def sortGrades(grades: list[int]) -> None:
    '''
     Функция принимает список из 10 чисел (оценки). В зависимости от выбора пользователя
     сортирует список по убыванию или по возрастанию.
    :param grades: список из 10 чисел (list[int])
    :return: отсортированный список из 10 чисел (grades[int])
    '''
    not_reverse = input("\nВы хотите отсортировать список по возрастанию? (y/n) ")
    print("\nСписок отсортирован!")
    return grades.sort() if not_reverse.lower() == "y" else grades.sort(reverse=True)

def mainMenu() -> None:
    '''
    Функция запрашивает ввести номер команды. В зависимости от введенной команды
    либо вызывает функцию, либо выходит из программы.
    :return: None
    '''
    grades = inputGrades()
    choice = ""

    while choice != "5":
        print("\n1) Вывести оценки.\n"
              "2) Пересдать экзамен.\n"
              "3) Возможна ли стипендия?\n"
              "4) Отсортировать оценки\n"
              "5) Выйти из программы")
        choice = input("Выберете необходимое действие: ")

        match choice:
            case "1": print(f"\nОценки: {printGrades(grades)}")
            case "2": retakeExam(grades)
            case "3": print(isGrants(grades))
            case "4": sortGrades(grades)
            case "5": print("До свидания!")
            case _: print("\nНет такой команды")

mainMenu()
