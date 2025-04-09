# Первое задание
first = int(input(f"Введите первое число: "))
second = int(input(f"Введите второе число: "))
third = int(input(f"Введите третье число: "))
total = first + second + third
multiplication = first * second * third
choice = str(input(f"Введите (без кавычек): 'сумма' или 'произведение' - для получения результатов: "))

if choice == "сумма":
    print(f"Сумма чисел = {total}")
elif choice == "произведение":
    print(f"Произведение чисел = {multiplication}")
else:
    print(f"Введено неверное условие")

# Второе задание
first = int(input(f"Введите первое число: "))
second = int(input(f"Введите второе число: "))
third = int(input(f"Введите третье число: "))
maximum = 0
minimum = 0
middle = (first + second + third) / 3
choice = str(input(f"Введите (без кавычек): 'максимум' или 'минимум' или 'среднее' - для получения результатов:  "))

if choice == "максимум":
    if first > second and first > third:
        maximum = first
    elif second > first and second > third:
        maximum = second
    elif third > first and third > second:
        maximum = third
    else:
        print(f"Среди чисел нет максимального, возможно они равны")
    print(f"Максимальное число из введенных: {maximum}")
elif choice == "минимум":
    if first < second and first < third:
        minimum = first
    elif second < first and second < third:
        minimum = second
    elif third < first and third < second:
        minimum = third
    else:
        print(f"Среди чисел нет минимального, возможно они равны")
    print(f"Минимальное число из введенных: {minimum}")
elif choice == "среднее":
    print(f"Среднее арифметическое = {middle}")
else:
    print(f"Введено неверное условие")

# Третье задание
milesScale = 1609
inchScale = 39.37
yardScale = 1.094
result = 0
meter = int(input(f"Введите расстояние в метрах:  "))
converter = str(input(f"Введите (без кавычек): 'миля' или 'дюйм' или 'ярд' - для получения результатов:  "))

if converter == "миля":
    result = meter / milesScale
    print(f"{meter} метр(ов) = {result} миля/миль")
elif converter == "дюйм":
    result = meter * inchScale
    print(f"{meter} метр(ов) = {result} дюйм(ов)")
elif converter == "ярд":
    result = meter * yardScale
    print(f"{meter} метр(ов) = {result} ярд(ов)")
else:
    print(f"Введено неверное условие")