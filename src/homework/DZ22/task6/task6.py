
def GetFileStrings(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        stringsFile = file.read().split("\n")

    return stringsFile

def SwapWord(file, target, new_word) -> int:

    i = 0
    for line in file:

        line_list = line.split()
        j = 0
        for word in line_list:

            if word.lower() == target:
                line_list[j] = new_word
            j += 1

        file[i] = " ".join(line_list)
        i += 1

    return file


def main() -> None:
    file = GetFileStrings("Стихотворение.txt")
    target = input("Введите слово, которое Вы хотите найти и заменить: ").lower()
    new_word = input("Введите слово, которым Вы хотите заменить искомое: ")
    result = SwapWord(file, target, new_word)
    print()
    print("\n".join(result))

main()