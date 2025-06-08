from device import Device

class CoffeeMachine(Device):


    __volume_tank = 0.0
    __heater_type = str()
    __coffee_type = str()

    def __init__(self, name: str = "Название",
                 fabricator: str = "Производитель",
                 color: str = "Цвет",
                 price: float = 0.0,
                 volume_tank: float = 0.0,
                 heater_type: str = "Тип нагревателя",
                 coffee_type: str = "Используемый кофе"
                 ):

        super().__init__(name, fabricator, color, price)
        self.__volume_tank = volume_tank
        self.__heater_type = heater_type
        self.__coffee_type = coffee_type
    #

    def __del__(self):
        super().__del__()

    def get_data(self):
        return (f"{super().get_data()}\n"
                f"Объем резервуара для воды: {self.__volume_tank} литров\n"
                f"Тип нагревателя: {self.__heater_type}\n"
                f"Используемый кофе: {self.__coffee_type}")

    def make_coffee(self):
        if self.switch:
            return f"{self.__coffee_type} кофе приготовлен"
        return f"{self._name} не включен"

    def fill_water(self):
        return f"Резервуар для воды заполнен"




coffee_1 = CoffeeMachine(name="DeLonghi ECAM 22.110.SB", fabricator="DeLonghi", volume_tank=2.4, heater_type="Термоблок", coffee_type="Молотый")
coffee_1.price = 80_000
print(coffee_1.get_data())
print("-===========================================-")
coffee_1.switch = True
print(coffee_1.device_status())
print(coffee_1.fill_water())
print(coffee_1.make_coffee())
coffee_1.switch = False
print(coffee_1.device_status())
print("-===========================================-")

