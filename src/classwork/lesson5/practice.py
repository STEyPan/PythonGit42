# 1 - Калькулятор через сложение
# Пользователь вводит пример вида Число Знак Число и необходимо посчитать ответ и вывести
# на экран в виде сообщения: "<первое число> <знак> <второе число> = <ответ>"
# ВСЕ ОПЕРАЦИИ ЧЕРЕЗ СЛОЖЕНИЕ
# Операция деления предпологает деление только НАЦЕЛО

first = int(input(f"Введите первое целое число: "))
sign = input(f"Выберите операцию и введите из предложеного (что-то одно) '+' '-' '*' '/' '^' ")
second = int(input(f"Введите второе целое число: "))
result = 0
temp = 0

match sign:
    case "+":
        result = first + second
        print(f"{first} {sign} {second} = {result}")
    case "-":
        result = first + (-second)
        print(f"{first} {sign} {second} = {result}")
    case "*":
        for i in range(0, second):
            result = result + first
        print(f"{first} {sign} {second} = {result}")
    case "/":
        residue = 0
        if second == 0:
            print(f"Ошибка: деление на {second}")
        elif second > first:
            print(f"Ошибка: {first} не должен быть меньше {second}")
        else:
            while temp != first:
                temp = temp + second
                result += 1
                if temp > first:
                    temp = temp + (-second)
                    result = result + (-1)
                    residue = first + (-temp)
                    break
            print(f"{first} {sign} {second} = {result} и остаток от деления {residue}")
    case "^":
        result = first
        if second == 0:
            result = 1
            print(f"{first} {sign} {second} = {result}")
        else:
            for i in range(0, second-1):
                temp = result
                for i in range(0, first-1):
                    result += temp
            print(f"{first} {sign} {second} = {result}")
    case _:
        print(f"Введено неверное условие")