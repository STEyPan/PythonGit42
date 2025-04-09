# Первое задание
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

print(f"Сумма чисел = {first+second+third}")
print(f"Произведение чисел = {first*second*third}")

# Второе задание
salary = int(input(f"Какая у Вас зарплата?  "))
credit = int(input(f"Сколько Вам необходимо платить по кредиту?  "))
utilities = int(input(f"Какой у Вас долг по коммунальным услугам?  "))
balance=salary-(credit+utilities)

print(f"У вас останется: {balance}")

# Третье задание
firstDiagonal = int(input(f"Введите длину первой диагонали: "))
secondDiagonal = int(input(f"Введите длину второй диагонали: "))
rhombusArea = (firstDiagonal*secondDiagonal)/2

print(f"Площадь ромба = {rhombusArea}")

# Четвертое задание
print("   To be", "   or not", "   to be", sep='\n')

# Пятое задание
print('   "Life is what happens')
print("         when")
print('''            you're busy making other plans"''')
print("                                        John Lennon")