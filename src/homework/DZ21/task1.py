from random import randint


def makeRandomList():
    return [randint(-10,10) for _ in range(10)]

def sumLists(lists):
    sum_lists = []

    for list in lists:
        sum_lists += list

    return sum_lists

    # return [item for sublist in lists for item in sublist]

def initLists(amount):
    lists = []

    for i in range(amount):
        list = makeRandomList()
        lists.append(list)
        print(f"Список №{i+1}: {list}")
    print()

    return sumLists(lists)

def BubbleSorted(list, is_reverse=False):
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


def linearSearch(list, target) -> int:

    for index, elem in enumerate(list):
        if elem == target:
            return index

    return -1

def InteractiveMenu(list):
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


def main():
    sum_lists = initLists(4)
    print(f"Объединенный список: {sum_lists}")
    InteractiveMenu(sum_lists)


main()
