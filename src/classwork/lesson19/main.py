# Лямбда-выражения aka Анонимные функции
# Это функции у которых нет привычного имени объявления.
# Они создаются в одной конкретной переменной и могут вызываться ТОЛЬКО
# через эту переменную
# Синтаксис: <переменная> =  lambda <список параметров> : <тело функции>

square = lambda num: num * num
print(square(2))

# Сортировки
lst = [2, 5, 4, 1, 8, 0, 9, 7, 6, 3]

# Сортировка пузырьком
def BubbleSort(lst: list) -> lst:
    i = 1
    while i < len(lst):
        if lst[i] < lst[i-1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            j = i - 1
            while j > 0:
                if lst[j] < lst[j-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                else:
                    break
                j -= 1
            i -= 1
        i += 1
    return lst

#print(BubbleSort(lst))

# Сортировка вставками
def SelectionSort(lst: list) -> list:
    for i in range(len(lst)):
        minElem = i
        for j in range(i, len(lst)):
            if lst[minElem] > lst[j]:
                minElem = j
        lst[minElem], lst[i] = lst[i], lst[minElem]
    return lst

#print(SelectionSort(lst))


# Сортировка слиянием
def merge(leftList, rightList):
    mergeList = []
    left = right = 0

    for _ in range(len(leftList) + len(rightList)):

        if left < len(leftList) and right < len(rightList):

            if leftList[left] < rightList[right]:
                mergeList.append(leftList[left])
                left += 1

            else:
                mergeList.append(rightList[right])
                right += 1

        elif left == len(leftList):
            mergeList.append(rightList[right])
            right += 1

        elif right == len(rightList):
            mergeList.append(leftList[left])
            left += 1

    return mergeList

def MergeSort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    rightList = MergeSort(lst[mid:])
    leftList = MergeSort(lst[:mid])

    return merge(leftList, rightList)

print(MergeSort(lst))