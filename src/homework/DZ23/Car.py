class Car:
    def __init__(self, model, release, fabricator, motor, color, price):
        self.__model = model
        self.__release = release
        self.__fabricator = fabricator
        self.__motor = motor
        self.__color = color
        self.__price = price

    def model_car(self):
        return self.__model


new_car = Car("Мерс-107", "1980",
              "Мерседес", "V16", "желтый", "6.500.000 рублей")


print(new_car.model_car())