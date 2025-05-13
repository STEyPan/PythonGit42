
def GetFileStrings(path: str) -> list:
    with open(path) as file:
        stringsFile = file.read().split("\n")

    return stringsFile

def IsFilesEqual() -> str:
    first_file = GetFileStrings("first.txt")
    second_file = GetFileStrings("second.txt")
    incorrect_string = {}
    i = 1

    for first_file_string,second_file_string in zip(first_file, second_file):

        if first_file_string != second_file_string:
            incorrect_string[i] = [first_file_string, second_file_string]
        i += 1

    if incorrect_string:
        return "".join([f"В {key} строке обоих файлов есть несовпадающие строки: "
                        f"'{value[0]}' и '{value[1]}'" for key, value in incorrect_string.items()])
    else:
        return "Файлы совпадают"


print(IsFilesEqual())
