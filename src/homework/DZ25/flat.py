from optparse import Option


class Flat:
    __flat_area = 0
    __price = 0.0

    def __init__(self,
                 flat_area : int = 0,
                 price : float = 0.0):

        self.__flat_area = flat_area
        self.__price = price

    def __del__(self):
        pass

    def __str__(self):
        return (f"Площадь квартиры: {self.__flat_area} кв/м\n"
                f"Цена квартиры: {self.__price:,} рублей")

    def __eq__(self, other): # flat_area == flat_area
        if isinstance(other, Flat):
            return self.__flat_area == other.__flat_area
        else:
            raise "Ошибка типов"

    def __ne__(self, other): # flat_area != flat_area
        if isinstance(other, Flat):
            return self.__flat_area != other.__flat_area
        else:
            raise "Ошибка типов"

    def __gt__(self, other): # price > price
        if isinstance(other, Flat):
            return self.__price > other.__price
        else:
            raise "Ошибка типов"

    def __ge__(self, other): # price >= price
        if isinstance(other, Flat):
            return self.__price >= other.__price
        else:
            raise "Ошибка типов"

    def __lt__(self, other): # price < price
        if isinstance(other, Flat):
            return self.__price < other.__price
        else:
            raise "Ошибка типов"

    def __le__(self, other):
        if isinstance(other, Flat): # price <= price
            return self.__price <= other.__price
        else:
            raise "Ошибка типов"

flat_1 = Flat(100, 120000000)
flat_2 = Flat(150, 220000000)
print(flat_1)
print("-=============================================-")
print(flat_2)
print("-=============================================-")
print(f"area flat_1 == flat_2: {flat_1 == flat_2}")
print(f"area flat_1 != flat_2: {flat_1 != flat_2}")
print("-=============================================-")
print(f"price flat_1 > flat_2: {flat_1 > flat_2}")
print(f"price flat_1 >= flat_2: {flat_1 >= flat_2}")
print(f"price flat_1 < flat_2: {flat_1 < flat_2}")
print(f"price flat_1 <= flat_2: {flat_1 <= flat_2}")