from car_menu import car_menu
from book_menu import book_menu
from stadium_menu import stadium_menu

def main() -> None:

    print("1) Автомобиль\n"
          "2) Книга\n"
          "3) Стадион\n")

    choice = input("Выберете объект: ")

    match choice:

        case "1": car_menu()
        case "2": book_menu()
        case "3": stadium_menu()
        case _: print("Нет такой команды")


if __name__ == "__main__":
    main()