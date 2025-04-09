def swapNumbers (firstNumber: int, secondNumber: int):
    if firstNumber < secondNumber:
        return firstNumber, secondNumber
    else:
        return secondNumber, firstNumber


def multiplicationRange (smallerNumber: int, greaterNumber: int):
    temp = smallerNumber
    while temp < greaterNumber:
        temp += 1
        print(f"{temp-1} * {temp} = {temp * (temp - 1)}")
    else:
        print(f"{temp} * {temp} = {temp * temp}")

firstNumber= int(input(f"Введите первое целое число: "))
secondNumber= int(input(f"Введите второе целое число: "))

smaller, greater = swapNumbers(firstNumber, secondNumber)
multiplicationRange(smaller, greater)