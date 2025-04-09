# def getMinimalNumber(arrayNumbers):
#     if len(arrayNumbers) > 5:
#         print(f"Введено более 5 чисел")
#     elif len(arrayNumbers) < 5:
#         print(f"Введено менее 5 чисел")
#     else:
#         minNumber = arrayNumbers[0]
#         for i in range (len(arrayNumbers)):
#             if arrayNumbers[i] < minNumber:
#                 minNumber = arrayNumbers[i]
#         print(minNumber)

def getMinimalNumber(arrayNumbers: float):
    if len(arrayNumbers) > 5:
        return f"Введено более 5 чисел"
    elif len(arrayNumbers) < 5:
        return f"Введено менее 5 чисел"
    else:
        return min(arrayNumbers)

numbers = input(f"Введите 5 любых чисел через запятую: ")
numbersList = numbers.split(",")
numbersList = [float(num) for num in numbersList]

# getMinimalNumber(numbersList)
print(getMinimalNumber(numbersList))