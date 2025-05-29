from car import Car

def car_input_data(new_car: object):
    new_car = Car()

    return new_car

def car_get_data(new_car: object):
    return new_car.get_data()

def car_menu():
    new_car = Car()
    choice = ""

    while choice != "0":

        print(f"1) Ввести данные\n"
              f"2) Показать данные\n"
              f"0) Выйти из программы\n")
        choice = input("Выберете пункт меню: ")

        if choice == "1":
            car_input_data(new_car)

        elif choice == "2":
            return car_get_data(new_car)

        elif choice == "0":
            print("До свидания!")

        else:
            print("Нет такой команды!")

car_menu()