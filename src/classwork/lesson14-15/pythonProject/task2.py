# Задание 1
# Пользователь вводит 2 числа. Необходимо написать функцию, которую принимает эти 2 числа и возвращает словарь, содержащий массив элементов из диапазона, ограниченного указанными числами, который представляет следующую структуру:
# - number: <число>
# - isEven: True/False
# - isNumber: True/False
# - Factorial: <число>
# - Square: <число>

# После обращения к функции, необходимо вывести данный словарь

def makeNumbersList(numberFirst, numberSecond):
    numbersList = []
    for num in range(numberFirst, numberSecond+1):
        numbersList.append(num)
    return numbersList

def isEven(numbersList):
    isEvenList = []
    for num in numbersList:
        if num % 2 == 0:
            isEvenList.append(True)
        else:
            isEvenList.append(False)
    return isEvenList

def isNumber(numberList):
    isNumberList = []
    for num in numberList:
        if num >= 10:
            isNumberList.append(True)
        else:
            isNumberList.append(False)
    return isNumberList

def evalFactorial(numbersList):
    factorialList = []
    for num in numbersList:
        factorial = 1
        for n in range(2, num+1):
            factorial *= n
        factorialList.append(factorial)
    return factorialList

def evalSquare(numbersList):
    squareList = []
    for num in numbersList:
        squareList.append(num*num)
    return squareList

def makeDict(numbersList, isEvenList, isNumberList, factorialList, squareList):
    dictNumbers = dict()
    for i in range(0, len(numbersList)-1):
        dictNumbers[i] = {"numbers": numbersList[i], "isEven": isEvenList[i], "isNumber": isNumberList[i], "Fact": factorialList[i], "Square": squareList[i]}
    return dictNumbers

def task1():
    numberFirst = int(input("Введите первое число диапазона: "))
    numberSecond = int(input("Введите второе число диапазона: "))
    numbersList = makeNumbersList(numberFirst, numberSecond)
    even = isEven(numbersList)
    number = isNumber(numbersList)
    factorial = evalFactorial(numbersList)
    square = evalSquare(numbersList)
    dict = makeDict(numbersList, even, number, factorial, square)
    print(dict)


# task1()

# Задание 2
# Необходимо разработать приложение для хранения информации о сотрудниках компании
# Каждый сотрудник программист, характеризуется:
# 1. ФИО
# 2. Возраст
# 3. Пол
# 4. Опыт работы
# 5. Должность
# 6. Язык программирования
# 7. Зарплата
# Необходимо создать полноценное меню с пункатами - Добавить, Изменить, Уволить, Вывести информацию о сотруднике
# Каждый пункт содержит подменю со списком ФИО сотрудников
# Последний пункт меню - выход - закрывает программу

def addInfo(employees):
    addName = input("Введите ФИО нового сотрудника: ")
    addAge = input("Введите возраст: ")
    addGender = input("Введите пол: ")
    addExp = input("Введите опыт работы: ")
    addPost = input("Введите должность: ")
    addSalary = input("Введите зарплату: ")

    subDict = {}
    subDict


def main():
    employees = {
        "Иванов Иван Иванович":{
            "Возраст" : "42",
            "Пол" : "Мужской",
            "Опыт работы" : "22",
            "Должность" : "Самый главный",
            "Язык программирования" : "С++",
            "Зарплата" : "1.500.000"
        }
    }
    choice = 0
    while choice != 5:
        print("1. Добавить")
        print("2. Изменить")
        print("3. Уволить")
        print("4. Вывести информацию о сотруднике")
        print("5. Выход")
        choice = int(input("Выберете необходимое действие"))

        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case _:
                pass