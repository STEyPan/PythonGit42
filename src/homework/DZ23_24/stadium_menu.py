from stadium import Stadium

def stadium_input_data() -> object:
    new_stadium = Stadium()

    new_stadium.stadium_name = input("\nВведите название стадиона: ")
    new_stadium.stadium_date = int(input("Введите дату открытия: "))
    new_stadium.stadium_country = input("Введите страну: ")
    new_stadium.stadium_city = input("Введите город: ")
    new_stadium.stadium_capacity = int(input("Введите вместимость стадиона: "))
    print()

    return new_stadium


def stadium_menu() -> None:
    new_stadium = Stadium()
    choice = ""

    while choice != "0":

        print("\nСтадион\n")
        print(f"1) Ввести данные\n"
              f"2) Показать данные\n"
              f"0) Выйти из программы\n")
        choice = input("Выберете пункт меню: ")

        if choice == "1":
            new_stadium = stadium_input_data()

        elif choice == "2":
            print(f"\n{new_stadium.get_data()}")

        elif choice == "0":
            print("До свидания!")

        else:
            print("Нет такой команды!")