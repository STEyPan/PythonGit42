from pkgutil import get_data

from device import Device

class Blender(Device):
    __max_power = 0
    __whisk = False
    __measuring_cup = False
    __count_chopper = 0

    def __init__(self,
                 name: str = "Название",
                 fabricator: str = "Производитель",
                 color: str = "Цвет",
                 price: float = 0.0,
                 max_power : int = 0,
                 whisk : bool = False,
                 measuring_cup : bool = False,
                 count_chopper : int = 0):

        super().__init__(name, fabricator, color, price)
        self.__max_power = max_power
        self.__whisk = whisk
        self.__measuring_cup = measuring_cup
        self.__count_chopper = count_chopper

    def __del__(self):
        super().__del__()

    def get_data(self):
        return (f"{super().get_data()}\n"
                f"Максимальная мощность: {self.__max_power} Вт\n"
                f"Венчик для взбивания: {"есть" if self.__whisk else "нет"}\n"
                f"Мерный стаканчик: {"есть" if self.__measuring_cup else "нет"}\n"
                f"Количество насадок: {self.__count_chopper} шт")

    def start_work(self):
        if self.switch:
            return f"{self._name} измельчает продукты"
        return f"{self._name} не включен"

    def stop_work(self):
        if self.switch:
            return f"{self._name} завершает измельчение"
        return f"{self._name} не включен"

    def start_whisking(self):
        if self.switch:

            if self.__whisk:
                return f"{self._name} взбивает продукт"
            return f"У вам нет венчика для взбивания"

        return f"{self._name} не включен"

    def stop_whisking(self):

        if not self.switch or self.start_whisking() == "У вам нет венчика для взбивания":
            return ""
        else:
            return f"{self._name} завершает взбитие"


blender_1 = Blender(name="Braun MQ7035", fabricator="Braun", max_power=220, color="Черный")
blender_1.price = 4500
print(blender_1.get_data())
print("-===========================================-")
blender_1.switch = True
print(blender_1.device_status())
# blender_1.switch = False
print(blender_1.start_work())
print(blender_1.stop_work())
print(blender_1.start_whisking())
print(blender_1.stop_whisking())
blender_1.switch = False
print(blender_1.device_status())
print("-===========================================-")