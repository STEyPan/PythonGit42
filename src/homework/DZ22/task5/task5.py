
def GetFileStrings(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        stringsFile = file.read().split("\n")

    return stringsFile

def CountWord(file, target) -> int:
    count_target = 0

    for line in file:
        line_list = line.split()
        count_target += line_list.count(target)

    return count_target


def main() -> None:
    file = GetFileStrings("Стихотворение.txt")
    target = input("Введите слово, которое Вы хотите найти: ").lower()
    result = CountWord(file, target)

    print(f"Количество найденных совпадений с словом '{target}' : {result}")

main()