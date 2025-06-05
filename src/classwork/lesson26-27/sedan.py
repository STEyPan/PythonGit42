from automobile import Automobile


class Sedan(Automobile):

    def forward_moving(self):
        return f"{self._name} {super().forward_moving()}"

    def backward_moving(self):
        return f"{self._name} {super().backward_moving()}"

    def hand_brake(self):
        return f"{self._name} {super().hand_brake()}"

    def start_engine(self):
        return f"{super().start_engine()} - Врум-врум"

    __transmission_box = str()
    __additional_option = 0

    def __init__(self,
                 name: str = "Название",
                 color: str = "Цвет",
                 power_engine: float = 0.0,
                 price: float = 0.0,
                 max_speed: int = 0,
                 transmission_box: str = "Коробка передач",
                 additional_option: int = 0):

        super().__init__(name, color, power_engine, price, max_speed)
        self.__transmission_box = transmission_box
        self.__additional_option = additional_option

    def __del__(self):
        pass
    @property
    def transmission_box(self):
        return self.__transmission_box

    @transmission_box.setter
    def transmission_box(self, new_transmission_box : str = None):
        if new_transmission_box != None and isinstance(new_transmission_box, str):
            self.__transmission_box = new_transmission_box
        else:
            raise "Ошибка типов"

    @property
    def additional_option(self):
        return self.__transmission_box

    @additional_option.setter
    def additional_option(self, new_additional_option: int = None):
        if new_additional_option != None and isinstance(new_additional_option, int):
            self.__additional_option = new_additional_option
        else:
            raise "Ошибка типов"

    def get_info(self):
        return (f"Седан:\n"
                f"{super().get_info()}\n"
                f"Коробка передач: {self.__transmission_box}\n"
                f"Количество доп.опций: {self.__additional_option}")