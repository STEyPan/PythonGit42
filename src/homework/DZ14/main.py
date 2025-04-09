def addInfo(employees: dict) -> dict:
    f'''
    Функция добавляет информацию о новом сотруднике в словарь (employees)
    '''
    addName = input("Введите ФИО нового сотрудника: ")
    addAge = int(input("Введите возраст: "))
    addGender = input("Введите пол: ")
    addExp = int(input("Введите опыт работы: "))
    addPost = input("Введите должность: ")
    addProgLang = input("Введите язык программирования: ")
    addSalary = int(input("Введите зарплату: "))

    employeer = {}
    employeer["Возраст"] = addAge
    employeer["Пол"] = addGender
    employeer["Опыт работы"] = addExp
    employeer["Должность"] = addPost
    employeer["Язык программирования"] = addProgLang
    employeer["Зарплата"] = addSalary
    employees[addName] = employeer
    print(f"\nСотрудник {addName} принят в компанию.\n")
    return employees

def changeInfo(employees: dict) -> dict:
    '''
    Функция изменят информацию о существующем сотруднике в словаре (employees)
    '''
    changeName = input("Введите ФИО сотрудника, чтобы изменить данные: ")
    if changeName not in employees:
        print("\nНет такого сотрудника\n")
    else:
        employees.pop(changeName)
        employeer = {}
        newName = input("Введите новое ФИО: ")
        newAge = int(input("Введите возраст: "))
        newGender = input("Введите пол: ")
        newExp = int(input("Введите опыт работы: "))
        newPost = input("Введите должность: ")
        newProgLang = input("Введите язык программирования: ")
        newSalary = int(input("Введите зарплату: "))

        employeer["Возраст"] = newAge
        employeer["Пол"] = newGender
        employeer["Опыт работы"] = newExp
        employeer["Должность"] = newPost
        employeer["Язык программирования"] = newProgLang
        employeer["Зарплата"] = newSalary
        print("\nДанные обновлены")
        employees[newName] = employeer
        return employees



def delInfo(employees: dict) -> None:
    '''
    Функция удаляет всю информацию о сотруднике из словаря (employees)
    '''
    delName = input("Введите ФИО сотрудника, которого хотите уволить: ")
    if delName not in employees:
        print("\nНет такого сотрудника\n")
    else:
        employees.pop(delName)
        print(f"\nСотрудник {delName} уволен из компании!\n")

def showInfo(employees: dict) -> None:
    '''
    Функция выводит информацию о сотруднике из словаря (employees)
    '''
    searchName = input("Введите ФИО сотрудника: ")
    if searchName not in employees:
        print("\nНет такого сотрудника\n")
    else:
        print(f"\n{searchName}")
        employeer = employees[searchName]
        for key, value in employeer.items():
            print(f"\t{key} : {value}")
        print()


def main() -> None:
    '''
    Основная функция, хранит словарь (employees) и содержит главное меню для
    вызова необходимых функций
    '''
    employees = {
        "Иванов Иван Иванович":{
            "Возраст": 42,
            "Пол": "Мужской",
            "Опыт работы": 22,
            "Должность": "Самый главный",
            "Язык программирования": "C++",
            "Зарплата": 500000
        },

        "Иванов Иван Петрович": {
            "Возраст": 34,
            "Пол": "Мужской",
            "Опыт работы": 10,
            "Должность": "Питонист",
            "Язык программирования": "Python",
            "Зарплата": 150000
        }
    }
    choice = ""
    while choice != "5":
        print("\nГЛАВНОЕ МЕНЮ:")
        print("1. Добавить")
        print("2. Изменить")
        print("3. Уволить")
        print("4. Вывести информацию о сотруднике")
        print("5. Выход")
        choice = input("\nВыберете команду и введите цифру: ")

        match choice:
            case "1":
                addInfo(employees)
            case "2":
                changeInfo(employees)
            case "3":
                delInfo(employees)
            case "4":
                showInfo(employees)
            case "5":
                print("Good bye!")
            case _:
                print("Введена неверная команда")


main()