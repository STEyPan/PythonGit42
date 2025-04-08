def numberFibonachi(limit, num1 = 0, num2 = 1, count = 2):
    num3 = 0
    if limit == 0:
        return num1
    elif limit == 2:
        return num2
    elif limit <= count:
        num3 = num1 + num2
        return num3
    else:
        return numberFibonachi(limit, num2, num1+num2, count+1)

limit = int(input(f"Сколько чисел Фибоначи Вы хотите увидеть? "))

dictFibonachi = {}
i = 0
for limit in range(limit+1):
    dictFibonachi[limit] = numberFibonachi(limit)
    limit -= 1

for item in dictFibonachi:
    print(f"Num Fib: {item} = {dictFibonachi[item]}")