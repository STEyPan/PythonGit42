from src.homework.DZ19.task1 import printCalcResult as task1
from src.homework.DZ19.task2 import printResultFilters as task2

def main() -> None:
    '''
    Функция вызывает другие функции из внешних файлов
    :return: None
    '''
    print("1 задание\n2 задание")
    choice = input("Введите номер задания: ")

    match choice:
        case "1": task1()
        case "2": task2()
        case _: print("Нет такого задания")


if __name__ == "__main__":
    main()