# Задание 1
numberOfWeek = int(input(f"Введите число от 1 до 7: "))

match numberOfWeek:
    case 1:
        print(f"День недели - понедельник")
    case 2:
        print(f"День недели - вторник")
    case 3:
        print(f"День недели - среда")
    case 4:
        print(f"День недели - четверг")
    case 5:
        print(f"День недели - пятница")
    case 6:
        print(f"День недели - суббота")
    case 7:
        print(f"День недели - воскресение")
    case _:
        print(f"Введено число вне диапазона")

# Задание 2

# 1 способ

numberOfMonth = int(input(f"Введите число от 1 до 12: "))

match numberOfMonth:
    case 1:
        print(f"Январь")
    case 2:
        print(f"Февраль")
    case 3:
        print(f"Март")
    case 4:
        print(f"Апрель")
    case 5:
        print(f"Май")
    case 6:
        print(f"Июнь")
    case 7:
        print(f"Июль")
    case 8:
        print(f"Август")
    case 9:
        print(f"Сентябрь")
    case 10:
        print(f"Октябрь")
    case 11:
        print(f"Ноябрь")
    case 12:
        print(f"Декабрь")
    case _:
        print(f"Введено число вне диапазона")

# 2 способ

getMonthNumber = int(input(f"Введите число от 1 до 12: "))
numbersOfMonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
twelveMonth = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

if getMonthNumber == numbersOfMonths[getMonthNumber-1] :
    monthName = twelveMonth[getMonthNumber-1]
    print(f"{monthName}")
else:
    print(f"Введено число вне диапазона")

# 3 способ (нейросетевое решение)

getMonthNumber = int(input(f"Введите число от 1 до 12: "))
twelveMonth = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

if 1 <= getMonthNumber <= 12:
    monthName = twelveMonth[getMonthNumber-1]
    print(f"{monthName}")
else:
    print(f"Введено число вне диапазона")

# Задание 3

getNumber = int(input(f"Введите целое число: "))

if getNumber > 0:
    print(f"Number {getNumber} is Positive")
elif getNumber < 0:
    print(f"Number {getNumber} is Negative")
else:
    print(f"Number {getNumber} is Equal to zero")

# Задание 4

getNumberFirst = int(input(f"Введите первое число: "))
getNumberSecond = int(input(f"Введите второе число: "))

if getNumberFirst == getNumberSecond:
    print(f"Числа равны")
elif getNumberFirst > getNumberSecond:
    print(f"{getNumberSecond} {getNumberFirst}")
else:
    print(f"{getNumberFirst} {getNumberSecond}")