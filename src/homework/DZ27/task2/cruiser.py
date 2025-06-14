from ship import Ship

class Cruiser(Ship):
    __flagship = False

    def __init__(self,
                 name: str = "Название",
                 country: str = "Страна",
                 speed: float = 0.0,
                 displacement: float = 0.0,
                 armament: list = [],
                 flagship : bool = False):

        super().__init__(name, country, speed, displacement, armament)
        self.__flagship = flagship

    def __del__(self):
        super().__del__()

    def get_info(self):
        return (f"Тип эсминец.\n"
                f"Название: {self._name}\n"
                f"Страна: {self._country}\n"
                f"Водоизмещение: {self._displacement} тонн\n"
                f"Скорость: {self._speed} узлов\n"
                f"Вооружение: {", ".join(self._armament)}\n"
                f"Флагман: {"да" if self.__flagship else "нет"}")