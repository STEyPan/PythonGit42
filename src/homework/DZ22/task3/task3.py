
def GetFileStrings(path: str) -> list:
    with open(path, encoding='windows-1251') as file:
        stringsFile = file.read().split("\n")

    return stringsFile

def DeleteLastString() -> tuple:
    file = GetFileStrings("Стихотворение.txt")
    last_string = "".join(file.pop())
    origin = "\n".join(file)

    return last_string, origin



def MakingChanges(files):
    last_string, origin = files

    with open("Стихотворение.txt", "w+") as origin_file:
        origin_file.write(origin)

    with open("last_string.txt", "w+") as new_file:
        new_file.write(last_string)

MakingChanges(DeleteLastString())
