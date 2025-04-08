# Задание 3
# Необходимо разработать программу, которая хранит в себе данные о хоккеистов:
# 1. ФИО
# 2. Номер игрока
# 3. Возраст
# 4. Данные о количестве забитых шайб за последние 10 лет (в год)
# Нужно дать возможность Добавлять, Удалять и Выводить данную информацию


def hockeyPlayers() -> dict:
    players = {}
    return players

def addInfo(players: dict) -> dict:
    player = {}
    addName = input("Введите ФИО игрока: ")
    addNumber = int(input("Введите номер игрока: "))
    addAge = int(input("Введите возраст игрока: "))
    print("Введите данные о количестве забитых шайб в год за последние 10 лет\n")

    addStatistic = []
    currentYear = 2025
    year = currentYear - 10
    while year != currentYear:
        stats = int(input(f"Введите количество забитых шайб за {year} год: "))
        year += 1
        addStatistic.append(stats)

    player["ФИО"] = addName
    player["Возраст"] = addAge
    player["Статистика"] = addStatistic
    players[addNumber] = player
    return players

def delInfo(players: dict) -> dict:
    delKey = int(input("Введите номер игрока, которого хотите удалить: "))
    if delKey not in players:
        print("Нет такого игрока")
    else:
        print(f"Игрок номер: {delKey} - {players[delKey]["ФИО"]} удален из команды")
        players.pop(delKey)
        return players

def showInfo(players: dict) -> None:
    searchNumber = int(input("Введите номер игрока, которого хотите найти: "))
    if searchNumber not in players:
        print("Нет такого игрока")
    else:
        for key, value in players.items():
            print(f"\nНомер игрока: {key}"
                  f"\t\nФИО: {value["ФИО"]}"
                  f"\t\nВозраст: {value["Возраст"]}"
                  f"\t\nСтатистика игрока а последние 10 лет: {value["Статистика"]}")


def main() -> None:
    players = hockeyPlayers()
    choice = ""
    while choice != "4":
        print("\n1. Добавить")
        print("2. Удалить")
        print("3. Вывести информацию")
        print("4. Закрыть программу")
        choice = input(f"\n\tВыберете действие: ")

        match choice:
            case "1":
                addInfo(players)
            case "2":
                delInfo(players)
            case "3":
                showInfo(players)
            case "4":
                break
            case _:
                print("Введена неверная команда")


main()