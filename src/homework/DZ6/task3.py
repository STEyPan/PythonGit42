def drawSquare (lengthSquare: int, sign: str, fill=True):
    if lengthSquare <= 0:
        print(f"{lengthSquare} должен быть положительным числом")
    else:
        sign = f" {sign} "
        empty = "   "
        for i in range(lengthSquare):
            if fill == "Да":
                print(lengthSquare * sign)
            elif fill == "Нет":
                if i == 0 or i == lengthSquare - 1: #верхняя и нижняя сторона квадрата (строки начинаются с 0, поэтому 0 : это верхняя сторона квадрата, а lengthSquare - 1 : нижняя)
                    print(lengthSquare * sign)
                else:
                    print(f"{sign}{empty*(lengthSquare-2)}{sign}") # lengthSquare-2 : создаем пустое пространство минус ДВЕ боковые стороны
            else:
                fill = input(f"Вы хотите, чтобы квадрат был заполнен (Да / Нет)?: ")


lengthSquare = int(input(f"Введите целое положительное число: "))
sign = input(f"Введите любой символ: ")
fill = input(f"Вы хотите, чтобы квадрат был заполнен (Да / Нет)?: ")

drawSquare(lengthSquare, sign, fill)