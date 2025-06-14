from ship import Ship

class Frigate(Ship):
    __sonar_type = str()

    def __init__(self,
                 name: str = "Название",
                 country: str = "Страна",
                 speed: float = 0.0,
                 displacement: float = 0.0,
                 armament: list = [],
                 sonar_type : str = "Тип сонара"):

        super().__init__(name, country, speed, displacement, armament)
        self.__sonar_type = sonar_type

    def __del__(self):
        super().__del__()

    def get_info(self):
        return (f"Тип фрегат.\n"
                f"Название: {self._name}\n"
                f"Страна: {self._country}\n"
                f"Водоизмещение: {self._displacement} тонн\n"
                f"Скорость: {self._speed} узлов\n"
                f"Вооружение: {", ".join(self._armament)}\n"
                f"Тип сонара: {self.__sonar_type}")