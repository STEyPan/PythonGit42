from ship import Ship

class Destroyer(Ship):
    __missile_system = str()

    def __init__(self,
                 name: str = "Название",
                 country: str = "Страна",
                 speed: float = 0.0,
                 displacement: float = 0.0,
                 armament: list = [],
                 missile_system : str = "Ракетная система"):

        super().__init__(name, country, speed, displacement, armament)
        self.__missile_system = missile_system

    def __del__(self):
        super().__del__()

    def get_info(self):
        return (f"Тип эсминец.\n"
                f"Название: {self._name}\n"
                f"Страна: {self._country}\n"
                f"Водоизмещение: {self._displacement} тонн\n"
                f"Скорость: {self._speed} узлов\n"
                f"Вооружение: {", ".join(self._armament)}\n"
                f"Ракетная система: {self.__missile_system}")