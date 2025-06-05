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
                 type_fuel : str = "Тип топлива"):

        super().__init__(name, color, power_engine, price, max_speed)
        self.__frame = frame
        self.__full_drive = full_drive
        self.__blocking = blocking
        self.__type_fuel = type_fuel

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, new_frame : bool = None):
        if new_frame != None and isinstance(new_frame, bool):
            self.__frame = new_frame
        else:
            raise "Ошибка типов"

    @property
    def full_drive(self):
        return self.__full_drive

    @full_drive.setter
    def full_drive(self, new_full_drive : bool = None):
        if new_full_drive != None and isinstance(new_full_drive, bool):
            self.__full_drive = new_full_drive
        else:
            raise "Ошибка типов"

    @property
    def blocking(self):
        return self.__blocking

    @blocking.setter
    def blocking(self, new_blocking: bool = None):
        if new_blocking != None and isinstance(new_blocking, bool):
            self.__full_drive = new_blocking
        else:
            raise "Ошибка типов"
    @property
    def type_fuel(self):
        return self.__type_fuel

    @type_fuel.setter
    def type_fuel(self, new_type_fuel: str = None):
        if new_type_fuel != None and isinstance(new_type_fuel, str):
            self.__full_drive = new_type_fuel
        else:
            raise "Ошибка типов"

    def get_info(self):
        return (f"Внедорожник:\n"
                f"{super().get_info()}\n"
                f"Рамный: {"Да" if self.__frame else "Нет"}\n"
                f"Полный привод: {"Да" if self.__full_drive else "Нет"}\n"
                f"Блокировка: {"Да" if self.__blocking else "Нет"}\n"
                f"Тип топлива: {self.__type_fuel}")