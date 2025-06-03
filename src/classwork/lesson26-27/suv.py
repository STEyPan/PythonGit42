from automobile import Automobile

class SUV(Automobile):

    __frame = True
    __full_drive = True
    __blocking = True
    __type_fuel = str()

    def __init__(self,
                 name: str = "Название",
                 color: str = "Цвет",
                 power_engine: float = 0.0,
                 price: float = 0.0,
                 max_speed: int = 0,
                 frame : bool = True,
                 full_drive : bool = True,
                 blocking : bool = True,
                 type_fuel = "Тип топлива"):

        super().__init__(name, color, power_engine, price, max_speed)
        self.__frame = frame
        self.__full_drive = full_drive
        self.__blocking = blocking
        self.__type_fuel = type_fuel


    def frame(self):
        return self.__frame

    def full_drive(self):
        return self.__full_drive

    def blocking(self):
        return self.__blocking

    def type_fuel(self):
        return self.__type_fuel

    def get_info(self):
        return (f"Внедорожник:\n"
                f"{super().get_info()}\n"
                f"Рамный: {"Да" if self.__frame else "Нет"}\n"
                f"Полный привод: {"Да" if self.__full_drive else "Нет"}\n"
                f"Блокировка: {"Да" if self.__blocking else "Нет"}\n"
                f"Тип топлива: {self.__type_fuel}")


    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, new_name: str = None):
    #     if new_name != None:
    #         self._name = new_name
    #
    # @property
    # def color(self):
    #     return self._color
    #
    # @color.setter
    # def color(self, new_color: str = None):
    #     if new_color != None:
    #         self._color = new_color
    #
    # @property
    # def power_engine(self):
    #     return self._power_engine
    #
    # @power_engine.setter
    # def power_engine(self, new_power_engine: float = None):
    #     if new_power_engine != None:
    #         self._power_engine = new_power_engine
    #
    # @property
    # def price(self):
    #     return self._price
    #
    # @price.setter
    # def price(self, new_price: float = None):
    #     if new_price != None:
    #         self._price = new_price
    # @property
    # def max_speed(self):
    #     return self._max_speed
    #
    # @max_speed.setter
    # def max_speed(self, new_max_speed: int = None):
    #     if new_max_speed != None:
    #         self._max_speed = new_max_speed