from random import randint
from searching import LinearSearch
from sorting import BubbleSort


def makeRandomList() -> list[int]:
    '''
    Функция генерирует список случайных чисел.
    :return: список случайных чисел (list[int])
    '''
    return [randint(-10,10) for _ in range(10)]

def sumLists(lists: list) -> list:
    '''
    Функция объединяет все списки в один список.
    :param lists: список, содержащий списки (list[list])
    :return: объединенный список (list)
    '''
    sum_lists = []

    for list in lists:
        sum_lists += list
        # sum_lists.extend(list)

    return sum_lists

    # return [item for sublist in lists for item in sublist]

def initLists(amount: int) -> list:
    '''
    Функция создает заданное количество списков со случайными числами,
    выводит в консоль сообщение с номером списка и его содержимым,
    и добавляет их в общий список.
    :param amount: количество списков (int)
    :return: список со списками (list[list])
    '''
    lists = []

    for i in range(amount):
        list = makeRandomList()
        lists.append(list)
        print(f"Список №{i+1}: {list}")
    print()

    return lists


def InteractiveMenu(list: list[int]) -> None:
    '''
    Функция принимает в себя список чисел (list[int]), и в зависимости от выбора пользователя
    выводит в консоль результат выполнения выбранной функции.
    :param list: список с числами (list[int])
    :return: None
    '''
    choice = ""
    sorted_list = list

    while choice != "3":
        choice = input(f"\n1. Отсортировать список.\n"
                       f"2. Найти элемент в списке.\n"
                       f"3. Выйти из программы.\n"
                       f"Выберете необходимое действие: ")

        match choice:

            case "1":
                sort_choice = input(f"\nВы хотите отсортировать список по возрастанию (y/n)? ")

                if sort_choice.lower() == "y":
                    sorted_list = BubbleSort(list)
                    print(f"\nОтсортированный список по возрастанию: {sorted_list}")

                else:
                    sorted_list = BubbleSort(list, is_reverse=True)
                    print(f"\nОтсортированный список по убыванию: {sorted_list}")

            case "2":
                target = int(input(f"\nВведите элемент индекс которого Вы хотите найти: "))
                search_result = LinearSearch(sorted_list, target)

                if search_result >= 0:
                    print(f"\nИндекс элемента {target}: [{search_result}]")
                else:
                    print(f"\nЭлемент [{target}] в списке не обнаружен :(")

            case "3":
                print("Good Bye!")

            case _:
                print("Нет такой команды, попробуйте снова!")


def main() -> None:
    '''
    Функция инициализирует список со списками случайных чисел,
    объединяет их с помощью функции sumLists(), выводит результат объедения в консоль.
    Далее вызывается функция InteractiveMenu()
    и в качестве параметра в неё передается объединенный список.
    :return: None
    '''
    lists = initLists(4)
    sum_lists = sumLists(lists)
    print(f"Объединенный список: {sum_lists}")
    InteractiveMenu(sum_lists)


main()