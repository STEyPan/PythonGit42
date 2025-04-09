def reverseNumber (number: int):
    temp = number
    reversedNumber = 0
    while temp > 0:
        digit = temp % 10
        reversedNumber = reversedNumber * 10 + digit
        temp = temp // 10
    else:
       return reversedNumber

def checkPalidrom (nativeNumber: int, reversedNumber: int):
    if nativeNumber == reversedNumber:
        return f"Это палидром - {nativeNumber}"
    else:
        return f"Это не палидром - {nativeNumber}"


nativeNumber = int(input(f"Введите целое число: "))
reversedNumber = reverseNumber(nativeNumber)
print(checkPalidrom(nativeNumber, reversedNumber))