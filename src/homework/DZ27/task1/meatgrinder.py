from device import Device

class MeatGrinder(Device):
    __type_grinder = str()
    __productivity = 0.0
    __reverse = False


    def __init__(self,
                 name: str = "Название",
                 fabricator: str = "Производитель",
                 color: str = "Цвет",
                 price: float = 0.0,
                 type_grinder : str = "Тип мясорубки",
                 productivity : float = 0.0,
                 reverse : bool = False):

        super().__init__(name, fabricator, color, price)
        self.__type_grinder = type_grinder
        self.__productivity = productivity
        self.__reverse = reverse

    def __del__(self):
        super().__del__()

    def get_data(self):
        return (f"{super().get_data()}\n"
                f"Тип мясорубки: {self.__type_grinder}\n"
                f"Производительность: {self.__productivity} кг/мин\n"
                f"Реверс: {"есть" if self.__reverse else "нет"}")

    def start_work(self):
        if self.switch:
            return f"{self._name} перерабатывает мясо"
        return f"{self._name} не включен"

    def stop_work(self):
        if self.switch:
            return f"{self._name} заканчивает переработку"
        return f"{self._name} не включен"

    def start_reverse(self):
        if self.switch:

            if self.__reverse:
                return f"{self._name} запускает обратный ход"

            return f"У {self._name} нет функции реверса"

        return f"{self._name} не включен"

    def stop_reverse(self):
        if not self.switch or "нет функции реверса" in self.start_reverse():
            return ""

        return f"{self._name} завершает реверс"




meat_grinder_1 = MeatGrinder(name="Polaris PMG 2058",
                             fabricator="Polaris", price=5_990,
                             color="Серый",
                             type_grinder="Автоматический",
                             productivity=3.56)
print(meat_grinder_1.get_data())
print("-===========================================-")
meat_grinder_1.switch = True
print(meat_grinder_1.device_status())
print(meat_grinder_1.start_work())
print(meat_grinder_1.stop_work())
print(meat_grinder_1.start_reverse())
print(meat_grinder_1.stop_reverse())
meat_grinder_1.switch = False
print(meat_grinder_1.start_work())
print(meat_grinder_1.stop_work())
print(meat_grinder_1.device_status())