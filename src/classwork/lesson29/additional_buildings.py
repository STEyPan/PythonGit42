from home import Home

class AdditionalBuildings(Home):

    __buildings = list()

    def __init__(self,
                 area: float = 0.0,
                 input_power: float = 0.0,
                 buildings: list = []):

        super().__init__(area, input_power)
        self.__buildings = buildings

    def __del__(self):
        super().__del__()

    def total_cost(self):
        sum_area = self._area * 15
        sum_input_power = self._input_power * 5

        return sum_area + sum_input_power

    def __str__(self):
        return (f"\n------ Дополнительные постройки ------\n"
                f"\t-{"\n\t-".join(self.__buildings)}\n"
                f"Общая площадь построек: {self._area} кв/м\n"
                f"Мощность входной электрики: {self._input_power} к/ват\n"
                f"Общая стоимость построек: {self.total_cost():,} рублей")