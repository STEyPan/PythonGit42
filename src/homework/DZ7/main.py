import random

def create_board():
    """Создает случайное игровое поле 4x4 с плитками от 1 до 15 и одной пустой клеткой."""
    numbers = list(range(1, 16)) + [0]  # 0 представляет пустую клетку
    random.shuffle(numbers)
    board = [numbers[i:i + 4] for i in range(0, 16, 4)]
    return board

def print_board(board):
    """Отображает текущее состояние игрового поля."""
    for row in board:
        print(" ".join(f"{num:2}" for num in row))
    print()

def find_zero(board):
    """Находит позицию пустой клетки (0) на поле."""
    for i, row in enumerate(board):
        if 0 in row:
            return i, row.index(0)

def is_winning(board):
    """Проверяет, достигнуто ли выигрышное состояние."""
    flat_board = [num for row in board for num in row]
    return flat_board == list(range(1, 16)) + [0]

def move(board, direction):
    """Перемещает плитки в зависимости от введенного направления."""
    x, y = find_zero(board)
    if direction == "up" and x < 3:
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
    elif direction == "down" and x > 0:
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
    elif direction == "left" and y < 3:
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
    elif direction == "right" and y > 0:
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]

def recursive_solve(board, depth=0):
    """Рекурсивная функция для поиска решения (для улучшения, не используется в основном коде)."""
    if is_winning(board):
        print("Решение найдено!")
        print_board(board)
        return True
    if depth > 10:  # Ограничение глубины для предотвращения бесконечной рекурсии
        return False

    for direction in ["up", "down", "left", "right"]:
        new_board = [row[:] for row in board]  # Копируем текущее состояние поля
        move(new_board, direction)
        if not is_winning(new_board):
            if recursive_solve(new_board, depth + 1):
                return True
    return False

def game():
    """Основная функция для запуска игры."""
    board = create_board()
    while not is_winning(board):
        print_board(board)
        move_direction = input("Введите направление (up, down, left, right): ").strip().lower()
        if move_direction in ["up", "down", "left", "right"]:
            move(board, move_direction)
        else:
            print("Неверное направление. Попробуйте снова.")
    print("Поздравляем! Вы выиграли!")

game()
