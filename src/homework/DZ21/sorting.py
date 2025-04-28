
# Сортировка пузырьком

def BubbleSort(input_list: list[int], is_reverse: bool = False) -> list[int]:
    '''
    Функция пузырьковым методом сортирует полученный список в порядке возрастания (по-умолчанию).
    Если параметр is_reverse=True, то возвращает отсортированный список в порядке убывания.
    :param input_list: список с числами (list[int])
    :param is_reverse: выбор сортировки списка: True - в порядке убывания,
    False - в порядке возрастания (bool)
    :return: отсортированный список чисел (list[int])
    '''
    i = 1

    while i < len(input_list):

        if input_list[i] < input_list[i - 1]:
            input_list[i], input_list[i - 1] = input_list[i - 1], input_list[i]
            j = i - 1

            while j > 0:

                if input_list[j] < input_list[j - 1]:
                    input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
                    j -= 1

                else:
                    break
        i += 1

    if is_reverse:
        return input_list[::-1]

    return input_list

# Сортировка слиянием

def MergeLists(left_list: list[int], right_list: list[int]) -> list[int]:
    '''
    Функция принимает два отсортированных списка и объединяет их в один список.
    :param left_list: первый отсортированный список (list[int])
    :param right_list: второй отсортированный список (list[int])
    :return: объединенный отсортированный список (list[int])
    '''
    sorted_list = []

    i = j = 0

    while i < len(left_list) and j < len(right_list):

        if left_list[i] < right_list[j]:
            sorted_list.append(left_list[i])
            i += 1

        else:
            sorted_list.append(right_list[j])
            j += 1

    if i < len(left_list):
        sorted_list += left_list[i:]

    if j < len(right_list):
        sorted_list += right_list[j:]

    return sorted_list


def MergeSort(input_list: list[int]) -> list[int]:
    '''

    Функция принимает список чисел. Если длина списка <= 1,
    то функция возвращает список, как отсортированный.
    Если длина списка больше 1, то делит его на две половины, используя индекс середины.
    Рекурсивно вызывает MergeSort для каждой половины.
    И объединят отсортированные половины, используя MergeSort.
    :param input_list: список с числами (list[int])
    :return: новый отсортированный список (list[int])
    '''

    if len(input_list) <= 1:
        return input_list

    middle = len(input_list) // 2

    left_list = MergeSort(input_list[:middle])
    right_list = MergeSort(input_list[middle:])

    return MergeLists(left_list, right_list)