
def GetFileStrings(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        stringsFile = file.read().split("\n")

    return stringsFile

def CountSymbols(file) -> int:
    # all_sum = 0
    #
    # for string in file:
    #     all_sum += len(string)
    #
    # return all_sum

    return sum(map(len, file))

def CountStrings(file) -> int:
    return len(file)

def СountVowels(file) -> int:
    count_vowels = 0

    for string in file:
        for char in string:
            if char.lower() in "аеёиоуыэя":
                count_vowels += 1

    return count_vowels

def CountСonsonants(file) -> int:
    count_consonant = 0

    for string in file:
        for char in string:
            if char.lower() in "бвгджзйклмнпрстфхцчшщ":
                count_consonant += 1

    return count_consonant

def CountDigits(file) -> int:
    count_digit = 0

    for string in file:
        for char in string:
            if char.lower() in "1234567890":
                count_digit += 1

    return count_digit

def fileStatistics() -> str:
    file = GetFileStrings("Стихотворение.txt")

    result = (f"Количество символов: {CountSymbols(file)}\n"
              f"Количество строк: {CountStrings(file)}\n"
              f"Количество гласных букв: {СountVowels(file)}\n"
              f"Количество согласных букв: {CountСonsonants(file)}\n"
              f"Количество цифр: {CountDigits(file)}\n")

    with open("stats.txt", "w+") as result_file:
        result_file.write(result)

    return result

print(fileStatistics())