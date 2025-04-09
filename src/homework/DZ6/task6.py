def numberCounter (number: int):
    numberAbs = abs(number)
    count = 0
    while numberAbs != 0:
        numberAbs = numberAbs // 10
        count += 1
    else:
        return f"В числе ({number}) - {count} цифр(ы)"


num = int((input(f"Введите любое целое число: ")))
print(numberCounter(num))