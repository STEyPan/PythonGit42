def LinearSearch(input_list: list[int], target: int) -> int:
    '''
    Функция принимает список чисел и искомый элемент в виде числа.
    С помощью линейного поиска проходимся по списку, и если число
    есть в списке возвращает его индекс, если нет возвращает -1.
    :param input_list: список чисел (list[int])
    :param target: искомый элемент в виде числа (int)
    :return: индекс элемента (int)
    '''
    if len(input_list) == 0:
        return - 1

    for index, elem in enumerate(input_list):
        if elem == target:
            return index

    return -1

def BibarySearch(input_list: list[int], target: int) -> int:
    '''
    Функция принимает список чисел и искомы элемент в виде числа.
    С помощью бинарного поиска находим искомый элемент и выводим его индекс.
    Если элемент не найден, то список выводит -1.
    Важно! Список должен быть предварительно отсортирован.
    :param input_list: список чисел (list[int])
    :param target: искомый элемент в виде числа (int)
    :return: индекс элемента (int)
    '''
    length_list = len(input_list)

    if length_list == 0:
        return -1


    if input_list[0] < input_list[-1]:
        if target < input_list[0] or target > input_list[-1]:
            return -1
        # Если первый элемент меньше последнего, значит список отсортирован по-возрастанию.
        low_half = start = 0
        # Первая половина списка начинается с 0 элемента
        high_half = stop = length_list-1
        # Вторая половина списка начинается с последнего элемента


    else:
        if target > input_list[0] or target < input_list[-1]:
            return -1
        # Иначе список отсортирован по-убыванию.
        low_half = stop = length_list-1
        # Первая половина списка начинается с последнего элемента
        high_half = start = 0
        # Вторая половина списка начинается с 0 элемента


    while start <= stop:

        middle = (low_half + high_half) // 2

        if target == input_list[middle]:
            return middle

        if target > input_list[middle]:
            low_half = start = middle
        else:
            high_half = start = middle

    else:
        return -1