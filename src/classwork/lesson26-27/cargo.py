from automobile import Automobile

class Cargo(Automobile):
    __tonnage = 0
    __trailer = True
    __sleeping_place = True
    __count_seats = 0

    def __init__(self,
                 name: str = "Название",
                 color: str = "Цвет",
                 power_engine: float = 0.0,
                 price: float = 0.0,
                 max_speed: int = 0,
                 tonnage : float = 0.0,
                 trailer : bool = True,
                 sleeping_place : bool = True,
                 count_seats : int = 0
                 ):

        super().__init__(name, color, power_engine, price, max_speed)
        self.__tonnage = tonnage
        self.__trailer = trailer
        self.__sleeping_place = sleeping_place
        self.__count_seats = count_seats

    def __del__(self):
        pass
    @property
    def tonnage(self):
        return self.__tonnage

    @tonnage.setter
    def tonnage(self, new_tonnage : float = None):
        if new_tonnage != None and isinstance(new_tonnage, float):
            self.__tonnage = new_tonnage
        else:
            raise "Ошибка типов"

    @property
    def trailer(self):
        return self.__trailer

    @trailer.setter
    def trailer(self, new_trailer : bool = None):
        if new_trailer != None and isinstance(new_trailer, bool):
            self.__trailer = new_trailer
        else:
            raise "Ошибка типов"

    @property
    def sleeping_place(self):
        return self.__sleeping_place

    @sleeping_place.setter
    def sleeping_place(self, new_sleeping_place : bool = None):
        if new_sleeping_place != None and isinstance(new_sleeping_place, bool):
            self.__sleeping_place = new_sleeping_place
        else:
            raise "Ошибка типов"

    @property
    def count_seats(self):
        return self.__count_seats

    @count_seats.setter
    def count_seats(self, new_count_seats : int = None):
        if new_count_seats != None and isinstance(new_count_seats, int):
            self.__count_seats = new_count_seats
        else:
            raise "Ошибка типов"

    def get_info(self):
        return (f"Грузовик:\n"
                f"{super().get_info()}\n"
                f"Тоннаж: {self.__tonnage} тонн\n"
                f"Возможность установки прицепа: {"Да" if self.__trailer else "Нет"}\n"
                f"Наличие спальных мест: {"Да" if self.__sleeping_place else "Нет"}\n"
                f"Количество мест: {self.__count_seats}")