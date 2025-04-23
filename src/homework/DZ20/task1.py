from random import randint


def makeRandomList() -> list:
    '''
    Функция генерирует список случайных чисел в заданном диапазоне
    :return:
    '''
    return [randint(-10,10) for _ in range(9)]

def sortReverseList(numbers: list[int]) -> list[int]:
    '''
    Функция принимает список случайных чисел (numbers[int]) ив зависимости от условий:
    часть списка сортирует, часть списка разворачивает
    :param numbers: список случайных чисел (list[int])
    :return: измененный список чисел (list[int])
    '''
    sorted_list = []
    meanList = sum(numbers) / len(numbers)
    list_third = len(numbers) // 3

    if meanList > 0:
        two_thirds = numbers[:list_third] + numbers[list_third:list_third*2]
        #reversed_part = list(reversed(numbers[list_third*2:list_third*3]))
        reversed_part = numbers[:-list_third-1:-1]
        sorted_list = list(sorted(two_thirds)) + reversed_part
        return sorted_list
    else:
        one_third = numbers[:list_third]
        reversed_two = numbers[:-list_third*2-1:-1]
        sorted_list = list(sorted(one_third)) + reversed_two
        return sorted_list


def main() -> None:
    randomList = makeRandomList()
    print(f"Оригинальный список:\n{randomList}")
    print(f"Измененный список:\n{sortReverseList(randomList)}")

main()