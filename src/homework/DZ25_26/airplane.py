class Airplane:
    __airplane_type = str()
    __count_passengers = 0
    __max_passengers = 0

    def __init__(self,
                 airplane_type : str = "Тип самолета",
                 count_passengers : int = 0,
                 max_passengers : int = 0):

        self.__airplane_type = airplane_type
        self.__count_passengers = count_passengers
        self.__max_passengers = max_passengers

    def __del__(self):
        pass

    def __str__(self):
        return (f"Тип самолета: {self.__airplane_type}\n"
                f"Количество пассажиров: {self.__count_passengers}\n"
                f"Максимальное количество пассажиров: {self.__max_passengers}")

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.__airplane_type == other.__airplane_type
        elif isinstance(other, str):
            return self.__airplane_type == other
        else:
            raise "Ошибка типов"


    def __add__(self, other): # +
        if self.__count_passengers >= self.__max_passengers:
            raise "Места заполнены"

        if isinstance(other, int):
            add_passengers = self.__count_passengers + other

            if add_passengers > self.__max_passengers:
                raise "Места заполнены"

            return Airplane(self.__airplane_type, add_passengers, self.__max_passengers)

    def __sub__(self, other): # -
        if self.__count_passengers < 0:
            raise "Пассажиров не может быть меньше нуля"

        if isinstance(other, int):
            sub_passengers = self.__count_passengers - other

            if sub_passengers < 0:
                raise "Пассажиров не может быть меньше нуля"

            return Airplane(self.__airplane_type, sub_passengers, self.__max_passengers)

    def __iadd__(self, other): # +=
        if self.__count_passengers >= self.__max_passengers:
            raise "Места заполнены"

        if isinstance(other, int):

            if (self.__count_passengers + other) > self.__max_passengers:
                raise "Места заполнены"

            self.__count_passengers += other

            return self

    def __isub__(self, other):
        if self.__count_passengers < 0:
            raise "Пассажиров не может быть меньше нуля"

        if isinstance(other, int):

            if (self.__count_passengers - other) < 0:
                raise "Пассажиров не может быть меньше нуля"

            self.__count_passengers -= other

            return self

    def __gt__(self, other): # >
        if isinstance(other, Airplane):
            return self.__max_passengers > other.__max_passengers
        else:
            raise "Ошибка типов"

    def __ge__(self, other): # >=
        if isinstance(other, Airplane):
            return self.__max_passengers >= other.__max_passengers
        else:
            raise "Ошибка типов"

    def __lt__(self, other):  # <
        if isinstance(other, Airplane):
            return self.__max_passengers < other.__max_passengers
        else:
            raise "Ошибка типов"

    def __le__(self, other):  # <=
        if isinstance(other, Airplane):
            return self.__max_passengers <= other.__max_passengers
        else:
            raise "Ошибка типов"






airplane_1 = Airplane("АН-208", 2, 40)
airplane_2 = Airplane("Boing-747", 400, 40)
print(airplane_1 == airplane_2)
print(airplane_1)
airplane_1 = airplane_1 + 5
print(airplane_1)
print("-==============================================-")
airplane_1 += 2
print(airplane_1)
print("-==============================================-")
airplane_2 = airplane_2 - 10
print(airplane_2)
print("-==============================================-")
airplane_2 -= 390
print(airplane_2)
print("-==============================================-")
print(f"max_passengers airplane_1 < airplane_2: {airplane_1 < airplane_2}")
print(f"max_passengers airplane_1 <= airplane_2: {airplane_1 <= airplane_2}")
print(f"max_passengers airplane_1 > airplane_2: {airplane_1 > airplane_2}")
print(f"max_passengers airplane_1 >= airplane_2: {airplane_1 >= airplane_2}")