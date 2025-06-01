from car import Car

def car_input_data() -> object:
    model = input("\nВведите название модели автомобиля: ")
    release = int(input("Введите дату изготовления автомобиля: "))
    fabricator = input("Введите производителя автомобиля: ")
    engine = input("Введите название двигателя автомобиля: ")
    color = input("Введите цвет автомобиля: ")
    price = int(input("Введите цену автомобиля: "))
    print()

    new_car = Car(model, release, fabricator, engine, color, price)

    return new_car


def car_menu() -> None:
    new_car = Car()
    choice = ""

    while choice != "0":

        print("\nАвтомобиль\n")
        print(f"1) Ввести данные\n"
              f"2) Показать данные\n"
              f"0) Выйти из программы\n")
        choice = input("Выберете пункт меню: ")

        if choice == "1":
            new_car = car_input_data()

        elif choice == "2":
            print(f"\n{new_car.get_data()}")

        elif choice == "0":
            print("До свидания!")

        else:
            print("Нет такой команды!")