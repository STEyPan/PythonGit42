from home import Home

class Roof(Home):

    __type_roof = str()
    __satellite = False

    def __init__(self,
                 area: float = 0.0,
                 input_power: float = 0.0,
                 type_roof : str = "",
                 satellite : bool = False):

        super().__init__(area, input_power)
        self.__type_roof = type_roof
        self.__satellite = satellite

    def __del__(self):
        super().__del__()

    def total_cost(self):

        roof_prices = {
            "плоская" : 3000,
            "односкатная" : 4000,
            "двускатная" : 4500,
            "вальмовая" : 5400
        }

        sum_area = self._area * 15
        sum_input_power = self._input_power * 5
        satellite_price = 20000 if self.__satellite else 0
        roof_price = 0

        for key, value in roof_prices.items():
            if self.__type_roof.lower() == key:
                roof_price = value

        return sum_area + sum_input_power + satellite_price + roof_price


    def __str__(self):
        return (f"\n------ Крыша ------\n"
                f"Тип крыши: {self.__type_roof}\n"
                f"Наличие чердака: {"да" if self._area > 0 else "нет"}\n"
                f"{f"Общая площадь чердака: {self._area} кв/м\n" if self._area > 0 else ""}"
                f"Мощность входной электрики: {self._input_power} к/ват\n"
                f"Спутниковая антенна: {"да" if self.__satellite else "нет"}\n"
                f"Общая стоимость: {self.total_cost():,} рублей.")

# roof = Roof(area=2, type_roof="плоская",input_power=2000, satellite=True)
# print(roof)

