
def GetFileStrings(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        stringsFile = file.read().split("\n")

    return stringsFile

def LongestLine() -> str:
    file = GetFileStrings("Стихотворение.txt")
    max_length = len(file[0])
    #max_length = max(map(len, file))

    for line in file:
        line_length = len(line)
        if line_length > max_length:
            max_length = line_length

    return f"Длина самой длинной строки = {max_length}"


print(LongestLine())
