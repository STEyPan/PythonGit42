def parity_detection (num1: int, num2: int):
    if num1 <= num2:
        num_temp = num1
        while num_temp <= num2:
            if num_temp % 2 == 0:
                print(num_temp)
                num_temp += 1
            else:
                num_temp += 1
    elif num2 <= num1:
        num_temp = num2
        while num_temp <= num1:
            if num_temp % 2 == 0:
                print(num_temp)
                num_temp += 1
            else:
                num_temp += 1
    else:
        print(f"Введены неверные значения")

firstNumber= int(input(f"Введите первое целое число: "))
secondNumber= int(input(f"Введите второе целое число: "))
parity_detection(firstNumber, secondNumber)

# 0 тоже является четным числом

#lvl 2
# numbers = input(f"Введите два целых числа через пробел: ")
# numbersList = numbers.split()
# numbersList = [int(num) for num in numbersList]
# с помощью for проходим по всему списку и преобразуем строку в целое число и создаем новый список
# firstNumber = numbersList[0]
# secondNumber = numbersList[1]
# parity_detection(firstNumber, secondNumber)