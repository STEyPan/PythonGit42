# Пользователь вводит несколько чисел больше (Х > 0).
# Необходимо сформировать список и вывести на экран с каждым числом
# в списке вида: {число} - {четное/нечетное}
# Признаком завершения ввода пользователя будет -1

# numbers = 1
# evenList = []
# notEvenList = []
#
# while numbers >= 0:
#     numbers = int(input("Введите целое число больше 0: "))
#     if numbers % 2 == 0:
#         evenList.append(numbers)
#     elif numbers < 0:
#         print(f" Четные - {evenList} Нечетные - {notEvenList}")
#     else:
#         notEvenList.append(numbers)
#
#
# for even in evenList:
#     print(f"{even} - четное")
# print()
# for notEven in notEvenList:
#     print(f"{notEven} - нечетное")

numbers = 1
numbersList = []

while numbers >= 0:
    numbers = int(input("Введите целое число больше 0: "))
    if numbers >= 0:
        numbersList.append(numbers)

for item in numbersList:
    if item % 2 == 0:
        print(f"{item} - четное")
    else:
        print(f"{item} - нечетное")