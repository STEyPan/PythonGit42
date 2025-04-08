# Задание 1 - пользователь вводит шестизначное число.

def checkPalindrome(number: str) -> bool:
    i = 0
    while i < len(number):
        if number[i] != number[len(number) - 1 - i]:
            return False
        i += 1
    return True

def checkLucky(number: str) -> bool:
    left = 0
    right = 0

    for i in range(0, len(number)):
        if i < len(number) / 2:
            left += int(number[i])
        else:
            right += int(number[i])

    return left == right


def task1():
    number = input("Введите 6-значное число: ")
    lucky = checkLucky(number)
    poli = checkPalindrome(number)
    if lucky and poli:
        print(f"Число {number} - счастливый палиндром")
    elif lucky and not poli:
        print(f"Число {number} - счастливый, но не палиндром")
    elif not lucky and poli:
        print(f"Число {number} - не счастливое, но палиндром")
    else:
        print(f"Число {number} - не счастливое, не палиндром")

task1()

# def makeBoard():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     return board
#
# def printBoard(board):
#     for col in board:
#         for row in col:
#             print(f"[{row}]", end=' ')
#         print()
#
# def moveXO(board, move):
#     index = move
#     if board[x][y]
#
# def main():
#     board = makeBoard()
#     printBoard(board)
#     while True:
#         move = int(input("\n Введите координату от 1 до 9: ")) - 1
#         moveXO(board, move)
#         printBoard(board)
#
#
# main()

# def PrintBoard(board):
#     for row in board:
#         for elem in row:
#             if elem == 1:
#                 print("X", end=" ")
#             elif elem == -1:
#                 print("0", end=" ")
#             else:
#                 print("_", end=" ")
#         print()
#
# def StepOnGame(num, sign, board):
#     row = (num - 1) // 3
#     col = (num - 1) % 3
#     if not board[row][col]:
#         board[row][col] = sign
#     return board
#
# # def checkWin(board):
#
#
# def task2():
#     board = [[0,0,0][0,0,0][0,0,0]]
