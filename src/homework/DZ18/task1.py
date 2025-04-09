def bigestDigity (num1: int, num2: int):
    '''
    Функция с помощью рекурсии вычисляет наибольший делитель
    двух целых чисел (num1 и num2)
    :param num1: Первое вводимое целое число
    :param num2: Второе вводимое целое число
    :return:
    '''
    if num2 == 0:
        return f"Наибольший делитель двух чисел = {num1}"
    else:
        return bigestDigity(num2, num1 % num2)

num1 = int(input(f"Введите первое целое число: "))
num2 = int(input(f"Введите второе целое число: "))
print(bigestDigity(num1, num2))