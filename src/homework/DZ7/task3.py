def makeBoard():
    '''
    Функция создает шахматную доску 8 х 8 в виде точек '.'
    :return:
    '''
    board = [['.' for _ in range(8)] for _ in range(8)]
    return board

def checkLocatition(x:int, y:int, board):
    '''
    Функция проверяет правильность координат (x) and (y) передаваемых извне,
    и свободна ли ячейка board[x][y] - по заданным координатам
    :param x: координата от 1 до 8 (из функции main)
    :param y: координата от 1 до 8 (из функции main)
    :param board: шахматная доска 8 х 8 в виде двумерного списка
    :return:
    '''
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == '.'

def avilableMove():
    '''
    Функция дает доступ к возможным ходам для коня
    :return:
    '''
    movesX = [2, 1, -1, -2, -2, -1, 1, 2]
    movesY = [1, 2, 2, 1, -1, -2, -2, -1]
    return movesX, movesY

def knightMarch(x, y, moveCount, board):
    '''
    Функция отвечает за изменение координат (x, y) фигуры коня на шахматной доске (board)
    и меняет
    :param x: координата от 1 до 8 (из функции main)
    :param y: координата от 1 до 8 (из функции main)
    :param moveCount: счетчик ходов, начинается с 1
    :param board: шахматная доска 8 х 8 в виде двумерного списка
    :return:
    '''
    moveX, moveY = avilableMove()

    if moveCount == 64:
        return True

    for i in range (8):
        nextX = x + moveX[i]
        nextY = y + moveY[i]
        if checkLocatition(nextX, nextY, board):
            board[nextX][nextY] = 'K'
            if knightMarch(nextX, nextY, moveCount+1, board):
                return True
    return False

def main():
    '''
    Основная функция, в которой происходит ввод координат X and Y,
    при правильном вводе инициализируется функция knightMarch
    :return:
    '''
    board = makeBoard()
    startX = int(input("Введите координату Х (1-8): ")) - 1
    startY = int(input("Введите координату Y (1-8): ")) - 1
    if checkLocatition(startX, startY, board):
        board[startX][startY] = 'K'
        if knightMarch(startX, startY, 1, board):
            print("Решение найдено")
            for row in board:
                print('  '.join(row))
        else:
            print("Решение не найдено")
    else:
        print("Некорректные координаты")

main()