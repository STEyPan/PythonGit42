class Car:
    __model = str()
    __release = 1970
    __fabricator = str()
    __engine = str()
    __color = str()
    __price = 0.0

    def __init__(self,
                 model: str = "Модель",
                 release: int = 1970,
                 fabricator: str = "Производитель",
                 engine: str = "Двигатель",
                 color: str = "Цвет",
                 price: float = 0.0):

        self.__model = model
        self.__release = release
        self.__fabricator = fabricator
        self.__engine = engine
        self.__color = color
        self.__price = price

    def __del__(self):
        pass

    def input_data(self,
                   model: str = None,
                   release: int = None,
                   fabricator: str = None,
                   engine: str = None,
                   color: str = None,
                   price: float = None
                   ):

        self.__model = model if model != None else self.__model
        self.__release = release if release != None else self.__release
        self.__fabricator = fabricator if fabricator != None else self.__fabricator
        self.__engine = engine if engine != None else self.__engine
        self.__color = color if color != None else self.__color
        self.__price = price if price != None else self.__price

    def get_data(self):
        return (f"Модель: {self.__model}\n"
                f"Год выпуска: {self.__release}\n"
                f"Производитель: {self.__fabricator}\n"
                f"Двигатель: {self.__engine}\n"
                f"Цвет: {self.__color}\n"
                f"Цена: {self.__price} р")

    @property
    def car_model(self):
        return self.__model

    @car_model.setter
    def car_model(self, new_model: str = None):
        if new_model != None:
            self.__model = new_model

    @property
    def car_release(self):
        return self.__release

    @car_release.setter
    def car_release(self, new_relese: str = None):
        if new_relese != None:
            self.__release = new_relese

    @property
    def car_fabricator(self):
        return self.__fabricator

    @car_fabricator.setter
    def car_fabricator(self, new_fabricator: str = None):
        if new_fabricator != None:
            self.__fabricator = new_fabricator

    @property
    def car_engine(self):
        return self.__fabricator

    @car_engine.setter
    def car_engine(self, new_engine: str = None):
        if new_engine != None:
            self.__engine = new_engine

    @property
    def car_color(self):
        return self.__color

    @car_color.setter
    def car_color(self, new_color: str = None):
        if new_color != None:
            self.__color = new_color

    @property
    def car_price(self):
        return self.__price

    @car_price.setter
    def car_price(self, new_price: str = None):
        if new_price != None:
            self.__price = new_price


# new_car = Car("Мерс-107", 1980,
#               "Мерседес", "V16", "желтый", 6500000)
#
#
# new_car.car_release = 1990
# print(new_car.get_data())