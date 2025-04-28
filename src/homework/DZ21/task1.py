from random import randint


def makeRandomList() -> list[int]:
    '''
    Функция генерирует список случаныйх чисел.
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

def BubbleSorted(list: list[int], is_reverse: bool = False) -> list[int]:
    '''
    Функция пузырьковым методом сортирует полученный список в порядке возрастания (по-умолчанию).
    Если параметр is_reverse=True, то возвращает отсортированный список в порядке убывания.
    :param list: список с числами (list[int])
    :param is_reverse: выбор сортировки списка: True - в порядке убывания,
    False - в порядке возрастания (bool)
    :return: отсортированный список чисел (list[int])
    '''
    i = 1

    while i < len(list):

        if list[i] < list[i - 1]:
            list[i], list[i - 1] = list[i - 1], list[i]
            j = i - 1

            while j > 0:

                if list[j] < list[j - 1]:
                    list[j], list[j - 1] = list[j - 1], list[j]
                    j -= 1

                else:
                    break
        i += 1

    if is_reverse:
        list.reverse()
        return list

    return list


def linearSearch(list: list[int], target: int) -> int:
    '''
    Функция принимает список чисел и искомый элемент в виде числа.
    С помощью линейного поиска проходимся по списку, и если число есть в списке возвращает его индекс,
    если нет возвращает -1.
    :param list: список чисел (list[int])
    :param target: искомый элемент в виде числа (int)
    :return: индекс элемента (int)
    '''

    for index, elem in enumerate(list):
        if elem == target:
            return index

    return -1

def InteractiveMenu(list: list[int]) -> None:
    '''
    Функция принимает в себя список чисел (list[int]), и в зависимости от выбора пользователя
    выводит в консоль реультат выполнения выбранной функции.
    :param list: список с числами (list[int])
    :return: None
    '''
    choice = ""

    while choice != "3":
        choice = input(f"\n1. Отсортировать список.\n"
                       f"2. Найти элемент в списке.\n"
                       f"3. Выйти из программы.\n"
                       f"Выберете необходимое действие: ")

        match choice:

            case "1":
                sort_choice = input(f"\nВы хотите отсортировать список по возрастанию (y/n)? ")

                if sort_choice.lower() == "y":
                    print(f"\nОтсортированный список по возрастанию: {BubbleSorted(list)}")
                else:
                    print(f"\nОтсортированный список по убыванию: {BubbleSorted(list, is_reverse=True)}")

            case "2":
                target = int(input(f"\nВведите элемент индекс которого Вы хотите найти: "))
                search_result = linearSearch(list, target)

                if search_result >= 0:
                    print(f"\nИндекс элемента {target}: [{search_result}]")
                else:
                    print(f"\nЭлемент {target} в списке не обнаружен :(")

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
