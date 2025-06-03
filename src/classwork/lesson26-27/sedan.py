from automobile import Automobile


class Sedan(Automobile):

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
        if new_transmission_box != None:
            self.__transmission_box = new_transmission_box
    @property
    def additional_option(self):
        return self.__transmission_box

    @additional_option.setter
    def additional_option(self, new_additional_option: int = None):
        if new_additional_option != None:
            self.__additional_option = new_additional_option

    def get_info(self):
        return (f"Седан:\n"
                f"{super().get_info()}\n"
                f"Коробка передач: {self.__transmission_box}\n"
                f"Количество доп.опций: {self.__additional_option}")