from home import Home

class Floor(Home):

    __count_rooms = 0
    __count_bathrooms = 0

    def __init__(self,
                 area: float = 0.0,
                 input_power: float = 0.0,
                 count_rooms : int = 0,
                 count_bathrooms : int = 0):

        super().__init__(area, input_power)
        self.__count_rooms = count_rooms
        self.__count_bathrooms = count_bathrooms

    def __del__(self):
        super().__del__()

    def total_cost(self):

        sum_area = self._area * 15
        sum_input_power = self._input_power * 5

        return sum_area + sum_input_power

    def __str__(self):
        return (f"Общая площадь этажа: {self._area} кв/м\n"
                f"Мощность входной электрики: {self._input_power} к/ват\n"
                f"Количество комнат: {self.__count_rooms}\n"
                f"Количество санузлов: {self.__count_bathrooms}")
